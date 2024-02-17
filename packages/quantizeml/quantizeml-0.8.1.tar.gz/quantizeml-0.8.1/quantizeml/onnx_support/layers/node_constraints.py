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
__all__ = ["check_supported_attributes"]

from ..graph_tools import get_field


def check_supported_attributes(nodes_block):
    """Helper to check supported attribute values

    Args:
        nodes_block (NodeProto): the block node to check.
    """
    for node in nodes_block:
        if node.op_type in ["Conv", "DepthwiseConv"]:
            auto_pad = get_field(node, 'auto_pad', 'NOTSET')
            if auto_pad != 'NOTSET':
                raise NotImplementedError(f"{auto_pad} is not implemented yet.")
            dilations = get_field(node, 'dilations', [1])
            if any(x != 1 for x in dilations):
                raise NotImplementedError(f"Unsupported dilations: {dilations}.")
        elif node.op_type == "Flatten":
            axis = get_field(node, 'axis', 1)
            if axis != 1:
                raise ValueError(f"Unsupported axis ({axis}) in {node.name} ({node.op_type}).")
        elif node.op_type == "Gemm":
            alpha = get_field(node, 'alpha', 1.0)
            beta = get_field(node, 'beta', 1.0)
            transA = get_field(node, 'transA', 0)
            transB = get_field(node, 'transB', 1)
            if alpha != 1.0 or beta != 1.0 or bool(transA) or not bool(transB):
                raise ValueError(f"Unsupported {node.name} ({node.op_type}) attributes. "
                                 "Expected: alpha = beta = 1.0, transA = 0 and transB = 1.")
