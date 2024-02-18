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

from grscheller.datastructures.core.fp import Maybe, Nothing, Some
from grscheller.datastructures.core.fp import Either, Left, Right
from grscheller.datastructures.core.fp import maybeToEither, eitherToMaybe

def add2(x):
    return x + 2

class TestMaybe:
    def test_identity(self):
        n1 = Maybe()
        n2 = Maybe()
        o1 = Maybe(42)
        o2 = Maybe(40)
        assert o1 is o1
        assert o1 is not o2
        o3 = o2.map(add2)
        assert o3 is not o2
        assert o1 is not o3
        assert n1 is n1
        assert n1 is not n2
        assert o1 is not n1
        assert n2 is not o2

    def test_equality(self):
        n1 = Maybe()
        n2 = Maybe()
        o1 = Maybe(42)
        o2 = Maybe(40)
        assert o1 == o1
        assert o1 != o2
        o3 = o2.map(add2)
        assert o3 != o2
        assert o1 == o3
        assert n1 == n1
        assert n1 == n2
        assert o1 != n1
        assert n2 != o2

    def test_iterate(self):
        o1 = Maybe(38)
        o2 = o1.map(add2).map(add2)
        n1 = Maybe()
        l1 = []
        l2 = []
        for v in n1:
            l1.append(v)
        for v in o2:
            l2.append(v)
        assert len(l1) == 0
        assert len(l2) == 1
        assert l2[0] == 42

    def test_get(self):
        o1 = Maybe(1)
        n1 = Maybe()
        assert o1.get(42) == 1
        assert n1.get(42) == 42
        assert o1.get() == 1
        assert n1.get() is None
        assert n1.get(13) == (10 + 3)
        assert n1.get(10/7) == (10/7)

    def test_some(self):
        o1 = Some(42)
        n1 = Some(None)
        n2 = Some()
        assert n1 == n2
        o2 = o1.map(lambda x: x // 2) 
        assert o2 == Some(21)
        o3 = o1.map(lambda _: None) 
        assert o3 == Some() == Nothing

    def test_nothing(self):
        o1 = Maybe(42)
        n1 = Maybe()
        n2 = n1
        assert o1 != Nothing
        assert n1 == Nothing
        assert n1 is n1
        assert n1 is n2

class TestEither:
    def test_identity(self):
        e1 = Left(42)
        e2 = Either(42)
        e3 = Right('not 42')
        e4 = Right('not 42')
        e5 = Right('also not 42')
        e6 = e3
        assert e1 is e1
        assert e1 is not e2
        assert e1 is not e3
        assert e1 is not e4
        assert e1 is not e5
        assert e1 is not e6
        assert e2 is e2
        assert e2 is not e3
        assert e2 is not e4
        assert e2 is not e5
        assert e2 is not e6
        assert e3 is e3
        assert e3 is not e4
        assert e3 is not e5
        assert e3 is e6
        assert e4 is e4
        assert e4 is not e5
        assert e4 is not e6
        assert e5 is e5
        assert e5 is not e6
        assert e6 is e6

    def test_equality(self):
        e1 = Left(42)
        e2 = Left(42)
        e3 = Right('not 42')
        e4 = Right('not 42')
        e5 = Right('also not 42')
        e7 = e3
        assert e1 == e1
        assert e1 == e2
        assert e1 != e3
        assert e1 != e4
        assert e1 != e5
        assert e1 != e7
        assert e2 == e2
        assert e2 != e3
        assert e2 != e4
        assert e2 != e5
        assert e2 != e7
        assert e3 == e3
        assert e3 == e4
        assert e3 != e5
        assert e3 == e7
        assert e4 == e4
        assert e4 != e5
        assert e4 == e7
        assert e5 == e5
        assert e5 != e7
        assert e7 == e7

    def test_either_right(self):
        def noMoreThan5(x: int) -> int|None:
            if x <= 5:
                return x
            else:
                return None

        s1 = Left(3, right = 'foofoo rules')
        s2 = s1.map(noMoreThan5, 'more than 5')
        s3 = Left(42, right = 'foofoo rules')
        s4 = s3.map(noMoreThan5, 'more than 5')
        assert s1 == Left(3)
        assert s2 == Left(3)
        assert s4 == Right('more than 5')
        assert s1.getRight() == None
        assert s2.getRight() == None
        assert s3.getRight() == None
        assert s4.getRight() == 'more than 5'
        assert s1.get('nothing doing') == 3
        assert s3.get('nothing doing') == 42
        assert s4.get('nothing doing') == 'nothing doing'
        assert s4.getRight() == 'more than 5'

    def test_foldL_maybe(self):
        mb21 = Some(21)
        mbNot = Some()
        val21 = mb21.foldL(lambda x, y: x*y)
        val42 = mb21.foldL(lambda x, y: x*y, 2)
        val7 = mb21.foldL(lambda x, y: y//x, 3)
        valNone = mbNot.foldL(lambda x, y: y//x)
        valAlsoNone = mbNot.foldL(lambda x, y: y//x, 3)
        assert val21 == 21
        assert val42 == 42
        assert val7 == 7
        assert valNone == None
        assert valAlsoNone == None

    def test_accummulate_maybe(self):
        mb21 = Some(21)
        mbNot = Some()
        ph21 = mb21.accummulate()
        ph7 = mb21.accummulate(lambda x, y: y//x, 3)
        phNot = mbNot.accummulate()
        phAlsoNot = mbNot.accummulate(lambda x, y: y//x, 3)
        assert ph21 == Some(21)
        assert ph7 == Some(7)
        assert phAlsoNot == Nothing
        assert phNot == Nothing

    def test_foldL_either(self):
        lt42 = Left(42)
        lt13 = Left(13)
        rtNotInt = Right('Not an int')
        val42 = lt42.foldL(lambda x, y: x*y)
        val21 = lt42.foldL(lambda x, y: y//x, 2)
        valNotInt = rtNotInt.foldL(lambda x, y: y//x)
        valAlsoNotInt = rtNotInt.foldL(lambda x, y: y//x, 3)
        assert val42 == 42
        assert val21 == 21
        assert valNotInt == None
        assert valAlsoNotInt == None

    def test_accummulate_either(self):
        lt10 = Left(10)
        lt10accu = lt10.accummulate()
        lt30 = lt10.accummulate(lambda x, y: x*y, None, initial=3, right=' never')
        rtA = Right('A, ')
        rtB = rtA.accummulate(right='B, ')
        rtC = rtA.accummulate(lambda x, y: x*y, initial=3, right='C, ')
        assert lt10 == Left(10)
        assert lt10accu == Left(10)
        assert lt30 == Left(30)
        assert rtA == Right('A, ')
        assert rtB == Right('A, B, ')
        assert rtC == Right('A, C, ')

    def test_maybe_flatMap(self):
        mb10 = Maybe(10)
        mbNot = Maybe()
        mb20 = mb10.flatMap(lambda x: Maybe(2*x))
        mbNotA = mbNot.flatMap(lambda x: Maybe(2*x))
        mbNotB = mb10.flatMap(lambda _: Maybe())
        mbNotC = mbNot.flatMap(lambda _: Maybe())
        assert mb20 == Maybe(20)
        assert mbNotA == Nothing
        assert mbNotB == Nothing
        assert mbNotC == Nothing

        mb20 = mb10.mergeMap(lambda x: Maybe(2*x))
        mbNotA = mbNot.mergeMap(lambda x: Maybe(2*x))
        mbNotB = mb10.mergeMap(lambda _: Maybe())
        mbNotC = mbNot.mergeMap(lambda _: Maybe())
        assert mb20 == Maybe(20)
        assert mbNotA == Nothing
        assert mbNotB == Nothing
        assert mbNotC == Nothing

        mb20 = mb10.exhaustMap(lambda x: Maybe(2*x))
        mbNotA = mbNot.exhaustMap(lambda x: Maybe(2*x))
        mbNotB = mb10.exhaustMap(lambda _: Maybe())
        mbNotC = mbNot.exhaustMap(lambda _: Maybe())
        assert mb20 == Maybe(20)
        assert mbNotA == Nothing
        assert mbNotB == Nothing
        assert mbNotC == Nothing

    def test_either_flatMaps(self):
        def lessThan2(x: int) -> Either:
            if x < 2:
                return Either(x)
            else:
                return Either(None, '>=2')

        def lessThan5(x: int) -> Either:
            if x < 5:
                return Left(x)
            else:
                return Right('>=5')

        left1 = Left(1)
        left4 = Left(4)
        left7 = Left(7)
        right = Right('Nobody home')

        nobody = right.flatMap(lessThan2)
        assert nobody == Right('Nobody home')

        lt2 = left1.flatMap(lessThan2)
        lt5 = left1.flatMap(lessThan5)
        assert lt2 == Left(1)
        assert lt5 == Left(1)

        lt2 = left4.flatMap(lessThan2)
        lt5 = left4.flatMap(lessThan5)
        assert lt2 == Right('>=2')
        assert lt5 == Left(4)

        lt2 = left7.flatMap(lessThan2)
        lt5 = left7.flatMap(lessThan5)
        assert lt2 == Right('>=2')
        assert lt5 == Right('>=5')

        nobody = right.flatMap(lessThan5, 'NOBODY HOME')
        assert nobody == Right('NOBODY HOME')

        lt2 = left1.flatMap(lessThan2, 'greater than or equal 2')
        lt5 = left1.flatMap(lessThan5, 'greater than or equal 5')
        assert lt2 == Left(1)
        assert lt5 == Left(1)

        lt2 = left4.flatMap(lessThan2, 'greater than or equal 2')
        lt5 = left4.flatMap(lessThan5, 'greater than or equal 5')
        assert lt2 == Right('greater than or equal 2')
        assert lt5 == Left(4)

        lt2 = left7.flatMap(lessThan2, 'greater than or equal 2')
        lt5 = left7.flatMap(lessThan5, 'greater than or equal 5')
        assert lt2 == Right('greater than or equal 2')
        assert lt5 == Right('greater than or equal 5')


        nobody = right.mergeMap(lessThan2)
        assert nobody == Right('Nobody home')

        lt2 = left1.mergeMap(lessThan2)
        lt5 = left1.mergeMap(lessThan5)
        assert lt2 == Left(1)
        assert lt5 == Left(1)

        lt2 = left4.mergeMap(lessThan2)
        lt5 = left4.mergeMap(lessThan5)
        assert lt2 == Right('>=2')
        assert lt5 == Left(4)

        lt2 = left7.mergeMap(lessThan2)
        lt5 = left7.mergeMap(lessThan5)
        assert lt2 == Right('>=2')
        assert lt5 == Right('>=5')

        nobody = right.mergeMap(lessThan5, ', but us chickens!')
        assert nobody == Right('Nobody home, but us chickens!')

        lt2 = left1.mergeMap(lessThan2, ', tested for 2')
        lt5 = left1.mergeMap(lessThan5, ', tested for 5')
        assert lt2 == Left(1)
        assert lt5 == Left(1)

        lt2 = left4.mergeMap(lessThan2, ', tested for 2')
        lt5 = left4.mergeMap(lessThan5, ', tested for 5')
        assert lt2 == Right('>=2, tested for 2')
        assert lt5 == Left(4)

        lt2 = left7.mergeMap(lessThan2, ', tested for 2')
        lt5 = left7.mergeMap(lessThan5, ', tested for 5')
        assert lt2 == Right('>=2, tested for 2')
        assert lt5 == Right('>=5, tested for 5')
        
    def test_Maybe_Either(self):
        mb42 = Some(42)
        mbNot = Nothing

        left42 = maybeToEither(mb42)
        right = maybeToEither(mbNot, 'Nobody home')
        assert left42 == Left(42)
        assert right == Right('Nobody home')

        ph42 = eitherToMaybe(left42)
        phNot = eitherToMaybe(right)
        assert mb42 == ph42
        assert mbNot == phNot
