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

"""Module grscheller.datastructures.core.functional

class Maybe: Implements the Maybe Monad, also called the Optional Monad
class Either: Implements a left biased Either Monad.
class FP: default functional implementations for data structure methods
"""
from __future__ import annotations

__all__ = [ 'FP', 'maybeToEither', 'eitherToMaybe',
            'Either', 'Left', 'Right',
            'Maybe', 'Some', 'Nothing' ]
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

import operator
from typing import Any, Callable, Type
from itertools import accumulate, chain
from .iterlib import exhaust, merge

class FP():
    """Default functional implentations for data structures"""
    __slots__ = ()

    def foldL(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Fold with an optional initial value. If an initial value is not
        given and the datastructure is empty, return None.
        """
        if not self:
            return initial

        if initial is None:
            vs = iter(self)
        else:
            vs = chain((initial,), self)

        value = next(vs)
        for v in vs:
            value = f(value, v)

        return value

    def reduce(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Fold with an optional initial value. If an initial value is not
        given and the datastructure is empty, return None.

        Deprecation Warning: use foldL instead
        """
        return self.foldL(f, initial)

    def accummulate(self, f: Callable[[Any, Any], Any]=None, initial=None) -> type[FP]:
        """Accummulate partial fold results in same type data structure. Works
        best for variable sized containers."""
        if f is None:
            f = operator.add

        if initial is None:
            return type(self)(*accumulate(self, f))
        else:
            return type(self)(*accumulate(chain((initial,), self), f))

    # Default implentations for FIFO data structures - see stacks module LIFO examples

    def map(self, f: Callable[[Any], Any]) -> type[FP]:
        """Apply f over the elemrnts of the data structure"""
        return type(self)(*map(f, self))

    def flatMap(self, f: Callable[[Any], FP]) -> type[FP]:
        """Monadicly bind f to the data structure sequentially"""
        return type(self)(*chain(*map(iter, map(f, self))))

    def mergeMap(self, f: Callable[[Any], FP]) -> type[FP]:
        """Monadicly bind f to the data structure merging until one exhausted"""
        return type(self)(*merge(*map(iter, map(f, self))))

    def exhaustMap(self, f: Callable[[Any], FP]) -> type[FP]:
        """Monadicly bind f to the data structure merging until all exhausted"""
        return type(self)(*exhaust(*map(iter, map(f, self))))
    
class Maybe(FP):
    """Class representing a potentially missing value.

    - Implements the Option Monad
    - Maybe(value) constructs "Some(value)"
    - Both Maybe() or Maybe(None) constructs a "Nothing"
    - Immutable semantics - map & flatMap return modified copies
    - None is always treated as a non-existance value
    - None cannot be stored in an object of type Maybe
    - Semantically None represent non-existance
    - None only has any real existance as an implementration detail
    """
    __slots__ = '_value',

    def __init__(self, value: Any=None):
        self._value = value

    def __iter__(self):
        """Yields its value if not a Nothing"""
        if self:
            yield self._value

    def __repr__(self):
        if self:
            return 'Some(' + repr(self._value) + ')'
        else:
            return 'Nothing'

    def __bool__(self) -> bool:
        """Return false if a Nothing, otherwise true."""
        return self._value is not None

    def __len__(self) -> int:
        """A Maybe either contains something or nothing.

        Returns 1 if a "Some"
        Returns 0 if a "Nothing"
        """
        if self:
            return 1
        else:
            return 0

    def __eq__(self, other: Maybe) -> bool:
        """Returns true if both sides are Nothings, or if both sides are Somes
        contining values which compare as equal.
        """
        if not isinstance(other, type(self)):
            return False
        return self._value == other._value

    def get(self, alternate: Any=None) -> Any:
        """Get contents if they exist, otherwise return an alternate value.
        Caller is responsible with dealing with a None alternate return value.
        """
        if self:
            return self._value
        else:
            return alternate

    def foldL(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Left biased fold left"""
        if self:
            if initial is None:
                return self._value
            else:
                return f(initial, self._value)
        else:
            return None

    def reduce(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Left biased left fold

        Deprecated: use foldL instead
        """
        return self.foldL(f, initial)

    def accummulate(self,
                    f: Callable[[Any, Any], Any]=None,
                    initial=None) -> Maybe:
        """Accummulate but, since the data structure can hold at most only
        one value, do not include the initial value if the Maybe is not a Nothing, 
        """
        if f is None:
            f = operator.add

        return Maybe(self.foldL(f, initial))

# Maybe convenience functions/vars

def maybeToEither(m: Maybe, right: Any=None) -> Either:
    """Convert a Maybe to an Either"""
    return Either(m.get(), right)

def Some(value=None) -> Maybe:
    """Function for creating a Maybe from a value. If value is None or missing,
    returns a Nothing.
    """
    return Maybe(value)

#: Nothing is not a singleton! Test via equality, or in a boolean context.
Nothing: Maybe = Maybe()

class Either(FP):
    """Class that either contains a Left value or Right value, but not both.

    - Implements a left biased Either Monad
    - Maybe(value, altValue) constructs "Left(value)" if value is not None
    - Maybe(value, altValue) constructs "Right(altValue)" if value is None
    - If altValue not given, set it to the empty string
    - Immutable semantics - map & flatMap return modified copies
    """
    __slots__ = '_value', '_isLeft'

    def __init__(self, left: Any=None, right: Any=None):
        if right is None:
            right = ''
        if left == None:
            self._isLeft = False
            self._value = right
        else:
            self._isLeft = True
            self._value = left

    def __iter__(self):
        """Yields its value if a Left"""
        if self:
            yield self._value

    def __repr__(self):
        if self:
            return 'Left(' + repr(self._value) + ')'
        else:
            return 'Right(' + repr(self._value) + ')'

    def __bool__(self) -> bool:
        """Return true if a Left, false if a Right"""
        return self._isLeft

    def __len__(self) -> int:
        """An Either always contains just one thing, which is not None"""
        return 1

    def __eq__(self, other: Either) -> bool:
        """True if both sides are same "type" and values compare as equal"""
        if not isinstance(other, type(self)):
            return False
        if (self and other) or (not self and not other):
            return self._value == other._value
        return False

    def get(self, default: Any=None) -> Any:
        """Get value if a Left, otherwise return default value"""
        if self:
            return self._value
        return default

    def getRight(self) -> Any:
        """Get value if a Right, otherwise return None"""
        if self:
            return None
        return self._value

    def map(self, f: Callable[[Any], Any], right=None) -> Either:
        """Map over a Left(value)"""
        if self:
            return Either(f(self._value), right)
        return self

    def mapRight(self, g: Callable[[Any], Any]) -> Either:
        """Map over a Right(value)"""
        if self:
            return self
        return Right(g(self._value))

    def flatMap(self, f: Callable[[Any], Either], right: Any=None) -> Either:
        """flatMap with right as default. replace right"""
        if self:
            if right is None:
                return f(self._value)
            else:
                return f(self._value).mapRight(lambda _: right)
        else:
            if right is None:
                return self
            else:
                return self.mapRight(lambda _: right)

    def mergeMap(self, f: Callable[[Any], Either], right: Any=None) -> Either:
        """flatMap with right as default, concatenate rights"""
        if self:
            if right is None:
                return f(self._value)
            else:
                return f(self._value).mapRight(lambda x: x + right)
        else:
            if right is None:
                return self
            else:
                return self.mapRight(lambda x: x + right)

    def foldL(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Left biased left fold"""
        if self:
            if initial is None:
                return self._value
            else:
                return f(initial, self._value)
        else:
            return None

    def reduce(self, f: Callable[[Any, Any], Any], initial: Any=None) -> Any:
        """Left biased foldleft

        Deprecated: use foldL instead
        """
        return self.foldL(f, initial)

    def accummulate(self,
                    f: Callable[[Any, Any], Any]=None,
                    g: Callable[[Any, Any], Any]=None,
                    initial: Any=None,
                    right: Any=None) -> Either:
        """Accummulate. The data structure always holds one value, so what
        gets "accummulated" depends on if the Either is a Left or a Right.
        By default, a Left contains numeric data, a right a str.
        """
        if f is None:
            f = operator.add
        if g is None:
            g = operator.add
        if initial is None:
            initial = 0
        if right is None:
            right = ''

        if self:
            return Left(f(initial, self._value), right)
        else:
            return Right(g(self._value, right))

# Either convenience functions, act like subtype constructors.

def eitherToMaybe(e: Either) -> Maybe:
    """Convert an Either to a Maybe"""
    return Maybe(e.get())

def Left(left: Any, right: Any=None) -> Either:
    """Function returns Left Either if left != None, otherwise Right Either"""
    return Either(left, right)

def Right(right: Any) -> Either:
    """Function to construct a Right Either"""
    return Either(None, right)

if __name__ == "__main__":
    pass
