import tensorflow as tf

IMG_SIZE = 224
BATCH_SIZE = 32

def load_datasets(data_dir):

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="int"
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="int"
    )

    # Save class names BEFORE modifying dataset
    class_names = train_ds.class_names

    # Ignore corrupted images safely
    train_ds = train_ds.ignore_errors()
    val_ds = val_ds.ignore_errors()

    return train_ds, val_ds, class_names
