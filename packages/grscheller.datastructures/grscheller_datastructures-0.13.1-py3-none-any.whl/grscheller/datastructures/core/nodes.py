# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module grscheller.datastructure.core.nodes

Heap based nodes for for tree type data structures. Data structures should make
nodes inaccessible to client code.
"""
from __future__ import annotations

__all__ = ['SL_Node', 'Tree_Node']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any

class SL_Node():
    """Class implementing nodes that can be linked together to form a
    singularly linked list. This type of node always contain data, it
    either has a reference to the next SL_Node or None to indicate the
    bottom of the linked list of nodes.
    """
    __slots__ = '_data', '_next'

    def __init__(self, data: Any, next: SL_Node|None):
        """Construct an element of a linked list"""
        self._data = data
        self._next = next

    def __bool__(self):
        """Always return true, None will return as false"""
        return True

class Tree_Node():
    """Class implementing nodes that can be linked together to form
    a tree-like data structure. This type of node always contain data.
    """
    __slots__ = '_data', '_left', '_right'

    def __init__(self, data: Any, left: Tree_Node|None, right: Tree_Node|None):
        """Construct an element of a doubly linked list"""
        self._data = data
        self._left = left
        self._right = right

    def __bool__(self):
        """Always return true since a Tree_Node always contains data, even if
        that data is None."""
        return True

if __name__ == "__main__":
    pass
