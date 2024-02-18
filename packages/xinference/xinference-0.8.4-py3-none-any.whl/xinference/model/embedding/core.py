# Copyright 2022-2023 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import shutil
from collections import defaultdict
from typing import Dict, List, Optional, Tuple, Union, no_type_check

import numpy as np
from pydantic import BaseModel

from ...constants import XINFERENCE_CACHE_DIR
from ...types import Embedding, EmbeddingData, EmbeddingUsage
from ..core import ModelDescription
from ..utils import get_cache_dir, is_model_cached, valid_model_revision

logger = logging.getLogger(__name__)

SUPPORTED_SCHEMES = ["s3"]
# Used for check whether the model is cached.
# Init when registering all the builtin models.
MODEL_NAME_TO_REVISION: Dict[str, List[str]] = defaultdict(list)


EMBEDDING_MODEL_DESCRIPTIONS: Dict[str, List[Dict]] = defaultdict(list)


def get_embedding_model_descriptions():
    import copy

    return copy.deepcopy(EMBEDDING_MODEL_DESCRIPTIONS)


class EmbeddingModelSpec(BaseModel):
    model_name: str
    dimensions: int
    max_tokens: int
    language: List[str]
    model_id: str
    model_revision: Optional[str]
    model_hub: str = "huggingface"


class EmbeddingModelDescription(ModelDescription):
    def __init__(
        self,
        address: Optional[str],
        devices: Optional[List[str]],
        model_spec: EmbeddingModelSpec,
        model_path: Optional[str] = None,
    ):
        super().__init__(address, devices, model_path=model_path)
        self._model_spec = model_spec

    def to_dict(self):
        return {
            "model_type": "embedding",
            "address": self.address,
            "accelerators": self.devices,
            "model_name": self._model_spec.model_name,
            "dimensions": self._model_spec.dimensions,
            "max_tokens": self._model_spec.max_tokens,
            "language": self._model_spec.language,
            "model_revision": self._model_spec.model_revision,
        }

    def to_version_info(self):
        from .utils import get_model_version

        if self._model_path is None:
            is_cached = get_cache_status(self._model_spec)
            file_location = get_cache_dir(self._model_spec)
        else:
            is_cached = True
            file_location = self._model_path

        return {
            "model_version": get_model_version(self._model_spec),
            "model_file_location": file_location,
            "cache_status": is_cached,
            "dimensions": self._model_spec.dimensions,
            "max_tokens": self._model_spec.max_tokens,
        }


def generate_embedding_description(
    model_spec: EmbeddingModelSpec,
) -> Dict[str, List[Dict]]:
    res = defaultdict(list)
    res[model_spec.model_name].append(
        EmbeddingModelDescription(None, None, model_spec).to_version_info()
    )
    return res


def cache_from_uri(
    model_spec: EmbeddingModelSpec,
    self_hosted_storage: bool = False,
) -> str:
    from fsspec import AbstractFileSystem, filesystem

    from ..utils import copy_from_src_to_dst, parse_uri

    cache_dir = os.path.realpath(
        os.path.join(XINFERENCE_CACHE_DIR, model_spec.model_name)
    )
    if os.path.exists(cache_dir):
        logger.info(f"Embedding cache {cache_dir} exists")
        return cache_dir

    assert model_spec.model_uri is not None
    src_scheme, src_root = parse_uri(model_spec.model_uri)
    if src_root.endswith("/"):
        # remove trailing path separator.
        src_root = src_root[:-1]

    if src_scheme == "file":
        if not os.path.isabs(src_root):
            raise ValueError(
                f"Model URI cannot be a relative path: {model_spec.model_uri}"
            )
        os.makedirs(XINFERENCE_CACHE_DIR, exist_ok=True)
        os.symlink(src_root, cache_dir, target_is_directory=True)
        return cache_dir
    elif src_scheme in SUPPORTED_SCHEMES:
        # use anonymous connection for self-hosted storage.
        src_fs: AbstractFileSystem = filesystem(src_scheme, anon=self_hosted_storage)
        local_fs: AbstractFileSystem = filesystem("file")

        files_to_download = []
        os.makedirs(cache_dir, exist_ok=True)

        for path, _, files in src_fs.walk(model_spec.model_uri):
            for file in files:
                src_path = f"{path}/{file}"
                local_path = src_path.replace(src_root, cache_dir)
                files_to_download.append((src_path, local_path))

        from concurrent.futures import ThreadPoolExecutor

        failed = False
        with ThreadPoolExecutor(max_workers=min(len(files_to_download), 4)) as executor:
            futures = [
                (
                    src_path,
                    executor.submit(
                        copy_from_src_to_dst, src_fs, src_path, local_fs, local_path
                    ),
                )
                for src_path, local_path in files_to_download
            ]
            for src_path, future in futures:
                if failed:
                    future.cancel()
                else:
                    try:
                        future.result()
                    except:
                        logger.error(f"Download {src_path} failed", exc_info=True)
                        failed = True

        if failed:
            logger.warning(f"Removing cache directory: {cache_dir}")
            shutil.rmtree(cache_dir, ignore_errors=True)
            raise RuntimeError(
                f"Failed to download embedding model '{model_spec.model_name}' "
            )
        return cache_dir
    else:
        raise ValueError(f"Unsupported URL scheme: {src_scheme}")


