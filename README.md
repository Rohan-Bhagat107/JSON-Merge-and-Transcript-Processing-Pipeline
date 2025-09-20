# JSON-Merge-and-Transcript-Processing-Pipeline
This Python tool merges multiple JSON transcription files into one, converts the merged data into speaker-labeled SRT subtitles, and exports a formatted DOCX transcript with speaker-dialogue tables. Outputs are organized in folders for easy access and review.
This Python utility processes transcription JSON files by merging multiple JSON files from a specified directory into one consolidated JSON, converting the merged data into subtitle (SRT) format with speaker information, and exporting a structured DOCX transcript with speaker-tagged dialogues.

Features:

Validates input directory path.

Supports natural sorting of JSON files for ordered merging.

Handles JSON fields that can be either strings or lists.

Merges multiple JSON files into a single JSON file prefixed with "Merged_" in the same directory.

Converts merged JSON words data into time-coded SRT subtitles with speaker labels.

Parses SRT files and generates formatted DOCX files with speaker-dialogue tables.

Includes support for Tamil text font rendering in DOCX output.

Organizes outputs into dedicated folders for merged JSON, SRT, and DOCX files.

Easy-to-use CLI: prompts for input directory and handles the full pipeline automatically.

Usage:
Run the script and input the directory path containing your JSON files when prompted. The merged JSON, generated SRT subtitles, and final DOCX transcript will be saved in organized subfolders within the input directory.
