import os
import shutil

source = "source_folder/notes.txt"
destination_folder = "destination_folder"

os.makedirs(destination_folder, exist_ok=True)

shutil.copy(source, destination_folder)

print("File copied successfully!")
