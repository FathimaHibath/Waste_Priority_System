import cv2
import numpy as np

def estimate_fill_level(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    waste_pixels = np.sum(thresh == 255)
    total_pixels = img.shape[0] * img.shape[1]

    fill_ratio = waste_pixels / total_pixels
    return round(fill_ratio, 2)