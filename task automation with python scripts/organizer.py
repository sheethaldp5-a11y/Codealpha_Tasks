import os
import shutil
import datetime
from logger import log_json

def organize_files(source_dir, destination_dir, options):
    moved_count = 0

    for root, dirs, files in os.walk(source_dir):
        for filename in files:

            if filename.lower().endswith(tuple(options["allowed_types"])):

                source_path = os.path.join(root, filename)

                ext = filename.split('.')[-1].upper()

                destination_folder = os.path.join(destination_dir, ext)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                destination_path = os.path.join(destination_folder, filename)

                # move file
                shutil.move(source_path, destination_path)
                moved_count += 1

                # logging
                log_json(filename, destination_path)

    return moved_count