def cache(model_spec: EmbeddingModelSpec):
    from huggingface_hub import snapshot_download as hf_download
    from modelscope.hub.snapshot_download import snapshot_download as ms_download

    from ..utils import retry_download, symlink_local_file

    if (
        hasattr(model_spec, "model_uri")
        and getattr(model_spec, "model_uri", None) is not None
    ):
        logger.info(f"Embedding model caching from URI: {model_spec.model_uri}")
        return cache_from_uri(model_spec=model_spec)

    cache_dir = os.path.realpath(
        os.path.join(XINFERENCE_CACHE_DIR, model_spec.model_name)
    )
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir, exist_ok=True)
    meta_path = os.path.join(cache_dir, "__valid_download")
    if valid_model_revision(meta_path, model_spec.model_revision):
        return cache_dir

    from_modelscope: bool = model_spec.model_hub == "modelscope"
    if from_modelscope:
        download_dir = retry_download(
            ms_download,
            model_spec.model_name,
            None,
            model_spec.model_id,
            revision=model_spec.model_revision,
        )
        for subdir, dirs, files in os.walk(download_dir):
            for file in files:
                relpath = os.path.relpath(os.path.join(subdir, file), download_dir)
                symlink_local_file(os.path.join(subdir, file), cache_dir, relpath)
    else:
        retry_download(
            hf_download,
            model_spec.model_name,
            None,
            model_spec.model_id,
            revision=model_spec.model_revision,
            local_dir=cache_dir,
            local_dir_use_symlinks=True,
        )
    with open(meta_path, "w") as f:
        import json

        desc = EmbeddingModelDescription(None, None, model_spec)
        json.dump(desc.to_dict(), f)
    return cache_dir


def get_cache_status(
    model_spec: EmbeddingModelSpec,
) -> bool:
    return is_model_cached(model_spec, MODEL_NAME_TO_REVISION)


