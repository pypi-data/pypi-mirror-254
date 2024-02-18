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

from typing import Any
from grscheller.datastructures.arrays import PArray

class TestPArray:
    def test_map1(self):
        cl1 = PArray(0, 1, 2, 3, size=-6, default=-1)
        cl2 = cl1.map(lambda x: x+1, size=7, default=42)
        assert cl1[0] + 1 == cl2[0] == 0
        assert cl1[1] + 1 == cl2[1] == 0
        assert cl1[2] + 1 == cl2[2] == 1
        assert cl1[3] + 1 == cl2[3] == 2
        assert cl1[4] + 1 == cl2[4] == 3
        assert cl1[5] + 1 == cl2[5] == 4
        assert cl2[6] == 42

    def test_map2(self):
        cl1 = PArray(0, 1, 2, 3, size=6, default=-1)
        cl2 = cl1.map(lambda x: x+1)
        assert cl1[0] + 1 == cl2[0] == 1
        assert cl1[1] + 1 == cl2[1] == 2
        assert cl1[2] + 1 == cl2[2] == 3
        assert cl1[3] + 1 == cl2[3] == 4
        assert cl1[4] + 1 == cl2[4] == 0
        assert cl1[5] + 1 == cl2[5] == 0

    def test_map3(self):
        cl1 = PArray(1, 2, 3, 10)

        cl2 = cl1.map(lambda x: x*x-1)
        assert cl2 is not None
        assert cl1 is not cl2
        assert cl1 == PArray(1, 2, 3, 10)
        assert cl2 == PArray(0, 3, 8, 99)
        
    def test_default(self):
        cl1 = PArray(size=1, default=1)
        cl2 = PArray(size=1, default=2)
        assert cl1 != cl2
        assert cl1[0] == 1
        assert cl2[0] == 2
        assert not cl1
        assert not cl2
        assert len(cl1) == 1
        assert len(cl2) == 1

        foo = 42
        baz = 'hello world'

        try:
            foo = cl1[0]
        except IndexError as err:
            print(err)
            assert False
        else:
            assert True
        finally:
            assert True
            assert foo == 1

        try:
            baz = cl2[42]
        except IndexError as err:
            print(err)
            assert True
        else:
            assert False
        finally:
            assert True
            assert baz == 'hello world'

        cl1 = PArray(size=1, default=12)
        cl2 = PArray(size=1, default=30)
        assert cl1 != cl2
        assert not cl1
        assert not cl2
        assert len(cl1) == 1
        assert len(cl2) == 1

        cl0 = PArray()
        cl1 = PArray(default=())
        cl2 = PArray(None, None, None, size=2)
        cl3 = PArray(None, None, None, size=2, default=())
        assert len(cl0) == 0
        assert cl0.default() == ()
        assert len(cl1) == 0
        assert cl1.default() == ()
        assert len(cl2) == 2
        assert cl2.default() == ()
        assert len(cl3) == 2
        assert cl3.default() == ()
        assert cl2[0] == cl2[1] == ()
        assert cl3[0] == cl3[1] == ()
        assert not cl0
        assert not cl1
        assert not cl2
        assert not cl3

        cl1 = PArray(1, 2, size=3, default=42)
        cl2 = PArray(1, 2, None, size=3, default=42)
        assert cl1 == cl2
        assert cl1 is not cl2
        assert cl1
        assert cl2
        assert len(cl1) == 3
        assert len(cl2) == 3
        assert cl1[2] == cl2[2] == cl1[-1] == cl2[-1] == 42

        cl1 = PArray(1, 2, size=-3)
        cl2 = PArray((), 1, 2)
        assert cl1 == cl2
        assert cl1 is not cl2
        assert cl1
        assert cl2
        assert len(cl1) == 3
        assert len(cl2) == 3

        cl5 = PArray(*range(1,4), size=-5, default=42)
        assert cl5 == PArray(42, 42, 1, 2, 3)

    def test_set_then_get(self):
        cl = PArray(size=5, default=0)
        assert cl[1] == 0
        cl[3] = set = 42
        got = cl[3]
        assert set == got

    def test_equality(self):
        cl1 = PArray(1, 2, 'Forty-Two', (7, 11, 'foobar'))
        cl2 = PArray(1, 3, 'Forty-Two', [1, 2, 3])
        assert cl1 != cl2
        cl2[1] = 2
        assert cl1 != cl2
        cl1[3] = cl2[3]
        assert cl1 == cl2

    def test_len_getting_indexing_padding_slicing(self):
        cl = PArray(*range(2000))
        assert len(cl) == 2000

        cl = PArray(*range(542), size=42)
        assert len(cl) == 42
        assert cl[0] == 0
        assert cl[41] == cl[-1] == 41
        assert cl[2] == cl[-40]

        cl = PArray(*range(1042), size=-42)
        assert len(cl) == 42
        assert cl[0] == 1000
        assert cl[41] == 1041
        assert cl[-1] == 1041
        assert cl[41] == cl[-1] == 1041
        assert cl[1] == cl[-41] == 1001
        assert cl[0] == cl[-42]

        cl = PArray(*[1, 'a', (1, 2)], size=5, default=42)
        assert cl[0] == 1
        assert cl[1] == 'a'
        assert cl[2] == (1, 2)
        assert cl[3] == 42
        assert cl[4] == 42
        assert cl[-1] == 42
        assert cl[-2] == 42
        assert cl[-3] == (1, 2)
        assert cl[-4] == 'a'
        assert cl[-5] == 1
        try:
            foo = cl[5] 
            print(f'should never print: {foo}')
        except IndexError:
            assert True
        except Exception as error:
            print(error)
            assert False
        else:
            assert False
        try:
            bar = cl[-6] 
        except IndexError:
            assert True
        except Exception as error:
            print(error)
            assert False
        else:
            assert False

        cl = PArray(*[1, 'a', (1, 2)], size=-6, default=42)
        assert cl[0] == 42
        assert cl[1] == 42
        assert cl[2] == 42
        assert cl[3] == 1
        assert cl[4] == 'a'
        assert cl[5] == (1, 2)
        assert cl[-1] == (1, 2)
        assert cl[-2] == 'a'
        assert cl[-3] == 1
        assert cl[-4] == 42
        assert cl[-5] == 42
        assert cl[-6] == 42
        try:
            foo = cl[6] 
            print(f'should never print: {foo}')
        except IndexError:
            assert True
        except Exception as error:
            print(error)
            assert False
        else:
            assert False
        try:
            bar = cl[-7] 
            print(f'should never print: {bar}')
        except IndexError:
            assert True
        except Exception as error:
            print(error)
            assert False
        else:
            assert False

    def test_bool(self):
        cl_allNotNone = PArray(True, 0, '')
        cl_allNone = PArray(None, None, None, default=42)
        cl_firstNone = PArray(None, False, [])
        cl_lastNone = PArray(0.0, True, False, None)
        cl_someNone = PArray(0, None, 42, None, False)
        cl_defaultNone = PArray(default = None)
        cl_defaultNotNone = PArray(default = False)
        assert cl_allNotNone
        assert not cl_allNone
        assert cl_firstNone
        assert cl_lastNone
        assert cl_someNone
        assert not cl_defaultNone
        assert not cl_defaultNotNone

        cl_Nones = PArray(None, size=4321, default=())
        cl_0 = PArray(0, 0, 0)
        cl_42s = PArray(*([42]*42))
        cl_42s_d42 = PArray(*([42]*42), default=42)
        cl_emptyStr = PArray('')
        cl_hw = PArray('hello', 'world')
        assert not cl_Nones
        assert cl_0
        assert cl_42s
        assert not cl_42s_d42
        assert cl_emptyStr
        assert cl_hw

    def test_reversed_iter(self):
        """Tests that prior state of cl is used, not current one"""
        cl = PArray(1,2,3,4,5)
        clrevIter = reversed(cl)
        aa = next(clrevIter)
        assert cl[4] == aa == 5
        cl[2] = 42
        aa = next(clrevIter)
        assert cl[3] == aa == 4
        aa = next(clrevIter)
        assert cl[2] != aa == 3
        aa = next(clrevIter)
        assert cl[1] == aa == 2
        aa = next(clrevIter)
        assert cl[0] == aa == 1

    def test_reverse(self):
        cl1 = PArray(1, 2, 3, 'foo', 'bar')
        cl2 = PArray('bar', 'foo', 3, 2, 1)
        assert cl1 != cl2
        cl2.reverse()
        assert cl1 == cl2
        cl1.reverse()
        assert cl1 != cl2
        assert cl1[1] == cl2[-2]

        cl4 = cl2.copy()
        cl5 = cl2.copy()
        assert cl4 == cl5
        cl4.reverse()
        cl5.reverse()
        assert cl4 != cl2
        assert cl5 != cl2
        cl2.reverse()
        assert cl4 == cl2

    def test_copy_map(self):
        def ge3(n: int) -> int|None:
            if n < 3:
                return None
            return n

        cl4 = PArray(*range(43), size = 5)
        cl5 = PArray(*range(43), size = -5)
        cl4_copy = cl4.copy()
        cl5_copy = cl5.copy()
        assert cl4 == cl4_copy
        assert cl4 is not cl4_copy
        assert cl5 == cl5_copy
        assert cl5 is not cl5_copy
        assert cl4[0] == 0
        assert cl4[4] == cl4[-1] == 4
        assert cl5[0] == 38
        assert cl5[4] == cl5[-1] == 42

        cl0 = PArray(None, *range(1, 6), size=7, default=0)
        cl0b = PArray(*range(1, 6), size=-7, default=0)
        assert cl0 == PArray(1, 2, 3, 4, 5, 0, 0)
        assert cl0b == PArray(0, 0, 1, 2, 3, 4, 5)
        assert cl0.default() == 0
        assert cl0b.default() == 0
        cl1 = cl0.copy()
        cl2 = cl0.copy(default=4)
        assert cl1 == cl2 == cl0
        assert cl1.default() == 0
        assert cl2.default() == 4

        cl0 = cl0.map(ge3)
        cl3 = cl1.map(ge3)
        cl4 = cl2.map(ge3)
        assert cl0.default() == 0
        assert cl3.default() == 0
        assert cl4.default() == 4
        assert cl0 == PArray(0, 0, 3, 4, 5, 0, 0)
        assert cl3 == PArray(0, 0, 3, 4, 5, 0, 0)
        assert cl4 == PArray(4, 4, 3, 4, 5, 4, 4)
        assert cl3.copy(size=6).copy(size=-3) == PArray(4, 5, 0)
        assert cl3.copy(size=6).copy(size=3) == PArray(0, 0, 3)
        assert cl4.copy(size=6).copy(size=-3) == PArray(4, 5, 4)
        assert cl4.copy(size=6).copy(size=3) == PArray(4, 4, 3)
        cl5 = cl3.copy(default=2)
        cl6 = cl4.copy(default=2)
        assert cl6 != cl5
        cl7 = cl5.copy(default=-1)
        cl8 = cl6.copy(default=-1)
        assert cl8 != cl7
        assert cl8.default() == cl7.default() == -1
        assert cl8.map(ge3) != cl7.map(ge3)
        assert cl8.default() == cl7.default() == -1
        assert cl7.map(ge3) == PArray(-1, -1, 3, 4, 5, -1, -1, default = -1)

        cl0 = PArray(5,4,3,2,1)
        assert cl0.copy(size=3) == PArray(5, 4, 3)
        assert cl0.copy(size=-3) == PArray(3, 2, 1)
        cl1 = cl0.map(ge3)
        assert (cl1[0], cl1[1], cl1[2], cl1[3], cl1[4]) == (5, 4, 3, (), ())
        cl2 = cl0.copy(default=0).map(ge3)
        assert (cl2[0], cl2[1], cl2[2], cl2[3], cl2[4]) == (5, 4, 3, 0, 0)
        cl2 = cl0.map(ge3, default=42)
        assert (cl2[0], cl2[1], cl2[2], cl2[3], cl2[4]) == (5, 4, 3, 42, 42)

    def test_backQueue(self):
        cla1 = PArray(42, 'foo', 'bar', default=42)
        cla2 = cla1.copy()
        cla3 = cla1.copy(default=63)
        cla2[1] = None
        cla3[1] = None
        assert repr(cla2) == "PArray(42, 42, 'bar', size=3, default=42)"
        assert repr(cla3) == "PArray(42, 63, 'bar', size=3, default=63)"

        cla1 = PArray(16, 'foo', 'bar', 100, 101, '102', default=42)
        cla2 = cla1.copy(size=-4)
        cla3 = cla1.copy(size=4)
        assert repr(cla2) == "PArray('bar', 100, 101, '102', size=4, default=42)"
        assert repr(cla3) == "PArray(16, 'foo', 'bar', 100, size=4, default=42)"

        cla2[2] = None
        cla2[1] = None
        cla2[0] = None
        assert repr(cla2) == "PArray(42, 16, 'foo', '102', size=4, default=42)"

        cla3[-1] = None
        assert repr(cla3) == "PArray(16, 'foo', 'bar', 101, size=4, default=42)"
        cla3[-2] = None
        assert repr(cla3) == "PArray(16, 'foo', '102', 101, size=4, default=42)"
        cla3[-3] = None
        assert repr(cla3) == "PArray(16, 42, '102', 101, size=4, default=42)"

        cla4 = PArray(*range(1, 8), size=5, backlog=(42,), default=0)
        cla5 = PArray(*range(1, 8), size=-5, default=0, backlog=(42,))
        assert repr(cla4) == "PArray(1, 2, 3, 4, 5, size=5, default=0)"
        assert repr(cla5) == "PArray(3, 4, 5, 6, 7, size=5, default=0)"
    
        cla4[0] = cla4[1] = cla4[2] = cla4[3] = None
        cla5[1] = cla5[0] = cla5[2] = cla5[3] = None

        assert repr(cla5) == "PArray(1, 2, 42, 0, 7, size=5, default=0)"
    
    def test_flatMap(self):
        def ge1(n: Any) -> int|None:
            if n == ():
                return None
            if n >= 1:
                return n
            return None

        def lt2or42(n: Any) -> int|None:
            if n == ():
                return 42
            if n < 2:
                return n
            return None

        def lt3(n: Any) -> int|None:
            if n < 3:
                return n
            return None

        # Keep defaults all the same
        cl0 = PArray(*range(10), default=6)
        cl1 = cl0.flatMap(lambda x: PArray(*range(x%5)))
        cl2 = cl0.flatMap(lambda x: PArray(*range(x%5), default=6))
        cl3 = cl0.flatMap(lambda x: PArray(*range(x%5)), default=6)
        cl4 = cl0.flatMap(lambda x: PArray(*range(x%5), default=7), default=6)
        assert cl1 == cl2 == cl3 == cl4
        assert cl1 == PArray(0,0,1,0,1,2,0,1,2,3,0,0,1,0,1,2,0,1,2,3)
        assert cl0.default() == 6
        assert cl1.default() == 6
        assert cl2.default() == 6
        assert cl3.default() == 6
        assert cl4.default() == 6
        cl11 = cl1.map(ge1)
        cl12 = cl2.map(ge1)
        cl13 = cl3.map(ge1)
        cl14 = cl4.map(ge1)
        assert cl11 == cl12 == cl13 == cl14
        assert cl11 == PArray(6,6,1,6,1,2,6,1,2,3,6,6,1,6,1,2,6,1,2,3)
        assert cl11.default() == cl12.default() == cl13.default()
        assert cl13.default() == cl14.default() == 6
        cl11 = cl1.map(lt2or42)
        cl12 = cl2.map(lt2or42)
        cl13 = cl3.map(lt2or42)
        cl14 = cl4.map(lt2or42)
        assert cl11 == cl12 == cl13 == cl14
        assert cl11 == PArray(0,0,1,0,1,6,0,1,6,6,0,0,1,0,1,6,0,1,6,6)
        assert cl11.default() == 6
        assert cl12.default() == 6
        assert cl13.default() == 6
        assert cl14.default() == 6

        # Vary up the defaults
        cl0 = PArray(*range(10), default=6)
        assert cl0.default() == 6
        cl1 = cl0.flatMap(lambda x: PArray(*range(x%5)))
        cl2 = cl0.flatMap(lambda x: PArray(*range(x%5), default=7))
        cl3 = cl0.flatMap(lambda x: PArray(*range(x%5)), default=8)
        cl4 = cl0.flatMap(lambda x: PArray(*range(x%5), default=-1), default=9)
        assert cl1.default() == 6
        assert cl2.default() == 6
        assert cl3.default() == 8
        assert cl4.default() == 9
        assert cl1 == cl2 == cl3 == cl4
        assert cl1 == PArray(0,0,1,0,1,2,0,1,2,3,0,0,1,0,1,2,0,1,2,3)
        cl11 = cl1.map(lt2or42)
        cl12 = cl2.map(lt2or42)
        cl13 = cl3.map(lt2or42)
        cl14 = cl4.map(lt2or42)
        assert cl11 == PArray(0,0,1,0,1,6,0,1,6,6,0,0,1,0,1,6,0,1,6,6)
        assert cl12 == PArray(0,0,1,0,1,6,0,1,6,6,0,0,1,0,1,6,0,1,6,6)
        assert cl13 == PArray(0,0,1,0,1,8,0,1,8,8,0,0,1,0,1,8,0,1,8,8)
        assert cl14 == PArray(0,0,1,0,1,9,0,1,9,9,0,0,1,0,1,9,0,1,9,9)
        assert cl11.default() == 6
        assert cl12.default() == 6
        assert cl13.default() == 8
        assert cl14.default() == 9

        # Vary up the defaults, no default set on initial PArray
        cl0 = PArray(*range(10))
        assert cl0.default() == ()
        cl1 = cl0.flatMap(lambda x: PArray(*range(x%5)))
        cl2 = cl0.flatMap(lambda x: PArray(*range(x%5), default=7))
        cl3 = cl0.flatMap(lambda x: PArray(*range(x%5)), default=8)
        cl4 = cl0.flatMap(lambda x: PArray(*range(x%5), default=-1), default=9)
        assert cl1 == cl2 == cl3 == cl4
        assert cl1 == PArray(0,0,1,0,1,2,0,1,2,3,0,0,1,0,1,2,0,1,2,3)
        assert cl1.default() == ()
        assert cl2.default() == ()
        assert cl3.default() == 8
        assert cl4.default() == 9
        cl11 = cl1.map(lt2or42)
        cl12 = cl2.map(lt2or42)
        cl13 = cl3.map(lt2or42)
        cl14 = cl4.map(lt2or42)
        assert cl11 == PArray(0,0,1,0,1,(),0,1,(),(),0,0,1,0,1,(),0,1,(),())
        assert cl12 == PArray(0,0,1,0,1,(),0,1,(),(),0,0,1,0,1,(),0,1,(),())
        assert cl13 == PArray(0,0,1,0,1,8,0,1,8,8,0,0,1,0,1,8,0,1,8,8)
        assert cl14 == PArray(0,0,1,0,1,9,0,1,9,9,0,0,1,0,1,9,0,1,9,9)
        assert cl11.default() == ()
        assert cl12.default() == ()
        assert cl13.default() == 8
        assert cl14.default() == 9

        # Let f change default, set default set on initial PArray
        cl0 = PArray(*range(3), default=6)
        assert cl0.default() == 6
        cl1 = cl0.flatMap(lambda x: PArray(*range(x)))
        cl2 = cl0.flatMap(lambda x: PArray(*range(x), default=x*x))
        cl3 = cl0.flatMap(lambda x: PArray(*range(x)), default=8)
        cl4 = cl0.flatMap(lambda x: PArray(*range(x), default=-1), default=9)
        fcl5 = cl0.flatMap(lambda x: PArray(*range(x), default=cl0.default()))
        fcl6 = cl0.flatMap(lambda x: PArray(*range(x), default=8), default=8)
        assert cl1 == PArray(0, 0, 1)
        assert cl2 == PArray(0, 0, 1)
        assert cl3 == PArray(0, 0, 1)
        assert cl4 == PArray(0, 0, 1)
        assert fcl5 == PArray(0, 0, 1)
        assert fcl6 == PArray(0, 0, 1)
        assert cl1.default() == 6
        assert cl2.default() == 6
        assert cl3.default() == 8
        assert cl4.default() == 9
        assert fcl5.default() == 6
        assert fcl6.default() == 8

        cl0 = PArray(*range(1, 6), default=-1)
        assert cl0.default() == -1
        cl1 = cl0.flatMap(lambda x: PArray(*range(x, x+2), default=x+1))
        cl2 = cl0.flatMap(lambda x: PArray(*range(x-1, x+1), None, 42, default=x*x))
        cl3 = cl0.flatMap(lambda x: PArray(*range(x+1, x+3)), default=8)
        cl4 = cl0.flatMap(lambda x: PArray(*range(x-2, x+1), default=-1), size=-8, default=9)
        assert cl1 == PArray(1,2,2,3,3,4,4,5,5,6)
        assert cl2 == PArray(0,1,42,1,2,42,2,3,42,3,4,42,4,5,42)
        assert cl3 == PArray(2,3,3,4,4,5,5,6,6,7)
        assert cl4 == PArray(2,3,2,3,4,3,4,5)
        assert cl1.default() == -1
        assert cl2.default() == -1
        assert cl3.default() == 8
        assert cl4.default() == 9
        cl11 = cl1.map(lt3)
        cl12 = cl2.map(lt3)
        cl13 = cl3.map(lt3)
        cl14 = cl4.map(lt3)
        assert cl11 == PArray(1,  2,  2, -1, -1, -1, -1, -1, -1, -1)
        assert cl12 == PArray(0,  1, -1,  1,  2, -1,  2, -1, -1, -1, -1, -1, -1, -1, -1)
        assert cl13 == PArray(2,  8,  8,  8,  8,  8,  8,  8,  8,  8)
        assert cl14 == PArray(2,  9,  2,  9,  9,  9,  9,  9)
        assert cl11.default() == -1
        assert cl12.default() == -1
        assert cl13.default() == 8
        assert cl14.default() == 9

        def bar(x):
            return PArray(2, x, 3*x, size=4, default=7*x)

        cl0 = PArray(1, 2, size=3, default=-1)
        cl01 = cl0.flatMap(bar)
        assert repr(cl01) == 'PArray(2, 1, 3, 7, 2, 2, 6, 14, 2, -1, -3, -7, size=12, default=-1)'
        assert eval(repr(cl01)) == PArray(2, 1, 3, 7, 2, 2, 6, 14, 2, -1, -3, -7)

        cl02 = cl0.flatMap(bar, size=15)
        assert repr(cl02) == 'PArray(2, 1, 3, 7, 2, 2, 6, 14, 2, -1, -3, -7, -1, -1, -1, size=15, default=-1)'

        cl1 = PArray(1, 2, size=4, default=-2, backlog=(9,10,11))
        cl11 = cl1.flatMap(bar, size=12)
        assert repr(cl11) == 'PArray(2, 1, 3, 7, 2, 2, 6, 14, 2, 9, 27, 63, size=12, default=-2)'

        # Python always evaluates/assigns left to right
        cl11[0] = cl11[1] = cl11[2] = cl11[3] = None
        cl11[4] = cl11[5] = cl11[6] = cl11[7] = None
        cl11[8] = cl11[9] = cl11[10] = cl11[11] = None
        assert repr(cl11) == 'PArray(2, 10, 30, 70, -2, -2, -2, -2, -2, -2, -2, -2, size=12, default=-2)'
 
    def test_mergeMap(self):
        def lt3(n: Any) -> int|None:
            if n < 3:
                return n
            return None

        cl0 = PArray(*range(1, 6), default=-1)
        assert cl0.default() == -1
        cl1 = cl0.mergeMap(lambda x: PArray(*range(x, x+2), default=x+1))
        cl2 = cl0.mergeMap(lambda x: PArray(*range(x-1, x+1), default=x*x))
        cl3 = cl0.mergeMap(lambda x: PArray(*range(x+1, x+3)), default=8)
        cl4 = cl0.mergeMap(lambda x: PArray(*range(x-2, x+1), default=-1), size=-8, default=9)
        assert cl1 == PArray(1,2,3,4,5,2,3,4,5,6)
        assert cl2 == PArray(0,1,2,3,4,1,2,3,4,5)
        assert cl3 == PArray(2,3,4,5,6,3,4,5,6,7)
        assert cl4 == PArray(2,3,4,1,2,3,4,5)
        assert cl1.default() == -1
        assert cl2.default() == -1
        assert cl3.default() == 8
        assert cl4.default() == 9
        cl11 = cl1.map(lt3)
        cl12 = cl2.map(lt3)
        cl13 = cl3.map(lt3)
        cl14 = cl4.map(lt3)
        assert cl11 == PArray(1,2,-1,-1,-1,2,-1,-1,-1,-1)
        assert cl12 == PArray(0,1,2,-1,-1,1,2,-1,-1,-1)
        assert cl13 == PArray(2,8,8,8,8,8,8,8,8,8)
        assert cl14 == PArray(2,9,9,1,2,9,9,9)
        assert cl11.default() == -1
        assert cl12.default() == -1
        assert cl13.default() == 8
        assert cl14.default() == 9

        def bar(x):
            return PArray(2, x, 3*x, size=4, default=7*x)

        cl0 = PArray(1, 2, size=3, default=-1)
        cl01 = cl0.mergeMap(bar)
        assert repr(cl01) == 'PArray(2, 2, 2, 1, 2, -1, 3, 6, -3, 7, 14, -7, size=12, default=-1)'
        assert eval(repr(cl01)) == PArray(2, 2, 2, 1, 2, -1, 3, 6, -3, 7, 14, -7)

        cl02 = cl0.mergeMap(bar, size=15)
        assert repr(cl02) == 'PArray(2, 2, 2, 1, 2, -1, 3, 6, -3, 7, 14, -7, -1, -1, -1, size=15, default=-1)'

        cl1 = PArray(1, 2, size=4, default=-2, backlog=(9,10,11))
        cl11 = cl1.mergeMap(bar, size=11)
        assert repr(cl11) == 'PArray(2, 2, 2, 2, 1, 2, 9, 10, 3, 6, 27, size=11, default=-2)'

        # Python always evaluates/assigns left to right
        cl11[0] = cl11[1] = cl11[2] = cl11[3] = None
        cl11[4] = cl11[5] = cl11[6] = cl11[7] = None
        cl11[8] = cl11[9] = cl11[10] = None
        assert repr(cl11) == 'PArray(30, 7, 14, 63, 70, -2, -2, -2, -2, -2, -2, size=11, default=-2)'

    def test_exhaustMap(self):
        def le3(n: Any) -> int|None:
            if n <= 3:
                return n
            return None

        cl0 = PArray(*range(1, 6), default=-1)
        assert cl0.default() == -1
        cl1 = cl0.exhaustMap(lambda x: PArray(*range(x, x+2), default=x+1))
        cl2 = cl0.exhaustMap(lambda x: PArray(*range(x-1, x+1), 42, default=x*x))
        cl3 = cl0.exhaustMap(lambda x: PArray(*range(x+1, x+3)), default=8)
        cl4 = cl0.exhaustMap(lambda x: PArray(*range(x), default=-1), default=10)
        cl5 = cl0.exhaustMap(lambda x: PArray(*range(x), default=-1), size=8, default=11)
        cl6 = cl0.exhaustMap(lambda x: PArray(*range(x), default=-1), size=-8, default=12)
        assert cl1 == PArray(1,2,3,4,5,2,3,4,5,6)
        assert cl2 == PArray(0,1,2,3,4,1,2,3,4,5,42,42,42,42,42)
        assert cl3 == PArray(2,3,4,5,6,3,4,5,6,7)
        assert cl4 == PArray(0,0,0,0,0,1,1,1,1,2,2,2,3,3,4)
        assert cl5 == PArray(0,0,0,0,0,1,1,1)
        assert cl6 == PArray(1,1,2,2,2,3,3,4)
        assert cl1.default() == -1
        assert cl2.default() == -1
        assert cl3.default() == 8
        assert cl4.default() == 10
        assert cl5.default() == 11
        assert cl6.default() == 12
        cl11 = cl1.map(le3)
        cl12 = cl2.map(le3)
        cl13 = cl3.map(le3)
        cl14 = cl4.map(le3)
        cl15 = cl5.map(le3)
        cl16 = cl6.map(le3)
        assert cl11 == PArray(1,2,3,-1,-1,2,3,-1,-1,-1)
        assert cl12 == PArray(0,1,2,3,-1,1,2,3,-1,-1,-1,-1,-1,-1,-1)
        assert cl13 == PArray(2,3,8,8,8,3,8,8,8,8)
        assert cl14 == PArray(0,0,0,0,0,1,1,1,1,2,2,2,3,3,10)
        assert cl15 == PArray(0,0,0,0,0,1,1,1)
        assert cl16 == PArray(1,1,2,2,2,3,3,12)
        assert cl11.default() == -1
        assert cl12.default() == -1
        assert cl13.default() == 8
        assert cl14.default() == 10
        assert cl15.default() == 11
        assert cl16.default() == 12

        def bar(x):
            return PArray(*range(1, x+1), default = 2*x)

        cl0 = PArray(1, 2, 3, default=21)
        cl00 = cl0.exhaustMap(bar, size=8, mapDefault=True)
        assert repr(cl00) == 'PArray(1, 1, 1, 2, 2, 3, 42, 42, size=8, default=42)'
        assert eval(repr(cl00)) == PArray(1, 1, 1, 2, 2, 3, 42, 42)

        # Python always evaluates/assigns left to right
        cl00[0] = None
        cl00[4] = None
        assert cl00 == PArray(1, 1, 2, 42, 3, 42, 42, size=-8, default=42)
        assert repr(cl00) == 'PArray(42, 1, 1, 2, 42, 3, 42, 42, size=8, default=42)'
