import numpy as np
from mattress import tatamize, TatamiNumericPointer
import delayedarray as da

__author__ = "ltla, jkanche"
__copyright__ = "ltla, jkanche"
__license__ = "MIT"


def test_pointer_rewrap():
    y = np.random.rand(1000, 100)
    ptr = tatamize(y)
    reptr = tatamize(ptr)
    assert ptr.ptr == reptr.ptr


def test_simple_stats():
    y = np.random.rand(1000, 100)
    ptr = tatamize(y)

    assert np.allclose(ptr.row_sums(), y.sum(axis=1))
    assert np.allclose(ptr.column_sums(), y.sum(axis=0))
    assert np.allclose(ptr.row_variances(), y.var(axis=1, ddof=1))
    assert np.allclose(ptr.column_variances(), y.var(axis=0, ddof=1))

    assert ptr.row_medians().shape == (1000,)
    assert ptr.column_medians().shape == (100,)

    assert (ptr.row_mins() == y.min(axis=1)).all()
    assert (ptr.column_mins() == y.min(axis=0)).all()
    assert (ptr.row_maxs() == y.max(axis=1)).all()
    assert (ptr.column_maxs() == y.max(axis=0)).all()

    mn, mx = ptr.row_ranges()
    assert (mn == y.min(axis=1)).all()
    assert (mx == y.max(axis=1)).all()
    mn, mx = ptr.column_ranges()
    assert (mn == y.min(axis=0)).all()
    assert (mx == y.max(axis=0)).all()


def test_nan_counts():
    y = np.random.rand(20, 10)
    y[0, 0] = np.NaN
    y[1, 2] = np.NaN
    y[4, 3] = np.NaN
    y[2, 3] = np.NaN

    ptr = tatamize(y)
    rnan = ptr.row_nan_counts()
    cnan = ptr.column_nan_counts()
    assert rnan[0] == 1
    assert cnan[3] == 2


def test_grouped_stats():
    y = np.random.rand(20, 10)
    ptr = tatamize(y)

    cgrouping = ["D", "C", "B", "A", "A", "B", "C", "B", "A", "A"]
    rgrouping = []
    for i in range(20):
        rgrouping.append(i % 3)

    rmed, rlev = ptr.row_medians_by_group(cgrouping)
    assert rmed.shape == (20, 4)
    assert len(rlev) == 4
    assert (rmed[:, rlev.index("D")] == y[:, 0]).all()

    cmed, clev = ptr.column_medians_by_group(rgrouping)
    assert cmed.shape == (3, 10)
    assert len(clev) == 3

    keep = []
    for i, x in enumerate(rgrouping):
        if x == 1:
            keep.append(i)
    ref = y[keep, :]
    rptr = tatamize(ref)
    assert (cmed[clev.index(1), :] == rptr.column_medians()).all()

    rsum, rlev = ptr.row_sums_by_group(cgrouping)
    assert rsum.shape == (20, 4)
    assert len(rlev) == 4
    assert (rsum[:, rlev.index("D")] == y[:, 0]).all()

    csum, clev = ptr.column_sums_by_group(rgrouping)
    assert csum.shape == (3, 10)
    assert len(clev) == 3

    keep = []
    for i, x in enumerate(rgrouping):
        if x == 0:
            keep.append(i)
    ref = y[keep, :]
    rptr = tatamize(ref)
    assert (csum[clev.index(0), :] == rptr.column_sums()).all()


def test_DelayedArray_rewrap():
    y = np.random.rand(1000, 100)
    ptr = tatamize(y)

    da2 = da.DelayedArray(ptr)
    assert isinstance(da2.seed, TatamiNumericPointer)
    assert (np.array(da2) == y).all()

    sub = da2[10:50, 0:100:2]
    assert (np.array(sub) == y[10:50, 0:100:2]).all()

    sub = da2[10:50, :]
    assert (np.array(sub) == y[10:50, :]).all()

    sub = da2[:10:50]
    assert (np.array(sub) == y[:10:50]).all()
