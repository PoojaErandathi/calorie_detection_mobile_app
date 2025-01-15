import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os

# Create an ImageDataGenerator for augmentation
datagen = ImageDataGenerator(
    rotation_range=40,         # Random rotations
    width_shift_range=0.2,     # Random horizontal shift
    height_shift_range=0.2,    # Random vertical shift
    shear_range=0.2,           # Shear transformations
    zoom_range=0.2,            # Zoom in or out
    horizontal_flip=True,      # Random horizontal flip
    fill_mode='nearest'        # Pixel value filling strategy after transformation
)

# Load your 2 images and convert them to numpy arrays
img1 = tf.keras.preprocessing.image.load_img('pic2.jpg', target_size=(224, 224))
img2 = tf.keras.preprocessing.image.load_img('pic10.jpg', target_size=(224, 224))


img1_array = tf.keras.preprocessing.image.img_to_array(img1)
img2_array = tf.keras.preprocessing.image.img_to_array(img2)
  # Fix here

# Add an extra dimension to the image arrays (since ImageDataGenerator expects batches)
img1_array = np.expand_dims(img1_array, axis=0)
img2_array = np.expand_dims(img2_array, axis=0)
 # Fix here

# Ensure the directory exists for saving augmented images
output_dir = 'augmented_images'
os.makedirs(output_dir, exist_ok=True)

# Generate augmented images for img1
i = 0
for batch in datagen.flow(img1_array, batch_size=1, save_to_dir=output_dir, save_prefix='0', save_format='jpeg'):
    i += 1
    if i >= 10:  # Set the maximum number of images you want to generate for img1
        break

# Generate augmented images for img2
i = 0
for batch in datagen.flow(img2_array, batch_size=1, save_to_dir=output_dir, save_prefix='1', save_format='jpeg'):
    i += 1
    if i >= 10:  # Set the maximum number of images you want to generate for img2
        break


print("Augmentation complete. Images saved in:", output_dir)
