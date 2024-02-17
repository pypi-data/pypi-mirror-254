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
__all__ = ["nodes_to_ops_list", "get_node"]


def nodes_to_ops_list(nodes):
    """Helper to convert a list of nodes to a list of op types.

    Args:
        nodes (list of NodeProto): list of nodes.

    Returns:
        list of str: list of op types.
    """
    return tuple(node.op_type for node in nodes)


def get_node(nodes, op_type):
    """Helper to get a node of a specific type.

    Args:
        nodes (list of NodeProto): list of nodes.
        op_type (str): the type of the node to get.

    Returns:
        NodeProto: the node if found, None otherwise.
    """
    filtered_ops = [node for node in nodes if node.op_type == op_type]
    if len(filtered_ops) != 1:
        # Return None if not found or too many
        return None
    return filtered_ops[0]
