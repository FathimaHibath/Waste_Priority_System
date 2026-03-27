import os
import tensorflow as tf
from data_loader import load_datasets


DATA_DIR = r"E:\HIBA\Waste_Priority_System\Waste_Priority_System\data"
MODEL_PATH = "models/waste_classifier.h5"

train_ds, val_ds, class_names = load_datasets(DATA_DIR)

base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(class_names), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

steps_per_epoch = 16170 // 32
validation_steps = 4042 // 32

model.fit(
    train_ds.repeat(),
    validation_data=val_ds.repeat(),
    epochs=3,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps
)

os.makedirs("models", exist_ok=True)
model.save(MODEL_PATH)

print("Model saved successfully.")