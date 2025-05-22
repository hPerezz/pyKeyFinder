import numpy as np

# Major key profile (C Major template) - Order: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
MAJOR_PROFILE = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])

# Minor key profile (C Minor template) - Order: C, C#, D, D#, E, F, F#, G, G#, A, A#, B
MINOR_PROFILE = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

# Define the 12 chromatic pitch classes
CHROMA_LABELS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def normalize_profile(profile):
    """Normalize a key profile vector."""
    return profile / np.linalg.norm(profile)

def generate_all_profiles():
    """Generate all 24 major and minor key profiles by circular shifting."""
    # Normalize base profiles
    major_profile_norm = normalize_profile(MAJOR_PROFILE)
    minor_profile_norm = normalize_profile(MINOR_PROFILE)
    
    all_profiles = []
    key_names = []
    
    for i in range(12):
        # Add Major Key Profile
        all_profiles.append(np.roll(major_profile_norm, i))
        key_names.append(f"{CHROMA_LABELS[i]} Major")
        
        # Add Minor Key Profile
        all_profiles.append(np.roll(minor_profile_norm, i))
        key_names.append(f"{CHROMA_LABELS[i]} minor")
    
    return all_profiles, key_names 