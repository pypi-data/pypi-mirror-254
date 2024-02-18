// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_ORTHANTS_LOGGER_H
#define PTA_ORTHANTS_LOGGER_H

#include <chord_samplers/mvn_pdf_sampler.h>
#include <loggers/state_logger.h>

#include <dynamic_bitset.hpp>
#include <unordered_map>
#include <vector>

#include "steady_state_free_energies_descriptor.h"

namespace pta {

struct OrthantsHasher {
    std::size_t operator()(const std::vector<uint8_t>& k) const
    {
        std::size_t seed = k.size();
        for (auto& i : k) {
            seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

template <typename Scalar> class OrthantsStorage {
  public:
    typedef Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> StoredState;
    typedef std::vector<uint8_t> Orthant;
    typedef std::unordered_map<Orthant, uint32_t, OrthantsHasher> OrthantsMap;
    typedef std::vector<OrthantsMap> OrthantsMaps;

    OrthantsStorage(const size_t num_threads)
        : orthants_maps_(num_threads)
    {}

    const OrthantsMaps& get_orthants_maps() const { return orthants_maps_; }

    OrthantsMap get_aggregated_orthants_map() const
    {
        OrthantsMap result;
        for (const auto& map : orthants_maps_) {
            for (const auto& it : map) {
                auto insertion_result = result.insert({it.first, it.second});
                if (!insertion_result.second) {
                    insertion_result.first->second += it.second;
                }
            }
        }

        return result;
    }

    void log_state(const Orthant& orthant, const size_t worker_idx)
    {
        auto insertion_result =
            orthants_maps_[worker_idx].insert({std::move(orthant), 1});
        if (!insertion_result.second) {
            insertion_result.first->second++;
        }
    }

  private:
    OrthantsMaps orthants_maps_;
};

template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class OrthantsLogger : public samply::StateLogger<ChainState, DurationFormat> {
  public:
    OrthantsLogger(
        OrthantsStorage<double>& storage,
        const size_t worker_id,
        const size_t steps_log_interval,
        const size_t num_skipped_steps = 0u)
        : samply::StateLogger<ChainState, DurationFormat>(
              worker_id, steps_log_interval, num_skipped_steps)
        , storage_(storage)
        , descriptor_(nullptr)
        , sampler_(nullptr)
    {}

    OrthantsLogger(const OrthantsLogger<ChainState>& other)
        : samply::StateLogger<ChainState, DurationFormat>(other)
        , storage_(other.storage_)
        , descriptor_(other.descriptor_)
        , sampler_(other.sampler_)
    {}

    void start() override {}

    void stop(const bool time_limit_reached = false) override {}

    void set_descriptor(const SteadyStateFreeEnergiesDescriptor<double>& descriptor)
    {
        descriptor_ = &descriptor;
    }

    void set_sampler(const samply::MvnPdfSampler<double>& sampler)
    {
        sampler_ = &sampler;
    }

  protected:
    void log_state(ChainState& chain_state, const size_t step_idx) override
    {
        samply::Vector<double> ts = sampler_->get_last_sampled_ts();
        samply::Matrix<double> drgs = descriptor_->evaluate_last_drg_rays_at(ts);

        for (Eigen::Index sample_idx = 0u; sample_idx < drgs.cols(); sample_idx++) {
            dynamic_bitset direction_sample_bits(drgs.rows());
            for (Eigen::Index i = 0u; i < drgs.rows(); ++i) {
                direction_sample_bits.set(i, drgs(i, sample_idx) < 0);
            }
            storage_.log_state(
                std::move(direction_sample_bits.vector()), this->worker_id_);
        }
    }

  private:
    OrthantsStorage<double>& storage_;

    const SteadyStateFreeEnergiesDescriptor<double>* descriptor_;
    const samply::MvnPdfSampler<double>* sampler_;
};

} // namespace pta

#endif
