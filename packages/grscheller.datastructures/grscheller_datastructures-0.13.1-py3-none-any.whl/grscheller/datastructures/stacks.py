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

"""Module grscheller.datastructure.stacks - Stateful & Functional LIFO stacks:

   Module implementing a LIFO stacks using singularly linked linear trees of
   nodes. The nodes can be safely shared between different stack instances and
   are an implementation detail hidden from client code.
"""

from __future__ import annotations

__all__ = ['Stack', 'FStack']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any, Callable
from itertools import chain
from .core.iterlib import exhaust, merge
from .queues import CircularArray
from .core.nodes import SL_Node as Node
from .core.fp import FP

class StackBase():
    """Abstract base class for the purposes of DRY inheritance of classes
    implementing stack type data structures. Each stack is a very simple
    stateful object containing a count of the number of elements on it and
    a reference to an immutable node of a linear tree of singularly linked
    nodes. Different stack objects can safely share the same data by each
    pointing to the same node. Each stack class ensures None values do not
    get pushed onto the the stack.
    """
    __slots__ = '_head', '_count'

    def __init__(self, *ds):
        """Construct a LIFO Stack"""
        self._head = None
        self._count = 0
        for d in ds:
            if d is not None:
                node = Node(d, self._head)
                self._head = node
                self._count += 1

    def __iter__(self):
        """Iterator yielding data stored on the stack, starting at the head"""
        node = self._head
        while node:
            yield node._data
            node = node._next

    def __reversed__(self):
        """Reverse iterate over the contents of the stack"""
        return reversed(CircularArray(*self))

    def __repr__(self):
        return f'{self.__class__.__name__}(' + ', '.join(map(repr, reversed(self))) + ')'

    def __bool__(self):
        """Returns true if stack is not empty"""
        return self._count > 0

    def __len__(self):
        """Returns current number of values on the stack"""
        return self._count

    def __eq__(self, other: Any):
        """Returns True if all the data stored on the two stacks are the same
        and the two stacks are of the same subclass. Worst case is O(n) behavior
        which happens when all the corresponding data elements on the two stacks
        are equal, in whatever sense they equality is defined, and none of the
        nodes are shared.
        """
        if not isinstance(other, type(self)):
            return False

        if self._count != other._count:
            return False

        left = self._head
        right = other._head
        nn = self._count
        while nn > 0:
            if left is right:
                return True
            if left is None or right is None:
                return True
            if left._data != right._data:
                return False
            left = left._next
            right = right._next
            nn -= 1
        return True

class Stack(StackBase):
    """Class implementing a mutable Last In, First Out (LIFO) stack data structure
    pointing to a singularly linked list of nodes. This class is designed to share
    nodes with other Stack instances.

    Stacks are stateful objects, values can be pushed on & popped off.

    A Stack points to either the top node in the list, or to None which indicates
    an empty stack.

    A Stack keeps a count of the number of objects currently on it. Pushing to,
    popping from, getting the length and copying the Stack are all O(1) operations.

    None represents the absence of a value and ignored if pushed on a Stack.
    """
    __slots__ = ()

    def __str__(self):
        """Display the data in the Stack, left to right starting at bottom"""
        return '|| ' + ' <- '.join(reversed(CircularArray(*self).map(repr))) + ' ><'

    def copy(self) -> Stack:
        """Return shallow copy of a Stack in O(1) time & space complexity"""
        stack = Stack()
        stack._head, stack._count = self._head, self._count
        return stack

    def reverse(self) -> None:
        """Return shallow copy of a Stack in O(1) time & space complexity"""
        stack = Stack(*self)
        self._head, self._count = stack._head, stack._count

    def push(self, *ds: Any) -> None:
        """Push data that is not NONE onto top of stack,
        return the stack being pushed.
        """
        for d in ds:
            if d is not None:
                node = Node(d, self._head)
                self._head, self._count = node, self._count+1

    def pop(self) -> Any:
        """Pop data off of top of stack"""
        if self._head is None:
            return None
        else:
            data = self._head._data
            self._head, self._count = self._head._next, self._count-1
            return data

    def peak(self, default: Any=None) -> Any:
        """Returns the data at the top of the stack. Does not consume the data.
        If stack is empty, data does not exist so in that case return default.
        """
        if self._head is None:
            return default
        return self._head._data

    def map(self, f: Callable[[Any], Stack]) -> None:
        """Maps a function (or callable object) over the values on the Stack.
        Mutates the Stack object. O(n).
        """
        newStack = Stack(*map(f, reversed(self)))
        self._head, self._count = newStack._head, newStack._count

class FStack(StackBase, FP):
    """Class implementing an immutable Last IN, First Out (LIFO) data structure
    pointing to a singularly linked list of nodes. This class is designed to share
    nodes with other FStack instances.

    FStack stacks are immutable objects.

    An FStack points to either the top node in the list, or to None which indicates
    an empty FStack.

    An Fstack keeps a count of the number of objects currently on it. Getting the head,
    tail, length, copying and creating a new Fstack with cons are all O(1) operations.

    None represents the absence of a value and ignored if pushed on an FStack.
    """
    __slots__ = ()

    def __str__(self):
        """Display the data in the FStack, left to right starting at bottom"""
        return '| ' + ' <- '.join(reversed(CircularArray(*self).map(repr))) + ' ><'

    def copy(self) -> FStack:
        """Return shallow copy of a FStack in O(1) time & space complexity"""
        fstack = FStack()
        fstack._head = self._head
        fstack._count = self._count
        return fstack

    def reverse(self) -> FStack:
        return FStack(*self)

    def head(self, default: Any=None) -> Any:
        """Returns the data at the top of the FStack. Does not consume the data.
        If the FStack is empty, head does not exist so in that case return default.
        """
        if self._head is None:
            return default
        return self._head._data

    def tail(self, default=None) -> FStack:
        """Return tail of the FStack. If FStack is empty, tail does not exist, so
        return a default of type FStack instead. If default is not given, return
        an empty FStack.
        """
        if self._head:
            fstack = FStack()
            fstack._head = self._head._next
            fstack._count = self._count - 1
            return fstack
        elif default is None:
            return FStack()
        else:
            return default

    def cons(self, d: Any) -> FStack:
        """Return a new FStack with data as head and self as tail. Constructing
        an FStack using a non-existent value as head results in a non-existent
        FStack. In that case, just return a copy of the FStack.
        """
        if d is not None:
            fstack = FStack()
            fstack._head = Node(d, self._head)
            fstack._count = self._count + 1
            return fstack
        else:
            return self.copy()

    def map(self, f: Callable[[Any], Any]) -> FStack:
        """Apply f over the elemrnts of the data structure"""
        return FStack(*map(f, reversed(self)))

    def flatMap(self, f: Callable[[Any], FStack]) -> FStack:
        """Monadicly bind f to the data structure sequentially"""
        return FStack(*chain(*map(reversed, map(f, reversed(self)))))

    def mergeMap(self, f: Callable[[Any], FStack]) -> FStack:
        """Monadicly bind f to the data structure sequentially"""
        return FStack(*merge(*map(reversed, map(f, reversed(self)))))

    def exhaustMap(self, f: Callable[[Any], FStack]) -> FStack:
        """Monadicly bind f to the data structure merging until all exhausted"""
        return FStack(*exhaust(*map(reversed, map(f, reversed(self)))))

if __name__ == "__main__":
    pass
