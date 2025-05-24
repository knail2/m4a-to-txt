import os
import whisper

# Load Whisper model
model = whisper.load_model("base")

# Define input and output paths
input_file = "l29-extracted/ppt/media/media1.m4a"
output_dir = "output"
output_file = os.path.join(output_dir, "l29-media1.txt")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Transcribe
print(f"Transcribing {input_file}...")
result = model.transcribe(input_file)

# Write to output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"].strip())

print(f"✅ Transcript saved to {output_file}")