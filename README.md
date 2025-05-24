# M4A to Text Converter

A Python-based tool for transcribing M4A audio files to text using OpenAI's Whisper speech recognition model. This repository contains scripts to process audio files from PowerPoint presentations and generate consolidated text transcripts.

## Features

- Transcribe multiple M4A audio files to text
- Process files from single or multiple directories
- Configurable Whisper model selection (tiny, base, small, medium, large)
- Consolidated output with clear file separators
- Detailed logging of transcription process

## Prerequisites

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) installed and available in PATH
- PowerPoint files with embedded audio (optional, if starting from PPTX files)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/knail2/m4a-to-txt.git
   cd m4a-to-txt
   ```

2. Install the required Python packages:
   ```bash
   pip install openai-whisper
   ```

3. Ensure FFmpeg is installed:
   ```bash
   # On Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg

   # On macOS using Homebrew
   brew install ffmpeg

   # On Windows using Chocolatey
   choco install ffmpeg
   ```

## Usage

### Preparing Audio Files

If you're starting with PowerPoint files containing embedded audio:

1. Upload your PPTX file to [extract.me](https://extract.me/)
2. Download and extract the ZIP file
3. Audio files will be located in the `ppt/media/` directory of the extracted content

### Transcribing Files from Multiple Directories

To transcribe audio files from multiple directories:

```bash
python code/transcribe_all_audio_files.py
```

This script will:
- Process all M4A files in `l29-extracted/ppt/media/` and `l30-extracted/ppt/media/`
- Create output files `output/l29-media-all.txt` and `output/l30-media-all.txt`
- Use the "base" Whisper model by default

### Transcribing Files from a Single Directory

To transcribe audio files from a single directory:

```bash
python code/transcribe_directory.py <directory_path> --output <output_file> [--model <model_name>] [--limit <num_files>]
```

Arguments:
- `directory_path`: Path to the directory containing M4A files
- `--output`: Path to the output text file (default: `output/transcription.txt`)
- `--model`: Whisper model to use (default: "base")
- `--limit`: Limit the number of files to process (optional, for testing)

Example:
```bash
python code/transcribe_directory.py l30-extracted/ppt/media/ --output output/l30-transcript.txt --model small
```

## Models

The scripts support the following Whisper models:
- `tiny`: Fastest, least accurate
- `base`: Good balance of speed and accuracy for most use cases
- `small`: More accurate than base, but slower
- `medium`: High accuracy, slower processing
- `large`: Highest accuracy, slowest processing

## Project Structure

```
m4a-to-txt/
├── code/
│   ├── transcribe_all_audio_files.py  # Script to process multiple directories
│   └── transcribe_directory.py        # Script to process a single directory
├── output/
│   ├── l29-media-all.txt              # Transcriptions from l29 directory
│   └── l30-media-all-v2.txt           # Transcriptions from l30 directory
├── l29-extracted/                     # Extracted PowerPoint content
│   └── ppt/media/                     # Directory containing audio files
└── l30-extracted/                     # Extracted PowerPoint content
    └── ppt/media/                     # Directory containing audio files
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for the speech recognition model
- [extract.me](https://extract.me/) for PowerPoint extraction capabilities
