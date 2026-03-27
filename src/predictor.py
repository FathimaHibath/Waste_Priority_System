import tensorflow as tf
import numpy as np
import cv2

MODEL_PATH = "models/waste_classifier.h5"
IMG_SIZE = 224

model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def predict_waste(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)[0]
    # predictions = model.predict(img)[0]
    # max_confidence = np.max(predictions)
    
    # # should reject if the threshold is < 0.5
    # if max_confidence < 0.5:
    #     return None
    return predictions
