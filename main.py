from analysis.audio_analyzer import detect_key

def main():
    # Replace with your audio file path
    audio_file_path = 'Perez - Rouba Cena.mp3'
    
    try:
        # Detect key and get results
        results = detect_key(audio_file_path)
        
        # Print results
        print(f"Detected BPM:           {results['tempo']:.2f}")
        print(f"Detected Standard Key: {results['standard_key']}")
        print(f"Detected Camelot Key:  {results['camelot_key']}")
        print(f"Correlation Score:     {results['correlation_score']:.4f}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 