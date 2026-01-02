# Pillow (PIL) - Image Processing Library

> **What is it?** Python library for opening, manipulating, and saving image files
> **Install:** `pip install Pillow`
> **Import as:** `from PIL import Image`

---

## Table of Contents

1. [What is Pillow?](#1-what-is-pillow)
2. [Installation](#2-installation)
3. [Opening and Saving Images](#3-opening-and-saving-images)
4. [Image Properties](#4-image-properties)
5. [Basic Operations](#5-basic-operations)
6. [Image Transformations](#6-image-transformations)
7. [Color Operations](#7-color-operations)
8. [Filters and Effects](#8-filters-and-effects)
9. [Drawing on Images](#9-drawing-on-images)
10. [Working with Text](#10-working-with-text)
11. [Batch Processing](#11-batch-processing)
12. [ML Preprocessing with Pillow](#12-ml-preprocessing-with-pillow)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is Pillow?

### Simple Explanation

Pillow is a tool that lets Python **work with images** - open them, edit them, and save them.

```
What can Pillow do?

Open images:
- JPG, PNG, GIF, BMP, and more
- Read from files or URLs

Edit images:
- Resize, crop, rotate
- Change colors
- Apply filters
- Add text and shapes

Save images:
- Different formats
- Different quality levels
- Optimized for web

Why Pillow for AI/ML?
- Preprocess images before training
- Resize to consistent dimensions
- Convert formats
- Augment training data
- Simpler than OpenCV for basic tasks
```

### Pillow vs OpenCV

| Pillow | OpenCV |
|--------|--------|
| Simple, Pythonic | Complex, powerful |
| Basic image operations | Computer vision |
| RGB format | BGR format |
| Best for preprocessing | Best for analysis |
| Lightweight | Heavy |

**Use Pillow when:** Simple image manipulation, ML preprocessing
**Use OpenCV when:** Computer vision, video, face detection

---

## 2. Installation

```bash
# Install Pillow
pip install Pillow

# Verify installation
python -c "from PIL import Image; print('Pillow installed!')"
```

### Basic Import

```python
from PIL import Image

# Other useful modules
from PIL import ImageFilter, ImageEnhance, ImageDraw, ImageFont
```

---

## 3. Opening and Saving Images

### 3.1 Open an Image

```python
from PIL import Image

# Open image file
img = Image.open('photo.jpg')

# Check if loaded
print(f"Format: {img.format}")    # JPEG
print(f"Size: {img.size}")        # (width, height)
print(f"Mode: {img.mode}")        # RGB

# Display image (opens default viewer)
img.show()
```

### 3.2 Open from Different Sources

```python
from PIL import Image
import requests
from io import BytesIO

# From file
img = Image.open('local_image.jpg')

# From URL
url = 'https://example.com/image.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# From bytes
with open('image.jpg', 'rb') as f:
    img = Image.open(BytesIO(f.read()))
```

### 3.3 Save an Image

```python
from PIL import Image

img = Image.open('photo.jpg')

# Save as different format
img.save('photo.png')  # Convert to PNG
img.save('photo.bmp')  # Convert to BMP

# Save with quality (JPEG only)
img.save('compressed.jpg', quality=50)  # Lower quality, smaller file

# Save with optimization
img.save('optimized.png', optimize=True)

# Save as specific format
img.save('output', format='JPEG')
```

### 3.4 Convert Formats

```python
from PIL import Image

# Open PNG with transparency
img = Image.open('logo.png')  # RGBA mode

# Convert to JPEG (no transparency)
if img.mode == 'RGBA':
    # Create white background
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])  # 3 is alpha channel
    background.save('logo.jpg', 'JPEG')
else:
    img.save('logo.jpg', 'JPEG')
```

---

## 4. Image Properties

### 4.1 Get Image Information

```python
from PIL import Image

img = Image.open('photo.jpg')

# Basic properties
print(f"Filename: {img.filename}")
print(f"Format: {img.format}")      # JPEG, PNG, etc.
print(f"Mode: {img.mode}")          # RGB, RGBA, L, etc.
print(f"Size: {img.size}")          # (width, height)
print(f"Width: {img.width}")
print(f"Height: {img.height}")

# Info dictionary (metadata)
print(f"Info: {img.info}")
```

### 4.2 Image Modes

| Mode | Description | Channels |
|------|-------------|----------|
| `1` | Black and white | 1 bit |
| `L` | Grayscale | 8 bit |
| `RGB` | True color | 3x8 bit |
| `RGBA` | True color + alpha | 4x8 bit |
| `CMYK` | Print colors | 4x8 bit |
| `P` | Palette | 8 bit |

```python
from PIL import Image

img = Image.open('photo.jpg')

# Check mode
print(f"Mode: {img.mode}")  # RGB

# Convert modes
gray = img.convert('L')        # Grayscale
rgba = img.convert('RGBA')     # Add alpha
bw = img.convert('1')          # Black and white

print(f"Grayscale mode: {gray.mode}")  # L
```

### 4.3 Access Pixels

```python
from PIL import Image

img = Image.open('photo.jpg')

# Get pixel at position (x, y)
pixel = img.getpixel((100, 50))
print(f"Pixel at (100, 50): {pixel}")  # (R, G, B)

# Set pixel
img.putpixel((100, 50), (255, 0, 0))  # Set to red

# Get all pixels
pixels = list(img.getdata())
print(f"Total pixels: {len(pixels)}")

# Load for faster pixel access
pix = img.load()
print(f"Pixel: {pix[100, 50]}")
pix[100, 50] = (0, 255, 0)  # Set to green
```

---

## 5. Basic Operations

### 5.1 Resize Images

```python
from PIL import Image

img = Image.open('photo.jpg')
print(f"Original: {img.size}")  # (1920, 1080)

# Resize to exact dimensions
resized = img.resize((800, 600))
print(f"Resized: {resized.size}")  # (800, 600)

# Resize maintaining aspect ratio
def resize_with_aspect(img, max_size):
    """Resize while maintaining aspect ratio"""
    ratio = min(max_size[0] / img.width, max_size[1] / img.height)
    new_size = (int(img.width * ratio), int(img.height * ratio))
    return img.resize(new_size, Image.LANCZOS)

resized = resize_with_aspect(img, (800, 800))
print(f"Aspect preserved: {resized.size}")

# Resampling filters
# Image.NEAREST - fastest, lowest quality
# Image.BILINEAR - medium
# Image.BICUBIC - better
# Image.LANCZOS - best quality
high_quality = img.resize((800, 600), Image.LANCZOS)
```

### 5.2 Crop Images

```python
from PIL import Image

img = Image.open('photo.jpg')

# Crop (left, upper, right, lower)
box = (100, 100, 400, 300)  # x1, y1, x2, y2
cropped = img.crop(box)
print(f"Cropped size: {cropped.size}")  # (300, 200)

# Center crop
def center_crop(img, crop_size):
    """Crop from center"""
    width, height = img.size
    new_width, new_height = crop_size

    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    return img.crop((left, top, right, bottom))

centered = center_crop(img, (500, 500))
centered.save('centered_crop.jpg')
```

### 5.3 Thumbnail (Resize In-Place)

```python
from PIL import Image

img = Image.open('photo.jpg')
print(f"Original: {img.size}")

# Create thumbnail (modifies in place, maintains aspect ratio)
img.thumbnail((200, 200))
print(f"Thumbnail: {img.size}")  # Fits within 200x200

img.save('thumbnail.jpg')
```

### 5.4 Copy and Paste

```python
from PIL import Image

# Open images
background = Image.open('background.jpg')
logo = Image.open('logo.png')

# Paste logo onto background
position = (50, 50)  # Top-left corner

# Simple paste
background.paste(logo, position)

# Paste with transparency (if logo has alpha)
if logo.mode == 'RGBA':
    background.paste(logo, position, logo)  # Third arg is mask

background.save('combined.jpg')
```

---

## 6. Image Transformations

### 6.1 Rotate Images

```python
from PIL import Image

img = Image.open('photo.jpg')

# Rotate by angle (counterclockwise)
rotated_45 = img.rotate(45)  # Background is black
rotated_45.save('rotated_45.jpg')

# Rotate with expand (resize to fit)
rotated_expand = img.rotate(45, expand=True)
rotated_expand.save('rotated_expand.jpg')

# Rotate with fill color
rotated_fill = img.rotate(45, fillcolor='white')
rotated_fill.save('rotated_white.jpg')

# Specific rotations
rotated_90 = img.transpose(Image.ROTATE_90)
rotated_180 = img.transpose(Image.ROTATE_180)
rotated_270 = img.transpose(Image.ROTATE_270)
```

### 6.2 Flip Images

```python
from PIL import Image

img = Image.open('photo.jpg')

# Flip horizontally (mirror)
flipped_h = img.transpose(Image.FLIP_LEFT_RIGHT)

# Flip vertically
flipped_v = img.transpose(Image.FLIP_TOP_BOTTOM)

flipped_h.save('flipped_horizontal.jpg')
flipped_v.save('flipped_vertical.jpg')
```

### 6.3 All Transpose Operations

```python
from PIL import Image

img = Image.open('photo.jpg')

# All transpose methods
operations = {
    'FLIP_LEFT_RIGHT': Image.FLIP_LEFT_RIGHT,
    'FLIP_TOP_BOTTOM': Image.FLIP_TOP_BOTTOM,
    'ROTATE_90': Image.ROTATE_90,
    'ROTATE_180': Image.ROTATE_180,
    'ROTATE_270': Image.ROTATE_270,
    'TRANSPOSE': Image.TRANSPOSE,
    'TRANSVERSE': Image.TRANSVERSE
}

for name, op in operations.items():
    result = img.transpose(op)
    result.save(f'{name.lower()}.jpg')
```

---

## 7. Color Operations

### 7.1 Convert to Grayscale

```python
from PIL import Image

img = Image.open('photo.jpg')

# Convert to grayscale
gray = img.convert('L')
gray.save('grayscale.jpg')

print(f"Original mode: {img.mode}")   # RGB
print(f"Grayscale mode: {gray.mode}") # L
```

### 7.2 Split and Merge Channels

```python
from PIL import Image

img = Image.open('photo.jpg')

# Split into R, G, B channels
r, g, b = img.split()

# Each channel is grayscale image
r.save('red_channel.jpg')
g.save('green_channel.jpg')
b.save('blue_channel.jpg')

# Merge channels (swap R and B)
swapped = Image.merge('RGB', (b, g, r))
swapped.save('swapped_colors.jpg')

# Create single color images
zeros = Image.new('L', img.size, 0)
red_only = Image.merge('RGB', (r, zeros, zeros))
red_only.save('red_only.jpg')
```

### 7.3 Adjust Brightness, Contrast, Color

```python
from PIL import Image, ImageEnhance

img = Image.open('photo.jpg')

# Brightness (1.0 = original, <1 darker, >1 brighter)
enhancer = ImageEnhance.Brightness(img)
bright = enhancer.enhance(1.5)   # 50% brighter
dark = enhancer.enhance(0.5)     # 50% darker

# Contrast
enhancer = ImageEnhance.Contrast(img)
high_contrast = enhancer.enhance(2.0)
low_contrast = enhancer.enhance(0.5)

# Color saturation
enhancer = ImageEnhance.Color(img)
vibrant = enhancer.enhance(2.0)    # More colorful
desaturated = enhancer.enhance(0.5) # Less colorful

# Sharpness
enhancer = ImageEnhance.Sharpness(img)
sharp = enhancer.enhance(2.0)
soft = enhancer.enhance(0.5)

# Save
bright.save('bright.jpg')
high_contrast.save('high_contrast.jpg')
```

---

## 8. Filters and Effects

### 8.1 Built-in Filters

```python
from PIL import Image, ImageFilter

img = Image.open('photo.jpg')

# Blur
blurred = img.filter(ImageFilter.BLUR)
more_blur = img.filter(ImageFilter.GaussianBlur(5))

# Sharpen
sharpened = img.filter(ImageFilter.SHARPEN)

# Edge detection
edges = img.filter(ImageFilter.FIND_EDGES)
contour = img.filter(ImageFilter.CONTOUR)

# Emboss
embossed = img.filter(ImageFilter.EMBOSS)

# Smooth
smoothed = img.filter(ImageFilter.SMOOTH)
more_smooth = img.filter(ImageFilter.SMOOTH_MORE)

# Detail
detailed = img.filter(ImageFilter.DETAIL)

# Save examples
blurred.save('blurred.jpg')
edges.save('edges.jpg')
embossed.save('embossed.jpg')
```

### 8.2 All Built-in Filters

```python
from PIL import Image, ImageFilter

img = Image.open('photo.jpg')

filters = [
    ImageFilter.BLUR,
    ImageFilter.CONTOUR,
    ImageFilter.DETAIL,
    ImageFilter.EDGE_ENHANCE,
    ImageFilter.EDGE_ENHANCE_MORE,
    ImageFilter.EMBOSS,
    ImageFilter.FIND_EDGES,
    ImageFilter.SHARPEN,
    ImageFilter.SMOOTH,
    ImageFilter.SMOOTH_MORE,
]

for f in filters:
    result = img.filter(f)
    name = str(f).split()[0].lower()
    result.save(f'filter_{name}.jpg')
```

### 8.3 Custom Kernels

```python
from PIL import Image, ImageFilter

img = Image.open('photo.jpg')

# Custom kernel (3x3)
# Edge detection kernel
edge_kernel = ImageFilter.Kernel(
    size=(3, 3),
    kernel=[
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1
    ],
    scale=1
)

result = img.filter(edge_kernel)
result.save('custom_edge.jpg')

# Sharpen kernel
sharpen_kernel = ImageFilter.Kernel(
    size=(3, 3),
    kernel=[
        0, -1, 0,
        -1,  5, -1,
        0, -1, 0
    ],
    scale=1
)

sharpened = img.filter(sharpen_kernel)
sharpened.save('custom_sharpen.jpg')
```

---

## 9. Drawing on Images

### 9.1 Basic Shapes

```python
from PIL import Image, ImageDraw

# Create blank image or open existing
img = Image.new('RGB', (400, 300), 'white')
draw = ImageDraw.Draw(img)

# Draw line
draw.line((0, 0, 400, 300), fill='black', width=3)

# Draw rectangle
draw.rectangle((50, 50, 150, 100), outline='red', width=2)

# Filled rectangle
draw.rectangle((200, 50, 300, 100), fill='blue', outline='black')

# Draw ellipse (oval)
draw.ellipse((50, 150, 150, 250), outline='green', width=2)

# Filled circle
draw.ellipse((200, 150, 300, 250), fill='yellow', outline='black')

# Draw polygon
draw.polygon([(320, 50), (380, 100), (350, 150)], fill='purple')

# Draw arc
draw.arc((50, 200, 150, 280), start=0, end=180, fill='orange', width=3)

img.save('shapes.png')
img.show()
```

### 9.2 Draw on Existing Image

```python
from PIL import Image, ImageDraw

# Open image
img = Image.open('photo.jpg')
draw = ImageDraw.Draw(img)

# Draw bounding box (like object detection)
box = (100, 100, 300, 250)
draw.rectangle(box, outline='green', width=3)

# Add label background
label = "Person"
draw.rectangle((100, 80, 180, 100), fill='green')

# Draw point
draw.ellipse((195, 170, 205, 180), fill='red')  # Center point

img.save('annotated.jpg')
```

---

## 10. Working with Text

### 10.1 Add Simple Text

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (400, 200), 'white')
draw = ImageDraw.Draw(img)

# Simple text (default font)
draw.text((50, 50), "Hello Pillow!", fill='black')

# With specific position
draw.text((50, 100), "X=50, Y=100", fill='blue')

img.save('text_simple.png')
```

### 10.2 Custom Fonts

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (400, 200), 'white')
draw = ImageDraw.Draw(img)

# Load TrueType font (need .ttf file)
try:
    # Try system fonts
    font = ImageFont.truetype("arial.ttf", 36)
except:
    # Fallback to default
    font = ImageFont.load_default()

draw.text((50, 50), "Custom Font!", font=font, fill='navy')

# Different sizes
small_font = ImageFont.truetype("arial.ttf", 16)
large_font = ImageFont.truetype("arial.ttf", 48)

draw.text((50, 100), "Small", font=small_font, fill='gray')
draw.text((50, 130), "Large", font=large_font, fill='black')

img.save('text_fonts.png')
```

### 10.3 Text with Background

```python
from PIL import Image, ImageDraw, ImageFont

def add_text_with_bg(img, text, position, font_size=24):
    """Add text with background rectangle"""
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Get text size
    bbox = draw.textbbox(position, text, font=font)

    # Draw background
    padding = 5
    draw.rectangle(
        (bbox[0]-padding, bbox[1]-padding, bbox[2]+padding, bbox[3]+padding),
        fill='white',
        outline='black'
    )

    # Draw text
    draw.text(position, text, font=font, fill='black')

    return img

# Usage
img = Image.open('photo.jpg')
img = add_text_with_bg(img, "Label", (50, 50), 20)
img.save('labeled.jpg')
```

---

## 11. Batch Processing

### 11.1 Process Multiple Images

```python
from PIL import Image
import os

def batch_resize(input_folder, output_folder, size=(224, 224)):
    """Resize all images in a folder"""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)

            # Resize
            img_resized = img.resize(size, Image.LANCZOS)

            # Convert mode if needed
            if img_resized.mode == 'RGBA':
                img_resized = img_resized.convert('RGB')

            # Save
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)

            print(f"Processed: {filename}")

# Usage
batch_resize('raw_images', 'processed_images', (224, 224))
```

### 11.2 Convert All to Grayscale

```python
from PIL import Image
import os

def batch_grayscale(input_folder, output_folder):
    """Convert all images to grayscale"""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)

            gray = img.convert('L')

            output_path = os.path.join(output_folder, filename)
            gray.save(output_path)

            print(f"Converted: {filename}")

batch_grayscale('color_images', 'gray_images')
```

### 11.3 Create Image Thumbnails

```python
from PIL import Image
import os

def create_thumbnails(input_folder, output_folder, max_size=(150, 150)):
    """Create thumbnails for all images"""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)

            # Create thumbnail
            img.thumbnail(max_size, Image.LANCZOS)

            # Save with prefix
            output_path = os.path.join(output_folder, f'thumb_{filename}')
            img.save(output_path)

            print(f"Thumbnail created: {filename}")

create_thumbnails('photos', 'thumbnails')
```

---

## 12. ML Preprocessing with Pillow

### 12.1 Preprocess for CNN

```python
from PIL import Image
import numpy as np

def preprocess_for_cnn(image_path, target_size=(224, 224)):
    """Preprocess image for CNN model (like ResNet, VGG)"""
    # Open image
    img = Image.open(image_path)

    # Convert to RGB (in case of grayscale or RGBA)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Resize
    img = img.resize(target_size, Image.LANCZOS)

    # Convert to numpy array
    img_array = np.array(img, dtype=np.float32)

    # Normalize to [0, 1]
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

# Usage
preprocessed = preprocess_for_cnn('cat.jpg')
print(f"Shape: {preprocessed.shape}")  # (1, 224, 224, 3)
print(f"Range: {preprocessed.min():.2f} - {preprocessed.max():.2f}")  # 0.00 - 1.00
```

### 12.2 Data Augmentation

```python
from PIL import Image, ImageEnhance, ImageFilter
import random

def augment_image(img):
    """Apply random augmentations"""
    augmentations = []

    # Random horizontal flip
    if random.random() > 0.5:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        augmentations.append('flip_h')

    # Random rotation (-15 to 15 degrees)
    if random.random() > 0.5:
        angle = random.uniform(-15, 15)
        img = img.rotate(angle, fillcolor='white')
        augmentations.append(f'rotate_{angle:.1f}')

    # Random brightness
    if random.random() > 0.5:
        factor = random.uniform(0.8, 1.2)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(factor)
        augmentations.append(f'brightness_{factor:.2f}')

    # Random contrast
    if random.random() > 0.5:
        factor = random.uniform(0.8, 1.2)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(factor)
        augmentations.append(f'contrast_{factor:.2f}')

    return img, augmentations

# Usage
img = Image.open('photo.jpg')

# Create multiple augmented versions
for i in range(5):
    augmented, applied = augment_image(img.copy())
    augmented.save(f'augmented_{i}.jpg')
    print(f"Image {i}: {applied}")
```

### 12.3 Batch Preprocessing for Dataset

```python
from PIL import Image
import numpy as np
import os

def prepare_dataset(image_folder, target_size=(224, 224)):
    """Prepare all images for ML training"""
    images = []
    filenames = []

    for filename in sorted(os.listdir(image_folder)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load and preprocess
            path = os.path.join(image_folder, filename)
            img = Image.open(path)

            # Convert to RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize
            img = img.resize(target_size, Image.LANCZOS)

            # To numpy and normalize
            img_array = np.array(img, dtype=np.float32) / 255.0

            images.append(img_array)
            filenames.append(filename)

    # Stack into single array
    dataset = np.array(images)

    print(f"Dataset shape: {dataset.shape}")  # (N, 224, 224, 3)
    print(f"Images loaded: {len(filenames)}")

    return dataset, filenames

# Usage
X, names = prepare_dataset('training_images')
```

### 12.4 Convert Between Pillow and NumPy

```python
from PIL import Image
import numpy as np

# Pillow to NumPy
img = Image.open('photo.jpg')
array = np.array(img)
print(f"Array shape: {array.shape}")  # (height, width, channels)
print(f"Array dtype: {array.dtype}")  # uint8

# NumPy to Pillow
array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
img = Image.fromarray(array)
img.save('from_array.jpg')

# Normalized array to Pillow
normalized = np.random.random((100, 100, 3))  # 0-1 range
denormalized = (normalized * 255).astype(np.uint8)
img = Image.fromarray(denormalized)
```

---

## 13. Quick Reference

### Common Operations

| Operation | Code |
|-----------|------|
| Open image | `Image.open('file.jpg')` |
| Save image | `img.save('output.jpg')` |
| Show image | `img.show()` |
| Get size | `img.size` → (width, height) |
| Resize | `img.resize((w, h))` |
| Crop | `img.crop((x1, y1, x2, y2))` |
| Rotate | `img.rotate(45)` |
| Flip horizontal | `img.transpose(Image.FLIP_LEFT_RIGHT)` |
| Grayscale | `img.convert('L')` |
| Thumbnail | `img.thumbnail((w, h))` |

### Common Imports

```python
from PIL import Image                 # Core
from PIL import ImageFilter           # Filters
from PIL import ImageEnhance          # Brightness, contrast
from PIL import ImageDraw             # Draw shapes
from PIL import ImageFont             # Text fonts
from PIL import ImageOps              # Operations
import numpy as np                    # Array conversion
```

### Image Modes

| Mode | Meaning |
|------|---------|
| `RGB` | Color (3 channels) |
| `RGBA` | Color + transparency |
| `L` | Grayscale |
| `1` | Black and white |
| `P` | Palette |

### Resize Methods

| Method | Quality | Speed |
|--------|---------|-------|
| `Image.NEAREST` | Low | Fast |
| `Image.BILINEAR` | Medium | Medium |
| `Image.BICUBIC` | High | Slow |
| `Image.LANCZOS` | Highest | Slowest |

### ML Preprocessing Template

```python
from PIL import Image
import numpy as np

def preprocess(path, size=(224, 224)):
    img = Image.open(path)
    img = img.convert('RGB')
    img = img.resize(size, Image.LANCZOS)
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)
```

---

## Summary

Pillow is essential for image preprocessing in ML:

1. **Open/Save** - `Image.open()`, `img.save()`
2. **Resize** - `img.resize()`, `img.thumbnail()`
3. **Transform** - `img.rotate()`, `img.transpose()`
4. **Convert** - `img.convert('L')` for grayscale
5. **Enhance** - `ImageEnhance` for brightness/contrast
6. **Filter** - `ImageFilter` for blur/sharpen
7. **Draw** - `ImageDraw` for shapes/text
8. **NumPy** - `np.array(img)` for ML

Master Pillow for image preprocessing before training models!
