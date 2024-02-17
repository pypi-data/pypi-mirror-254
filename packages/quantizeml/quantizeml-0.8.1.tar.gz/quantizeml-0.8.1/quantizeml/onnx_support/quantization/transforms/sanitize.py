#!/usr/bin/env python
# ******************************************************************************
# Copyright 2023 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
__all__ = ['sanitize']

import warnings
import tempfile
from pathlib import Path

import onnx
import onnx.version_converter
from onnxruntime.quantization.quant_utils import load_model

from .remove_pad_nodes import fold_pad_into_conv


def clean_graph_io(model):
    # Remove the 'inputs' and 'outputs' that are contained in initializer graph field:
    # these are constants and may not be considered as inputs/outputs of the graph
    initializer_names = [x.name for x in model.graph.initializer]
    for value_info in model.graph.input[:]:
        if value_info.name in initializer_names:
            model.graph.input.remove(value_info)

    for value_info in model.graph.output[:]:
        if value_info.name in initializer_names:
            model.graph.output.remove(value_info)


def replace_model_version(model):
    # Try to replace the ONNX version in the graph with the current one
    version = onnx.defs.onnx_opset_version()
    try:
        model = onnx.version_converter.convert_version(model, target_version=version)
    except Exception as e:
        warnings.warn(f"Impossible to convert model in version {version}. The model may not be "
                      f"compatible with the quantization pipeline. Reason: \n{str(e)}")
    return model


def sanitize(model):
    """Sanitize a model preparing it for quantization.

    This is a wrapping successive calls to several model transformations
    which aims at making the model quantization ready.

    Args:
        model: the input model

    Returns:
        the sanitized model
    """
    # Replace operations to match with current ONNX version
    model = replace_model_version(model)

    # Perfom optimization
    with tempfile.TemporaryDirectory(prefix="pre.quant.") as quant_tmp_dir:
        # To perfom ONNXRuntime optimization, we would like to use
        # onnxruntime.quantization.load_model, to optimize the model (when required)
        # and infer the intermediate shapes.
        # However, it always expects to read the model from a path. That is why we
        # save the input model if it is not a path.
        onnx.save_model(model, f"{quant_tmp_dir}/model.onnx")
        model_input = f"{quant_tmp_dir}/model.onnx"

        # Perform preprocessing
        model = load_model(Path(model_input), need_optimize=True)

    # Clean inputs/outputs
    clean_graph_io(model)

    # Fold pad into conv when possible
    fold_pad_into_conv(model)

    return model
