from PIL import Image
import os

input_folder = "images"
output_folder = "resized"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img = Image.open(os.path.join(input_folder, file))
        img = img.resize((800, 800))  # Resize to 800x800
        img.save(os.path.join(output_folder, file), optimize=True, quality=70)
