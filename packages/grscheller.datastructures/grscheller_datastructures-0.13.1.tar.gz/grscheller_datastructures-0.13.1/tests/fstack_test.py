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

from grscheller.datastructures.stacks import FStack
from itertools import chain

class Test_FStack:
    def test_consHeadTail(self):
        s1 = FStack()
        s2 = s1.cons(42)
        head = s2.head(())
        assert head == 42
        head = s1.head(())
        assert head == ()
        s3 = s2.cons(1).cons(2).cons(3)
        s4 = s3.tail()
        assert s4 == FStack(42, 1, 2)
        assert s1 == FStack()
        s0 = s1.tail(s1.cons(42).cons(0))
        assert s0 == FStack(42, 0)

    def test_headOfEmptyStack(self):
        s1 = FStack()
        assert s1.head() is None

        s2 = FStack(1, 2, 3, 42)
        while s2:
            assert s2.head() is not None
            s2 = s2.tail()
            if not s2:
                break
        assert not s2
        assert len(s2) == 0
        assert s2.head() is None
        s2 = s2.cons(42)
        assert s2.head() == 40+2

    def test_Stacklen(self):
        s0 = FStack()
        s1 = FStack(*range(0,2000))

        assert len(s0) == 0
        assert len(s1) == 2000
        s0 = s0.cons(42)
        s1 = s1.tail().tail()
        assert len(s0) == 1
        assert len(s1) == 1998

    def test_tailcons(self):
        s1 = FStack()
        s1 = s1.cons("fum").cons("fo").cons("fi").cons("fe")
        assert type(s1) == FStack
        s2 = s1.tail()
        if s2 is None:
            assert False
        s3 = s2.cons("fe")
        assert s3 == s1
        while s1:
            s1 = s1.tail()
        assert s1.head() is None
        assert s1.tail() == FStack()

    def test_stackIter(self):
        giantStack = FStack(*[" Fum", " Fo", " Fi", "Fe"])
        giantTalk = giantStack.head()
        giantStack = giantStack.tail()
        assert giantTalk == "Fe"
        for giantWord in giantStack:
            giantTalk += giantWord
        assert len(giantStack) == 3
        assert giantTalk == "Fe Fi Fo Fum"

        es = FStack()
        for _ in es:
            assert False

    def test_equality(self):
        s1 = FStack(*range(3))
        s2 = s1.cons(42)
        assert s2 is not None  # How do I let the typechecker
                               # know this can't be None?
        assert s1 is not s2
        assert s1 is not s2.tail()
        assert s1 != s2
        assert s1 == s2.tail()

        assert s2.head() == 42

        s3 = FStack(range(10000))
        s4 = s3.copy()
        assert s3 is not s4
        assert s3 == s4
        
        s3 = s3.cons(s4.head())
        s4 = s4.tail()
        assert s3 is not s4
        assert s3 != s4
        assert s3 is not None  # Not part of the tests,
                               # code idiot checking.
        s3 = s3.tail().tail()
        assert s3 == s4
        assert s3 is not None
        assert s4 is not None

        s5 = FStack(*[1,2,3,4])
        s6 = FStack(*[1,2,3,42])
        assert s5 != s6
        for aa in range(10):
            s5 = s5.cons(aa)
            s6 = s6.cons(aa)
        assert s5 != s6

        ducks = ["huey", "dewey"]
        s7 = FStack(ducks)
        s8 = FStack(ducks)
        s9 = FStack(["huey", "dewey", "louie"])
        assert s7 == s8
        assert s7 != s9
        assert s7.head() == s8.head()
        assert s7.head() is s8.head()
        assert s7.head() != s9.head()
        assert s7.head() is not s9.head()
        ducks.append("louie")
        assert s7 == s8
        assert s7 == s9
        s7 = s7.cons(['moe', 'larry', 'curlie'])
        s8 = s8.cons(['moe', 'larry'])
        assert s7 != s8
        assert s8 is not None
        s8.head(default = []).append("curlie")
        assert s7 == s8

    def test_doNotStoreNones(self):
        s1 = FStack()
        assert s1.cons(None) == s1
        s2 = s1.cons(42)
        assert len(s2) == 1
        assert s2
        s2 = s2.tail()
        assert not s1
        assert not s2
        assert len(s2) == 0

    def test_reversing(self):
        s1 = FStack('a', 'b', 'c', 'd')
        s2 = FStack('d', 'c', 'b', 'a')
        assert s1 != s2
        assert s2 == FStack(*iter(s1))
        s0 = FStack()
        assert s0 == FStack(*iter(s0))
        s2 = FStack(chain(iter(range(1, 100)), iter(range(98, 0, -1))))
        s3 = FStack(*iter(s2))
        assert s3 == s2

    def test_reversed(self):
        lf = [1.0, 2.0, 3.0, 4.0]
        lr = [4.0, 3.0, 2.0, 1.0]
        s1 = FStack(*lr)
        l_s1 = list(s1)
        l_r_s1 = list(reversed(s1))
        assert lf == l_s1
        assert lr == l_r_s1
        s2 = FStack(*lf)
        while s2:
            assert s2.head() == lf.pop()
            s2 = s2.tail()
        assert len(s2) == 0

    def test_reverse(self):
        fs1 = FStack(1, 2, 3, 'foo', 'bar')
        fs2 = FStack('bar', 'foo', 3, 2, 1)
        assert fs1 == fs2.reverse()
        assert fs1 == fs1.reverse().reverse()
        assert fs1.head(42) != fs2.head(42)
        assert fs1.head() == fs2.reverse().head(42)

        fs3 = FStack(1, 2, 3)
        assert fs3.reverse() == FStack(3, 2, 1)
        fs4 = fs3.reverse()
        assert fs3 is not fs4
        assert fs3 == FStack(1, 2, 3)
        assert fs4 == FStack(3, 2, 1)
        assert fs3 == fs3.reverse().reverse()

    def test_map(self):
        s1 = FStack(1,2,3,4,5)
        s2 = s1.map(lambda x: 2*x+1)
        assert s1.head() == 5
        assert s2.head() == 11
        s3 = s2.map(lambda y: (y-1)//2)
        assert s1 == s3
        assert s1 is not s3

    def test_flatMap1(self):
        c1 = FStack(2, 1, 3)
        c2 = c1.flatMap(lambda x: FStack(*range(x, 3*x)))
        assert c2 == FStack(2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8)
        c3 = FStack()
        c4 = c3.flatMap(lambda x: FStack(x, x+1))
        assert c3 == c4 == FStack()
        assert c3 is not c4

    def test_flatMap2(self):
        c0 = FStack()
        c1 = FStack(2, 1, 3)
        assert c1.flatMap(lambda x: FStack(*range(x, 3*x))) == FStack(2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8)
        assert c1.flatMap(lambda x: FStack(x, x+1)) == FStack(2, 3, 1, 2, 3, 4)
        assert c0.flatMap(lambda x: FStack(x, x+1)) == FStack()

    def test_mergeMap1(self):
        c1 = FStack(2, 1, 3)
        c2 = c1.mergeMap(lambda x: FStack(*range(x, 3*x)))
        assert c2 == FStack(2, 1, 3, 3, 2, 4)
        c3 = FStack()
        c4 = c3.mergeMap(lambda x: FStack(x, x+1))
        assert c3 == c4 == FStack()
        assert c3 is not c4

    def test_mergeMap2(self):
        c0 = FStack()
        c1 = FStack(2, 1, 3)
        assert c1.mergeMap(lambda x: FStack(*range(x, 2*x+1))) == FStack(2, 1, 3, 3, 2, 4)
        assert c1.mergeMap(lambda x: FStack(x, x+1)) == FStack(2, 1, 3, 3, 2, 4)
        assert c0.mergeMap(lambda x: FStack(x, x+1)) == FStack()

    def test_exhaustMap1(self):
        c1 = FStack(2, 1, 3)
        assert c1.exhaustMap(lambda x: FStack(*range(x, 3*x))) == FStack(2, 1, 3, 3, 2, 4, 4, 5, 5, 6, 7, 8)
        c3 = FStack()
        c4 = c3.exhaustMap(lambda x: FStack(x, x+1))
        assert c3 == c4 == FStack()
        assert c3 is not c4

    def test_exhaustMap2(self):
        c0 = FStack()
        c1 = FStack(2, 1, 3)
        assert c0.exhaustMap(lambda x: FStack(x, x+1)) == FStack()
        assert c1.exhaustMap(lambda x: FStack(x, x+1)) == FStack(2, 1, 3, 3, 2, 4)
        assert c1.exhaustMap(lambda x: FStack(*range(x, 2*x+1))) == FStack(2, 1, 3, 3, 2, 4, 4, 5, 6)
        assert c1.exhaustMap(lambda _: FStack()) == FStack()
