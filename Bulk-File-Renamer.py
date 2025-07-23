import os
from datetime import datetime

folder = r"C:\Users\YourName\Screenshots"

for index, filename in enumerate(os.listdir(folder)):
    ext = os.path.splitext(filename)[1]
    new_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{index}{ext}"
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
