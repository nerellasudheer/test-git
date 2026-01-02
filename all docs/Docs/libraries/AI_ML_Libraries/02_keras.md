# Keras - Deep Learning Made Easy

> **What is it?** High-level Deep Learning library (runs on TensorFlow)
> **Install:** `pip install tensorflow` (Keras is included)
> **Import as:** `from tensorflow import keras` or `import keras`

---

## Table of Contents

1. [What is Keras?](#1-what-is-keras)
2. [Installation](#2-installation)
3. [Core Concepts](#3-core-concepts)
4. [Building Your First Neural Network](#4-building-your-first-neural-network)
5. [Understanding Layers](#5-understanding-layers)
6. [Activation Functions](#6-activation-functions)
7. [Compiling Models](#7-compiling-models)
8. [Training Models](#8-training-models)
9. [Making Predictions](#9-making-predictions)
10. [Image Classification Example](#10-image-classification-example)
11. [Saving and Loading Models](#11-saving-and-loading-models)
12. [Common Mistakes](#12-common-mistakes)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is Keras?

### Simple Explanation

Keras is like **LEGO blocks for building AI brains (neural networks)**.

```
Building a house:
- LEGO: Stack blocks together → Get a house
- Keras: Stack layers together → Get a neural network

Without Keras (raw TensorFlow/PyTorch):
- You build everything from scratch
- Complex, lots of code

With Keras:
- Pre-made building blocks
- Simple, few lines of code
```

### Keras vs TensorFlow vs PyTorch

| Library | Difficulty | When to Use |
|---------|------------|-------------|
| **Keras** | Easy | Learning, prototyping, most projects |
| **TensorFlow** | Medium-Hard | Production, custom operations |
| **PyTorch** | Medium | Research, dynamic networks |

### What Can Keras Do?

- Image recognition (cats vs dogs)
- Text classification (spam detection)
- Sequence prediction (stock prices)
- Generative AI (create images)
- And much more!

---

## 2. Installation

```bash
# Keras comes with TensorFlow
pip install tensorflow

# Verify installation
python -c "import tensorflow as tf; print(tf.__version__)"
```

### Basic Import

```python
# Modern way (TensorFlow 2.x)
from tensorflow import keras
from tensorflow.keras import layers

# Or directly
import tensorflow as tf
print(tf.__version__)  # Output: 2.x.x
```

---

## 3. Core Concepts

### 3.1 What is a Neural Network?

```
Neural Network = A system that learns patterns from data

Structure:
INPUT → [HIDDEN LAYERS] → OUTPUT

Example: Is this image a cat or dog?

Input Layer        Hidden Layers       Output Layer
(Image pixels)     (Learn patterns)    (Cat or Dog)

    [●]               [●]──[●]              [●] → Cat
    [●]──────────────►[●]──[●]──────────────►
    [●]               [●]──[●]              [●] → Dog
    [●]               [●]──[●]

   784 pixels      Learns features     2 categories
```

### 3.2 Key Terms

| Term | Meaning | Analogy |
|------|---------|---------|
| **Layer** | A group of neurons | A floor in a building |
| **Neuron** | A single computation unit | A worker |
| **Weights** | Numbers that get adjusted | Worker's skills |
| **Activation** | Decision function | "Should I pass this forward?" |
| **Epoch** | One pass through all data | One study session |
| **Batch** | Subset of data processed together | Study one chapter at a time |

### 3.3 The Keras Workflow

```
STEP 1: Define the model (stack layers)
    ↓
STEP 2: Compile (choose optimizer, loss, metrics)
    ↓
STEP 3: Fit (train on data)
    ↓
STEP 4: Evaluate (test accuracy)
    ↓
STEP 5: Predict (use on new data)
```

---

## 4. Building Your First Neural Network

### 4.1 Sequential Model (Stack Layers)

```python
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# ═══════════════════════════════════════════════════════════
# STEP 1: Create the model
# ═══════════════════════════════════════════════════════════
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),  # Input: 10 features
    layers.Dense(32, activation='relu'),                      # Hidden layer
    layers.Dense(1, activation='sigmoid')                     # Output: 1 probability
])

# See model structure
model.summary()

# Output:
# Model: "sequential"
# _________________________________________________________________
#  Layer (type)                Output Shape              Param #
# =================================================================
#  dense (Dense)               (None, 64)                704
#  dense_1 (Dense)             (None, 32)                2080
#  dense_2 (Dense)             (None, 1)                 33
# =================================================================
# Total params: 2,817
```

### 4.2 Complete Example: Binary Classification

```python
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# ═══════════════════════════════════════════════════════════
# STEP 1: Create dummy data
# ═══════════════════════════════════════════════════════════
# 1000 samples, 10 features each
X_train = np.random.random((1000, 10))
y_train = np.random.randint(2, size=(1000, 1))  # 0 or 1

X_test = np.random.random((200, 10))
y_test = np.random.randint(2, size=(200, 1))

print(f"Training data: {X_train.shape}")  # (1000, 10)
print(f"Training labels: {y_train.shape}")  # (1000, 1)

# ═══════════════════════════════════════════════════════════
# STEP 2: Build the model
# ═══════════════════════════════════════════════════════════
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# ═══════════════════════════════════════════════════════════
# STEP 3: Compile the model
# ═══════════════════════════════════════════════════════════
model.compile(
    optimizer='adam',              # How to update weights
    loss='binary_crossentropy',    # How to measure error
    metrics=['accuracy']           # What to track
)

# ═══════════════════════════════════════════════════════════
# STEP 4: Train the model
# ═══════════════════════════════════════════════════════════
history = model.fit(
    X_train, y_train,
    epochs=10,                     # Go through data 10 times
    batch_size=32,                 # Process 32 samples at a time
    validation_split=0.2,          # Use 20% for validation
    verbose=1                      # Show progress
)

# Output:
# Epoch 1/10
# 25/25 [======] - 1s 10ms/step - loss: 0.7012 - accuracy: 0.4925 - val_loss: 0.6985
# Epoch 2/10
# ...

# ═══════════════════════════════════════════════════════════
# STEP 5: Evaluate the model
# ═══════════════════════════════════════════════════════════
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# ═══════════════════════════════════════════════════════════
# STEP 6: Make predictions
# ═══════════════════════════════════════════════════════════
predictions = model.predict(X_test[:5])
print("\nPredictions (probabilities):")
print(predictions)
# Output: [[0.45], [0.67], [0.23], [0.89], [0.12]]

# Convert to classes
predicted_classes = (predictions > 0.5).astype(int)
print("Predicted classes:", predicted_classes.flatten())
# Output: [0, 1, 0, 1, 0]
```

---

## 5. Understanding Layers

### 5.1 Dense Layer (Fully Connected)

```python
# Every neuron connects to every neuron in previous layer
layers.Dense(
    units=64,                    # Number of neurons
    activation='relu',           # Activation function
    input_shape=(10,)            # Only for first layer
)

# Example:
# Input: 10 features → Dense(64) → Output: 64 values
```

### 5.2 Dropout Layer (Prevent Overfitting)

```python
# Randomly "drops" neurons during training
layers.Dropout(0.5)  # Drop 50% of neurons randomly

# Why? Prevents model from memorizing training data
# Use between layers
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dropout(0.3),  # Drop 30%
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')
])
```

### 5.3 Flatten Layer (For Images)

```python
# Converts 2D image to 1D array
layers.Flatten()

# Example:
# Input: 28x28 image → Flatten → Output: 784 values
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # 28*28 = 784
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### 5.4 Convolutional Layers (For Images)

```python
# Extracts features from images (edges, shapes, etc.)
layers.Conv2D(
    filters=32,           # Number of feature detectors
    kernel_size=(3, 3),   # Size of filter
    activation='relu',
    input_shape=(28, 28, 1)  # Height, Width, Channels
)

# MaxPooling: Reduces image size
layers.MaxPooling2D(pool_size=(2, 2))  # Halves dimensions
```

### 5.5 Common Layer Patterns

```python
# Pattern 1: Simple Classification
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(features,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Pattern 2: Image Classification (CNN)
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Pattern 3: With Dropout (prevents overfitting)
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(features,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation='softmax')
])
```

---

## 6. Activation Functions

### When to Use Which?

| Activation | Use For | Output Range |
|------------|---------|--------------|
| `relu` | Hidden layers (default) | 0 to infinity |
| `sigmoid` | Binary classification (output) | 0 to 1 |
| `softmax` | Multi-class classification (output) | 0 to 1 (sums to 1) |
| `tanh` | Hidden layers (alternative) | -1 to 1 |
| `linear` | Regression (output) | -infinity to infinity |

### Visual Examples

```python
import numpy as np

# ReLU: Returns x if positive, else 0
# relu(-2) = 0, relu(3) = 3
def relu(x):
    return max(0, x)

# Sigmoid: Squashes to 0-1 (probability)
# sigmoid(0) = 0.5, sigmoid(large) ≈ 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Softmax: Multi-class probabilities (sum = 1)
# softmax([1, 2, 3]) = [0.09, 0.24, 0.67]
```

### Usage in Code

```python
# Binary Classification (Cat or Not Cat)
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Output: 0-1 probability
])
# Loss: binary_crossentropy

# Multi-class Classification (Cat, Dog, Bird)
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')  # Output: 3 probabilities
])
# Loss: categorical_crossentropy

# Regression (Predict Price)
model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='linear')  # Output: any number
])
# Loss: mean_squared_error
```

---

## 7. Compiling Models

### 7.1 The compile() Method

```python
model.compile(
    optimizer='adam',           # How to update weights
    loss='binary_crossentropy', # How to measure error
    metrics=['accuracy']        # What to track
)
```

### 7.2 Choosing the Right Loss Function

| Problem Type | Output Activation | Loss Function |
|--------------|-------------------|---------------|
| Binary Classification | `sigmoid` | `binary_crossentropy` |
| Multi-class (one label) | `softmax` | `categorical_crossentropy` |
| Multi-class (integer labels) | `softmax` | `sparse_categorical_crossentropy` |
| Regression | `linear` | `mse` or `mae` |

### 7.3 Common Optimizers

```python
# Adam (most popular - use this by default)
optimizer='adam'

# SGD (Stochastic Gradient Descent)
optimizer='sgd'

# With custom learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.001)
```

### 7.4 Complete Compile Examples

```python
# Binary Classification
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Multi-class Classification (one-hot encoded labels)
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Multi-class Classification (integer labels: 0, 1, 2, ...)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Regression
model.compile(
    optimizer='adam',
    loss='mse',  # mean_squared_error
    metrics=['mae']  # mean_absolute_error
)
```

---

## 8. Training Models

### 8.1 The fit() Method

```python
history = model.fit(
    X_train,                    # Training features
    y_train,                    # Training labels
    epochs=10,                  # Number of passes through data
    batch_size=32,              # Samples per gradient update
    validation_split=0.2,       # Use 20% of training for validation
    verbose=1                   # Show progress (0=silent, 1=progress, 2=one line per epoch)
)
```

### 8.2 Understanding Epochs and Batches

```
Total data: 1000 samples
Batch size: 100
Epochs: 5

Each Epoch:
- 1000 / 100 = 10 batches
- Model updates weights 10 times per epoch

Total training:
- 5 epochs × 10 batches = 50 weight updates
```

### 8.3 Using Validation Data

```python
# Method 1: validation_split (automatically splits training data)
history = model.fit(
    X_train, y_train,
    epochs=10,
    validation_split=0.2  # 20% of X_train used for validation
)

# Method 2: validation_data (use separate validation set)
history = model.fit(
    X_train, y_train,
    epochs=10,
    validation_data=(X_val, y_val)
)
```

### 8.4 Training History

```python
# Access training metrics
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# Plot training history
import matplotlib.pyplot as plt

# Accuracy
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()
```

### 8.5 Callbacks (Stop Early, Save Best Model)

```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Stop if validation loss doesn't improve
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,           # Wait 5 epochs before stopping
    restore_best_weights=True
)

# Save the best model
checkpoint = ModelCheckpoint(
    'best_model.keras',
    monitor='val_accuracy',
    save_best_only=True
)

# Use callbacks during training
history = model.fit(
    X_train, y_train,
    epochs=100,
    validation_split=0.2,
    callbacks=[early_stop, checkpoint]
)
```

---

## 9. Making Predictions

### 9.1 predict() Method

```python
# Get raw predictions
predictions = model.predict(X_test)
print(predictions[:5])
# Binary: [[0.23], [0.87], [0.45], [0.92], [0.12]]
# Multi-class: [[0.1, 0.2, 0.7], [0.8, 0.1, 0.1], ...]

# Convert to classes
# Binary
predicted_classes = (predictions > 0.5).astype(int)
print(predicted_classes.flatten())  # [0, 1, 0, 1, 0]

# Multi-class
predicted_classes = np.argmax(predictions, axis=1)
print(predicted_classes)  # [2, 0, 1, 2, 0]
```

### 9.2 Evaluate on Test Data

```python
# Get loss and metrics
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
```

---

## 10. Image Classification Example

### Complete MNIST Example (Handwritten Digits)

```python
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# ═══════════════════════════════════════════════════════════
# STEP 1: Load the MNIST dataset
# ═══════════════════════════════════════════════════════════
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"Training images: {X_train.shape}")  # (60000, 28, 28)
print(f"Training labels: {y_train.shape}")  # (60000,)
print(f"Test images: {X_test.shape}")       # (10000, 28, 28)

# Visualize some images
fig, axes = plt.subplots(1, 5, figsize=(12, 3))
for i, ax in enumerate(axes):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f"Label: {y_train[i]}")
    ax.axis('off')
plt.savefig('mnist_samples.png')
plt.show()

# ═══════════════════════════════════════════════════════════
# STEP 2: Preprocess the data
# ═══════════════════════════════════════════════════════════
# Normalize pixel values to 0-1
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Reshape for CNN (add channel dimension)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print(f"Reshaped training: {X_train.shape}")  # (60000, 28, 28, 1)

# ═══════════════════════════════════════════════════════════
# STEP 3: Build the CNN model
# ═══════════════════════════════════════════════════════════
model = keras.Sequential([
    # First Convolutional Block
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    # Second Convolutional Block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Flatten and Dense layers
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 digits (0-9)
])

model.summary()

# ═══════════════════════════════════════════════════════════
# STEP 4: Compile the model
# ═══════════════════════════════════════════════════════════
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Integer labels
    metrics=['accuracy']
)

