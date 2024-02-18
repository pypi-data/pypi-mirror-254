#include "Mattress.h"
#include <cstdint>
#include <algorithm>

//[[export]]
int extract_nrow(const void* mat) {
    return reinterpret_cast<const Mattress*>(mat)->ptr->nrow();
}

//[[export]]
int extract_ncol(const void* mat) {
    return reinterpret_cast<const Mattress*>(mat)->ptr->ncol();
}

//[[export]]
int extract_sparse(const void* mat) {
    return reinterpret_cast<const Mattress*>(mat)->ptr->sparse();
}

/** Extraction **/

//[[export]]
void extract_row(void* rawmat, int32_t r, double* output /** void_p */) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    if (!mat->byrow) {
        mat->byrow = mat->ptr->dense_row();
    }
    mat->byrow->fetch_copy(r, output);
}

//[[export]]
void extract_column(void* rawmat, int32_t c, double* output /** void_p */) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    if (!mat->bycol) {
        mat->bycol = mat->ptr->dense_column();
    }
    mat->bycol->fetch_copy(c, output);
}

/** Stats **/

//[[export]]
void compute_column_sums(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_sums(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_row_sums(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_sums(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_column_variances(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_variances(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_row_variances(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_variances(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_column_medians(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_medians(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_row_medians(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_medians(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_column_mins(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_mins(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_row_mins(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_mins(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_column_maxs(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_maxs(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_row_maxs(void* rawmat, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    auto res = tatami::row_maxs(mat->ptr.get(), num_threads);
    std::copy(res.begin(), res.end(), output);
}

//[[export]]
void compute_column_ranges(void* rawmat, double* min_output /** void_p */, double* max_output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_ranges(mat->ptr.get(), min_output, max_output, num_threads);
}

//[[export]]
void compute_row_ranges(void* rawmat, double* min_output /** void_p */, double* max_output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_ranges(mat->ptr.get(), min_output, max_output, num_threads);
}

//[[export]]
void compute_row_nan_counts(void* rawmat, int32_t* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::row_nan_counts(mat->ptr.get(), output, num_threads);
}

//[[export]]
void compute_column_nan_counts(void* rawmat, int32_t* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::column_nan_counts(mat->ptr.get(), output, num_threads);
}

/** Grouped stats **/

//[[export]]
void compute_row_sums_by_group(void* rawmat, const int32_t* grouping /** void_p */, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    size_t num_groups = tatami::stats::total_groups(grouping, mat->ptr->ncol());
    tatami::row_sums_by_group(mat->ptr.get(), grouping, num_groups, output, num_threads);
}

//[[export]]
void compute_column_sums_by_group(void* rawmat, const int32_t* grouping /** void_p */, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    size_t num_groups = tatami::stats::total_groups(grouping, mat->ptr->nrow());
    tatami::column_sums_by_group(mat->ptr.get(), grouping, num_groups, output, num_threads);
}

//[[export]]
void compute_row_medians_by_group(void* rawmat, const int32_t* grouping /** void_p */, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    auto group_sizes = tatami::stats::tabulate_groups(grouping, mat->ptr->ncol());
    tatami::row_medians_by_group(mat->ptr.get(), grouping, group_sizes, output, num_threads);
}

//[[export]]
void compute_column_medians_by_group(void* rawmat, const int32_t* grouping /** void_p */, double* output /** void_p */, int32_t num_threads) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    auto group_sizes = tatami::stats::tabulate_groups(grouping, mat->ptr->nrow());
    tatami::column_medians_by_group(mat->ptr.get(), grouping, group_sizes, output, num_threads);
}

/** Extraction **/

//[[export]]
void extract_dense_full(void* rawmat, double* output /** void_p */) {
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    tatami::convert_to_dense<true>(mat->ptr.get(), output);
}

//[[export]]
void extract_dense_subset(void* rawmat,
    uint8_t row_noop,
    const int32_t* row_sub /** void_p */,
    int32_t row_len,
    uint8_t col_noop,
    const int32_t* col_sub /** void_p */,
    int32_t col_len,
    double* output /** void_p */)
{
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    if (row_noop && col_noop) {
        return tatami::convert_to_dense<true>(mat->ptr.get(), output);
    }

    auto ptr = mat->ptr;
    if (!row_noop) {
        ptr = tatami::make_DelayedSubset<0>(std::move(ptr), tatami::ArrayView<int32_t>(row_sub, row_len));
    }
    if (!col_noop) {
        ptr = tatami::make_DelayedSubset<1>(std::move(ptr), tatami::ArrayView<int32_t>(col_sub, col_len));
    }

    tatami::convert_to_dense<true>(ptr.get(), output);
}

//[[export]]
void extract_sparse_subset(void* rawmat,
    uint8_t row_noop,
    const int32_t* row_sub /** void_p */,
    int32_t row_len,
    uint8_t col_noop,
    const int32_t* col_sub /** void_p */,
    int32_t col_len,
    int32_t* output_count /** void_p */,
    int32_t* output_indices /** void_p */,
    double* output_values /** void_p */)
{
    auto mat = reinterpret_cast<Mattress*>(rawmat);
    auto ptr = mat->ptr;

    if (!row_noop) {
        ptr = tatami::make_DelayedSubset<0>(std::move(ptr), tatami::ArrayView<int32_t>(row_sub, row_len));
    }
    if (!col_noop) {
        ptr = tatami::make_DelayedSubset<1>(std::move(ptr), tatami::ArrayView<int32_t>(col_sub, col_len));
    }

    auto NC = ptr->ncol();
    auto NR = ptr->nrow();

    if (ptr->prefer_rows()) {
        auto ext = tatami::consecutive_extractor<true, true>(ptr.get(), 0, NR);
        std::vector<double> vbuffer(NC);
        std::vector<int32_t> ibuffer(NC);
        std::fill(output_count, output_count + NC, 0); // avoid adding to an uninitialized count.

        for (int32_t r = 0; r < NR; ++r) {
            auto info = ext->fetch(r, vbuffer.data(), ibuffer.data());
            for (int32_t i = 0; i < info.number; ++i) {
                auto c = info.index[i];
                auto& count = output_count[c];
                auto offset = count + static_cast<size_t>(c) * NR;
                output_indices[offset] = r;
                output_values[offset] = info.value[i];
                ++count;
            }
        }
    } else {
        auto ext = tatami::consecutive_extractor<false, true>(ptr.get(), 0, NC);
        for (int32_t c = 0; c < NC; ++c, output_values += NR, output_indices += NR) {
            auto info = ext->fetch_copy(c, output_values, output_indices);
            output_count[c] = info.number;
        }
    }
}

/** Freeing **/

//[[export]]
void free_mat(void* mat) {
    delete reinterpret_cast<Mattress*>(mat);
}
