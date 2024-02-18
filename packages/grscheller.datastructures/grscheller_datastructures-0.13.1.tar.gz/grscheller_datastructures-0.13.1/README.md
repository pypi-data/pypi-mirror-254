# PyPI grscheller.datastructures

Data Structures which support the use and implementation of algorithms.

* Functional and imperative programming styles are supported
* Supports functional programming while endeavoring to remain Pythonic
* Methods which mutate objects don't return anything
* For detailed API documentation click [here][1].

## Overview

The data structures in this package allow developers to focus on the
algorithms they are using instead of all the "bit fiddling" required to
implement behaviors, perform memory management, and handle edge cases
needed if Python builtin types were used instead. These data structures
allow iterators to leisurely iterate over inaccessible copies of
internal state while the data stuctures themselves safely mutate. Some
of these data structures allow data to be safely shared between multiple
data structure instances by making shared data immutable and
inaccessible to client code.

This package does not force functional programming paradigms on client
code, but provide functional tools to opt into. It also does not force
unnecessary exception driven code paths upon client code. Purity is
important, but not at the expense of practicality. Sometimes the real
power of a data structure comes not from what it empowers you to do, but
from what it prevents you from doing to yourself.

As a design choice, Python `None` is semantically used by this package
to indicate the absence of a value. While still freely used as an
implementation detail, `None` as a value is not stored in these data
structures unless specifically documented. `Maybe` & `Either` classes
are provided in the functional sub-package as better ways to handle
"missing" data.

---

[1]: https://grscheller.github.io/datastructures/API/development/html/grscheller/datastructures/index.html