# ═══════════════════════════════════════════════════════════
# STEP 5: Train the model
# ═══════════════════════════════════════════════════════════
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# ═══════════════════════════════════════════════════════════
# STEP 6: Evaluate the model
# ═══════════════════════════════════════════════════════════
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")  # Should be ~99%

# ═══════════════════════════════════════════════════════════
# STEP 7: Make predictions
# ═══════════════════════════════════════════════════════════
predictions = model.predict(X_test[:10])
predicted_labels = np.argmax(predictions, axis=1)

# Show predictions
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"Pred: {predicted_labels[i]}, True: {y_test[i]}")
    ax.axis('off')
plt.tight_layout()
plt.savefig('mnist_predictions.png')
plt.show()
```

---

## 11. Saving and Loading Models

### 11.1 Save Entire Model

```python
# Save (includes architecture, weights, optimizer state)
model.save('my_model.keras')

# Load
loaded_model = keras.models.load_model('my_model.keras')

# Use loaded model
predictions = loaded_model.predict(X_test)
```

### 11.2 Save Weights Only

```python
# Save weights
model.save_weights('model_weights.weights.h5')

# Load weights (model architecture must match)
model.load_weights('model_weights.weights.h5')
```

### 11.3 Save Architecture Only

```python
# Save as JSON
json_config = model.to_json()
with open('model_architecture.json', 'w') as f:
    f.write(json_config)

