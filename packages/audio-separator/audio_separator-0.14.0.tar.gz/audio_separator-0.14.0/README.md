# Audio Separator 🎶

[![PyPI version](https://badge.fury.io/py/audio-separator.svg)](https://badge.fury.io/py/audio-separator)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/audio-separator.svg)](https://anaconda.org/conda-forge/audio-separator)
[![Docker pulls](https://img.shields.io/docker/pulls/beveradb/audio-separator.svg)](https://hub.docker.com/r/beveradb/audio-separator/tags)

Summary: Easy to use vocal separation on CLI or as a python package, using the amazing MDX-Net models from UVR trained by @Anjok07

Audio Separator is a Python package that allows you to separate an audio file into two stems, primary and secondary, using a model in the ONNX format trained by @Anjok07 for use with UVR (https://github.com/Anjok07/ultimatevocalremovergui).

The primary stem typically contains the instrumental part of the audio, while the secondary stem contains the vocals, but in some models this is reversed.

## Features

- Separate audio into instrumental and vocal stems.
- Supports all common audio formats (WAV, MP3, FLAC, M4A, etc.)
- Ability to specify a pre-trained deep learning model in ONNX format.
- CLI support for easy use in scripts and batch processing.
- Python API for integration into other projects.

## Installation 🛠️

### 🎮 Nvidia GPU with CUDA acceleration

💬 If successfully configured, you should see this log message when running audio-separator:
 `ONNXruntime has CUDAExecutionProvider available, enabling acceleration`

Conda: `conda install pytorch=*=*cuda* onnxruntime=*=*cuda* audio-separator -c pytorch -c conda-forge`

Pip: `pip install "audio-separator[gpu]"`

Docker: `beveradb/audio-separator:gpu`

### 🧪 Google Colab

Colab has recently upgraded to CUDA 12, which isn't yet supported by the official ONNX Runtime releases.

To get `audio-separator` working with GPU acceleration on colab, first install this `onnxruntime-gpu` wheel (which I built with CUDA 12 support):

`pip install https://github.com/karaokenerds/python-audio-separator/releases/download/v0.12.1/onnxruntime_gpu-1.17.0-cp310-cp310-linux_x86_64.whl`

Then install audio-separator:
`pip install "audio-separator[gpu]"`

### 🐢 No hardware acceleration, CPU only:

Conda: `conda install audio-separator-c pytorch -c conda-forge`

Pip: `pip install "audio-separator[cpu]"`

Docker: `beveradb/audio-separator`

###  Apple Silicon, macOS Sonoma+ with CoreML acceleration

💬 If successfully configured, you should see this log message when running audio-separator:
 `ONNXruntime has CoreMLExecutionProvider available, enabling acceleration`

Pip: `pip install "audio-separator[silicon]"`

### FFmpeg dependency (if using pip)

If you installed `audio-separator` using `pip`, you'll separately need to ensure you have `ffmpeg` installed.
This should be easy to install on most platforms, e.g.:

🐧 Debian/Ubuntu: `apt-get update; apt-get install -y ffmpeg`

 macOS:`brew update; brew install ffmpeg`


## GPU / CUDA specific installation steps with Pip

In theory, all you should need to do to get `audio-separator` working with a GPU is install it with the `[gpu]` extra as above.

However, sometimes getting both PyTorch and ONNX Runtime working with CUDA support can be a bit tricky so it may not work that easily.

You may need to reinstall both packages directly, allowing pip to calculate the right versions for your platform:

- `pip uninstall torch onnxruntime`
- `pip cache purge`
- `pip install --force-reinstall torch torchvision torchaudio`
- `pip install --force-reinstall onnxruntime-gpu`

Depending on your hardware, you may get better performance with the optimum version of onnxruntime:
- `pip install --force-reinstall "optimum[onnxruntime-gpu]"`

Depending on your CUDA version and hardware, you may need to install torch from the `cu118` index instead:
- `pip install --force-reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

> Note: if anyone knows how to make this cleaner so we can support both different platform-specific dependencies for hardware acceleration without a separate installation process for each, please let me know or raise a PR!

## Usage in Docker 🐳

There are [images published on Docker Hub](https://hub.docker.com/r/beveradb/audio-separator/tags) for GPU (CUDA) and CPU inferencing, for both `amd64` and `arm64` platforms.

You probably want to volume-mount a folder containing whatever file you want to separate, which can then also be used as the output folder.

For example, if the current directory contains your input file `input.wav`, you could run `audio-separator` like so:

```
docker run -it -v `pwd`:/workdir beveradb/audio-separator input.wav
```

If you're using a machine with a GPU, you'll want to use the GPU specific image and pass in the GPU device to the container, like this:

```
docker run -it --gpus all -v `pwd`:/workdir beveradb/audio-separator:gpu input.wav
```

If the GPU isn't being detected, make sure your docker runtime environment is passing through the GPU correctly - there are [various guides](https://www.celantur.com/blog/run-cuda-in-docker-on-linux/) online to help with that.


## Usage 🚀

### Command Line Interface (CLI)

You can use Audio Separator via the command line:

```sh
usage: audio-separator [-h] [-v] [--log_level LOG_LEVEL] [--model_name MODEL_NAME] [--model_file_dir MODEL_FILE_DIR] [--output_dir OUTPUT_DIR] [--output_format OUTPUT_FORMAT] [--denoise DENOISE] [--normalize NORMALIZE]
                       [--single_stem SINGLE_STEM] [--invert_spect INVERT_SPECT] [--samplerate SAMPLERATE] [--adjust ADJUST] [--dim_c DIM_C] [--hop HOP] [--segment_size SEGMENT_SIZE] [--overlap overlap] [--batch_size BATCH_SIZE]
                       [audio_file]

Separate audio file into different stems.

positional arguments:
  audio_file                       The audio file path to separate, in any common format.

options:
  -h, --help                       show this help message and exit
  -v, --version                    show program's version number and exit
  --log_level LOG_LEVEL            Optional: logging level, e.g. info, debug, warning (default: info). Example: --log_level=debug
  --model_name MODEL_NAME          Optional: model name to be used for separation (default: UVR_MDXNET_KARA_2). Example: --model_name=UVR-MDX-NET-Inst_HQ_3
  --model_file_dir MODEL_FILE_DIR  Optional: model files directory (default: /tmp/audio-separator-models/). Example: --model_file_dir=/app/models
  --output_dir OUTPUT_DIR          Optional: directory to write output files (default: <current dir>). Example: --output_dir=/app/separated
  --output_format OUTPUT_FORMAT    Optional: output format for separated files, any common format (default: FLAC). Example: --output_format=MP3
  --denoise DENOISE                Optional: enable or disable denoising during separation (default: True). Example: --denoise=False
  --normalize NORMALIZE            Optional: enable or disable normalization during separation (default: True). Example: --normalize=False
  --single_stem SINGLE_STEM        Optional: output only single stem, either instrumental or vocals. Example: --single_stem=instrumental
  --invert_spect INVERT_SPECT      Optional: invert secondary stem using spectogram (default: True). Example: --invert_spect=False
  --samplerate SAMPLERATE          Optional: samplerate (default: 44100). Example: --samplerate=44100
  --adjust ADJUST                  Optional: adjust (default: 1). Example: --adjust=1
  --dim_c DIM_C                    Optional: dim_c (default: 4). Example: --dim_c=4
  --hop HOP                        Optional: hop (default: 1024). Example: --hop=1024
  --segment_size SEGMENT_SIZE      Optional: segment_size (default: 256). Example: --segment_size=256
  --overlap overlap        Optional: overlap (default: 0.25). Example: --overlap=0.25
  --batch_size BATCH_SIZE          Optional: batch_size (default: 4). Example: --batch_size=4
```

Example:

```
audio-separator /path/to/your/audio.wav --model_name UVR_MDXNET_KARA_2
```

This command will process the file and generate two new files in the current directory, one for each stem.

### As a Dependency in a Python Project

You can use Audio Separator in your own Python project. Here's how you can use it:

```
from audio_separator.separator import Separator

# Initialize the Separator class (with optional configuration properties below)
separator = Separator()

# Load a machine learning model (if unspecified, defaults to 'UVR-MDX-NET-Inst_HQ_3')
separator.load_model()

# Perform the separation on specific audio files without reloading the model
primary_stem_output_path, secondary_stem_output_path = separator.separate('audio1.wav')

print(f'Primary stem saved at {primary_stem_output_path}')
print(f'Secondary stem saved at {secondary_stem_output_path}')
```

#### Batch processing, or processing with multiple models

You can process multiple separations without reloading the model, to save time and memory.

You only need to load a model when choosing or changing models. See example below:

```
from audio_separator.separator import Separator

# Initialize the Separator with other configuration properties below
separator = Separator()

# Load a model
separator.load_model('UVR-MDX-NET-Inst_HQ_3')

# Separate multiple audio files without reloading the model
output_file_paths_1 = separator.separate('audio1.wav')
output_file_paths_2 = separator.separate('audio2.wav')
output_file_paths_3 = separator.separate('audio3.wav')

# Load a different model
separator.load_model('UVR_MDXNET_KARA_2')

# Separate the same files with the new model
output_file_paths_4 = separator.separate('audio1.wav')
output_file_paths_5 = separator.separate('audio2.wav')
output_file_paths_6 = separator.separate('audio3.wav')
```

## Parameters for the Separator class

- audio_file: The path to the audio file to be separated. Supports all common formats (WAV, MP3, FLAC, M4A, etc.)
- log_level: (Optional) Logging level, e.g. info, debug, warning. Default: INFO
- log_formatter: (Optional) The log format. Default: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
- model_name: (Optional) The name of the model to use for separation. Defaults to 'UVR-MDX-NET-Inst_HQ_3', a very powerful model for Karaoke instrumental tracks.
- model_file_dir: (Optional) Directory to cache model files in. Default: /tmp/audio-separator-models/
- output_dir: (Optional) Directory where the separated files will be saved. If not specified, outputs to current dir.
- output_format: (Optional) Format to encode output files, any common format (WAV, MP3, FLAC, M4A, etc.). Default: WAV
- enable_denoise: (Optional) Flag to enable or disable denoising as part of the separation process. Default: True
- normalization_enabled: (Optional) Flag to enable or disable normalization as part of the separation process. Default: False
- output_single_stem: (Optional) Output only single stem, either instrumental or vocals.
- invert_secondary_stem_using_spectogram=True,
- samplerate: (Optional) Modify the sample rate of the output audio. Default: 44100
- hop_length: (Optional) Hop length; advanced parameter used by the separation process. Default: 1024
- segment_size: (Optional) Segment size; advanced parameter used by the separation process. Default: 256
- overlap: (Optional) Overlap; advanced parameter used by the separation process. Default: 0.25
- batch_size: (Optional) Batch Size; advanced parameter used by the separation process. Default: 4

## Requirements 📋

Python >= 3.9

Libraries: onnx, onnxruntime, numpy, librosa, torch, wget, six

## Developing Locally

This project uses Poetry for dependency management and packaging. Follow these steps to setup a local development environment:

### Prerequisites

- Make sure you have Python 3.9 or newer installed on your machine.
- Install Poetry by following the installation guide here.

### Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/YOUR_USERNAME/audio-separator.git
cd audio-separator
```

Replace YOUR_USERNAME with your GitHub username if you've forked the repository, or use the main repository URL if you have the permissions.

### Install Dependencies

Run the following command to install the project dependencies:

```
poetry install
```

### Activate the Virtual Environment

To activate the virtual environment, use the following command:

```
poetry shell
```

### Running the Command-Line Interface Locally

You can run the CLI command directly within the virtual environment. For example:

```
audio-separator path/to/your/audio-file.wav
```

### Deactivate the Virtual Environment

Once you are done with your development work, you can exit the virtual environment by simply typing:

```
exit
```

### Building the Package

To build the package for distribution, use the following command:

```
poetry build
```

This will generate the distribution packages in the dist directory - but for now only @beveradb will be able to publish to PyPI.

## Contributing 🤝

Contributions are very much welcome! Please fork the repository and submit a pull request with your changes, and I'll try to review, merge and publish promptly!

- This project is 100% open-source and free for anyone to use and modify as they wish. 
- If the maintenance workload for this repo somehow becomes too much for me I'll ask for volunteers to share maintainership of the repo, though I don't think that is very likely
- Development and support for the MDX-Net separation models is part of the main [UVR project](https://github.com/Anjok07/ultimatevocalremovergui), this repo is just a CLI/Python package wrapper to simplify running those models programmatically. So, if you want to try and improve the actual models, please get involved in the UVR project and look for guidance there!

## License 📄

This project is licensed under the MIT [License](LICENSE).

- **Please Note:** If you choose to integrate this project into some other project using the default model or any other model trained as part of the [UVR](https://github.com/Anjok07/ultimatevocalremovergui) project, please honor the MIT license by providing credit to UVR and its developers!

## Credits 🙏

- [Anjok07](https://github.com/Anjok07) - Author of [Ultimate Vocal Remover GUI](https://github.com/Anjok07/ultimatevocalremovergui), which almost all of the code in this repo was copied from! Definitely deserving of credit for anything good from this project. Thank you!
- [DilanBoskan](https://github.com/DilanBoskan) - Your contributions at the start of this project were essential to the success of UVR. Thank you!
- [Kuielab & Woosung Choi](https://github.com/kuielab) - Developed the original MDX-Net AI code. 
- [KimberleyJSN](https://github.com/KimberleyJensen) - Advised and aided the implementation of the training scripts for MDX-Net and Demucs. Thank you!
- [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) - Helped implement chunks into the MDX-Net AI code. Thank you!

## Contact 💌

For questions or feedback, please raise an issue or reach out to @beveradb ([Andrew Beveridge](mailto:andrew@beveridge.uk)) directly.
