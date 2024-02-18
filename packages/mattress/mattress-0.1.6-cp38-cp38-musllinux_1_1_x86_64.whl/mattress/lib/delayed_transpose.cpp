#include "Mattress.h"

//[[export]]
void* initialize_delayed_transpose(void* ptr) {
    auto mat = reinterpret_cast<Mattress*>(ptr);
    return new Mattress(tatami::make_DelayedTranspose(mat->ptr));
}