# Load from JSON
with open('model_architecture.json', 'r') as f:
    json_config = f.read()
new_model = keras.models.model_from_json(json_config)
```

---

## 12. Common Mistakes

### Mistake 1: Wrong Output Layer for Task

```python
# WRONG: Sigmoid for multi-class
model.add(layers.Dense(10, activation='sigmoid'))  # NO!

# CORRECT: Softmax for multi-class
model.add(layers.Dense(10, activation='softmax'))  # YES!

# Rule:
# Binary (2 classes) → sigmoid + binary_crossentropy
# Multi-class → softmax + categorical_crossentropy
```

### Mistake 2: Not Normalizing Input Data

```python
# WRONG: Raw pixel values (0-255)
model.fit(X_train, y_train)  # Will train poorly!

# CORRECT: Normalize to 0-1
X_train = X_train / 255.0
model.fit(X_train, y_train)  # Much better!
```

### Mistake 3: Wrong Input Shape

```python
# Data shape: (1000, 28, 28)  # 1000 images, 28x28 pixels
# WRONG:
layers.Dense(64, input_shape=(28, 28))  # Expects 2D input

# CORRECT (for Dense): Flatten first
layers.Flatten(input_shape=(28, 28))

# CORRECT (for CNN): Add channel dimension
X_train = X_train.reshape(-1, 28, 28, 1)
layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1))
```

### Mistake 4: Overfitting (Model Memorizes Training Data)

```python
# Signs of overfitting:
# - Training accuracy: 99%
# - Validation accuracy: 60%

