#include "Mattress.h"
#include <cstring>
#include <cstdint>

//[[export]]
void* initialize_delayed_binary_isometric_op(void* left, void* right, const char* op) {
    auto lmat = reinterpret_cast<Mattress*>(left);
    auto rmat = reinterpret_cast<Mattress*>(right);

    if (std::strcmp(op, "add") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryAddHelper()));
    } else if (std::strcmp(op, "subtract") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinarySubtractHelper()));
    } else if (std::strcmp(op, "multiply") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryMultiplyHelper()));
    } else if (std::strcmp(op, "divide") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryDivideHelper()));
    } else if (std::strcmp(op, "remainder") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryModuloHelper()));
    } else if (std::strcmp(op, "floor_divide") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryIntegerDivideHelper()));
    } else if (std::strcmp(op, "power") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryPowerHelper()));

    } else if (std::strcmp(op, "equal") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryEqualHelper()));
    } else if (std::strcmp(op, "not_equal") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryNotEqualHelper()));
    } else if (std::strcmp(op, "greater") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryGreaterThanHelper()));
    } else if (std::strcmp(op, "greater_equal") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryGreaterThanOrEqualHelper()));
    } else if (std::strcmp(op, "less") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryLessThanHelper()));
    } else if (std::strcmp(op, "less_equal") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryLessThanOrEqualHelper()));

    } else if (std::strcmp(op, "logical_and") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryBooleanAndHelper()));
    } else if (std::strcmp(op, "logical_or") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryBooleanOrHelper()));
    } else if (std::strcmp(op, "logical_xor") == 0) {
        return new Mattress(tatami::make_DelayedBinaryIsometricOp(lmat->ptr, rmat->ptr, tatami::make_DelayedBinaryBooleanXorHelper()));

    } else {
        throw std::runtime_error("unknown binary isometric operation '" + std::string(op) + "'");
    }
    return NULL;
}
