# PyTorch - Quick Reference

Deep learning framework with dynamic computation graphs.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Tensors](#2-tensors)
3. [Autograd](#3-autograd)
4. [Building Models](#4-building-models)
5. [Training Loop](#5-training-loop)
6. [Common Layers](#6-common-layers)
7. [Quick Reference](#7-quick-reference)

---

## 1. Overview

### What is PyTorch?

PyTorch is an open-source deep learning framework developed by Facebook's AI Research lab, known for its dynamic computation graphs and Pythonic interface.

### Installation and Import

```python
# Install
pip install torch torchvision

# Import
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
```

### Check Version and Device

```python
print(torch.__version__)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

---

## 2. Tensors

### Creating Tensors

```python
import torch

# From Python list
tensor = torch.tensor([1, 2, 3, 4])

# 2D tensor
matrix = torch.tensor([[1, 2], [3, 4]])

# Zeros and ones
zeros = torch.zeros(3, 4)
ones = torch.ones(2, 3)

# Random tensors
rand = torch.rand(3, 3)      # Uniform [0, 1)
randn = torch.randn(3, 3)    # Normal distribution

# Range
arange = torch.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
```

### Tensor Operations

```python
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Element-wise operations
print(a + b)  # Add
print(a * b)  # Multiply
print(a - b)  # Subtract

# Matrix multiplication
print(torch.matmul(a, b))  # or a @ b

# In-place operations (with underscore)
a.add_(1)  # Modifies a in place
```

### Tensor Properties and Methods

```python
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

print(tensor.shape)      # torch.Size([2, 3])
print(tensor.dtype)      # torch.int64
print(tensor.device)     # cpu or cuda

# Reshaping
reshaped = tensor.view(3, 2)   # New view
reshaped = tensor.reshape(6)   # Reshape

# To NumPy and back
numpy_array = tensor.numpy()
back_to_tensor = torch.from_numpy(numpy_array)

# Move to device
tensor = tensor.to(device)
```

---

## 3. Autograd

### Automatic Differentiation

```python
import torch

# Create tensor with gradient tracking
x = torch.tensor([2.0, 3.0], requires_grad=True)

# Forward computation
y = x ** 2 + 3 * x + 1
z = y.sum()

# Backward pass (compute gradients)
z.backward()

# Access gradients
print(x.grad)  # dy/dx at x=[2, 3]
```

### No Gradient Context

```python
# Disable gradient computation (for inference)
with torch.no_grad():
    predictions = model(inputs)

# Or use decorator
@torch.no_grad()
def inference(model, inputs):
    return model(inputs)
```

---

## 4. Building Models

### Using nn.Sequential

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 10)
)
```

### Custom Model Class

```python
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = NeuralNetwork()
```

### Move Model to Device

```python
model = model.to(device)
```

---

## 5. Training Loop

### Basic Training Loop

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Model, loss, optimizer
model = NeuralNetwork().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()  # Set to training mode

    for batch_x, batch_y in train_loader:
        batch_x = batch_x.to(device)
        batch_y = batch_y.to(device)

        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        # Backward pass
        optimizer.zero_grad()  # Clear gradients
        loss.backward()        # Compute gradients
        optimizer.step()       # Update weights

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

### Evaluation

```python
def evaluate(model, test_loader):
    model.eval()  # Set to evaluation mode
    correct = 0
    total = 0

    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)

            outputs = model(batch_x)
            _, predicted = torch.max(outputs, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()

    accuracy = 100 * correct / total
    return accuracy
```

### Save and Load

```python
# Save model
torch.save(model.state_dict(), 'model.pth')

# Load model
model = NeuralNetwork()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

---

## 6. Common Layers

### Linear Layers

```python
nn.Linear(in_features, out_features)
```

### Activation Functions

```python
nn.ReLU()
nn.Sigmoid()
nn.Tanh()
nn.Softmax(dim=1)
nn.LeakyReLU(0.1)
```

### Convolutional Layers

```python
nn.Conv2d(in_channels, out_channels, kernel_size)
nn.MaxPool2d(kernel_size)
nn.BatchNorm2d(num_features)
```

### Recurrent Layers

```python
nn.LSTM(input_size, hidden_size, num_layers)
nn.GRU(input_size, hidden_size, num_layers)
```

### Regularization

```python
nn.Dropout(p=0.5)
nn.BatchNorm1d(num_features)
```

---

## 7. Quick Reference

### Tensor Creation

| Function | Description |
|----------|-------------|
| `torch.tensor()` | From data |
| `torch.zeros()` | Zeros |
| `torch.ones()` | Ones |
| `torch.rand()` | Uniform random |
| `torch.randn()` | Normal random |
| `torch.arange()` | Range |

### Common Operations

| Operation | Description |
|-----------|-------------|
| `tensor.view()` | Reshape (view) |
| `tensor.reshape()` | Reshape |
| `tensor.squeeze()` | Remove dim=1 |
| `tensor.unsqueeze()` | Add dimension |
| `tensor.to(device)` | Move to device |

### Loss Functions

| Loss | Use Case |
|------|----------|
| `nn.CrossEntropyLoss()` | Multi-class |
| `nn.BCELoss()` | Binary |
| `nn.MSELoss()` | Regression |
| `nn.L1Loss()` | MAE |

### Optimizers

| Optimizer | Description |
|-----------|-------------|
| `optim.Adam()` | Adaptive (common) |
| `optim.SGD()` | Stochastic GD |
| `optim.RMSprop()` | Good for RNNs |

### Training Workflow

```python
# 1. Create model
model = MyModel().to(device)

# 2. Define loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())

# 3. Training loop
for epoch in range(epochs):
    for x, y in dataloader:
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
```

---

## Coverage Checklist

- [x] Tensor basics
- [x] Tensor operations
- [x] Autograd
- [x] Sequential and custom models
- [x] Training loop
- [x] Evaluation
- [x] Save/load models
- [x] Common layers
- [x] Quick reference
