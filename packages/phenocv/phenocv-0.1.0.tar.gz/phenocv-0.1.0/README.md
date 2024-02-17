# phenocv

## Introduction

**phenocv** is a toolkits for handling preporecess and postprocess for rice high-throught phenotyping images.

**phenocv** is still under development. We will keep refactoring the code and add more features. Any contribution is welcome. If you encounter any problems when using phenocv, please feel free to [raise an issue](https://github.com/r1cheu/phenocv/issues/new)

For label-studio semi-automatic annotation, please refer to [playground](https://github.com/open-mmlab/playground).

For mmdetection training, please refer to [mmdetection](https://github.com/open-mmlab/mmdetection).

For yolo training, please refer to [Ultralytics](https://github.com/ultralytics/ultralytics).

## Installation

Pip install the phenocv package including all [requirements](https://github.com/r1cheu/phenocv/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

### Install for developer

if you wish to modify the code, you can install phenocv in developer mode.

```shell
git clone https://github.com/r1cheu/phenocv.git
cd phenocv
pip install -e .
```

## License

This project is released under the [AGPL-3.0 license](LICENSE).

## Citation

If you find this project useful in your research, please consider cite:

```Bibtex
@misc{2023phenocv,
    title={Rice high-throught phenotyping computer vision toolkits},
    author={RuLei Chen},
    howpublished = {\url{https://github.com/r1cheu/phenocv}},
    year={2023}
}
```
