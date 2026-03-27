import os
import cv2
import matplotlib.pyplot as plt

DATASET_PATH = "data"

print("Current working directory:", os.getcwd())
print("Dataset path exists:", os.path.exists(DATASET_PATH))

categories = [
    d for d in os.listdir(DATASET_PATH)
    if os.path.isdir(os.path.join(DATASET_PATH, d))
]

print("Categories:", categories)

# Show ONLY ONE image per category (non-blocking)
for cat in categories:
    cat_path = os.path.join(DATASET_PATH, cat)
    images = os.listdir(cat_path)

    if len(images) == 0:
        continue

    img_path = os.path.join(cat_path, images[0])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(3, 3))
    plt.imshow(img)
    plt.title(cat)
    plt.axis("off")
    plt.pause(0.5)   # show briefly
    plt.close()