class EmbeddingModel:
    def __init__(self, model_uid: str, model_path: str, device: Optional[str] = None):
        self._model_uid = model_uid
        self._model_path = model_path
        self._device = device
        self._model = None

    def load(self):
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError:
            error_message = "Failed to import module 'SentenceTransformer'"
            installation_guide = [
                "Please make sure 'sentence-transformers' is installed. ",
                "You can install it by `pip install sentence-transformers`\n",
            ]

            raise ImportError(f"{error_message}\n\n{''.join(installation_guide)}")
        from ..utils import patch_trust_remote_code

        patch_trust_remote_code()
        self._model = SentenceTransformer(self._model_path, device=self._device)

    def create_embedding(self, sentences: Union[str, List[str]], **kwargs):
        from sentence_transformers import SentenceTransformer

        normalize_embeddings = kwargs.pop("normalize_embeddings", True)

        # copied from sentence-transformers, and modify it to return tokens num
        @no_type_check
        def encode(
            model: SentenceTransformer,
            sentences: Union[str, List[str]],
            batch_size: int = 32,
            show_progress_bar: bool = None,
            output_value: str = "sentence_embedding",
            convert_to_numpy: bool = True,
            convert_to_tensor: bool = False,
            device: str = None,
            normalize_embeddings: bool = False,
        ):
            """
            Computes sentence embeddings

            :param sentences: the sentences to embed
            :param batch_size: the batch size used for the computation
            :param show_progress_bar: Output a progress bar when encode sentences
            :param output_value:  Default sentence_embedding, to get sentence embeddings. Can be set to token_embeddings to get wordpiece token embeddings. Set to None, to get all output values
            :param convert_to_numpy: If true, the output is a list of numpy vectors. Else, it is a list of pytorch tensors.
            :param convert_to_tensor: If true, you get one large tensor as return. Overwrites any setting from convert_to_numpy
            :param device: Which torch.device to use for the computation
            :param normalize_embeddings: If set to true, returned vectors will have length 1. In that case, the faster dot-product (util.dot_score) instead of cosine similarity can be used.

            :return:
               By default, a list of tensors is returned. If convert_to_tensor, a stacked tensor is returned. If convert_to_numpy, a numpy matrix is returned.
            """
            import torch
            from sentence_transformers.util import batch_to_device
            from tqdm.autonotebook import trange

            model.eval()
            if show_progress_bar is None:
                show_progress_bar = (
                    logger.getEffectiveLevel() == logging.INFO
                    or logger.getEffectiveLevel() == logging.DEBUG
                )

            if convert_to_tensor:
                convert_to_numpy = False

            if output_value != "sentence_embedding":
                convert_to_tensor = False
                convert_to_numpy = False

            input_was_string = False
            if isinstance(sentences, str) or not hasattr(
                sentences, "__len__"
            ):  # Cast an individual sentence to a list with length 1
                sentences = [sentences]
                input_was_string = True

            if device is None:
                device = model._target_device

            model.to(device)

            all_embeddings = []
            all_token_nums = 0
            length_sorted_idx = np.argsort(
                [-model._text_length(sen) for sen in sentences]
            )
            sentences_sorted = [sentences[idx] for idx in length_sorted_idx]

            for start_index in trange(
                0,
                len(sentences),
                batch_size,
                desc="Batches",
                disable=not show_progress_bar,
            ):
                sentences_batch = sentences_sorted[
                    start_index : start_index + batch_size
                ]
                features = model.tokenize(sentences_batch)
                features = batch_to_device(features, device)
                all_token_nums += sum([len(f) for f in features])

                with torch.no_grad():
                    out_features = model.forward(features)

                    if output_value == "token_embeddings":
                        embeddings = []
                        for token_emb, attention in zip(
                            out_features[output_value], out_features["attention_mask"]
                        ):
                            last_mask_id = len(attention) - 1
                            while (
                                last_mask_id > 0 and attention[last_mask_id].item() == 0
                            ):
                                last_mask_id -= 1

                            embeddings.append(token_emb[0 : last_mask_id + 1])
                    elif output_value is None:  # Return all outputs
                        embeddings = []
                        for sent_idx in range(len(out_features["sentence_embedding"])):
                            row = {
                                name: out_features[name][sent_idx]
                                for name in out_features
                            }
                            embeddings.append(row)
                    else:  # Sentence embeddings
                        embeddings = out_features[output_value]
                        embeddings = embeddings.detach()
                        if normalize_embeddings:
                            embeddings = torch.nn.functional.normalize(
                                embeddings, p=2, dim=1
                            )

                        # fixes for #522 and #487 to avoid oom problems on gpu with large datasets
                        if convert_to_numpy:
                            embeddings = embeddings.cpu()

                    all_embeddings.extend(embeddings)

            all_embeddings = [
                all_embeddings[idx] for idx in np.argsort(length_sorted_idx)
            ]

            if convert_to_tensor:
                all_embeddings = torch.stack(all_embeddings)
            elif convert_to_numpy:
                all_embeddings = np.asarray([emb.numpy() for emb in all_embeddings])

            if input_was_string:
                all_embeddings = all_embeddings[0]

            return all_embeddings, all_token_nums

        all_embeddings, all_token_nums = encode(
            self._model,
            sentences,
            convert_to_numpy=False,
            normalize_embeddings=normalize_embeddings,
            **kwargs,
        )
        if isinstance(sentences, str):
            all_embeddings = [all_embeddings]
        embedding_list = []
        for index, data in enumerate(all_embeddings):
            embedding_list.append(
                EmbeddingData(index=index, object="embedding", embedding=data.tolist())
            )
        usage = EmbeddingUsage(
            prompt_tokens=all_token_nums, total_tokens=all_token_nums
        )
        return Embedding(
            object="list",
            model=self._model_uid,
            data=embedding_list,
            usage=usage,
        )


def match_embedding(model_name: str) -> EmbeddingModelSpec:
    from ..utils import download_from_modelscope
    from . import BUILTIN_EMBEDDING_MODELS, MODELSCOPE_EMBEDDING_MODELS
    from .custom import get_user_defined_embeddings

    # first, check whether it is a user-defined embedding model
    for model_spec in get_user_defined_embeddings():
        if model_name == model_spec.model_name:
            return model_spec

    if download_from_modelscope():
        if model_name in MODELSCOPE_EMBEDDING_MODELS:
            logger.debug(f"Embedding model {model_name} found in ModelScope.")
            return MODELSCOPE_EMBEDDING_MODELS[model_name]
        else:
            logger.debug(
                f"Embedding model {model_name} not found in ModelScope, "
                f"now try to load it via builtin way."
            )

    if model_name in BUILTIN_EMBEDDING_MODELS:
        return BUILTIN_EMBEDDING_MODELS[model_name]
    else:
        raise ValueError(
            f"Embedding model {model_name} not found, available"
            f"model list: {BUILTIN_EMBEDDING_MODELS.keys()}"
        )


def create_embedding_model_instance(
    subpool_addr: str, devices: List[str], model_uid: str, model_name: str, **kwargs
) -> Tuple[EmbeddingModel, EmbeddingModelDescription]:
    model_spec = match_embedding(model_name)
    model_path = cache(model_spec)
    model = EmbeddingModel(model_uid, model_path, **kwargs)
    model_description = EmbeddingModelDescription(
        subpool_addr, devices, model_spec, model_path=model_path
    )
    return model, model_description
