# OpenCV - Computer Vision Library

> **What is it?** Library for image and video processing
> **Install:** `pip install opencv-python`
> **Import as:** `import cv2`

---

## Table of Contents

1. [What is OpenCV?](#1-what-is-opencv)
2. [Installation](#2-installation)
3. [Reading and Displaying Images](#3-reading-and-displaying-images)
4. [Basic Image Operations](#4-basic-image-operations)
5. [Image Transformations](#5-image-transformations)
6. [Drawing on Images](#6-drawing-on-images)
7. [Color Spaces](#7-color-spaces)
8. [Image Filtering](#8-image-filtering)
9. [Edge Detection](#9-edge-detection)
10. [Working with Video](#10-working-with-video)
11. [Face Detection](#11-face-detection)
12. [Real-World Examples](#12-real-world-examples)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is OpenCV?

### Simple Explanation

OpenCV (Open Computer Vision) is a library that lets your computer **"see" and understand images and videos**.

```
What can OpenCV do?

See Images:
- Read photos from files
- Display images on screen
- Save modified images

Process Images:
- Resize, crop, rotate
- Change colors
- Apply filters (blur, sharpen)

Understand Images:
- Detect faces
- Find objects
- Read text
- Track movement

Used in:
- Self-driving cars
- Security cameras
- Photo apps (Instagram filters)
- Medical imaging
- Robotics
```

### Why OpenCV for AI/ML?

```
Machine Learning needs data → Images are data

Before training a model:
1. Load images (OpenCV)
2. Resize to same size (OpenCV)
3. Convert colors (OpenCV)
4. Augment data (OpenCV)
5. Feed to model (TensorFlow/PyTorch)

OpenCV = The tool that prepares images for AI
```

---

## 2. Installation

```bash
# Basic installation
pip install opencv-python

# With extra modules (recommended)
pip install opencv-contrib-python

# Verify installation
python -c "import cv2; print(cv2.__version__)"
```

### Basic Import

```python
import cv2
import numpy as np

print(f"OpenCV Version: {cv2.__version__}")
# Output: OpenCV Version: 4.x.x
```

---

## 3. Reading and Displaying Images

### 3.1 Read an Image

```python
import cv2

# Read image from file
img = cv2.imread('photo.jpg')

# Check if image loaded successfully
if img is None:
    print("Error: Could not load image!")
else:
    print(f"Image shape: {img.shape}")
    # Output: (height, width, channels)
    # Example: (480, 640, 3) = 480 pixels tall, 640 wide, 3 color channels (BGR)
```

### 3.2 Reading Modes

```python
# Color image (default) - 3 channels (Blue, Green, Red)
img_color = cv2.imread('photo.jpg', cv2.IMREAD_COLOR)
# Or
img_color = cv2.imread('photo.jpg', 1)

# Grayscale image - 1 channel
img_gray = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)
# Or
img_gray = cv2.imread('photo.jpg', 0)

# Unchanged (with alpha channel if exists)
img_unchanged = cv2.imread('photo.png', cv2.IMREAD_UNCHANGED)
# Or
img_unchanged = cv2.imread('photo.png', -1)

print(f"Color shape: {img_color.shape}")      # (480, 640, 3)
print(f"Grayscale shape: {img_gray.shape}")   # (480, 640)
```

### 3.3 Display an Image

```python
import cv2

img = cv2.imread('photo.jpg')

# Display in a window
cv2.imshow('My Image', img)

# Wait for key press
cv2.waitKey(0)  # 0 = wait forever, 1000 = wait 1 second

# Close all windows
cv2.destroyAllWindows()
```

### 3.4 Save an Image

```python
import cv2

img = cv2.imread('photo.jpg')

# Save image
cv2.imwrite('output.jpg', img)
cv2.imwrite('output.png', img)  # Different format

print("Image saved successfully!")
```

### 3.5 Complete Example

```python
import cv2

# Read
img = cv2.imread('photo.jpg')

if img is not None:
    print(f"Dimensions: {img.shape[1]}x{img.shape[0]}")  # width x height
    print(f"Channels: {img.shape[2]}")
    print(f"Data type: {img.dtype}")

    # Display
    cv2.imshow('Original', img)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', gray)

    # Save grayscale
    cv2.imwrite('gray_photo.jpg', gray)

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load image!")
```

---

## 4. Basic Image Operations

### 4.1 Image Properties

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg')

# Shape: (height, width, channels)
height, width, channels = img.shape
print(f"Height: {height}")    # 480
print(f"Width: {width}")      # 640
print(f"Channels: {channels}") # 3

# Total pixels
total_pixels = img.size
print(f"Total values: {total_pixels}")  # 480 * 640 * 3 = 921600

# Data type
print(f"Data type: {img.dtype}")  # uint8 (0-255)
```

### 4.2 Accessing Pixels

```python
import cv2

img = cv2.imread('photo.jpg')

# Access a single pixel (row, column)
# OpenCV uses BGR (Blue, Green, Red) not RGB!
pixel = img[100, 200]  # Row 100, Column 200
b, g, r = pixel
print(f"Blue: {b}, Green: {g}, Red: {r}")

# Modify a pixel
img[100, 200] = [255, 255, 255]  # Set to white

# Access a region (ROI - Region of Interest)
roi = img[50:150, 100:200]  # Rows 50-150, Columns 100-200
print(f"ROI shape: {roi.shape}")
```

### 4.3 Resize Images

```python
import cv2

img = cv2.imread('photo.jpg')
print(f"Original: {img.shape}")  # (480, 640, 3)

# Resize to specific dimensions
resized = cv2.resize(img, (320, 240))  # (width, height)
print(f"Resized: {resized.shape}")  # (240, 320, 3)

# Resize by scale factor
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)  # Half size
print(f"Scaled: {scaled.shape}")  # (240, 320, 3)

# Different interpolation methods
resized_best = cv2.resize(img, (320, 240), interpolation=cv2.INTER_AREA)
# INTER_AREA - Best for shrinking
# INTER_LINEAR - Default, good for enlarging
# INTER_CUBIC - Better quality enlarging (slower)
```

### 4.4 Crop Images

```python
import cv2

img = cv2.imread('photo.jpg')

# Crop using slicing [y_start:y_end, x_start:x_end]
cropped = img[100:300, 150:450]  # 200x300 pixels

cv2.imshow('Original', img)
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save cropped image
cv2.imwrite('cropped_photo.jpg', cropped)
```

### 4.5 Copy Images

```python
import cv2

img = cv2.imread('photo.jpg')

# WRONG - Creates reference (changes affect both)
img_ref = img
img_ref[0, 0] = [255, 255, 255]  # This also changes img!

# CORRECT - Creates actual copy
img_copy = img.copy()
img_copy[0, 0] = [255, 255, 255]  # Only changes img_copy
```

---

## 5. Image Transformations

### 5.1 Rotate Images

```python
import cv2

img = cv2.imread('photo.jpg')
height, width = img.shape[:2]

# Method 1: Simple rotations
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Method 2: Rotate by any angle
center = (width // 2, height // 2)
angle = 45  # degrees
scale = 1.0

# Get rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Apply rotation
rotated_45 = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow('Rotated 45', rotated_45)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 5.2 Flip Images

```python
import cv2

img = cv2.imread('photo.jpg')

# Flip horizontally (mirror)
flipped_h = cv2.flip(img, 1)

# Flip vertically
flipped_v = cv2.flip(img, 0)

# Flip both
flipped_both = cv2.flip(img, -1)

cv2.imshow('Original', img)
cv2.imshow('Horizontal Flip', flipped_h)
cv2.imshow('Vertical Flip', flipped_v)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 5.3 Translate (Move) Images

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg')
height, width = img.shape[:2]

# Translation matrix
# Move 100 pixels right and 50 pixels down
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply translation
translated = cv2.warpAffine(img, translation_matrix, (width, height))

cv2.imshow('Translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 5.4 Perspective Transform

```python
import cv2
import numpy as np

img = cv2.imread('document.jpg')
height, width = img.shape[:2]

# Source points (corners of document in original image)
src_points = np.float32([
    [100, 50],    # Top-left
    [400, 60],    # Top-right
    [50, 400],    # Bottom-left
    [450, 380]    # Bottom-right
])

# Destination points (where we want them to be)
dst_points = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

# Get perspective transform matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply transform
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Original', img)
cv2.imshow('Transformed', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 6. Drawing on Images

### 6.1 Draw Lines

```python
import cv2
import numpy as np

# Create blank image (black)
img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw line
# cv2.line(image, start_point, end_point, color, thickness)
cv2.line(img, (0, 0), (600, 400), (255, 0, 0), 2)  # Blue diagonal
cv2.line(img, (0, 200), (600, 200), (0, 255, 0), 5)  # Green horizontal

cv2.imshow('Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 6.2 Draw Rectangles

```python
import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw rectangle
# cv2.rectangle(image, top_left, bottom_right, color, thickness)
cv2.rectangle(img, (50, 50), (200, 150), (0, 255, 0), 2)  # Green outline
cv2.rectangle(img, (250, 50), (400, 150), (0, 0, 255), -1)  # Red filled (-1 = filled)

cv2.imshow('Rectangles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 6.3 Draw Circles

```python
import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw circle
# cv2.circle(image, center, radius, color, thickness)
cv2.circle(img, (150, 200), 50, (255, 0, 0), 2)   # Blue outline
cv2.circle(img, (350, 200), 50, (0, 255, 255), -1)  # Yellow filled

cv2.imshow('Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 6.4 Draw Text

```python
import cv2
import numpy as np

img = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw text
# cv2.putText(image, text, position, font, scale, color, thickness)
cv2.putText(
    img,
    'Hello OpenCV!',
    (50, 200),                      # Position (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,       # Font
    2,                              # Scale
    (255, 255, 255),                # White color
    3                               # Thickness
)

# Available fonts:
# cv2.FONT_HERSHEY_SIMPLEX
# cv2.FONT_HERSHEY_PLAIN
# cv2.FONT_HERSHEY_DUPLEX
# cv2.FONT_HERSHEY_COMPLEX
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

cv2.imshow('Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 6.5 Draw on Existing Image

```python
import cv2

img = cv2.imread('photo.jpg')

# Draw bounding box (common in object detection)
cv2.rectangle(img, (100, 100), (300, 250), (0, 255, 0), 2)
cv2.putText(img, 'Person', (100, 95), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Draw circle at a point
cv2.circle(img, (200, 175), 5, (0, 0, 255), -1)

cv2.imshow('Annotated', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 7. Color Spaces

### 7.1 BGR vs RGB

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('photo.jpg')

# OpenCV uses BGR by default
# Matplotlib uses RGB

# Display with OpenCV (correct colors)
cv2.imshow('OpenCV (BGR)', img)

# For Matplotlib, convert to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Matplotlib (RGB)')
plt.savefig('matplotlib_display.png')
plt.show()
```

### 7.2 Convert Color Spaces

```python
import cv2

img = cv2.imread('photo.jpg')

# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

print(f"Original shape: {img.shape}")   # (480, 640, 3)
print(f"Grayscale shape: {gray.shape}") # (480, 640)
print(f"HSV shape: {hsv.shape}")        # (480, 640, 3)
```

### 7.3 Split and Merge Channels

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg')

# Split into B, G, R channels
b, g, r = cv2.split(img)

print(f"Blue channel shape: {b.shape}")  # (480, 640)

# Show individual channels
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

# Merge channels back
merged = cv2.merge([b, g, r])

# Create color-highlighted channels
zeros = np.zeros_like(b)
blue_only = cv2.merge([b, zeros, zeros])
green_only = cv2.merge([zeros, g, zeros])
red_only = cv2.merge([zeros, zeros, r])

cv2.imshow('Blue Only', blue_only)
cv2.imshow('Green Only', green_only)
cv2.imshow('Red Only', red_only)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 8. Image Filtering

### 8.1 Blur (Smoothing)

```python
import cv2

img = cv2.imread('photo.jpg')

# Average Blur
blur_avg = cv2.blur(img, (5, 5))  # 5x5 kernel

# Gaussian Blur (most common)
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur (good for salt-and-pepper noise)
blur_median = cv2.medianBlur(img, 5)

# Bilateral Filter (preserves edges)
blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', blur_gaussian)
cv2.imshow('Median Blur', blur_median)
cv2.imshow('Bilateral', blur_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 8.2 Sharpen

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg')

# Sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 8.3 Thresholding

```python
import cv2

img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Simple thresholding
# Pixels > 127 become 255 (white), others become 0 (black)
_, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Inverse
_, thresh_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Adaptive thresholding (better for varying lighting)
thresh_adaptive = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

# Otsu's thresholding (automatic threshold)
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Binary', thresh_binary)
cv2.imshow('Adaptive', thresh_adaptive)
cv2.imshow('Otsu', thresh_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 9. Edge Detection

### 9.1 Canny Edge Detection

```python
import cv2

img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Canny edge detection
# Lower and upper threshold
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 9.2 Sobel Edge Detection

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel in X direction (vertical edges)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel in Y direction (horizontal edges)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert to displayable format
sobel_x_abs = np.uint8(np.absolute(sobel_x))
sobel_y_abs = np.uint8(np.absolute(sobel_y))

cv2.imshow('Sobel X', sobel_x_abs)
cv2.imshow('Sobel Y', sobel_y_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 9.3 Laplacian Edge Detection

```python
import cv2
import numpy as np

img = cv2.imread('photo.jpg', cv2.IMREAD_GRAYSCALE)

# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_abs = np.uint8(np.absolute(laplacian))

cv2.imshow('Original', img)
cv2.imshow('Laplacian', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 10. Working with Video

### 10.1 Read from Webcam

```python
import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Display frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
```

### 10.2 Read from Video File

```python
import cv2

# Open video file
cap = cv2.VideoCapture('video.mp4')

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"FPS: {fps}")
print(f"Resolution: {width}x{height}")
print(f"Total frames: {total_frames}")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Process frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', gray)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### 10.3 Save Video

```python
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' to stop")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Write frame
    out.write(frame)

    cv2.imshow('Recording', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video saved as output.avi")
```

---

## 11. Face Detection

### 11.1 Using Haar Cascades

```python
import cv2

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Read image
img = cv2.imread('people.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,   # How much to reduce image size each scale
    minNeighbors=5,    # How many neighbors to confirm detection
    minSize=(30, 30)   # Minimum face size
)

print(f"Found {len(faces)} faces!")

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 11.2 Real-time Face Detection (Webcam)

```python
import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Open webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show count
    cv2.putText(frame, f'Faces: {len(faces)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### 11.3 Eye Detection

```python
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Search for eyes within face region
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('Face and Eyes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 12. Real-World Examples

### Example 1: Image Preprocessing for ML

```python
import cv2
import numpy as np

def preprocess_for_ml(image_path, target_size=(224, 224)):
    """
    Preprocess image for machine learning model
    """
    # Read image
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(f"Could not load image: {image_path}")

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize
    img = cv2.resize(img, target_size)

    # Normalize to 0-1
    img = img.astype(np.float32) / 255.0

    # Add batch dimension (for model input)
    img = np.expand_dims(img, axis=0)

    return img

# Usage
preprocessed = preprocess_for_ml('photo.jpg')
print(f"Shape: {preprocessed.shape}")  # (1, 224, 224, 3)
print(f"Min: {preprocessed.min()}, Max: {preprocessed.max()}")  # 0.0, 1.0
```

### Example 2: Batch Image Processing

```python
import cv2
import os

def batch_resize(input_folder, output_folder, size=(256, 256)):
    """
    Resize all images in a folder
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Read
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            if img is not None:
                # Resize
                resized = cv2.resize(img, size)

                # Save
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, resized)

                print(f"Processed: {filename}")

# Usage
batch_resize('raw_images', 'processed_images', size=(224, 224))
```

### Example 3: Document Scanner

```python
import cv2
import numpy as np

def scan_document(image_path):
    """
    Simple document scanner effect
    """
    # Read image
    img = cv2.imread(image_path)
    original = img.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur and detect edges
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 75, 200)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Sort by area, get largest
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Find document contour (4 points)
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == 4:
            document_contour = approx
            break

    # Draw contour
    cv2.drawContours(img, [document_contour], -1, (0, 255, 0), 2)

    cv2.imshow('Original', original)
    cv2.imshow('Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# scan_document('document.jpg')
```

### Example 4: Color Detection

```python
import cv2
import numpy as np

def detect_color(image_path, color='blue'):
    """
    Detect specific color in image
    """
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Color ranges in HSV
    colors = {
        'blue': ([100, 50, 50], [130, 255, 255]),
        'green': ([40, 50, 50], [80, 255, 255]),
        'red': ([0, 50, 50], [10, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255])
    }

    lower, upper = colors.get(color, colors['blue'])
    lower = np.array(lower)
    upper = np.array(upper)

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Apply mask
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.imshow(f'{color.capitalize()} Objects', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# detect_color('objects.jpg', 'blue')
```

---

## 13. Quick Reference

### Common Operations

| Operation | Code |
|-----------|------|
| Read image | `cv2.imread('img.jpg')` |
| Show image | `cv2.imshow('Title', img)` |
| Save image | `cv2.imwrite('out.jpg', img)` |
| Resize | `cv2.resize(img, (w, h))` |
| Grayscale | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` |
| Blur | `cv2.GaussianBlur(img, (5,5), 0)` |
| Edges | `cv2.Canny(img, 100, 200)` |
| Draw rect | `cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)` |
| Draw text | `cv2.putText(img, 'text', (x,y), font, 1, (255,255,255), 2)` |

### Color Conversions

| Conversion | Code |
|------------|------|
| BGR to RGB | `cv2.COLOR_BGR2RGB` |
| BGR to Gray | `cv2.COLOR_BGR2GRAY` |
| BGR to HSV | `cv2.COLOR_BGR2HSV` |
| Gray to BGR | `cv2.COLOR_GRAY2BGR` |

### Video Operations

| Operation | Code |
|-----------|------|
| Open webcam | `cv2.VideoCapture(0)` |
| Open file | `cv2.VideoCapture('video.mp4')` |
| Read frame | `ret, frame = cap.read()` |
| Release | `cap.release()` |

### Common Imports

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# For face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
```

---

## Summary

OpenCV is essential for AI/ML image preprocessing:

1. **Read/Write** - `imread()`, `imwrite()`
2. **Display** - `imshow()`, `waitKey()`
3. **Transform** - `resize()`, `rotate()`, `flip()`
4. **Colors** - `cvtColor()`, BGR vs RGB
5. **Filter** - `GaussianBlur()`, `Canny()`
6. **Draw** - `rectangle()`, `circle()`, `putText()`
7. **Video** - `VideoCapture()`, frame loop
8. **Detect** - Haar cascades for faces

Master these basics before moving to advanced computer vision!
