# TensorFlow - Quick Reference

Deep learning and machine learning framework.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Tensors](#2-tensors)
3. [Building Models](#3-building-models)
4. [Training](#4-training)
5. [Common Layers](#5-common-layers)
6. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is TensorFlow?

TensorFlow is an open-source machine learning framework developed by Google for building and training neural networks.

### Installation and Import

```python
# Install
pip install tensorflow

# Import
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
```

### Check Version

```python
print(tf.__version__)
```

---

## 2. Tensors

### Creating Tensors

```python
import tensorflow as tf

# From Python list
tensor = tf.constant([1, 2, 3, 4])
print(tensor)

# 2D tensor (matrix)
matrix = tf.constant([[1, 2], [3, 4]])

# Zeros and ones
zeros = tf.zeros([3, 4])
ones = tf.ones([2, 3])

# Random tensors
random = tf.random.normal([3, 3])
uniform = tf.random.uniform([2, 2])
```

### Tensor Operations

```python
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

# Element-wise operations
print(a + b)  # Add
print(a * b)  # Multiply
print(a - b)  # Subtract

# Matrix multiplication
print(tf.matmul(a, b))  # or a @ b

# Reduction operations
print(tf.reduce_sum(a))   # Sum all elements
print(tf.reduce_mean(a))  # Mean
print(tf.reduce_max(a))   # Max
```

### Tensor Properties

```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

print(tensor.shape)   # (2, 3)
print(tensor.dtype)   # int32
print(tensor.numpy()) # Convert to NumPy array
```

---

## 3. Building Models

### Sequential API (Simple)

```python
from tensorflow import keras
from tensorflow.keras import layers

# Create sequential model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# View model summary
model.summary()
```

### Functional API (Flexible)

```python
from tensorflow import keras
from tensorflow.keras import layers

# Define inputs
inputs = keras.Input(shape=(784,))

# Define layers
x = layers.Dense(128, activation='relu')(inputs)
x = layers.Dropout(0.2)(x)
x = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)

# Create model
model = keras.Model(inputs=inputs, outputs=outputs)
```

### Compile Model

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

---

## 4. Training

### Basic Training

```python
# Train model
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)
```

### With Validation Data

```python
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(x_val, y_val)
)
```

### Evaluate and Predict

```python
# Evaluate on test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_new)
```

### Callbacks

```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

callbacks = [
    EarlyStopping(patience=3, restore_best_weights=True),
    ModelCheckpoint('best_model.h5', save_best_only=True)
]

model.fit(x_train, y_train, epochs=100, callbacks=callbacks)
```

### Save and Load

```python
# Save model
model.save('my_model.h5')

# Load model
loaded_model = keras.models.load_model('my_model.h5')
```

---

## 5. Common Layers

### Dense Layer

```python
# Fully connected layer
layers.Dense(units=64, activation='relu')
```

### Convolutional Layers

```python
# 2D Convolution (for images)
layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu')

# Max pooling
layers.MaxPooling2D(pool_size=(2, 2))
```

### Recurrent Layers

```python
# LSTM
layers.LSTM(units=64, return_sequences=True)

# GRU
layers.GRU(units=64)
```

### Regularization

```python
# Dropout
layers.Dropout(rate=0.5)

# Batch normalization
layers.BatchNormalization()
```

### Reshaping

```python
# Flatten
layers.Flatten()

# Reshape
layers.Reshape(target_shape=(28, 28, 1))
```

---

## 6. Quick Reference

### Tensor Creation

| Function | Description |
|----------|-------------|
| `tf.constant()` | Create constant tensor |
| `tf.zeros()` | Tensor of zeros |
| `tf.ones()` | Tensor of ones |
| `tf.random.normal()` | Random normal |
| `tf.random.uniform()` | Random uniform |

### Common Layers

| Layer | Use Case |
|-------|----------|
| `Dense` | Fully connected |
| `Conv2D` | Image features |
| `MaxPooling2D` | Downsampling |
| `LSTM` | Sequences |
| `Dropout` | Regularization |
| `Flatten` | Reshape to 1D |

### Activations

| Activation | Use Case |
|------------|----------|
| `relu` | Hidden layers |
| `sigmoid` | Binary output |
| `softmax` | Multi-class output |
| `tanh` | Range [-1, 1] |

### Optimizers

| Optimizer | Description |
|-----------|-------------|
| `adam` | Adaptive (recommended) |
| `sgd` | Stochastic gradient descent |
| `rmsprop` | Good for RNNs |

### Loss Functions

| Loss | Use Case |
|------|----------|
| `sparse_categorical_crossentropy` | Multi-class (int labels) |
| `categorical_crossentropy` | Multi-class (one-hot) |
| `binary_crossentropy` | Binary classification |
| `mse` | Regression |

### Model Workflow

```python
# 1. Build model
model = keras.Sequential([...])

# 2. Compile
model.compile(optimizer='adam', loss='...', metrics=['accuracy'])

# 3. Train
model.fit(x_train, y_train, epochs=10)

# 4. Evaluate
model.evaluate(x_test, y_test)

# 5. Predict
model.predict(x_new)
```

---

## Coverage Checklist

- [x] Tensors basics
- [x] Sequential API
- [x] Functional API
- [x] Model compilation
- [x] Training and evaluation
- [x] Common layers
- [x] Save/load models
- [x] Quick reference
