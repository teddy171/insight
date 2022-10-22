# Insight

[中文](README.zh-CN.md)

Insight is a useful tool for you to watch foreign language videos. It can automatically generate subtitles and translate them. If you have installed it, you can use if offline. It is based on whisper and Hugging Face translation. Thank them for their excellent open source software.

## Table of Contents

- [Insight](#insight)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
  - [License](#license)

## Install

We used Python 3.10, Wisper and Hugging Face Transformers. The following command will help you to create a virtual environment and install its dependencies.

Start by creating a virtual environment in your project directory:

```bash
python -m venv .env
```

Activate the virtual environment. On Linux and MacOs:

```bash
source .env/bin/activate
```

Activate Virtual environment on Windows:

```bash
.env/Scripts/activate
```

Now install 🤗 Transformers with the following command *[1]* :

```bash
pip install transformers
```

For CPU-support only, you can conveniently install 🤗 Transformers and a deep learning library in one line. For example, install 🤗 Transformers and PyTorch with:

```bash
pip install transformers[torch]
```

🤗 Transformers and TensorFlow 2.0:

```bash
pip install transformers[tf-cpu]
```

🤗 Transformers and Flax:

```bash
pip install transformers[flax]
```

SentencePiece:

```bash
pip install SentencePiece
```

Now install whisper and its dependencies *[2]* :

First we install ffmepg.

If you have package manager, you can use the following command. Else you can download at <https://ffmpeg.org>

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

You may need [`rust`](http://rust-lang.org) installed as well, in case [tokenizers](https://pypi.org/project/tokenizers/) does not provide a pre-built wheel for your platform. If you see installation errors during the `pip install` command above, please follow the [Getting started page](https://www.rust-lang.org/learn/get-started) to install Rust development environment. Additionally, you may need to configure the `PATH` environment variable, e.g. `export PATH="$HOME/.cargo/bin:$PATH"`. If the installation fails with `No module named 'setuptools_rust'`, you need to install `setuptools_rust`, e.g. by running:

```bash
pip install setuptools-rust
```

Than install whisper:

```bash
pip install git+https://github.com/openai/whisper.git
```

OK, you have already installed all dependencies.

## Usage

First run main.py. For example:

```bash
python main.py 
```

Than you can input the path to the video. If you want to merge the subtitles to the video, you can input 'y' when it print 'Do you want to merge the subtitle to the video now?(y/n)'

## License

MIT License

`[1]: The following three guides are from https://huggingface.co/docs/transformers/installation`

`[2]: The following three guides are from https://github.com/openai/whisper`
