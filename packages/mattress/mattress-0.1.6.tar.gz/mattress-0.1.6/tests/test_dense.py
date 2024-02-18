import numpy as np
from mattress import tatamize

__author__ = "ltla, jkanche"
__copyright__ = "ltla, jkanche"
__license__ = "MIT"


def test_dense():
    y = np.random.rand(1000, 100)
    ptr = tatamize(y)
    assert all(ptr.row(0) == y[0, :])
    assert all(ptr.column(1) == y[:, 1])
    assert ptr.shape == (1000, 100)
    assert ptr.dtype == np.float64


def test_numpy_with_dtype():
    y = (np.random.rand(50, 12) * 100).astype("i8")
    ptr = tatamize(y)
    assert all(ptr.row(0) == y[0, :])
    assert all(ptr.column(1) == y[:, 1])


def test_dense_column_major():
    y = np.ndarray((1000, 100), order="F")
    y[:, :] = np.random.rand(1000, 100)
    assert y.flags["F_CONTIGUOUS"]
    ptr = tatamize(y)
    assert all(ptr.row(0) == y[0, :])
    assert all(ptr.column(1) == y[:, 1])