# Solutions:
# 1. Add Dropout
layers.Dropout(0.5)

# 2. Use Early Stopping
early_stop = EarlyStopping(patience=5)

# 3. Get more data

# 4. Simplify model (fewer layers/neurons)
```

---

## 13. Quick Reference

### Model Building Template

```python
from tensorflow import keras
from tensorflow.keras import layers

# 1. Build
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(num_features,)),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# 2. Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 3. Train
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# 4. Evaluate
loss, acc = model.evaluate(X_test, y_test)

# 5. Predict
predictions = model.predict(X_new)

# 6. Save
model.save('model.keras')
```

### Common Layers

| Layer | Purpose | Example |
|-------|---------|---------|
| `Dense` | Fully connected | `Dense(64, activation='relu')` |
| `Dropout` | Prevent overfitting | `Dropout(0.5)` |
| `Flatten` | 2D to 1D | `Flatten()` |
| `Conv2D` | Image features | `Conv2D(32, (3,3), activation='relu')` |
| `MaxPooling2D` | Reduce size | `MaxPooling2D((2,2))` |
| `BatchNormalization` | Stabilize training | `BatchNormalization()` |

### Choosing Activation & Loss

| Task | Output Activation | Loss |
|------|-------------------|------|
| Binary | `sigmoid` | `binary_crossentropy` |
| Multi-class | `softmax` | `categorical_crossentropy` |
| Multi-class (int labels) | `softmax` | `sparse_categorical_crossentropy` |
| Regression | `linear` | `mse` |

### Common Imports

```python
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
```

---

## Summary

Keras makes Deep Learning simple:

1. **Sequential()** - Stack layers like LEGO
2. **Dense()** - Basic building block
3. **compile()** - Set optimizer, loss, metrics
4. **fit()** - Train the model
5. **evaluate()** - Test accuracy
6. **predict()** - Make predictions
7. **save()** - Save for later

Start with simple Dense networks, then try CNNs for images!
