# Map standard key names to Camelot Wheel notation
# B = Major, A = minor
CAMELOT_MAP = {
    "C Major": "8B", "G Major": "9B", "D Major": "10B", "A Major": "11B", "E Major": "12B", "B Major": "1B",
    "F# Major": "2B", "C# Major": "3B", "G# Major": "4B", "D# Major": "5B", "A# Major": "6B", "F Major": "7B",
    "A minor": "8A", "E minor": "9A", "B minor": "10A", "F# minor": "11A", "C# minor": "12A", "G# minor": "1A",
    "D# minor": "2A", "A# minor": "3A", "F minor": "4A", "C minor": "5A", "G minor": "6A", "D minor": "7A",
}

def get_camelot_key(standard_key):
    """Convert a standard key name to its Camelot wheel notation."""
    return CAMELOT_MAP.get(standard_key, "Unknown") 