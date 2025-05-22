import librosa
import numpy as np
from ..profiles.key_profiles import generate_all_profiles
from ..utils.camelot_mapping import get_camelot_key

def detect_tempo(y, sr):
    """Detect the tempo (BPM) of an audio signal."""
    try:
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return tempo
    except Exception as e:
        raise Exception(f"BPM detection error: {e}")

def analyze_audio_chroma(y, sr):
    """Analyze the chroma features of an audio signal."""
    if len(y) < 2048:
        raise ValueError("Audio file is too short for analysis")
    
    # Compute the Chroma Short-Time Fourier Transform
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr, n_fft=4096, hop_length=512)
    
    # Calculate the mean chroma feature across time
    mean_chroma = np.mean(chromagram, axis=1)
    
    if np.sum(mean_chroma) == 0:
        raise ValueError("Audio segment appears silent, cannot determine key")
    
    return mean_chroma / np.linalg.norm(mean_chroma)

def detect_key(audio_file_path):
    """Main function to detect the key of an audio file."""
    try:
        # Load audio file
        y, sr = librosa.load(audio_file_path)
        
        # Get all key profiles
        all_profiles, key_names = generate_all_profiles()
        
        # Analyze chroma features
        mean_chroma_normalized = analyze_audio_chroma(y, sr)
        
        # Calculate correlations with all key profiles
        correlations = [np.dot(mean_chroma_normalized, profile) for profile in all_profiles]
        
        # Find the key with highest correlation
        estimated_key_index = np.argmax(correlations)
        estimated_key_standard = key_names[estimated_key_index]
        estimated_key_camelot = get_camelot_key(estimated_key_standard)
        
        # Get tempo
        tempo = detect_tempo(y, sr)
        
        return {
            'standard_key': estimated_key_standard,
            'camelot_key': estimated_key_camelot,
            'correlation_score': correlations[estimated_key_index],
            'tempo': tempo
        }
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Audio file not found at {audio_file_path}")
    except Exception as e:
        raise Exception(f"An error occurred during processing: {e}") 