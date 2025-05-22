# Python Key Finder

## Description

A Python package that analyzes audio files to estimate their musical key. It distinguishes between all 12 major and 12 minor keys (24 possible keys in total). The package uses the Librosa library to extract Chroma features and compares the audio's overall pitch class distribution against standard Krumhansl-Schmuckler key profiles to determine the best match.

## Features

* Detects the key of an audio file (WAV, MP3, etc. - formats supported by Librosa)
* Identifies both major and minor keys (e.g., "C Major", "A minor")
* Uses Chroma features (`librosa.feature.chroma_stft`) for pitch class analysis
* Employs Krumhansl-Schmuckler key profiles for robust key estimation
* Calculates correlation between audio features and key profiles to find the best match
* Detects the BPM (tempo) of the audio file using `librosa.beat.beat_track`
* Maps detected keys to Camelot Wheel notation for DJ-friendly key representation
* Provides correlation scores to indicate confidence in key detection
* Interactive command-line interface for easy file analysis

## Project Structure

```
pyKeyFinder/
├── src/
│   ├── analysis/      # Audio analysis modules
│   ├── profiles/      # Key profile definitions
│   ├── utils/         # Utility functions
│   └── main.py        # Main entry point
├── setup.py           # Package installation configuration
└── README.md          # This file
```

## Requirements

* Python 3.x
* Librosa
* NumPy

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hPerezz/pyKeyFinder.git
   cd pyKeyFinder
   ```

2. **Install the package:**
   ```bash
   pip install -e .
   ```

   *Note: Librosa might require `ffmpeg` for loading certain audio formats like MP3. If you encounter loading errors, ensure ffmpeg is installed and accessible in your system's PATH.*

## Usage

1. **Run the script:**
   ```bash
   python -m src.main
   ```

2. **Enter the audio file path when prompted:**
   ```
   Please enter the path to your audio file: path/to/your/audio/Perez - Rouba Cena.mp3
   ```

3. **View the results:**
   ```
   Detected BPM:           128.00
   Detected Standard Key:  A minor
   Detected Camelot Key:   8A
   Correlation Score:      0.9234
   ```

## How it Works

1. **Load Audio:** The package loads the specified audio file using `librosa.load()`
2. **Compute Chromagram:** Calculates the Chroma Short-Time Fourier Transform (`chroma_stft`), representing the energy distribution across the 12 pitch classes (C, C#, D, ..., B) over time
3. **Average Chroma:** The chromagram is averaged across the time dimension to get a single 12-element vector representing the overall prominence of each pitch class
4. **Normalize:** Both the audio's average chroma vector and the pre-defined Krumhansl-Schmuckler key profiles are normalized
5. **Correlate:** Calculates the correlation between the normalized audio chroma vector and each of the 24 normalized key profiles
6. **Identify Best Match:** The key profile with the highest correlation score is considered the best match
7. **Output Results:** The detected key, Camelot notation, BPM, and correlation score are displayed

## Key Profiles

The package uses the Krumhansl-Schmuckler key profiles, derived from psychoacoustic experiments by Carol Krumhansl, which represent the perceived hierarchy and stability of tones within major and minor key contexts.

## Limitations

* The accuracy depends on the quality and characteristics of the audio recording (e.g., mix clarity, instrumentation)
* Music with ambiguous tonality, frequent key changes within the analyzed segment, or highly chromatic/atonal passages might result in less accurate estimations
* The package analyzes the *entire* audio file to produce a *single* key estimate. It doesn't track key changes within the file
* The correlation score provides an indication of confidence in the key detection

Made with ❤️ in UNIFEI - Federal de Itajubá :)
