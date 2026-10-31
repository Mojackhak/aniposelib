# Cage integration for the `val` branch

This document describes cage integration on the local `val` branch, based on the
approved stable upstream release. The original fork branch is retained for
comparison. Changes on `val` are maintained locally and have not been published.
The acceptance scope is the single-animal cage pipeline and configurable
multi-candidate inference. Other fork-specific 3D changes are outside this scope.

## Recalculation boundaries

Inference changes or a change in num_outputs require regenerating raw poses and
their dependent filtering and mapping results. Viterbi settings affect Viterbi
and downstream results only. Autoencoder settings affect that stage and its
downstream results. Documentation, packaging metadata, formatting, and unused
3D settings do not invalidate cage results. No global cache or invalidation
mechanism is introduced. Existing output-skipping behavior is retained; stale
outputs must be moved aside explicitly before rerunning an affected stage.

## Validation

Run focused configuration, predictor, serialization, and filtering tests first.
Compare identical heatmaps and recorded pose inputs before comparing real-video
inference. Reuse the existing cage weights and autoencoder; do not retrain or
modify source model files. Run a short Windows CUDA integration in the isolated
val environment. Record actual results and any remaining limitation below.

## aniposelib contract

The `val` branch is based on upstream v0.8.0. The tag contains stale 0.7.2 package/runtime version
strings, while PyPI publishes 0.8.0. Compare the published source package with the
tag before aligning those strings with the approved 0.8.0 release. Do not invent
a fork version. Keep upstream calibration and triangulation implementations.
This package does not implement DeepLabCut num_outputs.

Verify imports from Anipose and the required OpenCV interfaces. Use the CPU JAX
runtime required by upstream; the cage CUDA path belongs to PyTorch. Keep one
opencv-contrib-python installation. No 3D data analysis is required for cage
acceptance.

## Other fork changes

The old fork changed calibration video sampling from every 20th frame to every
frame, ChArUco detector thresholds, and bundle-adjustment tolerance. These custom
behaviors are not ported into the `val` branch. Other 3D consumers must
review these changes before adopting this branch.

## Validation results

The approved base is 36b92f13a2d9cb4127d40baded1f91b0a65c56fe. The original
master branch is retained. The upgrade is maintained on the local `val` branch.

The official PyPI 0.8.0 source distribution and v0.8.0 tag have identical Python
algorithm source. Only setup.py and __init__.py version strings differ; the
local metadata now matches PyPI. Runtime and installed-distribution versions
both report 0.8.0.

Anipose imports succeeded with this library. OpenCV 4.11 generated a 7-by-5
ChArUco board and detected all 24 corners through the upstream class-based API.
The validation environment contains only opencv-contrib-python. No calibration
accuracy or full 3D reconstruction claim is made by this smoke check.

See the [joint validation report](../../VAL/docs/cage-dependency-validation.md)
for exact environment pins, the retained cage scope, and other fork impacts.
