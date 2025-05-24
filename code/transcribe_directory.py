#!/usr/bin/env python3
"""
Script to transcribe all .m4a files in a specified directory using Whisper.
Creates a consolidated output file with clear file breaks between transcriptions.
"""

import os
import sys
import glob
import argparse
import whisper

def find_audio_files(directory_path):
    """Find all .m4a files in the specified directory."""
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        sys.exit(1)
    
    audio_files = glob.glob(os.path.join(directory_path, "**", "*.m4a"), recursive=True)
    audio_files.sort()  # Sort files to ensure consistent order
    
    if not audio_files:
        print(f"No .m4a files found in '{directory_path}'.")
        sys.exit(1)
    
    return audio_files

def transcribe_audio_files(audio_files, output_file, model_name="base", limit=None):
    """Transcribe audio files and write to output file."""
    # Load the Whisper model
    print(f"Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Process files
    files_to_process = audio_files[:limit] if limit else audio_files
    total_files = len(files_to_process)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, audio_file in enumerate(files_to_process, 1):
            file_name = os.path.basename(audio_file)
            print(f"[{i}/{total_files}] Transcribing {file_name}...")
            
            # Add file separator
            f.write("="*80 + "\n")
            f.write(f"FILE: {file_name}\n")
            f.write("="*80 + "\n\n")
            
            # Transcribe audio
            try:
                result = model.transcribe(audio_file)
                transcript = result["text"].strip()
                f.write(transcript + "\n\n\n")
                f.flush()  # Ensure content is written immediately
            except Exception as e:
                error_msg = f"Error transcribing {file_name}: {str(e)}"
                print(error_msg)
                f.write(f"[TRANSCRIPTION ERROR: {error_msg}]\n\n\n")
    
    print(f"Transcription complete. Output saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Transcribe .m4a files in a directory using Whisper")
    parser.add_argument("directory", help="Directory containing .m4a files to transcribe")
    parser.add_argument("--output", "-o", help="Output file path", required=True)
    parser.add_argument("--model", "-m", default="base", help="Whisper model to use (tiny, base, small, medium, large)")
    parser.add_argument("--limit", "-l", type=int, help="Limit the number of files to process (for testing)")
    
    args = parser.parse_args()
    
    # Find audio files
    audio_files = find_audio_files(args.directory)
    print(f"Found {len(audio_files)} .m4a files in '{args.directory}'")
    
    # Transcribe files
    transcribe_audio_files(audio_files, args.output, args.model, args.limit)

if __name__ == "__main__":
    main()