# openpack-torch

[![Test](https://github.com/open-pack/openpack-torch/actions/workflows/test.yaml/badge.svg)](https://github.com/open-pack/openpack-torch/actions/workflows/test.yaml)
[![GitHub Pages](https://github.com/open-pack/openpack-torch/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/open-pack/openpack-torch/actions/workflows/deploy-docs.yaml)

PyTorch utilities to work around with [OpenPack Dataset](https://open-pack.github.io/).

## Setup

You can install via pip with the following command.

```bash
# Pip
pip install openpack-torch

# Poetry
poetry add  openpack-torch
```

## Docs

- [Dataset Page](https://open-pack.github.io/)
- [API Docs](https://open-pack.github.io/openpack-torch/openpack_torch)
- [PyPI - openpack-torch](https://pypi.org/project/openpack-torch/)

## Examples

See [./examples/README.md](./examples/)

### Operation Recognition (Semantic Segmentation)

#### IMU

- Acceleration
  - [U-Net](./examples/run_unet.py) ([PyTorch Model](./openpack_torch/models/imu/unet.py))
  - [DeepConvLSTM](./examples/run_dcl.py) ([PyTorch Model](./openpack_torch/models/imu/deep_conv_lstm.py))

#### Vision

- Keypoints
  - [ST-GCN](./examples/run_stgcn.py) ([PyTorch Model](./openpack_torch/models/keypoint/stgcn.py))

#### Scores of Baseline Moodel (Preliminary Experiments)

##### Split: Pilot Challenge

| Model        | F1 (Test Set) | F1 (Submission Set) | Date       | Code                                    |
| ------------ | ------------- | ------------------- | ---------- | --------------------------------------- |
| UNet         | 0.3451        | 0.3747              | 2022-06-28 | [run_unet.py](./examples/run_unet.py)   |
| DeepConvLSTM | 0.7081        | 0.7695              | 2022-06-28 | [run_dcl.py](./examples/run_dcl.py)     |
| ST-GCN       | 0.7024        | 0.6106              | 2022-07-07 | [run_stgcn.py](./examples/run_stgcn.py) |

NOTE: F1 = F1-measure (macro average)

##### Split: OpenPack Challenge 2022

This split is defined for OpenPack Challenge 2022.

| Model        | F1 (Test Set) | F1 (Submission Set) | Date | Code |
| ------------ | ------------- | ------------------- | ---- | ---- |
| UNet         | TBA           | TBA                 | -    | -    |
| DeepConvLSTM | TBA           | TBA                 | -    | -    |
| ST-GCN       | TBA           | TBA                 | -    | -    |

## OpenPack Challenge 2022 @ PerCom2023 WS Bird

We are hosting an activity recognition competition, using the OpenPack dataset at a [PerCom 2023 Workshop](https://bio-navigation.jp/bird2023/)!
The task is very simple: Recognize 10 work operations from the OpenPack dataset.
Please join this exciting opportunity. For more information about the competition, click [here](https://open-pack.github.io/challenge2022).

### Tutorials

- [Train a baseline model and make submission file.](./examples/notebooks/U-Net_Train-Model-and-Make-Submission-File.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-torch/blob/main/examples/notebooks/U-Net_Train-Model-and-Make-Submission-File.ipynb)
- [Change input modalities.](./examples/notebooks/U-Net_Change-Input-Data.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-torch/blob/main/examples/notebooks/U-Net_Change-Input-Data.ipynb)

![OpenPack Challenge Logo](./assets/img/OpenPackCHALLENG-black.png)

## LICENCE

This software (openpack-torch) is distributed under [MIT Licence](./LICENSE).
For the license of "OpenPack Dataset", please check [this site (https://open-pack.github.io/)](https://open-pack.github.io/).
