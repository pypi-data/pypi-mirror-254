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

from __future__ import annotations

from typing import Any
from grscheller.datastructures import *

class Test_FP:
    def test_foldL(self):
        ft0 = FTuple()
        fs0 = FStack()
        pa0 = PArray()
        ft1 = FTuple(1,2,3,4,5)
        fs1 = FStack(1,2,3,4,5)
        pa1 = PArray(1,2,3,4,5)
        l1 = lambda x, y: x + y
        l2 = lambda x, y: x * y
        def push(x: Any, y: Any) -> Any:   # TODO: add generic typing hints
            x.push(y)
            return x

        assert ft1.foldL(l1) == 15
        assert ft1.foldL(l1, 10) == 25
        assert ft1.foldL(l2) == 120
        assert ft1.foldL(l2, 10) == 1200
        assert ft1.foldL(push, FIFOQueue()) == FIFOQueue(1,2,3,4,5)
        assert ft0.foldL(l1) == None
        assert ft0.foldL(l1, 10) == 10
        assert ft0.foldL(push, FIFOQueue()) == FIFOQueue()

        assert fs1.foldL(l1) == 15
        assert fs1.foldL(l1, 10) == 25
        assert fs1.foldL(l2) == 120
        assert fs1.foldL(l2, 10) == 1200
        assert fs1.foldL(push, FIFOQueue()) == FIFOQueue(5,4,3,2,1)
        assert fs0.foldL(l1) == None
        assert fs0.foldL(l1, 10) == 10
        assert fs0.foldL(push, FIFOQueue()) == FIFOQueue()

        assert pa1.foldL(l1) == 15
        assert pa1.foldL(l1, 10) == 25
        assert pa1.foldL(l2) == 120
        assert pa1.foldL(l2, 10) == 1200
        assert pa1.foldL(push, FIFOQueue()) == FIFOQueue(1,2,3,4,5)
        assert pa0.foldL(l1) == None
        assert pa0.foldL(l1, 10) == 10
        assert pa0.foldL(push, FIFOQueue()) == FIFOQueue()

        assert ft1.accummulate(l1) == FTuple(1,3,6,10,15)
        assert ft1.accummulate(l1, 10) == FTuple(10,11,13,16,20,25)
        assert ft1.accummulate(initial=20) == FTuple(20,21,23,26,30,35)
        assert ft1.accummulate(l2) == FTuple(1,2,6,24,120)
        assert ft1.accummulate(l2, 10) == FTuple(10,10,20,60,240,1200)
        assert ft0.accummulate(l1) == FTuple()
        assert ft0.accummulate(l1, 10) == FTuple(10)

        assert fs1.accummulate(l1) == FStack(5,9,12,14,15)
        assert fs1.accummulate(l1, 10) == FStack(10,15,19,22,24,25)
        assert fs1.accummulate(initial=20) == FStack(20,25,29,32,34,35)
        assert fs1.accummulate(l2) == FStack(5,20,60,120,120)
        assert fs1.accummulate(l2, 10) == FStack(10,50,200,600,1200,1200)
        assert fs0.accummulate(l1) == FStack()
        assert fs0.accummulate(l1, 10) == FStack(10)

        assert pa1.accummulate(l1) == PArray(1,3,6,10,15)
        assert pa1.accummulate(l1, 10) == PArray(10,11,13,16,20,25)
        assert pa1.accummulate(initial=20) == PArray(20,21,23,26,30,35)
        assert pa1.accummulate(l2) == PArray(1,2,6,24,120)
        assert pa1.accummulate(l2, 10) == PArray(10,10,20,60,240,1200)
        assert pa0.accummulate(l1) == PArray()
        assert pa0.accummulate(l1, 10) == PArray(10)

    def test_ftuple_inherited(self):
        ft = FTuple(*range(3, 101))
        l1 = lambda x: 2*x + 1
        l2 = lambda x: FTuple(*range(1, x+1)).accummulate()
        ft1 = ft.map(l1)
        ft2 = ft.flatMap(l2)
        ft3 = ft.mergeMap(l2)
        ft4 = ft.exhaustMap(l2)
        assert (ft1[0], ft1[1], ft1[-1]) == (7, 9, 201)
        assert (ft2[0], ft2[1], ft2[2]) == (1, 3, 6)
        assert (ft2[3], ft2[4], ft2[5], ft2[6])  == (1, 3, 6, 10)
        assert (ft2[7], ft2[8], ft2[9], ft2[10], ft2[11])  == (1, 3, 6, 10, 15)
        assert ft2[-1] == ft2[5046] == 5050
        assert ft2[5047] is None
        assert (ft3[0], ft3[1]) == (1, 1)
        assert (ft3[2], ft3[3]) == (1, 1)
        assert (ft3[4], ft3[5]) == (1, 1)
        assert (ft3[96], ft3[97]) == (1, 1)
        assert (ft3[98], ft3[99]) == (3, 3)
        assert (ft3[194], ft3[195]) == (3, 3)
        assert (ft3[196], ft3[197]) == (6, 6)
        assert ft3[-1] == ft3[293] == 6
        assert ft3[294] is None
        assert (ft4[0], ft4[1], ft4[2]) == (1, 1, 1)
        assert (ft4[95], ft4[96], ft4[97]) == (1, 1, 1)
        assert (ft4[98], ft4[99], ft4[100]) == (3, 3, 3)
        assert (ft4[193], ft4[194], ft4[195]) == (3, 3, 3)
        assert (ft4[196], ft4[197], ft4[198]) == (6, 6, 6)
        assert ft2[-1] == ft2[5046] == 5050
        assert ft2[5047] is None
