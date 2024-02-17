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
__all__ = ['align_clip_relu']

from ...graph_tools import get_variable


def align_clip_relu(model):
    pre_msg_erro = "Impossible to handle Clip {} node: "
    for node in model.graph.node:
        if node.op_type == 'Clip':
            if len(node.input) == 1 or not node.input[1]:
                raise RuntimeError(pre_msg_erro.format(node.name) + "Expected a min_value input.")

            # Check if it is possible to convert a Clip into a Relu(max_value).
            # Both operations are compatible if min_value = 0.
            min_value = get_variable(node.input[1], model.graph)
            if min_value != 0:
                raise RuntimeError(pre_msg_erro.format(node.name) + "min_value must be zero.")

            node.op_type = "Relu"
