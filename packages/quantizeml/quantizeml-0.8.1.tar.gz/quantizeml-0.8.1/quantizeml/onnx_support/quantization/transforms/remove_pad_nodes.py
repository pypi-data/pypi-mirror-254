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
__all__ = ['fold_pad_into_conv']

from onnxruntime.quantization.onnx_model import _clean_initializers_helper

from ...graph_tools import get_field, get_variable, replace_field, has_field, to_field


def fold_pad_into_conv(model):
    pre_msg_erro = "Impossible to fold {} into {}: "
    for pnode, tnode in zip(model.graph.node[:-1], model.graph.node[1:]):
        if tnode.op_type == 'Conv' and pnode.op_type == 'Pad':
            # Check valid model
            mode = get_field(pnode, "mode", "constant")
            if mode != "constant":
                raise RuntimeError(pre_msg_erro.format(pnode.name, tnode.name) +
                                   f"Unsupported '{mode}' mode.")

            # Check valid constant value
            if len(pnode.input) > 2 and pnode.input[2]:
                constant_value = get_variable(pnode.input[2], model.graph)
                if constant_value != 0:
                    raise RuntimeError(pre_msg_erro.format(pnode.name, tnode.name) +
                                       "Constant value is not zero.")

            # Input rank in a 'Conv' is the same as kernel one
            input_ndim = get_variable(tnode.input[1], model.graph).ndim

            # Retrieve pad_pads and axes (if any)
            pad_pads = get_variable(pnode.input[1], model.graph).tolist()
            if len(pnode.input) > 3 and pnode.input[3]:
                axes = get_variable(pnode.input[3], model.graph)
                axes = [x if x >= 0 else input_ndim + x for x in axes]
            else:
                axes = list(range(input_ndim))

            # Fulfill pad_pads in every dimension (filling with zero the other ones)
            for axis in range(input_ndim):
                if axis not in axes:
                    pad_len = len(pad_pads) // 2
                    pad_pads.insert(pad_len + axis, 0)
                    pad_pads.insert(axis, 0)

            # Check pad only in spatial dimensions
            if any(pad_pads[:2] + pad_pads[input_ndim:input_ndim + 2]):
                raise RuntimeError(pre_msg_erro.format(pnode.name, tnode.name) +
                                   "Pad has non-zero values on batch or channel dimension.")
            # Get only spatial pads
            new_pads = pad_pads[2:input_ndim] + pad_pads[input_ndim + 2:]

            # Replace conv pads = new + old
            if has_field(tnode, "pads"):
                target_pads = get_field(tnode, "pads", [0] * 2 * (input_ndim - 2))
                replace_field(tnode, "pads", [x + y for x, y in zip(target_pads, new_pads)])
            else:
                new_pads_attr = to_field("pads", new_pads)
                tnode.attribute.append(new_pads_attr)

            # Prune node
            tnode.input[0] = pnode.input[0]
            model.graph.node.remove(pnode)

    # Clean graph, removing pointless initializers
    _clean_initializers_helper(model.graph, model)
