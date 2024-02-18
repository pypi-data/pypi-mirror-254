// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_HIT_AND_RUN_TRANSFORMS_H
#define SAMPLY_HIT_AND_RUN_TRANSFORMS_H

#include <Eigen/Dense>

#include "commons.h"
#include "reparametrized_object.h"

namespace samply {

template <typename TransformationScalar> class HitAndRunTransforms {
  public:
    // Fi is the coordinate system of the internal state.
    // If the chord sampler doesn't need a frame, Fs will be the same as Fi.
    template <
        typename DirectionSampler,
        typename SpaceDescriptor,
        typename ChordSampler>
    HitAndRunTransforms(
        const ReparametrizedObject<DirectionSampler>& direction_sampler_Fp,
        const ReparametrizedObject<SpaceDescriptor>& descriptor_Fi,
        const ReparametrizedObject<ChordSampler>& sampler_Fs)
        : from_Fi(descriptor_Fi.from_frame().template cast<TransformationScalar>())
        , to_Fi(descriptor_Fi.to_frame().template cast<TransformationScalar>())
        , Fp_to_Fi_linear((descriptor_Fi.to_frame().linear() *
                           direction_sampler_Fp.from_frame().linear())
                              .template cast<TransformationScalar>())
        , Fp_to_Fs_linear(
              make_Fp_to_Fs_transform(direction_sampler_Fp, descriptor_Fi, sampler_Fs))
        , Fi_to_Fs(make_Fi_to_Fs_transform(descriptor_Fi, sampler_Fs))
        , prefer_Fp_to_Fs_over_Fi_to_Fs(
              find_cheapest_linear_transform({Fi_to_Fs, Fp_to_Fs_linear}) == 1u)
        , Fs_equal_Fi(!sampler_Fs.needs_frame())
    {}

    template <typename DirectionsType>
    void transform_directions_from_Fp_to_Fi(
        DirectionsType& output, const DirectionsType& directions_Fp)
    {
        Fp_to_Fi_linear.transform(output, directions_Fp);
    }

    void transform_rays_from_Fi_to_Fs(
        RaysPacket<TransformationScalar>& output,
        const RaysPacket<TransformationScalar>& rays_Fi,
        const Matrix<TransformationScalar>& directions_Fp)
    {
        if (Fs_equal_Fi) {
            output = rays_Fi;
        }
        else if (prefer_Fp_to_Fs_over_Fi_to_Fs) {
            output.origins = Fi_to_Fs * rays_Fi.origins;
            output.directions = Fp_to_Fs_linear * directions_Fp;
        }
        else {
            Fi_to_Fs.transform(output, rays_Fi);
        }
    }

    void transform_rays_from_Fi_to_Fs(
        RaysPacket<TransformationScalar>& output,
        const AxisRaysPacket<TransformationScalar>& rays_Fi,
        const IndexVector& axis_ids)
    {
        if (Fs_equal_Fi) {
            output = AffineTransform<TransformationScalar>::identity(
                         static_cast<Index>(rays_Fi.origins.rows())) *
                     rays_Fi;
        }
        else if (prefer_Fp_to_Fs_over_Fi_to_Fs) {
            output = RaysPacket<TransformationScalar>{
                Fi_to_Fs * rays_Fi.origins,
                Fp_to_Fs_linear.get_linear()(Eigen::all, axis_ids)};
        }
        else {
            output = Fi_to_Fs * rays_Fi;
        }
    }

    Matrix<TransformationScalar>
    transform_from_Fi(const Matrix<TransformationScalar>& origins_Fi)
    {
        return from_Fi * origins_Fi;
    }

    Matrix<TransformationScalar>
    transform_to_Fi(const Matrix<TransformationScalar>& origins)
    {
        return to_Fi * origins;
    }

    bool is_Fs_equal_Fi() const { return Fs_equal_Fi; }

  protected:
    size_t find_cheapest_linear_transform(
        const std::vector<
            AffineTransform<TransformationScalar>,
            Eigen::aligned_allocator<AffineTransform<TransformationScalar>>>&
            transforms) const
    {
        assert(!transforms.empty());

        // Look for an identity transform
        auto optimal_transform_it = std::find_if(
            transforms.begin(), transforms.end(),
            [](const AffineTransform<TransformationScalar>& transform) {
                return transform.get_linear().isIdentity(TransformationScalar(1e-10));
            });
        if (optimal_transform_it != transforms.end())
            return std::distance(transforms.begin(), optimal_transform_it);

        // If none is found, look for a diagonal transform.
        optimal_transform_it = std::find_if(
            transforms.begin(), transforms.end(),
            [](const AffineTransform<TransformationScalar>& transform) {
                return transform.get_linear().isDiagonal();
            });
        if (optimal_transform_it != transforms.end())
            return std::distance(transforms.begin(), optimal_transform_it);

        // If none is found, all transforms are dense. Just return the first
        // one.
        return 0;
    }

    template <
        typename DirectionSampler,
        typename SpaceDescriptor,
        typename ChordSampler>
    AffineTransform<TransformationScalar> make_Fp_to_Fs_transform(
        const ReparametrizedObject<DirectionSampler>& direction_sampler_Fp,
        const ReparametrizedObject<SpaceDescriptor>& descriptor_Fi,
        const ReparametrizedObject<ChordSampler>& sampler_Fs)
    {
        if (sampler_Fs.needs_frame())
            return (sampler_Fs.to_frame().linear() *
                    direction_sampler_Fp.from_frame().linear())
                .template cast<TransformationScalar>();
        else
            return direction_sampler_Fp.from_frame();
    }

    template <typename SpaceDescriptor, typename ChordSampler>
    AffineTransform<TransformationScalar> make_Fi_to_Fs_transform(
        const ReparametrizedObject<SpaceDescriptor>& descriptor_Fi,
        const ReparametrizedObject<ChordSampler>& sampler_Fs)
    {
        if (sampler_Fs.needs_frame())
            return (sampler_Fs.to_frame() * descriptor_Fi.from_frame())
                .template cast<TransformationScalar>();
        else
            return AffineTransform<TransformationScalar>::identity(
                descriptor_Fi.from_frame().get_linear().cols());
    }

    const AffineTransform<TransformationScalar> from_Fi;
    const AffineTransform<TransformationScalar> to_Fi;

    const AffineTransform<TransformationScalar> Fp_to_Fi_linear;
    const AffineTransform<TransformationScalar> Fp_to_Fs_linear;
    const AffineTransform<TransformationScalar> Fi_to_Fs;

    bool prefer_Fp_to_Fs_over_Fi_to_Fs;
    bool Fs_equal_Fi;
};

} // namespace samply

#endif
