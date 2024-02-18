<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/mattress.svg?branch=main)](https://cirrus-ci.com/github/<USER>/mattress)
[![ReadTheDocs](https://readthedocs.org/projects/mattress/badge/?version=latest)](https://mattress.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/mattress/main.svg)](https://coveralls.io/r/<USER>/mattress)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/mattress.svg)](https://anaconda.org/conda-forge/mattress)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/mattress)
-->

[![PyPI-Server](https://img.shields.io/pypi/v/mattress.svg)](https://pypi.org/project/mattress/)
[![Monthly Downloads](https://static.pepy.tech/badge/mattress/month)](https://pepy.tech/project/mattress)
![Unit tests](https://github.com/BiocPy/mattress/actions/workflows/pypi-test.yml/badge.svg)

# Python bindings for tatami

## Overview

The **mattress** package implements Python bindings to the [**tatami**](https://github.com/tatami-inc) C++ library for matrix representations.
Downstream packages can use **mattress** to develop C++ extensions that are interoperable with many different matrix classes, e.g., dense, sparse, delayed or file-backed.
**mattress** is inspired by the [**beachmat**](https://bioconductor/packages/beachmat) Bioconductor package, which does the same thing for R packages.

## Instructions

**mattress** is published to [PyPI](https://pypi.org/project/mattress/), so installation is simple:

```shell
pip install mattress
```

**mattress** is intended for Python package developers writing C++ extensions that operate on matrices.

1. Add `mattress.includes()` to the `include_dirs=` of your `Extension()` definition in `setup.py`.
This will give you access to the various **tatami** headers to compile your C++ code.
2. Add `#include "Mattress.h"` to your C++ source files.
This defines a `Mattress` class where the `ptr` member is a pointer to a **tatami** matrix.
Python-visible C++ functions should expect to take a `Mattress*` or equivalent address (e.g., `uintptr_t`),
after which the `ptr` should be extracted for use in **tatami**-compatible functions.
3. Call `mattress.tatamize()` on Python matrix objects within each of your functions that call **tatami** C++ code.
This will wrap the Python matrix in a **tatami**-compatible C++ representation for use in the C++ code.
The pointer to the C++ instance can be accessed through the `ptr` property of the returned object,
which can then be passed to C++ code as an `uintptr_t` to a `Mattress` instance.

So, for example, we can write **ctypes** bindings like:

```cpp
#include "Mattress.h"

extern "C" {

int do_something_interesting(const void* mat) {
    return reinterpret_cast<const Mattress*>(mat)->ptr->nrow();
}

}
```

Which we can subsequently call like:

```python
import mattress

import ctypes as ct
lib = ct.CDLL("compiled.so")
lib.do_something_interesting.restype = ct.c_int
lib.do_something_interesting.argtypes = [ ct.c_void_p ]

def do_something_interesting(x):
    mat = mattress.tatamize(x)
    return do_something_interesting(x.ptr)
```

Of course, any FFI that accepts a pointer address can be used here.

## Supported matrices

Dense **numpy** matrices of varying numeric type:

```python
import numpy as np
from mattress import tatamize
x = np.random.rand(1000, 100)
tatamat = tatamize(x)

ix = (x * 100).astype(np.uint16)
tatamat2 = tatamize(ix)
```

Compressed sparse matrices from **scipy** with varying index/data types:

```python
from scipy import sparse as sp
from mattress import tatamize

xc = sp.random(100, 20, format="csc")
tatamat = tatamize(xc)

xr = sp.random(100, 20, format="csc", dtype=np.uint8)
tatamat2 = tatamize(xr)
```

Delayed arrays from the [**delayedarray**](https://github.com/BiocPy/DelayedArray) package:

```python
from delayedarray import DelayedArray
from scipy import sparse as sp
from mattress import tatamize
import numpy

xd = DelayedArray(sp.random(100, 20, format="csc"))
xd = numpy.log1p(xd * 5)

tatada = tatamize(xd)
```

To be added:

- File-backed matrices from the [**FileBackedArray**](https://github.com/BiocPy/FileBackedArray) package, including HDF5 and TileDB.
- Arbitrary Python matrices?

## Utility methods

The `TatamiNumericPointer` instance returned by `tatamize()` provides a few Python-visible methods for querying the C++ matrix.

```python
tatamat.nrow() // number of rows
tatamat.column(1) // contents of column 1
tatamat.sparse() // whether the matrix is sparse.
```

It also has a few methods for computing common statistics:

```python
tatamat.row_sums()
tatamat.column_variances(num_threads = 2)

grouping = [i%3 for i in range(tatamat.ncol())]
tatamat.row_medians_by_group(grouping)

tatamat.row_nan_counts()
tatamat.column_ranges()
```

These are mostly intended for non-intensive work or testing/debugging.
It is expected that any serious computation should be performed by iterating over the matrix in C++.

## Operating on an existing pointer

If we already have a `TatamiNumericPointer`, we can easily apply additional operations by wrapping it in the relevant **delayedarray** layers and calling `tatamize()` afterwards.
For example, if we want to add a scalar, we might do:

```python
from delayedarray import DelayedArray
from mattress import tatamize
import numpy

x = numpy.random.rand(1000, 10)
tatamat = tatamize(x)

wrapped = DelayedArray(tatamat) + 1
tatamat2 = tatamize(wrapped)
```

This avoids relying on `x` and is more efficient as it re-uses the `TatamiNumericPointer` generated from `x`.

## Developer Notes

Build the shared object file:

```shell
python setup.py build_ext --inplace
```

For quick testing, we usually do:

```shell
pytest
```

For more complex testing, we do:

```shell
python setup.py build_ext --inplace && tox
```

To rebuild the **ctypes** bindings with [**cpptypes**](https://github.com/BiocPy/ctypes-wrapper):

```shell
cpptypes src/mattress/lib --py src/mattress/_cpphelpers.py --cpp src/mattress/lib/bindings.cpp --dll _core
```
