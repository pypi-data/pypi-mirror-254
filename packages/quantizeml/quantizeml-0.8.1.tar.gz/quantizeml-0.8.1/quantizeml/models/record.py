#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
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
"""
Recording utilities.
"""

__all__ = ["record_quantization_variables"]

import numpy as np
import tensorflow as tf

from .transforms.transforms_utils import get_layers_by_type
from ..layers import recording, StatefulRecurrent, reset_states


def record_quantization_variables(model):
    """Helper method to record quantization objects in the graph.

    Passing a dummy sample through the model in recording mode, this triggers the
    recording of all dynamic quantization objects.

    Args:
        model (keras.Model): model for which objects need to be recorded.
    """
    def _gen_dummy_sample(shape, type=np.float32):
        if issubclass(type, np.floating):
            sample = np.random.randint(0, 255, size=(1, *shape))
            return sample.astype(type)
        return np.random.randint(np.iinfo(type).min, np.iinfo(type).max,
                                 size=(1, *shape), dtype=type)

    recurrent_layers = get_layers_by_type(model, StatefulRecurrent)

    with recording(True):
        if len(recurrent_layers):
            # Reset model (states and counter) to ensure a proprer recording
            reset_states(model)
            # Build a tf.function to run in graph mode
            model_func = tf.function(model)
            # The number of samples that will allow proper recording is equal to the lowest
            # common multiple among the subsampling ratios found in the model.
            sub_sample_ratios = []
            for rec in recurrent_layers:
                sub_sample_ratios.append(rec.subsample_ratio)
            num_samples = 2 * np.lcm.reduce(sub_sample_ratios)
            # For recurrent models, inputs are expected to be int16 so random samples are generated
            # accordingly
            sample = _gen_dummy_sample((num_samples, ) + model.input.shape[1:], np.int16)
            # Custom loop to ensure counter and subsampling ratio condition are met
            for i in range(num_samples):
                model_func(sample[:, i, :])
            # Reset model again
            reset_states(model)
        else:
            # Create sample and pass it through the model to calibrate variables
            sample = _gen_dummy_sample(model.input.shape[1:])
            model(sample)
