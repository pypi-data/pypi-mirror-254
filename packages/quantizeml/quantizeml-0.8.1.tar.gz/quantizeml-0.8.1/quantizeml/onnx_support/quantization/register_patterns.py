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
__all__ = ["custom_pattern_scope"]

from collections import namedtuple
from inspect import signature
from contextlib import contextmanager
from .. import layers as onnx_qlayers

# Define named tuples for QuantizerPattern
QuantizePattern = namedtuple('QuantizerPattern', ['pattern', 'f'])

# List of supported patterns, together with matching function
CUSTOM_PATTERNS_MAP = []
PATTERNS_MAP = [
    QuantizePattern(("Conv", "Relu", "GlobalAveragePool"), onnx_qlayers.get_qconv),
    QuantizePattern(("Conv", "Relu", "MaxPool"), onnx_qlayers.get_qconv),
    QuantizePattern(("Conv", "GlobalAveragePool"), onnx_qlayers.get_qconv),
    QuantizePattern(("Conv", "Relu"), onnx_qlayers.get_qconv),
    QuantizePattern(("Conv",), onnx_qlayers.get_qconv),
    QuantizePattern(("DepthwiseConv", "Relu"), onnx_qlayers.get_qdepthwise),
    QuantizePattern(("DepthwiseConv",), onnx_qlayers.get_qdepthwise),
    QuantizePattern(("Flatten", "Gemm", "Relu"), onnx_qlayers.get_qgemm),
    QuantizePattern(("Flatten", "Gemm"), onnx_qlayers.get_qgemm),
    QuantizePattern(("Gemm", "Relu"), onnx_qlayers.get_qgemm),
    QuantizePattern(("Gemm",), onnx_qlayers.get_qgemm),
    QuantizePattern(("Add",), onnx_qlayers.get_qadd),
]


@contextmanager
def custom_pattern_scope(patterns):
    """Register a custom pattern in the context to be used at quantization time.

    A pattern is understood as a sequence of continuous operations in the graph,
    whose representation can converge in an ``OnnxLayer``.

    Args:
        patterns (dict): a list of sequence of nodes (keys) and their mapper function (values).
    """
    # Use of global parameters
    global CUSTOM_PATTERNS_MAP
    # Transform input patterns in a valid format
    qpatterns = []
    for pattern, func in patterns.items():
        qpatterns.append(_custom_pattern_to_qpattern(pattern, func))
    try:
        # Extend CUSTOM_PATTERNS_MAP with new qpatterns
        CUSTOM_PATTERNS_MAP.extend(qpatterns)
        yield
    finally:
        # Restore to previous state
        CUSTOM_PATTERNS_MAP.clear()


def _custom_pattern_to_qpattern(pattern, func):
    assert callable(func), f"function has to be a callable. Receives: {func}"
    if len(signature(func).parameters) != 2:
        raise RuntimeError("function must have two inputs: sequence_nodes and graph")
    if isinstance(pattern, str):
        pattern = (pattern,)
    if not (isinstance(pattern, tuple) and all(isinstance(x, str) for x in pattern)):
        raise ValueError(f"Pattern must be a string-tuple. Receives: {pattern}")
    return QuantizePattern(pattern, func)
