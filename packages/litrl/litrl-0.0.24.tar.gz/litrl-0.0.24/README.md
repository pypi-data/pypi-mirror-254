# LitRL

<table>
    <tr>
        <td>Compatibility</td>
        <td>
            <a href="https://pypi.python.org/pypi/litrl" target="_blank">
                <img src="https://img.shields.io/pypi/pyversions/litrl?color=%2334D058" alt="Python">
            </a>
            <a href="https://pypi.python.org/pypi/litrl" target="_blank">
                <img src="https://img.shields.io/pypi/v/litrl.svg?color=%2334D058" alt="Pypi">
            </a>
            <a href="https://pypi.python.org/pypi/litrl" target="_blank">
                <img src="https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-2334D058" alt="Pypi">
            </a>
        </td>
    </tr>
    <tr>
        <td>CI</td>
        <td>
            <a href="https://github.com/c-gohlke/LitRL/actions/workflows/pytest.yaml" target="_blank">
                <img
                src="https://github.com/c-gohlke/LitRL/actions/workflows/pytest.yaml/badge.svg"
                alt="pytest">
            </a>
            <a href="https://github.com/c-gohlke/LitRL/actions/workflows/lint.yaml" target="_blank">
                <img
                src="https://github.com/c-gohlke/LitRL/actions/workflows/lint.yaml/badge.svg"
                alt="Lint">
            </a>
            <a href="https://codecov.io/gh/c-gohlke/LitRL" >
                <img
                src="https://codecov.io/gh/c-gohlke/LitRL/graph/badge.svg?token=NDPHZERUJJ"
                alt=coverage/>
            </a>
        </td>
    </tr>
    <tr>
        <td>Powered by</td>
        <td>
            <a href="https://github.com/Lightning-AI/lightning" target="_blank">
                <img
                src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"
                alt="PyTorch Lightning">
            </a>
            <a href="https://github.com/pytorch/rl" target="_blank">
                <img src="https://img.shields.io/badge/TorchRL-green" alt="TorchRL">
            </a>
            <a href="https://github.com/mlflow/mlflow" target="_blank">
                <img
                src="https://img.shields.io/badge/mlflow-%23d9ead3.svg?logo=mlflow&logoColor=blue"
                alt="MLFlow">
            </a>
            <a href="https://github.com/facebookresearch/hydra" target="_blank">
                <img src="https://img.shields.io/badge/Hydra-green" alt="Hydra">
            </a>
    </tr>
    </tr>
    <tr>
        <td>Contributing</td>
        <td>
            <a href="https://litrl.readthedocs.io/en/latest/" target="_blank">
                <img
                src="https://img.shields.io/readthedocs/litrl?color=%2334D058"
                alt="Docs">
            </a>
            <a href="https://pypi.python.org/pypi/litrl" target="_blank">
                <img
                src="https://img.shields.io/pypi/l/litrl.svg?color=%2334D058"
                alt="License">
            </a>
            <a href="http://mypy-lang.org" target="_blank">
                <img
                src="http://www.mypy-lang.org/static/mypy_badge.svg"
                alt="mypy">
            </a>
            <a href="https://github.com/psf/black" target="_blank">
                <img
                src="https://img.shields.io/badge/code%20style-black-000000.svg"
                alt="black">
            </a>
            <a href="https://github.com/astral-sh/ruff" target="_blank">
                <img
                src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"
                alt="ruff">
            </a>
        </td>
        </td>
    </tr>
    <tr>
        <td>Try it out</td>
        <td>
            <a href="https://huggingface.co/c-gohlke/LitRL" target="_blank">
                <img
                src="https://img.shields.io/badge/%F0%9F%A4%97%20Models-Huggingface-F8D521"
                alt="Models">
            </a>
            <a href="https://c-gohlke-litrl-demo.hf.space/folder/ConnectFour" target="_blank">
                <img
                src="https://img.shields.io/badge/%F0%9F%A4%97%20Demo-Huggingface-F8D521"
                alt="Demo">
            </a>
            <a
            href="https://githubtocolab.com/c-gohlke/LitRL/blob/main/notebooks/colab/train_lunar_sac.ipynb"
            target="_blank">
                <img
                src="https://colab.research.google.com/assets/colab-badge.svg"
                alt="Colab">
            </a>
        </td>
    </tr>
</table>

LitRL is optimized for code readability and expandability. It also provides a structure

 for Reinforcement Learning research.

## Get Started

```bash
pip install LitRL[torchrl]
```

TorchRL may not be found in PyPI depending on your Python version/OS. If that occurs,
 you can download the package using:

```bash
bash scripts/install_torchrl
pip install LitRL
```

## Run demo locally

```bash
python demo/backend/run.py
```

In a separate terminal

```bash
npm install --prefix demo/frontend
npm run dev --prefix demo/frontend
```

## Getting Started Windows

[C++ build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## Acknowledgments

The code structure was influenced by implementations in:

- [CleanRL](https://github.com/vwxyzjn/cleanrl/tree/master)
- [Lizhi-sjtu](https://github.com/Lizhi-sjtu/DRL-code-pytorch)
- [lightning_bolts](https://github.com/Lightning-Universe/lightning-bolts/tree/master/src/pl_bolts/models/rl)

Specific algorithms were also influenced by:

- SAC: [Haarnooja SAC](https://github.com/haarnoja/sac)
- Online Decision Transformer: [ODT](https://github.com/facebookresearch/online-dt)
- AlphaGo/Zero/MuZero: [Muzero](https://github.com/werner-duvaud/muzero-general)
