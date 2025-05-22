from analysis.audio_analyzer import detect_key

def main():
    # Get audio file path from user input
    audio_file_path = input("Please enter the path to your audio file: ").strip()
    
    try:
        # Detect key and get results
        results = detect_key(audio_file_path)
        
        # Print results
        print(f"Detected BPM:           {results['tempo']:.2f}")
        print(f"Detected Standard Key: {results['standard_key']}")
        print(f"Detected Camelot Key:  {results['camelot_key']}")
        print(f"Correlation Score:     {float(results['correlation_score']):.4f}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 