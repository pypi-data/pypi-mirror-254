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

import grscheller.datastructures.core.nodes as nodes

class Test_SL_Node:
    def test_bool(self):
        n1 = nodes.SL_Node(1, None)
        n2 = nodes.SL_Node(2, n1)
        assert n1
        assert n2

    def test_linking(self):
        n1 = nodes.SL_Node(1, None)
        n2 = nodes.SL_Node(2, n1)
        n3 = nodes.SL_Node(3, n2)
        assert n3._data == 3
        assert n3._next is not None
        assert n3._next._next is not None
        assert n2._next is not None
        assert n2._data == n3._next._data == 2
        assert n1._data == n2._next._data == n3._next._next._data == 1
        assert n3._next is not None
        assert n3._next._next is not None
        assert n3._next._next._next is None
        assert n3._next._next == n2._next

class Test_Tree_Node:
    def test_bool(self):
        tn1 = nodes.Tree_Node(42, None, None)
        tn2 = nodes.Tree_Node('Monty', tn1, None)
        tn3 = nodes.Tree_Node('Python', None, tn2)
        tn4 = nodes.Tree_Node('Monty Python', tn1, tn2)
        tn0 = nodes.Tree_Node(None, None, None)
        assert tn1
        assert tn2
        assert tn3
        assert tn4
        assert tn0
