import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Dataset (example data)
dataset = [
  {"image_name": "pic2.jpg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "pic10.jpg", "labels": [1, 1, 0, 0, 1, 1]},
     {"image_name": "1.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "2.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "3.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "4.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "5.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "6.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "7.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "8.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "9.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "10.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "11.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "12.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "13.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "14.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "15.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "16.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "17.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "18.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "19.jpeg", "labels": [1, 1, 0, 0, 1, 1]}, 
 
    {"image_name": "21.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "22.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "23.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "24.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "25.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "26.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "27.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "28.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "29.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "30.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "38.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "39.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "40.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "41.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "42.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "54.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "55.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "56.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "57.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "58.jpeg", "labels": [1, 1, 1, 0, 1, 1]},
    {"image_name": "59.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "60.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "61.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "62.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "63.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "64.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "65.jpeg", "labels": [1, 1, 0, 0, 1, 1]},
    {"image_name": "66.jpeg", "labels": [1, 1, 0, 0, 1, 1]}
  # Add more data as needed...
]

image_dir = 'images/'  # Path to the images directory
image_paths = [os.path.join(image_dir, entry['image_name']) for entry in dataset]
labels = np.array([entry['labels'] for entry in dataset])

# Calorie values for each class
calories_per_class = {
    'rice': 445,
    'dal': 50,
    'chicken': 67,
    'fish': 70,
    'mekaral': 40,
    'kolamellum': 20
}

# Function to preprocess the images
def preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)  # Load and resize image
    img_array = img_to_array(img) / 255.0  # Normalize to [0, 1]
    return img_array

# Load and preprocess all images
images = np.array([preprocess_image(img_path) for img_path in image_paths])

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

# Create the model using EfficientNetB0 as the base model
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Unfreeze the last few layers for fine-tuning
for layer in base_model.layers[-40:]:  # Unfreeze the last 40 layers
    layer.trainable = True

# Add custom layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)  # Add Dropout layer to prevent overfitting
output = Dense(y_train.shape[1], activation='sigmoid')(x)  # Output layer for multi-label classification

# Create the full model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model with a lower learning rate
model.compile(optimizer=Adam(learning_rate=1e-5), loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks: Early stopping and learning rate scheduler
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', patience=3, factor=0.5, min_lr=1e-6)

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

datagen.fit(X_train)

# Train the model
history = model.fit(datagen.flow(X_train, y_train, batch_size=16), validation_data=(X_val, y_val), epochs=20, callbacks=[early_stop, lr_scheduler])

# Save the trained model
model.save('multi_label_curry_model.h5')

# Prediction function
def predict_curry(image_path, model, threshold=0.5):
    img = preprocess_image(image_path)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)[0]
    predicted_classes = (prediction >= threshold).astype(int)
    
    curry_classes = ['rice', 'dal', 'chicken', 'fish', 'mekaral', 'kolamellum']
    predictions_dict = {curry_classes[i]: predicted_classes[i] for i in range(len(curry_classes))}
    
    # Find calories based on predictions
    calories_dict = {}
    for i, predicted in enumerate(predicted_classes):
        if predicted == 1:  # If the class is predicted as present
            calories_dict[curry_classes[i]] = calories_per_class[curry_classes[i]]

    return predictions_dict, calories_dict

# Visualize predictions
def visualize_prediction(image_path, model, threshold=0.5):
    predictions, calories = predict_curry(image_path, model, threshold)
    
    print("Predicted Labels: ")
    for curry, predicted in predictions.items():
        print(f"{curry}: {'Yes' if predicted else 'No'}")
    
    print("\nCalories: ")
    for curry, calorie in calories.items():
        print(f"{curry}: {calorie} kcal")

# Example usage
visualize_prediction('images/57.jpeg', model, threshold=0.5)
