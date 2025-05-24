import os
import glob
import whisper

def transcribe_directory(input_dir, output_file, model, limit=None):
    """
    Transcribe all .m4a files in a directory and write to a single output file
    with clear file breaks between transcriptions.
    
    Args:
        input_dir (str): Directory containing .m4a files
        output_file (str): Path to output file
        model: Loaded Whisper model
        limit (int, optional): Limit the number of files to process (for testing)
    """
    # Find all .m4a files in the directory
    audio_files = glob.glob(os.path.join(input_dir, "*.m4a"))
    
    # Sort files to ensure consistent order
    audio_files.sort()
    
    # Limit the number of files if specified
    if limit is not None:
        audio_files = audio_files[:limit]
        print(f"Limited to processing {limit} files for testing")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Open output file for writing
    with open(output_file, "w", encoding="utf-8") as f:
        for i, audio_file in enumerate(audio_files):
            # Get just the filename for the header
            filename = os.path.basename(audio_file)
            
            print(f"Transcribing {filename}... ({i+1}/{len(audio_files)})")
            
            # Transcribe the audio file
            result = model.transcribe(audio_file)
            
            # Write file header
            f.write(f"{'='*80}\n")
            f.write(f"FILE: {filename}\n")
            f.write(f"{'='*80}\n\n")
            
            # Write transcription
            f.write(result["text"].strip())
            
            # Add spacing between files
            f.write("\n\n\n")
    
    print(f"✅ All transcripts saved to {output_file}")

def main():
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Transcribe all .m4a files in specified directories")
    parser.add_argument("--limit", type=int, help="Limit the number of files to process per directory (for testing)")
    args = parser.parse_args()
    
    # Load Whisper model (only need to do this once)
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    
    # Define input and output paths
    l29_input_dir = "../l29-extracted/ppt/media"
    l30_input_dir = "../l30-extracted/ppt/media"
    
    output_dir = "../output"
    l29_output_file = os.path.join(output_dir, "l29-media-all.txt")
    l30_output_file = os.path.join(output_dir, "l30-media-all.txt")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each directory
    print("\nProcessing L29 files...")
    transcribe_directory(l29_input_dir, l29_output_file, model, args.limit)
    
    print("\nProcessing L30 files...")
    transcribe_directory(l30_input_dir, l30_output_file, model, args.limit)
    
    print("\n✅ All transcription tasks completed!")

if __name__ == "__main__":
    main()