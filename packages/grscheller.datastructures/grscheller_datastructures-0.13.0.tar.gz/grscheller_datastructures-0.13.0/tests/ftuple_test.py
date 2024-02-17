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

from grscheller.datastructures.tuples import FTuple

class TestFTuple:
    def test_method_returns_copy(self):
        ft1 = FTuple(1, 2, 3, 4, 5, 6)
        ft2 = ft1.map(lambda x: x % 3)
        assert ft2[2] == ft2[5] == 0
        assert 2*ft1[2] == ft1[5] == 6
        ft3 = ft1.reverse()
        assert ft3 == FTuple(6, 5, 4, 3, 2, 1)
        assert ft1 == FTuple(1, 2, 3, 4, 5, 6)

    def test_empty(self):
        ft1 = FTuple()
        ft2 = FTuple()
        assert ft1 == ft2
        assert ft1 is not ft2
        assert not ft1
        assert not ft2
        assert len(ft1) == 0
        assert len(ft2) == 0
        ft3 = ft1 + ft2
        assert ft3 == ft2 == ft3
        assert ft3 is not ft1
        assert ft3 is not ft2
        assert not ft3
        assert len(ft3) == 0
        assert type(ft3) == FTuple
        ft4 = ft3.copy()
        assert ft4 == ft3
        assert ft4 is not ft3
        ft1_rev = ft1.reverse()
        assert ft1_rev == ft1
        assert ft1_rev is not ft1
        assert not ft1_rev
        assert len(ft1_rev) == 0

        assert ft1[0] is None
        assert ft2[42] is None

    def test_reverse(self):
        ft1 = FTuple(1, 2, 3, 'foo', 'bar')
        ft2 = FTuple('bar', 'foo', 3, 2, 1)
        assert ft1 == ft2.reverse()
        assert ft1 == ft1.reverse().reverse()
        assert ft1[1] == ft2[-2]

        ft3 = ft1 + ft2
        assert ft3 == ft3.reverse()
        ft4 = ft3 + FTuple(42)
        ft4_rev = ft4.reverse()
        assert ft4 != ft4_rev
        assert ft4[-1] == ft4_rev[0]

        ft5 = FTuple(1, 2, 3)
        assert ft5.reverse() == FTuple(3, 2, 1)
        ft6 = ft5.reverse()
        assert ft5 is not ft6
        assert ft5 == FTuple(1, 2, 3)
        assert ft6 == FTuple(3, 2, 1)
        assert ft5 == ft5.reverse().reverse()
