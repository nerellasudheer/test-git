# Tkinter - Python GUI Toolkit Complete Guide

A comprehensive reference for building desktop applications with Python's standard GUI library.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Widget Configuration](#2-widget-configuration)
3. [Common Widgets](#3-common-widgets)
4. [Layout Managers](#4-layout-managers)
5. [Canvas Widget](#5-canvas-widget)
6. [Event Handling](#6-event-handling)
7. [MessageBox Dialogs](#7-messagebox-dialogs)
8. [Input Methods](#8-input-methods)
9. [Tkinter vs Other Tools](#9-tkinter-vs-other-tools)
10. [Quick Reference](#10-quick-reference)

---

## 1. Overview

### What is Tkinter?

Tkinter (Tk interface) is Python's standard built-in GUI (Graphical User Interface) library. It provides a fast and easy way to create desktop applications with windows, buttons, text fields, and other interactive elements.

### Key Features

| Feature | Description |
|---------|-------------|
| Built-in | No separate installation needed |
| Cross-platform | Works on Windows, macOS, Linux |
| Lightweight | Simple and fast for basic GUI applications |
| Based on Tcl/Tk | GUI toolkit originally from Tcl language |

### Basic Structure

```python
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

# Add widgets here
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Start the application
root.mainloop()
```

---

## 2. Widget Configuration

### Three Ways to Configure Widgets

**1. During Creation (Constructor)**

```python
label = tk.Label(root, text="Hello World", bg="yellow", fg="blue", font=("Arial", 16))
label.pack()
```

**2. Direct Attribute Access**

```python
label = tk.Label(root)
label["text"] = "Modified Text"
label["bg"] = "lightblue"
label["fg"] = "red"
label.pack()
```

**3. Using config() Method**

```python
label = tk.Label(root)
label.config(text="Updated Text", bg="green", fg="white", font=("Courier", 14))
label.pack()
```

---

## 3. Common Widgets

### Label - Display Text

```python
label = tk.Label(root,
                 text="Welcome!",
                 bg="yellow",
                 fg="blue",
                 font=("Arial", 16, "bold"))
label.pack(pady=10)
```

| Parameter | Description |
|-----------|-------------|
| `text` | Text to display |
| `bg` | Background color |
| `fg` | Text color |
| `font` | Font style (family, size, weight) |
| `image` | Display an image |

### Button - Clickable Button

```python
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root,
                   text="Click Me",
                   command=on_click,
                   bg="lightblue")
button.pack()
```

| Parameter | Description |
|-----------|-------------|
| `text` | Button text |
| `command` | Function to execute on click |
| `state` | "normal", "disabled", "active" |

### Entry - Single-Line Input

```python
def show_input():
    user_input = entry.get()
    print(f"You entered: {user_input}")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Password field
password_entry = tk.Entry(root, show="*")
```

| Parameter | Description |
|-----------|-------------|
| `width` | Width of entry box |
| `show` | Hide characters (e.g., `show="*"`) |
| `textvariable` | Link to StringVar |

### Text - Multi-Line Input

```python
text_box = tk.Text(root, height=5, width=40, wrap="word")
text_box.pack()
text_box.insert("1.0", "Type here...")

# Get content
content = text_box.get("1.0", tk.END)
```

| Method | Description |
|--------|-------------|
| `.insert(pos, text)` | Insert text at position |
| `.get(start, end)` | Get text between positions |
| `.delete(start, end)` | Delete text |

### Checkbutton - Checkbox

```python
var1 = tk.IntVar()
var2 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Python", variable=var1)
check1.pack()

check2 = tk.Checkbutton(root, text="Java", variable=var2)
check2.pack()

# Get values: var1.get() returns 0 or 1
```

### Radiobutton - Single Selection

```python
var = tk.StringVar(value="Python")  # Default selection

radio1 = tk.Radiobutton(root, text="Python", variable=var, value="Python")
radio1.pack()

radio2 = tk.Radiobutton(root, text="Java", variable=var, value="Java")
radio2.pack()

# Get selected: var.get()
```

### Listbox - List of Items

```python
listbox = tk.Listbox(root, height=4, selectmode="single")
listbox.pack()

fruits = ["Apple", "Banana", "Cherry", "Date"]
for fruit in fruits:
    listbox.insert(tk.END, fruit)

# Get selection
def show_selection():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        print(f"Selected: {item}")
```

### Spinbox - Numeric Selector

```python
spinbox = tk.Spinbox(root, from_=0, to=10, width=10)
spinbox.pack()

# Get value: spinbox.get()
```

### Scale - Slider

```python
def show_value(val):
    print(f"Value: {val}")

scale = tk.Scale(root,
                 from_=0,
                 to=100,
                 orient="horizontal",
                 length=300,
                 command=show_value)
scale.pack()
```

### Frame - Container

```python
frame = tk.Frame(root, bg="lightblue", bd=5, relief="raised")
frame.pack(pady=10, padx=10, fill="both")

tk.Label(frame, text="Inside Frame", bg="lightblue").pack()
tk.Button(frame, text="Button").pack()
```

| Relief Styles |
|---------------|
| `flat`, `raised`, `sunken`, `groove`, `ridge` |

### Combobox - Dropdown (ttk)

```python
from tkinter import ttk

combo = ttk.Combobox(root, values=["New York", "London", "Tokyo", "Paris"])
combo.pack()
combo.bind("<<ComboboxSelected>>", lambda e: print(combo.get()))
```

### Menu - Menu Bar

```python
def new_file():
    print("New File")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
```

---

## 4. Layout Managers

### pack() - Simple Stacking

```python
tk.Label(root, text="Top", bg="red").pack(side="top", fill="x")
tk.Label(root, text="Bottom", bg="blue").pack(side="bottom", fill="x")
tk.Label(root, text="Left", bg="green").pack(side="left", fill="y")
tk.Label(root, text="Right", bg="yellow").pack(side="right", fill="y")
```

| Parameter | Values |
|-----------|--------|
| `side` | "top", "bottom", "left", "right" |
| `fill` | "x", "y", "both", "none" |
| `expand` | True/False |
| `padx/pady` | External padding |

### grid() - Row-Column Layout

```python
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)
```

| Parameter | Description |
|-----------|-------------|
| `row`, `column` | Position in grid |
| `rowspan`, `columnspan` | Span multiple cells |
| `sticky` | Alignment ("n", "s", "e", "w", combinations) |

### place() - Absolute Positioning

```python
root.geometry("400x300")

tk.Label(root, text="Top-Left", bg="red").place(x=10, y=10)
tk.Label(root, text="Center", bg="yellow").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(root, text="Bottom-Right", bg="blue").place(x=300, y=270)
```

| Parameter | Description |
|-----------|-------------|
| `x`, `y` | Pixel coordinates |
| `relx`, `rely` | Relative position (0.0 to 1.0) |
| `anchor` | Reference point ("center", "nw", etc.) |

### Layout Manager Comparison

| Manager | Best For | Pros | Cons |
|---------|----------|------|------|
| `pack()` | Simple linear layouts | Easy, quick | Limited control |
| `grid()` | Forms, structured layouts | Organized, flexible | Can be complex |
| `place()` | Custom positioning | Full control | Hard to maintain |

**Important**: Don't mix layout managers in the same parent container!

---

## 5. Canvas Widget

### Basic Canvas

```python
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()
```

### Drawing Methods

**Lines**

```python
canvas.create_line(50, 50, 350, 50, fill="red", width=3, dash=(5, 2))
canvas.create_line(50, 50, 100, 150, 200, 100, 300, 200, fill="blue")  # Polyline
```

**Rectangles**

```python
canvas.create_rectangle(50, 50, 200, 150, fill="yellow", outline="black", width=3)
```

**Ovals/Circles**

```python
# Oval (bounding box coordinates)
canvas.create_oval(50, 50, 200, 150, fill="red", outline="blue")

# Circle (equal width and height)
canvas.create_oval(100, 100, 200, 200, fill="green")
```

**Polygons**

```python
# Triangle
canvas.create_polygon(200, 50, 150, 150, 250, 150, fill="orange", outline="black")
```

**Arcs**

```python
canvas.create_arc(50, 50, 200, 200, start=0, extent=120, fill="yellow", style="pieslice")
# Styles: "pieslice", "chord", "arc"
```

**Text**

```python
canvas.create_text(200, 100, text="Hello Canvas!", font=("Arial", 20, "bold"), fill="blue")
```

**Images**

```python
from tkinter import PhotoImage

img = PhotoImage(file="image.png")
canvas.create_image(200, 150, image=img)
canvas.image = img  # Keep reference to prevent garbage collection
```

### Managing Canvas Items

```python
# Each item returns a unique ID
rect_id = canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Modify item
canvas.itemconfig(rect_id, fill="red", outline="yellow")

# Move item (relative)
canvas.move(rect_id, 10, 5)  # Move 10 right, 5 down

# Set new coordinates (absolute)
canvas.coords(rect_id, 100, 100, 200, 200)

# Delete item
canvas.delete(rect_id)

# Delete all
canvas.delete("all")

# Tags for group operations
canvas.create_rectangle(50, 50, 100, 100, fill="red", tags="shape")
canvas.create_rectangle(150, 50, 200, 100, fill="blue", tags="shape")
canvas.itemconfig("shape", outline="black", width=3)  # Apply to all
```

### Animation Example

```python
def animate():
    canvas.move(ball_id, 5, 0)
    coords = canvas.coords(ball_id)
    if coords[2] < 400:
        root.after(50, animate)

ball_id = canvas.create_oval(0, 150, 40, 190, fill="red")
animate()
```

---

## 6. Event Handling

### Mouse Events

```python
def on_click(event):
    print(f"Clicked at: ({event.x}, {event.y})")

canvas.bind("<Button-1>", on_click)  # Left click
canvas.bind("<Button-2>", on_click)  # Middle click
canvas.bind("<Button-3>", on_click)  # Right click
canvas.bind("<Double-Button-1>", on_click)  # Double left click
```

### Drag Events

```python
def start_drag(event):
    canvas.start_x = event.x
    canvas.start_y = event.y

def on_drag(event):
    dx = event.x - canvas.start_x
    dy = event.y - canvas.start_y
    canvas.move(rect_id, dx, dy)
    canvas.start_x = event.x
    canvas.start_y = event.y

canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", on_drag)
```

### Keyboard Events

```python
def on_key(event):
    if event.keysym == "Up":
        canvas.move(rect_id, 0, -10)
    elif event.keysym == "Down":
        canvas.move(rect_id, 0, 10)
    elif event.keysym == "Left":
        canvas.move(rect_id, -10, 0)
    elif event.keysym == "Right":
        canvas.move(rect_id, 10, 0)

canvas.bind("<KeyPress>", on_key)
canvas.focus_set()  # Required for keyboard events
```

### Focus

```python
entry1.focus()  # Set focus to widget
entry1.focus_set()  # Same as above
widget = root.focus_get()  # Get focused widget
```

---

## 7. MessageBox Dialogs

### Import

```python
from tkinter import messagebox
```

### Simple Alerts

```python
# Information
messagebox.showinfo("Success", "File saved successfully!")

# Warning
messagebox.showwarning("Warning", "Disk space is running low!")

# Error
messagebox.showerror("Error", "Failed to connect to database!")
```

### Questions/Confirmations

```python
# Yes/No question (returns string)
response = messagebox.askquestion("Confirm", "Do you want to continue?")
if response == "yes":
    print("User chose Yes")

# Yes/No (returns boolean)
response = messagebox.askyesno("Save", "Save changes?")
if response:
    print("Saving...")

# OK/Cancel (returns boolean)
response = messagebox.askokcancel("Delete", "Delete this file?")
if response:
    print("Deleting...")

# Retry/Cancel (returns boolean)
response = messagebox.askretrycancel("Failed", "Retry operation?")

# Yes/No/Cancel (returns True, False, or None)
response = messagebox.askyesnocancel("Save", "Save before closing?")
if response is True:
    print("Save and close")
elif response is False:
    print("Close without saving")
else:
    print("Cancel")
```

### MessageBox Summary

| Function | Buttons | Returns |
|----------|---------|---------|
| `showinfo()` | OK | "ok" |
| `showwarning()` | OK | "ok" |
| `showerror()` | OK | "ok" |
| `askquestion()` | Yes, No | "yes" or "no" |
| `askyesno()` | Yes, No | True or False |
| `askokcancel()` | OK, Cancel | True or False |
| `askretrycancel()` | Retry, Cancel | True or False |
| `askyesnocancel()` | Yes, No, Cancel | True, False, or None |

---

## 8. Input Methods

### get() Method

```python
# Entry widget
text = entry.get()

# Text widget
content = text_widget.get("1.0", tk.END)  # All text
first_line = text_widget.get("1.0", "1.end")  # First line only

# Variable
var = tk.StringVar()
entry = tk.Entry(root, textvariable=var)
value = var.get()

# Listbox
item = listbox.get(0)  # First item
selected_index = listbox.curselection()

# Spinbox
value = spinbox.get()

# Combobox
value = combo.get()
```

### Complete Form Example

```python
import tkinter as tk

def submit():
    name = entry_name.get()
    age = spinbox_age.get()
    feedback = text_feedback.get("1.0", tk.END)
    print(f"Name: {name}, Age: {age}, Feedback: {feedback}")

root = tk.Tk()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()
entry_name.focus()  # Auto-focus

tk.Label(root, text="Age:").pack()
spinbox_age = tk.Spinbox(root, from_=1, to=100)
spinbox_age.pack()

tk.Label(root, text="Feedback:").pack()
text_feedback = tk.Text(root, height=3, width=30)
text_feedback.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()
```

---

## 9. Tkinter vs Other Tools

### Tkinter vs Turtle

| Aspect | Tkinter | Turtle |
|--------|---------|--------|
| Purpose | GUI applications | Graphics/education |
| Use Case | Desktop apps, forms | Drawings, animations |
| Complexity | Moderate | Simple |
| Interaction | Buttons, menus, input | Keyboard/mouse drawing |
| Learning | Steeper curve | Beginner-friendly |

### When to Use What

**Use Tkinter when:**
- Building desktop applications
- Need buttons, forms, menus
- User input and data processing
- Tools like calculators, text editors

**Use Turtle when:**
- Teaching programming concepts
- Drawing shapes and patterns
- Simple animations
- Visualizing algorithms

**Use Web Frameworks when:**
- Building websites
- Browser-based interfaces
- Online dashboards
- Cloud applications

### Python GUI Alternatives

| Framework | Best For |
|-----------|----------|
| Tkinter | Simple, built-in, cross-platform |
| PyQt/PySide | Professional, feature-rich |
| Kivy | Touch-based, mobile apps |
| wxPython | Native look and feel |

---

## 10. Quick Reference

### Widget Summary

| Widget | Purpose | Key Method |
|--------|---------|------------|
| Label | Display text/images | `.config(text=...)` |
| Button | Clickable button | `command=function` |
| Entry | Single-line input | `.get()` |
| Text | Multi-line input | `.get("1.0", END)` |
| Checkbutton | Multiple selections | `variable=IntVar()` |
| Radiobutton | Single selection | `variable=StringVar()` |
| Listbox | List of items | `.curselection()` |
| Spinbox | Numeric selector | `.get()` |
| Scale | Slider | `command=function` |
| Frame | Container | Groups widgets |
| Canvas | Drawing area | `.create_*()` |
| Menu | Menu bar | `.add_command()` |
| Combobox | Dropdown | `.get()` |

### Common Parameters

| Parameter | Description |
|-----------|-------------|
| `text` | Display text |
| `bg` | Background color |
| `fg` | Foreground/text color |
| `font` | Font tuple (family, size, style) |
| `width`, `height` | Widget dimensions |
| `padx`, `pady` | Padding |
| `command` | Function to call |
| `state` | "normal", "disabled" |
| `relief` | Border style |

### Event Bindings

| Event | Description |
|-------|-------------|
| `<Button-1>` | Left click |
| `<Button-3>` | Right click |
| `<Double-Button-1>` | Double click |
| `<B1-Motion>` | Drag with left button |
| `<Motion>` | Mouse movement |
| `<KeyPress>` | Any key press |
| `<Return>` | Enter key |
| `<Escape>` | Escape key |

### Canvas Methods

| Method | Purpose |
|--------|---------|
| `create_line()` | Draw lines |
| `create_rectangle()` | Draw rectangles |
| `create_oval()` | Draw ovals/circles |
| `create_polygon()` | Draw polygons |
| `create_arc()` | Draw arcs |
| `create_text()` | Add text |
| `create_image()` | Add images |
| `itemconfig()` | Modify item |
| `move()` | Move item (relative) |
| `coords()` | Get/set coordinates |
| `delete()` | Remove item |

---

## Coverage Checklist

- [x] Overview and basic structure
- [x] Widget configuration methods
- [x] Common widgets with examples
- [x] Layout managers (pack, grid, place)
- [x] Canvas drawing and animation
- [x] Event handling (mouse, keyboard)
- [x] MessageBox dialogs
- [x] Input methods and get()
- [x] Comparison with other tools
- [x] Quick reference tables
