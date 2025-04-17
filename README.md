# Python Key Finder

## Description

This Python script analyzes an audio file to estimate its musical key. It distinguishes between all 12 major and 12 minor keys (24 possible keys in total). The script uses the Librosa library to extract Chroma features and compares the audio's overall pitch class distribution against standard Krumhansl-Schmuckler key profiles to determine the best match.

## Features

* Detects the key of an audio file (WAV, MP3, etc. - formats supported by Librosa).
* Identifies both major and minor keys (e.g., "C Major", "A minor").
* Uses Chroma features (`librosa.feature.chroma_stft`) for pitch class analysis.
* Employs Krumhansl-Schmuckler key profiles for robust key estimation.
* Calculates correlation between audio features and key profiles to find the best match.

## Requirements

* Python 3.x
* Librosa
* NumPy

## Installation

1.  **Ensure Python 3 is installed.**
2.  **Install the required libraries using pip:**
    ```bash
    pip install numpy librosa
    ```
    *Note: Librosa might require `ffmpeg` for loading certain audio formats like MP3. If you encounter loading errors, ensure ffmpeg is installed and accessible in your system's PATH.*

## Usage

1.  **Save the script:** Save the provided Python code as a `.py` file (e.g., `key_detector.py`).
2.  **Modify the audio file path:** Open the script and change the line:
    ```python
    audio_file_path = 'Perez - Rouba Cena.mp3'
    ```
    Replace `'Perez - Rouba Cena.mp3'` with the actual path to *your* audio file.
3.  **Run the script:** Execute the script from your terminal:
    ```bash
    python key_detector.py
    ```
4.  **Output:** The script will print the estimated key to the console, for example:
    ```
    Detected Key: A minor
    ```
    or
    ```
    Detected Key: G Major
    ```
    It will also print warnings or errors if the file is not found or if issues occur during processing (like analyzing a silent file).

## How it Works

1.  **Load Audio:** The script loads the specified audio file using `librosa.load()`.
2.  **Compute Chromagram:** It calculates the Chroma Short-Time Fourier Transform (`chroma_stft`), which represents the energy distribution across the 12 pitch classes (C, C#, D, ..., B) over time.
3.  **Average Chroma:** The chromagram is averaged across the time dimension to get a single 12-element vector representing the overall prominence of each pitch class in the audio segment.
4.  **Normalize:** Both the audio's average chroma vector and the pre-defined Krumhansl-Schmuckler key profiles (one for major, one for minor, transposed to all 12 roots) are normalized.
5.  **Correlate:** The script calculates the dot product (correlation) between the normalized audio chroma vector and each of the 24 normalized key profiles.
6.  **Identify Best Match:** The key profile with the highest correlation score is considered the best match.
7.  **Output Key:** The name of the key corresponding to the best-matching profile is printed.

## Key Profiles

The script uses the Krumhansl-Schmuckler key profiles, derived from psychoacoustic experiments by Carol Krumhansl, which represent the perceived hierarchy and stability of tones within major and minor key contexts.

## Limitations

* The accuracy depends on the quality and characteristics of the audio recording (e.g., mix clarity, instrumentation).
* Music with ambiguous tonality, frequent key changes within the analyzed segment, or highly chromatic/atonal passages might result in less accurate estimations.
* The script analyzes the *entire* audio file (or segment loaded) to produce a *single* key estimate. It doesn't track key changes within the file.

Maid with ❤️ in UNIFEI - Federal de Itajubá :)
