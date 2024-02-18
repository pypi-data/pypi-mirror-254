#include "Mattress.h"
#include <cstring>
#include <cstdint>

template<bool right_, int along_>
void* initialize_delayed_unary_isometric_op_with_vector(const Mattress* mat, const char* op, const double* arg) {
    tatami::ArrayView<double> aview(arg, along_ == 0 ? mat->ptr->nrow() : mat->ptr->ncol());

    if (std::strcmp(op, "add") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedAddVectorHelper<along_>(std::move(aview))));
    } else if (std::strcmp(op, "subtract") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedSubtractVectorHelper<right_, along_>(std::move(aview))));
    } else if (std::strcmp(op, "multiply") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedMultiplyVectorHelper<along_>(std::move(aview))));
    } else if (std::strcmp(op, "divide") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedDivideVectorHelper<right_, along_>(std::move(aview))));
    } else if (std::strcmp(op, "remainder") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedModuloVectorHelper<right_, along_>(std::move(aview))));
    } else if (std::strcmp(op, "floor_divide") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedIntegerDivideVectorHelper<right_, along_>(std::move(aview))));
    } else if (std::strcmp(op, "power") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedPowerVectorHelper<right_, along_>(std::move(aview))));

    } else if (std::strcmp(op, "equal") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedEqualVectorHelper<along_>(std::move(aview))));
    } else if (std::strcmp(op, "not_equal") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedNotEqualVectorHelper<along_>(std::move(aview))));
    } else if ((right_ && std::strcmp(op, "greater") == 0) || (!right_ && std::strcmp(op, "less") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedGreaterThanVectorHelper<along_>(std::move(aview))));
    } else if ((right_ && std::strcmp(op, "greater_equal") == 0) || (!right_ && std::strcmp(op, "less_equal") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedGreaterThanOrEqualVectorHelper<along_>(std::move(aview))));
    } else if ((right_ && std::strcmp(op, "less") == 0) || (!right_ && std::strcmp(op, "greater") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedLessThanVectorHelper<along_>(std::move(aview))));
    } else if ((right_ && std::strcmp(op, "less_equal") == 0) || (!right_ && std::strcmp(op, "greater_equal") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedLessThanOrEqualVectorHelper<along_>(std::move(aview))));

    } else if (std::strcmp(op, "logical_and") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanAndVectorHelper<along_>(std::move(aview))));
    } else if (std::strcmp(op, "logical_or") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanOrVectorHelper<along_>(std::move(aview))));
    } else if (std::strcmp(op, "logical_xor") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanXorVectorHelper<along_>(std::move(aview))));

    } else {
        throw std::runtime_error("unknown unary isometric vector operation '" + std::string(op) + "'");
    }
    return NULL;
}

//[[export]]
void* initialize_delayed_unary_isometric_op_with_vector(void* ptr, const char* op, uint8_t right, int32_t along, const double* args /** numpy */) {
    auto mat = reinterpret_cast<Mattress*>(ptr);
    if (right) {
        if (along == 0) {
            return initialize_delayed_unary_isometric_op_with_vector<true, 0>(mat, op, args);
        } else {
            return initialize_delayed_unary_isometric_op_with_vector<true, 1>(mat, op, args);
        }
    } else {
        if (along == 0) {
            return initialize_delayed_unary_isometric_op_with_vector<false, 0>(mat, op, args);
        } else {
            return initialize_delayed_unary_isometric_op_with_vector<false, 1>(mat, op, args);
        }
    }
}

template<bool right_>
void* initialize_delayed_unary_isometric_op_with_scalar(const Mattress* mat, const char* op, double arg) {
    if (std::strcmp(op, "add") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedAddScalarHelper(arg)));
    } else if (std::strcmp(op, "subtract") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedSubtractScalarHelper<right_>(arg)));
    } else if (std::strcmp(op, "multiply") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedMultiplyScalarHelper(arg)));
    } else if (std::strcmp(op, "divide") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedDivideScalarHelper<right_>(arg)));
    } else if (std::strcmp(op, "remainder") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedModuloScalarHelper<right_>(arg)));
    } else if (std::strcmp(op, "floor_divide") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedIntegerDivideScalarHelper<right_>(arg)));
    } else if (std::strcmp(op, "power") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedPowerScalarHelper<right_>(arg)));

    } else if (std::strcmp(op, "equal") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedEqualScalarHelper(arg)));
    } else if (std::strcmp(op, "not_equal") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedNotEqualScalarHelper(arg)));
    } else if ((right_ && std::strcmp(op, "greater") == 0) || (!right_ && std::strcmp(op, "less") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedGreaterThanScalarHelper(arg)));
    } else if ((right_ && std::strcmp(op, "greater_equal") == 0) || (!right_ && std::strcmp(op, "less_equal") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedGreaterThanOrEqualScalarHelper(arg)));
    } else if ((right_ && std::strcmp(op, "less") == 0) || (!right_ && std::strcmp(op, "greater") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedLessThanScalarHelper(arg)));
    } else if ((right_ && std::strcmp(op, "less_equal") == 0) || (!right_ && std::strcmp(op, "greater_equal") == 0)) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedLessThanOrEqualScalarHelper(arg)));

    } else if (std::strcmp(op, "logical_and") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanAndScalarHelper<>(arg)));
    } else if (std::strcmp(op, "logical_or") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanOrScalarHelper<>(arg)));
    } else if (std::strcmp(op, "logical_xor") == 0) {
        return new Mattress(tatami::make_DelayedUnaryIsometricOp(mat->ptr, tatami::make_DelayedBooleanXorScalarHelper<>(arg)));

    } else {
        throw std::runtime_error("unknown unary isometric scalar operation '" + std::string(op) + "'");
    }
    return NULL;
}

//[[export]]
void* initialize_delayed_unary_isometric_op_with_scalar(void* ptr, const char* op, bool right, double arg) {
    auto mat = reinterpret_cast<Mattress*>(ptr);
    if (right) {
        return initialize_delayed_unary_isometric_op_with_scalar<true>(mat, op, arg);
    } else {
        return initialize_delayed_unary_isometric_op_with_scalar<false>(mat, op, arg);
    }
}
