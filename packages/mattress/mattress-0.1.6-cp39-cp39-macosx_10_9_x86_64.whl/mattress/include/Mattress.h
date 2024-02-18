#ifndef MATTRESS_COMMON_H
#define MATTRESS_COMMON_H

#include "tatami/tatami.hpp"
#include <iostream>

struct Mattress {
    Mattress(tatami::NumericMatrix* p) : ptr(p) {}
    Mattress(std::shared_ptr<tatami::NumericMatrix> p) : ptr(std::move(p)) {}
    std::shared_ptr<tatami::NumericMatrix> ptr;
    std::unique_ptr<tatami::FullDenseExtractor<double, int> > byrow, bycol;
};

#endif
