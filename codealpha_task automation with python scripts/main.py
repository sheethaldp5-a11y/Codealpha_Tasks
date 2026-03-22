import json
from organizer import organize_files

# load config
with open("config.json") as f:
    config = json.load(f)

source = "source_folder"
destination = "organized_files"

print("Program started...")

moved = organize_files(source, destination, config)

print(f"Total files moved: {moved}")