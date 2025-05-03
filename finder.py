import librosa
import numpy as np

# Load Audio File
audio_file_path = 'Perez - Rouba Cena.mp3' # <<< Replace with your audio file path

# Major key profile (C Major template) - Order: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
major_profile = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])

# Minor key profile (C Minor template) - Order: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
minor_profile = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

# Normalize profiles
major_profile /= np.linalg.norm(major_profile)
minor_profile /= np.linalg.norm(minor_profile)

# Define the 12 chromatic pitch classes
chroma_labels = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Generate all 24 major and minor key profiles by circular shifting
all_profiles = []
key_names = []

for i in range(12):
    # Add Major Key Profile
    all_profiles.append(np.roll(major_profile, i))
    key_names.append(f"{chroma_labels[i]} Major")

    # Add Minor Key Profile
    all_profiles.append(np.roll(minor_profile, i))
    key_names.append(f"{chroma_labels[i]} minor") # Use 'minor' for clarity and consistency

# --- Camelot Wheel Mapping ---
# Map standard key names to Camelot Wheel notation
# B = Major, A = minor
camelot_map = {
    "C Major": "8B", "G Major": "9B", "D Major": "10B", "A Major": "11B", "E Major": "12B", "B Major": "1B",
    "F# Major": "2B", "C# Major": "3B", "G# Major": "4B", "D# Major": "5B", "A# Major": "6B", "F Major": "7B",
    "A minor": "8A", "E minor": "9A", "B minor": "10A", "F# minor": "11A", "C# minor": "12A", "G# minor": "1A",
    "D# minor": "2A", "A# minor": "3A", "F minor": "4A", "C minor": "5A", "G minor": "6A", "D minor": "7A",
}
# --- End Camelot Mapping ---


try:
    y, sr = librosa.load(audio_file_path)

    # Check if audio is long enough
    if len(y) < 2048: # Needs at least one frame for STFT with default settings
        print(f"Warning: Audio file '{audio_file_path}' is too short for analysis.")
    else:
        # Compute the Chroma Short-Time Fourier Transform (chroma_stft)
        # Using a larger n_fft can sometimes improve harmonic resolution
        chromagram = librosa.feature.chroma_stft(y=y, sr=sr, n_fft=4096, hop_length=512)

        # Calculate the mean chroma feature across time
        mean_chroma = np.mean(chromagram, axis=1)

        if np.sum(mean_chroma) > 0: # Avoid division by zero if the audio segment is silent
            mean_chroma_normalized = mean_chroma / np.linalg.norm(mean_chroma) # Normalize the mean chroma vector
        else:
            print("Warning: Audio segment appears silent, cannot determine key.")
            mean_chroma_normalized = mean_chroma # Keep it as zeros

        # Calculate correlation (dot product) between audio's chroma and each key profile
        correlations = []
        for profile in all_profiles:
            # Ensure the profile vector also has unit norm (already done above, but safe to double-check)
            # profile_normalized = profile / np.linalg.norm(profile) if np.linalg.norm(profile) > 0 else profile
            correlation = np.dot(mean_chroma_normalized, profile)
            correlations.append(correlation)

        # Find the key profile with the highest correlation
        estimated_key_index = np.argmax(correlations)
        estimated_key_standard = key_names[estimated_key_index]

        # --- Get Camelot Key ---
        estimated_key_camelot = camelot_map.get(estimated_key_standard, "Unknown") # Use .get() for safety

        # Print the detected keys
        print(f"Detected Standard Key: {estimated_key_standard}")
        print(f"Detected Camelot Key:  {estimated_key_camelot}")
        print(f"Correlation Score:     {correlations[estimated_key_index]:.4f}")

except FileNotFoundError:
    print(f"Error: Audio file not found at {audio_file_path}")
except Exception as e:
    print(f"An error occurred during processing: {e}")
