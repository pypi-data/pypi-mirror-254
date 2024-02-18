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

"""Module grscheller.datastructure.tuples - tuple-like data structures

Module implementing an immutable tuple like object with a funtional interface.
"""

from __future__ import annotations

__all__ = ['FTuple']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any
from .core.fp import FP

class FTuple(tuple, FP):
    """Class extending tuple with FP behaviors."""
    __slots__ = ()

    def __new__(cls, *ds):
        """Construct the tuple with the None values filtered out"""
        return super().__new__(cls, (filter(lambda d: d is not None, ds)))

    def __repr__(self):
        return f'{self.__class__.__name__}(' + ', '.join(map(repr, self)) + ')'

    def __str__(self):
        """Display data in the FTuple."""
        return "((" + ", ".join(map(repr, self)) + "))"

    def __getitem__(self, sl: slice|int) -> Any:
        """Suports both indexing and slicing."""
        if isinstance(sl, slice):
            return FTuple(*super().__getitem__(sl))
        try:
            item = super().__getitem__(sl)
        except IndexError:
            item = None
        return item

    def copy(self) -> FTuple:
        """Return shallow copy of the FTuple in O(1) time & space complexity"""
        return FTuple(*self)

    def reverse(self) -> FTuple:
        """Return a reversed FTuple, new instance."""
        return(FTuple(*reversed(self)))

    def __add__(self, other: FTuple) -> FTuple:
        """Concatenate two FTuples"""
        return FTuple(*super().__add__(other))

    def __mul__(self, num: int) -> FTuple:
        """Return an FTuple which repeats anothr FTuples num times"""
        return FTuple(*super().__mul__(num))

if __name__ == "__main__":
    pass
