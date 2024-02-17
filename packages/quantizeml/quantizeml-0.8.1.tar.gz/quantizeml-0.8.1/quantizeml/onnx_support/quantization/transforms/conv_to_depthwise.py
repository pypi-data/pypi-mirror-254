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
__all__ = ["convert_conv_into_depthwise"]


from ...graph_tools import get_field, get_variable


def convert_conv_into_depthwise(model):
    for node in model.graph.node:
        if node.op_type == 'Conv':
            groups = get_field(node, "group", 1)
            if groups == 1:
                continue
            # A convolutional could be transformed into depthwise if:
            # * groups is equal to the filters
            # * kernel shape in input channel axis is equal to 1
            # Remember input shape is BCXY and kernel shape is FCKxKy
            filters, c_shape = get_variable(node.input[1], model.graph).shape[:2]
            if groups != filters:
                raise RuntimeError(f"Impossible to handle groups = {groups} on {node.name} node. "
                                   f"Expected ({filters}) number of filters.")
            elif c_shape != 1:
                raise RuntimeError(f"Impossible to handle kernel shape on {node.name} node. "
                                   f"Expected ({c_shape}) in axis=1 in the kernel shape.")
            node.op_type = 'DepthwiseConv'
