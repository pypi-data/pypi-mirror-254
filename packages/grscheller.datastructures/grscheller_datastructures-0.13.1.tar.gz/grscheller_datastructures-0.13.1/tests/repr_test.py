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
from grscheller.datastructures.arrays import PArray
from grscheller.datastructures.stacks import Stack, FStack
from grscheller.datastructures.queues import CircularArray, DoubleQueue, FIFOQueue, LIFOQueue
from grscheller.datastructures.tuples import FTuple
from grscheller.datastructures.core.fp import Maybe, Nothing, Some, Either, Left, Right

class Test_repr:
    def test_CircularArray(self):
        ca1 = CircularArray()
        assert repr(ca1) == 'CircularArray()'
        ca2 = eval(repr(ca1))
        assert ca2 == ca1
        assert ca2 is not ca1

        ca1.pushR(1)
        ca1.pushL('foo')
        assert repr(ca1) == "CircularArray('foo', 1)"
        ca2 = eval(repr(ca1))
        assert ca2 == ca1
        assert ca2 is not ca1

        assert ca1.popL() == 'foo'
        ca1.pushR(2)
        ca1.pushR(3)
        ca1.pushR(4)
        ca1.pushR(5)
        assert ca1.popL() == 1
        ca1.pushL(42)
        ca1.popR()
        assert repr(ca1) == "CircularArray(42, 2, 3, 4)"
        ca2 = eval(repr(ca1))
        assert ca2 == ca1
        assert ca2 is not ca1

    def test_DoubleQueue(self):
        ca1 = DoubleQueue()
        assert repr(ca1) == 'DoubleQueue()'
        dq2 = eval(repr(ca1))
        assert dq2 == ca1
        assert dq2 is not ca1

        ca1.pushR(1)
        ca1.pushL('foo')
        assert repr(ca1) == "DoubleQueue('foo', 1)"
        dq2 = eval(repr(ca1))
        assert dq2 == ca1
        assert dq2 is not ca1

        assert ca1.popL() == 'foo'
        ca1.pushR(2)
        ca1.pushR(3)
        ca1.pushR(4)
        ca1.pushR(5)
        assert ca1.popL() == 1
        ca1.pushL(42)
        ca1.popR()
        assert repr(ca1) == "DoubleQueue(42, 2, 3, 4)"
        dq2 = eval(repr(ca1))
        assert dq2 == ca1
        assert dq2 is not ca1

    def test_FIFOQueue(self):
        sq1 = FIFOQueue()
        assert repr(sq1) == 'FIFOQueue()'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        sq1.push(1)
        sq1.push('foo')
        assert repr(sq1) == "FIFOQueue(1, 'foo')"
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        assert sq1.pop() == 1
        sq1.push(2)
        sq1.push(3)
        sq1.push(4)
        sq1.push(5)
        assert sq1.pop() == 'foo'
        sq1.push(42)
        sq1.pop()
        assert repr(sq1) == 'FIFOQueue(3, 4, 5, 42)'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

    def test_LIFOQueue(self):
        sq1 = LIFOQueue()
        assert repr(sq1) == 'LIFOQueue()'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        sq1.push(1)
        sq1.push('foo')
        assert repr(sq1) == "LIFOQueue(1, 'foo')"
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

        assert sq1.pop() == 'foo'
        sq1.push(2, 3)
        sq1.push(4)
        sq1.push(5)
        assert sq1.pop() == 5
        sq1.push(42)
        assert repr(sq1) == 'LIFOQueue(1, 2, 3, 4, 42)'
        sq2 = eval(repr(sq1))
        assert sq2 == sq1
        assert sq2 is not sq1

    def test_clarray(self):
        cla1 = PArray()
        assert repr(cla1) == 'PArray(size=0, default=())'

        cla1 = PArray('foo', [10, 22], size=-3, default=42)
        assert repr(cla1) == "PArray(42, 'foo', [10, 22], size=3, default=42)"

        cla1[2].append(42)
        assert repr(cla1) == "PArray(42, 'foo', [10, 22, 42], size=3, default=42)"
        assert cla1[2].pop() == 42
        assert repr(cla1) == "PArray(42, 'foo', [10, 22], size=3, default=42)"

    def test_ftuple(self):
        ft1 = FTuple()
        assert repr(ft1) == 'FTuple()'
        ft2 = eval(repr(ft1))
        assert ft2 == ft1
        assert ft2 is not ft1

        ft1 = FTuple(42, 'foo', [10, 22])
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        ft2 = eval(repr(ft1))
        assert ft2 == ft1
        assert ft2 is not ft1

        ft1[2].append(42)
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22, 42])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"
        popped = ft1[2].pop()
        assert popped == 42
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"

        # beware immutable collections of mutable objects
        ft1 = FTuple(42, 'foo', [10, 22])
        ft2 = ft1.copy()
        ft1[2].append(42)
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22, 42])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22, 42])"
        popped = ft2[2].pop()
        assert popped == 42
        assert repr(ft1) == "FTuple(42, 'foo', [10, 22])"
        assert repr(ft2) == "FTuple(42, 'foo', [10, 22])"

    def test_Stack(self):
        ps1 = Stack()
        assert repr(ps1) == 'Stack()'
        ps2 = eval(repr(ps1))
        assert ps2 == ps1
        assert ps2 is not ps1

        ps1.push(1)
        ps1.push('foo')
        assert repr(ps1) == "Stack(1, 'foo')"
        ps2 = eval(repr(ps1))
        assert ps2 == ps1
        assert ps2 is not ps1

        assert ps1.pop() == 'foo'
        ps1.push(2)
        ps1.push(3)
        ps1.push(4)
        ps1.push(5)
        assert ps1.pop() == 5
        ps1.push(42)
        assert repr(ps1) == "Stack(1, 2, 3, 4, 42)"
        ps2 = eval(repr(ps1))
        assert ps2 == ps1
        assert ps2 is not ps1

    def test_FStack(self):
        fs1 = FStack()
        assert repr(fs1) == 'FStack()'
        fs2 = eval(repr(fs1))
        assert fs2 == fs1
        assert fs2 is not fs1

        fs1 = fs1.cons(1).cons('foo')
        assert repr(fs1) == "FStack(1, 'foo')"
        fs2 = eval(repr(fs1))
        assert fs2 == fs1
        assert fs2 is not fs1

        assert fs1.head() == 'foo'
        fs1 = fs1.tail()
        fs1 = fs1.cons(2).cons(3).cons(4).cons(5)
        assert fs1.head() == 5
        fs1 = fs1.tail().cons(42)
        assert repr(fs1) == 'FStack(1, 2, 3, 4, 42)'
        fs2 = eval(repr(fs1))
        assert fs2 == fs1
        assert fs2 is not fs1

    def test_maybe(self):
        mb1 = Nothing
        mb2 = Some()
        mb3 = Some(None)
        assert mb1 == mb2 == mb3 == Nothing
        assert repr(mb2) == 'Nothing'
        mb4 = eval(repr(mb3))
        assert mb4 == mb3
        # DO NOT USE THE NEXT 4!!!
        assert mb4 is not mb3
        assert mb4 is not mb2
        assert mb2 is not mb3
        assert mb4 is mb1

        def lt5OrNone(x: Any) -> Any:
            if x < 5:
                return x
            else:
                return None

        def lt5OrNoneMaybe(x: Any) -> Maybe:
            if x < 5:
                return Some(x)
            else:
                return Nothing

        mb1 = Some(lt5OrNone(2))
        mb2 = lt5OrNoneMaybe(2)
        mb3 = lt5OrNoneMaybe(3)
        mb7 = Some(lt5OrNone(7))
        mb8 = lt5OrNoneMaybe(8)

        assert mb1 == mb2
        assert mb2 != mb3
        assert mb7 == mb8

        assert repr(mb1) == repr(mb2) ==  'Some(2)'
        assert repr(mb3) ==  'Some(3)'
        assert repr(mb7) == repr(mb8) ==  'Nothing'

        foofoo = Some(Some('foo'))
        foofoo2 = eval(repr(foofoo))
        assert foofoo2 == foofoo
        assert repr(foofoo) == "Some(Some('foo'))"

    def test_either(self):
        e1 = Right('Nobody home!')
        e2 = Left(None, 'Nobody home!')
        e3 = Left(None)
        assert e1 == e2 == Right('Nobody home!')
        e5 = eval(repr(e2))
        assert e2 == Right('Nobody home!')
        assert e5 == e2
        assert e5 != e3
        assert e5 is not e2
        assert e5 is not e3

        def lt5OrNone(x: Any) -> Any:
            if x < 5:
                return x
            else:
                return None

        def lt5OrNoneEither(x: Any) -> Either:
            if x < 5:
                return Left(x)
            else:
                return Right(f'was to be {x}')

        e1 = Left(lt5OrNone(2))
        e2 = lt5OrNoneEither(2)
        e3 = lt5OrNoneEither(3)
        e7 = Left(lt5OrNone(7), 'was to be 7')
        e8 = lt5OrNoneEither(8)

        assert e1 == e2
        assert e2 != e3
        assert e7 != e8
        assert e7 == eval(repr(e7))

        assert repr(e1) == repr(e2) ==  'Left(2)'
        assert repr(e3) ==  'Left(3)'
        assert repr(e7) == "Right('was to be 7')"
        assert repr(e8) ==  "Right('was to be 8')"

        foofoo00 = Left(Left('foo'))
        foofoo01 = Left(Right('foo'))
        foofoo10 = Right(Left('foo'))
        foofoo11 = Right(Right('foo'))
        assert repr(foofoo00) == "Left(Left('foo'))"
        assert repr(foofoo01) == "Left(Right('foo'))"
        assert repr(foofoo10) == "Right(Left('foo'))"
        assert repr(foofoo11) == "Right(Right('foo'))"

        foofoo10clone = eval(repr(foofoo10))
        assert foofoo10clone != foofoo11
        assert foofoo10clone == foofoo10
        assert foofoo10clone is not foofoo10

class Test_repr_mix:
    def test_mix1(self):
        thing1 = Left(FIFOQueue(
            FTuple(42, Some(42), Left(None, 'nobody home')),
            Stack([1, 2, 3, Nothing], 42, Left(LIFOQueue('foo', 'bar')))
        ))

        thing2 = eval(repr(thing1))
        assert thing2 == thing1
        assert thing2 is not thing1

        repr_thing1 = repr(thing1)
        repr_thing2 = repr(thing2)
        assert repr_thing2 == repr_thing1

        repr_str = "Left(FIFOQueue(FTuple(42, Some(42), Right('nobody home')), Stack([1, 2, 3, Nothing], 42, Left(LIFOQueue('foo', 'bar')))))"
        assert repr_thing1 == repr_str
