import os
import shutil

# Change this to your Downloads or any messy folder
source_folder = r"C:\Users\YourName\Downloads"

# File extension categories
file_types = {
    'Images': ['.jpg', '.png', '.jpeg'],
    'Docs': ['.pdf', '.docx', '.txt'],
    'Zips': ['.zip', '.rar'],
    'Others': []
}

# Create folders and move files
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(source_folder, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break
        if not moved:
            dest_folder = os.path.join(source_folder, 'Others')
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))
