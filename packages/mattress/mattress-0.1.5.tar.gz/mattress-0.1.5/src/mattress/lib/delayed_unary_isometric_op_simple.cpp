#include "Mattress.h"
#include <cstring>

//[[export]]
void* initialize_delayed_unary_isometric_op_simple(void* ptr, const char* op) {
    auto mat = reinterpret_cast<Mattress*>(ptr);

    if (std::strcmp(op, "abs") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAbsHelper<>()));
    } else if (std::strcmp(op, "sign") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedSignHelper<>()));

    } else if (std::strcmp(op, "log") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedLogHelper<>()));
    } else if (std::strcmp(op, "log2") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedLogHelper(2.0)));
    } else if (std::strcmp(op, "log10") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedLogHelper(10.0)));
    } else if (std::strcmp(op, "log1p") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedLog1pHelper<>()));

    } else if (std::strcmp(op, "sqrt") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedSqrtHelper<>()));

    } else if (std::strcmp(op, "ceil") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedCeilingHelper<>()));
    } else if (std::strcmp(op, "floor") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedFloorHelper<>()));
    } else if (std::strcmp(op, "trunc") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedTruncHelper<>()));
    } else if (std::strcmp(op, "round") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedRoundHelper<>()));

    } else if (std::strcmp(op, "exp") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedExpHelper<>()));
    } else if (std::strcmp(op, "expm1") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedExpm1Helper<>()));

    } else if (std::strcmp(op, "cos") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedCosHelper<>()));
    } else if (std::strcmp(op, "sin") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedSinHelper<>()));
    } else if (std::strcmp(op, "tan") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedTanHelper<>()));

    } else if (std::strcmp(op, "cosh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedCoshHelper<>()));
    } else if (std::strcmp(op, "sinh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedSinhHelper<>()));
    } else if (std::strcmp(op, "tanh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedTanhHelper<>()));

    } else if (std::strcmp(op, "arccos") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAcosHelper<>()));
    } else if (std::strcmp(op, "arcsin") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAsinHelper<>()));
    } else if (std::strcmp(op, "arctan") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAtanHelper<>()));

    } else if (std::strcmp(op, "arccosh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAcoshHelper<>()));
    } else if (std::strcmp(op, "arcsinh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAsinhHelper<>()));
    } else if (std::strcmp(op, "arctanh") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::DelayedAtanhHelper<>()));

    } else {
        throw std::runtime_error("operation '" + std::string(op) + "' is currently not supported");
    }

    return NULL;
}
