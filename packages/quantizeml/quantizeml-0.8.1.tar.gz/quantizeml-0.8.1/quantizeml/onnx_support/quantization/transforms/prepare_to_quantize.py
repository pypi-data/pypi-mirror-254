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
__all__ = ['prepare_to_quantize']

from copy import deepcopy

from .conv_to_depthwise import convert_conv_into_depthwise
from .clip_to_relu import align_clip_relu


def prepare_to_quantize(target_model):
    """Rename some operations in order to have their equivalence with quantization patterns

    Note that the model is no longer compatible with ``ONNXRuntime``.

    Args:
        model (ModelProto): the input model

    Returns:
        ModelProto: the transformed model
    """
    model = deepcopy(target_model)

    # Convert convolutional candidates into depthwise
    convert_conv_into_depthwise(model)

    # Align Clip/Relu operations
    align_clip_relu(model)

    return model
