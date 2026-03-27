import os
from PIL import Image

DATA_DIR = r"E:\HIBA\Waste_Priority_System\Waste_Priority_System\data"

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

removed_files = 0

for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        file_path = os.path.join(root, file)

        # Remove non-image extensions
        if not file.lower().endswith(valid_extensions):
            print("Removing non-image file:", file_path)
            os.remove(file_path)
            removed_files += 1
            continue

        # Try opening image to detect corruption
        try:
            img = Image.open(file_path)
            img.verify()
        except:
            print("Removing corrupted image:", file_path)
            os.remove(file_path)
            removed_files += 1

print(f"\nDataset cleaning completed. Removed {removed_files} invalid files.")