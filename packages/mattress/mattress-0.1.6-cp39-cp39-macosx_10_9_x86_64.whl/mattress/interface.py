from functools import singledispatch
from typing import Any

import numpy as np
import delayedarray
from biocutils.package_utils import is_package_installed


from .TatamiNumericPointer import TatamiNumericPointer
from . import _cpphelpers as lib
from .utils import _sanitize_subset

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"


@singledispatch
def tatamize(x: Any) -> TatamiNumericPointer:
    """Converts Python matrix representations to a tatami pointer.

    Args:
        x: Any matrix-like object.

    Raises:
        NotImplementedError: if x is not supported.

    Returns:
        A pointer to tatami object.
    """
    raise NotImplementedError(
        f"tatamize is not supported for objects of class: {type(x)}"
    )


@tatamize.register
def _tatamize_pointer(x: TatamiNumericPointer) -> TatamiNumericPointer:
    return x  # no-op


@tatamize.register
def _tatamize_numpy(x: np.ndarray) -> TatamiNumericPointer:
    if len(x.shape) != 2:
        raise ValueError("'x' should be a 2-dimensional array")

    byrow = None
    if x.flags["C_CONTIGUOUS"]:
        byrow = True
    elif x.flags["F_CONTIGUOUS"]:
        byrow = False
    else:
        # I don't think it's possible to hit this, as a (non-view) ndarray
        # should be contiguous in at least one direction.
        raise ValueError("'x' must have contiguous storage for its arrays")

    return TatamiNumericPointer(
        ptr=lib.initialize_dense_matrix(
            x.shape[0],
            x.shape[1],
            str(x.dtype).encode("UTF-8"),
            x.ctypes.data,
            byrow,
        ),
        obj=[x],
    )

if is_package_installed("scipy"):
    import scipy.sparse

    @tatamize.register
    def _tatamize_sparse_csr_array(x: scipy.sparse.csr_array) -> TatamiNumericPointer:
        tmp = x.indptr.astype(np.uint64, copy=False)
        return TatamiNumericPointer(
            ptr=lib.initialize_compressed_sparse_matrix(
                x.shape[0],
                x.shape[1],
                len(x.data),
                str(x.data.dtype).encode("UTF-8"),
                x.data.ctypes.data,
                str(x.indices.dtype).encode("UTF-8"),
                x.indices.ctypes.data,
                tmp.ctypes.data,
                True,
            ),
            obj=[tmp, x],
        )


    @tatamize.register
    def _tatamize_sparse_csr_matrix(x: scipy.sparse.csr_matrix) -> TatamiNumericPointer:
        return _tatamize_sparse_csr_array(x)


    @tatamize.register
    def _tatamize_sparse_csc_array(x: scipy.sparse.csc_array) -> TatamiNumericPointer:
        tmp = x.indptr.astype(np.uint64, copy=False)
        return TatamiNumericPointer(
            ptr=lib.initialize_compressed_sparse_matrix(
                x.shape[0],
                x.shape[1],
                len(x.data),
                str(x.data.dtype).encode("UTF-8"),
                x.data.ctypes.data,
                str(x.indices.dtype).encode("UTF-8"),
                x.indices.ctypes.data,
                tmp.ctypes.data,
                False,
            ),
            obj=[tmp, x],
        )


    @tatamize.register
    def _tatamize_sparse_csc_matrix(x: scipy.sparse.csc_matrix) -> TatamiNumericPointer:
        return _tatamize_sparse_csc_array(x)


@tatamize.register
def _tatamize_delayed_array(x: delayedarray.DelayedArray) -> TatamiNumericPointer:
    return tatamize(x.seed)


@tatamize.register
def _tatamize_delayed_unary_isometric_op_simple(
    x: delayedarray.UnaryIsometricOpSimple,
) -> TatamiNumericPointer:
    components = tatamize(x.seed)
    ptr = lib.initialize_delayed_unary_isometric_op_simple(
        components.ptr, x.operation.encode("UTF-8")
    )
    return TatamiNumericPointer(ptr, components.obj)


@tatamize.register
def _tatamize_delayed_unary_isometric_op_with_args(
    x: delayedarray.UnaryIsometricOpWithArgs,
) -> TatamiNumericPointer:
    components = tatamize(x.seed)
    obj = components.obj

    if isinstance(x.value, np.ndarray):
        contents = x.value.astype(np.float64, copy=False)
        ptr = lib.initialize_delayed_unary_isometric_op_with_vector(
            components.ptr, x.operation.encode("UTF-8"), x.right, x.along, contents
        )
        obj.append(contents)
    else:
        ptr = lib.initialize_delayed_unary_isometric_op_with_scalar(
            components.ptr, x.operation.encode("UTF-8"), x.right, x.value
        )

    return TatamiNumericPointer(ptr, obj)


@tatamize.register
def _tatamize_delayed_subset(
    x: delayedarray.Subset,
) -> TatamiNumericPointer:
    components = tatamize(x.seed)
    obj = components.obj

    for dim in range(2):
        current = x.subset[dim]
        noop, current = _sanitize_subset(current, x.shape[dim])
        if not noop:
            ptr = lib.initialize_delayed_subset(
                components.ptr, dim, current, len(current)
            )
            obj.append(current)
            components = TatamiNumericPointer(ptr, obj)

    return components


@tatamize.register
def _tatamize_delayed_combine(
    x: delayedarray.Combine,
) -> TatamiNumericPointer:
    nseeds = len(x.seeds)
    objects = []
    converted = []
    ptrs = np.ndarray(nseeds, dtype=np.uintp)

    for i in range(nseeds):
        components = tatamize(x.seeds[i])
        converted.append(components)
        ptrs[i] = components.ptr
        objects += components.obj

    ptr = lib.initialize_delayed_combine(nseeds, ptrs.ctypes.data, x.along)
    return TatamiNumericPointer(ptr, objects)


@tatamize.register
def _tatamize_delayed_transpose(
    x: delayedarray.Transpose,
) -> TatamiNumericPointer:
    components = tatamize(x.seed)

    if x.perm == (1, 0):
        ptr = lib.initialize_delayed_transpose(components.ptr)
        components = TatamiNumericPointer(ptr, components.obj)

    return components


@tatamize.register
def _tatamize_delayed_binary_isometric_op(
    x: delayedarray.BinaryIsometricOp,
) -> TatamiNumericPointer:
    lcomponents = tatamize(x.left)
    rcomponents = tatamize(x.right)

    ptr = lib.initialize_delayed_binary_isometric_op(
        lcomponents.ptr, rcomponents.ptr, x.operation.encode("UTF-8")
    )

    return TatamiNumericPointer(ptr, lcomponents.obj + rcomponents.obj)


@tatamize.register
def _tatamize_delayed_round(
    x: delayedarray.Round,
) -> TatamiNumericPointer:
    components = tatamize(x.seed)

    if x.decimals != 0:
        raise NotImplementedError(
            "non-zero decimals in 'delayedarray.Round' are not yet supported"
        )

    ptr = lib.initialize_delayed_unary_isometric_op_simple(
        components.ptr, "round".encode("UTF-8")
    )

    return TatamiNumericPointer(ptr, components.obj)
