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

"""Module grscheller.datastructure.arrays

Module implementing array-like data structures.
"""

from __future__ import annotations

__all__ = ['PArray']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any, Callable, Iterable
from itertools import chain, repeat
from .queues import DoubleQueue
from .core.iterlib import merge, exhaust
from .core.fp import FP, Some

class PArray(FP):
    """Processing Array

    Class implementing a mutable fixed length array-like data structure with
    O(1) data access. All mutating methods are guaranteed not to change the
    length of the data structure. None values are not allowed in this data
    structures.

    - if size not given, None or 0 then size to the non-None data provided
    - if size > 0, pad right from back queue or send trailing data to back queue
    - if size < 0, pad left from back queue or slice initial data to back queue
    - attempt to preserve original order of sliced data on back queue
    - push extra non-None data from backlog to end of the back queue
    - use the default value if back Queue empty, default value "defaults" to ()

    Equality of objects is based on the array values and not on values in the
    back log nor the default value.
    """
    __slots__ = '_arrayQueue', '_backQueue', '_default'

    def __init__(self, *data,
                 size: int|None=None,
                 default: Any=(),
                 backlog: Iterable=()):

        arrayQueue = DoubleQueue()
        backQueue = DoubleQueue(*data)
        data_size = len(backQueue)

        if (size is None) or (size == 0):
            abs_size = size = data_size
        else:
            abs_size = abs(size)

        if size >= 0:
            if data_size < abs_size:
                # Pad CLArray on right from backlog, if empty use default value
                while backQueue:
                    arrayQueue.pushR(backQueue.popL())
                backQueue.pushR(*backlog)
                for ii in range(abs_size - data_size):
                    if backQueue:
                        arrayQueue.pushR(backQueue.popL())
                    else:
                        arrayQueue.pushR(default)
            else:
                # slice initial data on right
                for _ in range(abs_size):
                    arrayQueue.pushR(backQueue.popL())
        else:
            if data_size < abs_size:
                # Pad CLArray on left from backlog, if empty use default value
                while backQueue:
                    arrayQueue.pushL(backQueue.popR())
                backQueue.pushR(*backlog)
                for ii in range(abs_size - data_size):
                    if backQueue:
                        arrayQueue.pushL(backQueue.popL())
                    else:
                        arrayQueue.pushL(default)
            else:
                # slice initial data on left
                for _ in range(abs_size):
                    arrayQueue.pushL(backQueue.popR())
                backQueue.reverse()

        backQueue.pushR(*backlog)

        self._arrayQueue = arrayQueue
        self._backQueue = backQueue
        self._default = default

    def __iter__(self):
        """Iterate over the current state of the CLArray. Copy is made
        so original source can safely mutate.
        """
        for data in self._arrayQueue.copy():
            yield data

    def __reversed__(self):
        """Reverse iterate over the current state of the CLArray. Copy is made
        so original source can safely mutate.
        """
        for data in reversed(self._arrayQueue.copy()):
            yield data

    def __repr__(self):
        """Representation of current state of data, does not reproduce the backstore"""
        repr1 = f'{self.__class__.__name__}('
        repr2 = ', '.join(map(repr, self))
        if repr2 == '':
            repr3 = f'size={len(self)}, '
        else:
            repr3 = f', size={len(self)}, '
        repr4 = f'default={repr(self._default)})'
        return repr1 + repr2 + repr3 + repr4

    def __str__(self):
        return '[|' + ', '.join(map(repr, self)) + '|]'

    def __bool__(self):
        """Return true only if there exists an array value not equal to the
        default value which gets used in lieu of None.
        """
        for value in self:
            if value != self._default:
                return True
        return False

    def default(self) -> Any:
        """Return a reference to the default value that gets used in lieu of None"""
        return self._default

    def backQueue(self) -> DoubleQueue:
        """Return a copy of the backQueue"""
        return self._backQueue.copy()

    def __len__(self) -> int:
        """Returns the size of the CLArray"""
        return len(self._arrayQueue)

    def __getitem__(self, index: int) -> Any:
        return self._arrayQueue[index]

    def __setitem__(self, index: int, value: Any) -> Any:
        if value is None:
            self._arrayQueue[index] = Some(self._backQueue.popL()).get(self._default)
        else:
            self._arrayQueue[index] = value

    def __eq__(self, other: Any):
        """Returns True if all the data stored in both compare as equal. Worst case is
        O(n) behavior for the true case. The default value and the backQueue plays no
        role in determining equality.
        """
        if not isinstance(other, type(self)):
            return False
        return self._arrayQueue == other._arrayQueue

    def copy(self, size: int|None=None, default: Any|None=None) -> PArray:
        """Return shallow copy of the CLArray in O(n) complexity."""
        return self.map(lambda x: x, size, default)

    def map(self, f: Callable[[Any], Any],
            size: int|None=None,
            default: Any|None=None) -> PArray:
        """Apply function f over the CLArray contents. Return a new CLArray with the
        mapped contents. Size to the data unless size is given. If default is not given,
        use the value from the CLArray being mapped.

        Recommendation: default should be of the same type that f produces
        """
        if default is None:
            default = self._default

        def F(ff: Callable([Any], Any)) -> Callable([Any], Any):
            def FF(x: Any) -> Any:
                value = ff(x)
                if value is None:
                    return default
                else:
                    return value
            return FF

        if size is None:
            return PArray(*map(F(f), self), default=default)
        else:
            return PArray(*map(F(f), self), size=size, default=default)

    def flatMap(self,
                f: Callable[[Any], PArray],
                size: int|None=None,
                default: Any|None=None,
                mapDefault: bool=False) -> PArray:
        """Map f across self and flatten result by concatenating the CLArray elements
        generated by f. If a default value is not given, use the default value of the
        FLArray being flatMapped.

        Any default values of the FLArrays created by f need not have anything to do
        with the default value of the FPArray being flat-mapped.
        """
        if default is None:
            default = self.default()
        if mapDefault:
            default = f(default).default()

        return PArray(*chain(*self.map(f)), size=size, default=default)

    def mergeMap(self, f: Callable[[Any], PArray],
                 size: int|None=None,
                 default: Any|None=None,
                 mapDefault: bool=False) -> PArray:
        """Map f across self and flatten result by merging the CLArray elements
        generated by f until the first is exhausted. If a default value is not given,
        use the default value of the FLArray being flat-mapped.
        """
        if default is None:
            default = self._default
        if mapDefault:
            default = f(default).default()

        return PArray(*merge(*self.map(f)), size=size, default=default)

    def exhaustMap(self, f: Callable[[Any], PArray],
                  size: int|None=None,
                  default: Any|None=None,
                  mapDefault: bool=False) -> PArray:
        """Map f across self and flatten result by merging the CLArray elements
        generated by f until all are exhausted. If a default value is not given,
        use the default value of the FLArray being flat-mapped.
        """
        if default is None:
            default = self._default
        if mapDefault:
            default = f(default).default()

        return PArray(*exhaust(*self.map(f)), size=size, default=default)

    def reverse(self) -> None:
        """Reverse the elements of the CLArray"""
        self._arrayQueue = DoubleQueue(*reversed(self))

if __name__ == "__main__":
    pass
