#include "Mattress.h"

//[[export]]
void* initialize_delayed_combine(int32_t n, uintptr_t* ptrs /** void_p */, int32_t dim) {
    std::vector<std::shared_ptr<tatami::NumericMatrix> > combined;
    combined.reserve(n);

    for (int32_t i = 0; i < n; ++i) {
        auto mat = reinterpret_cast<Mattress*>(ptrs[i]);
        combined.push_back(mat->ptr);
    }

    if (dim == 0) {
        return new Mattress(tatami::make_DelayedBind<0>(std::move(combined)));
    } else {
        return new Mattress(tatami::make_DelayedBind<1>(std::move(combined)));
    }
}
