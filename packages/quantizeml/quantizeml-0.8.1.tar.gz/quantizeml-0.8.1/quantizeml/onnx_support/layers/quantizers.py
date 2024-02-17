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
__all__ = ["InputQuantizer", "Dequantizer"]

import numpy as np

from onnx.helper import make_node
from .base_layer import OnnxLayer
from ..graph_tools.tensor import TENSOR_SHAPE, value_info_to_tensor_shape, array_to_tp

from ..quantization.input_scale import input_zp_scale


class InputQuantizer(OnnxLayer):
    """Intermediate representation of QuantizeLinear(), use to quantize the input.

    Args:
        input_tp (TensorProto): the input of the ONNX model.
        input_signed (bool, optional): whether the input is signed. Defaults to False.
        name (str, optional): the node name. Defaults to ''.
    """

    def __init__(self, input_tp, input_signed=False, name=''):
        super().__init__("InputQuantizer", name=name)
        self.input_signed = input_signed
        self._input = [input_tp]

    def __build__(self, downscale=True):
        assert downscale, f"{self.name} ({self.base_name}) does not support 32bit output"
        input_ts = value_info_to_tensor_shape(self.input)
        assert input_ts.dtype == np.float32

        # Add weights
        zp_dtype = "int8" if self.input_signed else "uint8"
        self._add_weight("zero_point", value=np.zeros(input_ts.shape[1]), dtype=zp_dtype)

        # Compute output shape
        output_ts = TENSOR_SHAPE(input_ts.shape, np.dtype(zp_dtype))
        return output_ts

    def __quantize__(self, out_tensor_range, force_fp=False):
        if force_fp:
            raise NotImplementedError("Force input scale to be a FP is not implemented yet.")
        # Compute output scale
        input_scale, input_zp = input_zp_scale(out_tensor_range, allow_zp=not self.input_signed)

        # Scale to set in weights is the reciprocal of ONNX calibrated one.
        scale = np.array(1 / input_scale, dtype=np.float32)

        # Save zero point (used by next layer)
        self.set_weight("zero_point", input_zp)

        # Compute weights to serialize
        weights = {f"{self.name}/input_scale": scale, f"{self.name}/input_zp": input_zp}
        return weights, input_scale

    @staticmethod
    def build_subgraph(op_type):
        return [make_node('QuantizeLinear', inputs=["X", "scale", "zp"], outputs=["Y"])]


class Dequantizer(OnnxLayer):
    """Intermediate representation of DequantizeLinear(), use to dequantize the input.

    Args:
        name (str, optional): the node name. Defaults to ''.
    """

    def __init__(self, name=''):
        super().__init__("Dequantizer", name=name)

    def __build__(self, input_ts, downscale=True):
        assert input_ts.dtype in (np.int8, np.int32)

        # Compute output shape
        output_ts = TENSOR_SHAPE(input_ts.shape, np.dtype("float32"))
        return output_ts

    def quantize(self, qinput):
        # To keep homogenity with the other layers, this function is called 'quantize'
        # even though it does the opposite (dequantize): apply scale in the input integers.
        if self._output is None or self._input is None:
            # Build the layer if required
            self.build(qinput.output)

        # Scale to set in weights is the reciprocal of ONNX calibrated one.
        i_scale = qinput.weights["scale"]
        scale = np.array(1 / i_scale, dtype=np.float32)

        # Return ONNX node and weights
        weights = {f"{self.name}/deq_scale": scale}
        inputs = [ts.name for ts in self._input] + list(weights)
        onnx_node = self.make_node(inputs, [self.output.name])
        onnx_weights = array_to_tp(**weights)
        return onnx_node, onnx_weights

    @staticmethod
    def build_subgraph(op_type):
        return [make_node('DequantizeLinear', inputs=["X", 'scale'], outputs=["Y"])]
