# Complete HTML & CSS Guide for Beginners

> **Target Audience:** Complete beginners learning web development
> **Goal:** Master HTML and CSS fundamentals with clear examples

---

## Table of Contents

### HTML
1. [What is HTML?](#1-what-is-html)
2. [HTML Document Structure](#2-html-document-structure)
3. [Most Used HTML Tags](#3-most-used-html-tags)
4. [Void Elements (Self-Closing Tags)](#4-void-elements-self-closing-tags)
5. [Global Attributes](#5-global-attributes)

### CSS
6. [What is CSS?](#6-what-is-css)
7. [Three Ways to Add CSS](#7-three-ways-to-add-css)
8. [CSS Selectors](#8-css-selectors)
9. [CSS Specificity (Priority)](#9-css-specificity-priority)
10. [Font Sizes (px, em, rem, pt)](#10-font-sizes-px-em-rem-pt)
11. [The CSS Box Model](#11-the-css-box-model)
12. [Padding vs Border vs Margin](#12-padding-vs-border-vs-margin)
13. [Must-Know CSS Properties](#13-must-know-css-properties)
14. [Quick Reference](#14-quick-reference)

---

# HTML Section

---

## 1. What is HTML?

### Simple Explanation

HTML (HyperText Markup Language) is the **skeleton** of every website. It defines the **structure** and **content** of web pages.

```
Think of building a house:
- HTML = The structure (walls, rooms, doors)
- CSS = The decoration (paint, furniture, style)
- JavaScript = The functionality (lights, plumbing, electricity)

Without HTML → No website structure
Without CSS → Ugly but functional website
Without JS → Static but styled website
```

### What Does HTML Do?

```
HTML tells the browser:
- This is a heading
- This is a paragraph
- This is an image
- This is a link
- This is a list
- This is a table
- etc.

The browser reads HTML and displays content accordingly.
```

---

## 2. HTML Document Structure

### Basic HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Website</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>This is my first website.</p>
</body>
</html>
```

### Understanding Each Part

```
<!DOCTYPE html>
└── Tells browser: "This is HTML5"

<html lang="en">
└── Root element, lang="en" means English

<head>
├── Contains metadata (info about the page)
├── NOT visible on the page
└── Contains: title, styles, scripts, meta tags

<meta charset="UTF-8">
└── Character encoding (supports all languages)

<meta name="viewport" content="...">
└── Makes page responsive on mobile

<title>My First Website</title>
└── Shows in browser tab

<body>
└── Contains ALL visible content
```

### Visual Structure

```
┌─────────────────────────────────────┐
│ <!DOCTYPE html>                      │
│ ┌─────────────────────────────────┐ │
│ │ <html>                          │ │
│ │ ┌─────────────────────────────┐ │ │
│ │ │ <head>                      │ │ │
│ │ │   (invisible metadata)      │ │ │
│ │ └─────────────────────────────┘ │ │
│ │ ┌─────────────────────────────┐ │ │
│ │ │ <body>                      │ │ │
│ │ │   (visible content)         │ │ │
│ │ └─────────────────────────────┘ │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

---

## 3. Most Used HTML Tags

### 3.1 Headings (h1 - h6)

```html
<h1>Heading 1 - Largest (Main title)</h1>
<h2>Heading 2 - Section title</h2>
<h3>Heading 3 - Subsection</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6 - Smallest</h6>
```

**Output:**
```
Heading 1 - Largest (Main title)     ← Very big, bold
Heading 2 - Section title            ← Big, bold
Heading 3 - Subsection               ← Medium, bold
Heading 4                            ← Smaller, bold
Heading 5                            ← Even smaller
Heading 6 - Smallest                 ← Smallest heading
```

**Usage Rules:**
- Only ONE `<h1>` per page (main title)
- Use in order (don't skip from h1 to h4)
- Good for SEO (search engines read headings)

---

### 3.2 Paragraph and Text

```html
<!-- Paragraph -->
<p>This is a paragraph. It creates a block of text with space above and below.</p>

<!-- Line break (goes to next line) -->
<p>Line one<br>Line two<br>Line three</p>

<!-- Bold text -->
<p>This is <strong>very important</strong> text.</p>
<p>This is <b>bold</b> text.</p>

<!-- Italic text -->
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text.</p>

<!-- Underline -->
<p>This is <u>underlined</u> text.</p>

<!-- Strikethrough -->
<p>This is <s>deleted</s> text.</p>

<!-- Small text -->
<p>Normal text <small>small text</small></p>

<!-- Superscript and Subscript -->
<p>H<sub>2</sub>O (water)</p>
<p>x<sup>2</sup> (x squared)</p>
```

**Output:**
```
This is a paragraph.

Line one
Line two
Line three

This is very important text.     (bold)
This is emphasized text.         (italic)
This is underlined text.         (underlined)
This is deleted text.            (strikethrough)
H₂O (water)                      (subscript)
x² (x squared)                   (superscript)
```

---

### 3.3 Links (Anchor Tag)

```html
<!-- Basic link -->
<a href="https://google.com">Go to Google</a>

<!-- Open in new tab -->
<a href="https://google.com" target="_blank">Open Google in new tab</a>

<!-- Link to another page in your site -->
<a href="about.html">About Us</a>

<!-- Link to section on same page -->
<a href="#section2">Jump to Section 2</a>

<!-- Email link -->
<a href="mailto:example@email.com">Send Email</a>

<!-- Phone link -->
<a href="tel:+1234567890">Call Us</a>

<!-- Download link -->
<a href="file.pdf" download>Download PDF</a>
```

**Attributes Explained:**
| Attribute | Purpose | Example |
|-----------|---------|---------|
| `href` | URL to go to | `href="https://..."` |
| `target="_blank"` | Open in new tab | `target="_blank"` |
| `download` | Download instead of open | `download` |
| `title` | Tooltip on hover | `title="Click here"` |

---

### 3.4 Images

```html
<!-- Basic image -->
<img src="photo.jpg" alt="A beautiful photo">

<!-- With size -->
<img src="photo.jpg" alt="Photo" width="300" height="200">

<!-- Image from URL -->
<img src="https://example.com/image.jpg" alt="Online image">

<!-- Image as link -->
<a href="https://google.com">
    <img src="logo.png" alt="Click me">
</a>
```

**Important Attributes:**
| Attribute | Required? | Purpose |
|-----------|-----------|---------|
| `src` | YES | Path to image file |
| `alt` | YES | Description (for screen readers, SEO, if image fails) |
| `width` | No | Width in pixels |
| `height` | No | Height in pixels |

**Output Example:**
```
┌─────────────────┐
│                 │
│   [Image here]  │
│                 │
└─────────────────┘
If image fails: "A beautiful photo" text shows
```

---

### 3.5 Lists

```html
<!-- Unordered List (bullets) -->
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Orange</li>
</ul>

<!-- Ordered List (numbers) -->
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>

<!-- Nested List -->
<ul>
    <li>Fruits
        <ul>
            <li>Apple</li>
            <li>Banana</li>
        </ul>
    </li>
    <li>Vegetables
        <ul>
            <li>Carrot</li>
            <li>Broccoli</li>
        </ul>
    </li>
</ul>

<!-- Description List -->
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
</dl>
```

**Output:**
```
Unordered:          Ordered:           Nested:
• Apple             1. First step      • Fruits
• Banana            2. Second step       ◦ Apple
• Orange            3. Third step        ◦ Banana
                                       • Vegetables
                                         ◦ Carrot
```

---

### 3.6 Divisions and Spans

```html
<!-- DIV: Block-level container (takes full width) -->
<div>
    <h2>Section Title</h2>
    <p>This is a section of content.</p>
</div>

<div>
    <h2>Another Section</h2>
    <p>More content here.</p>
</div>

<!-- SPAN: Inline container (only wraps content) -->
<p>My favorite color is <span style="color: red;">red</span> and I love it!</p>
```

**DIV vs SPAN:**
| Feature | `<div>` | `<span>` |
|---------|---------|----------|
| Display | Block (new line) | Inline (same line) |
| Width | Full width | Content width only |
| Use for | Sections, containers | Styling part of text |

**Visual:**
```
<div> behavior:
┌──────────────────────────────┐
│ DIV 1 content                │
└──────────────────────────────┘
┌──────────────────────────────┐
│ DIV 2 content                │
└──────────────────────────────┘

<span> behavior:
Text before <span>styled part</span> text after
(all on same line)
```

---

### 3.7 Tables

```html
<table border="1">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>25</td>
            <td>New York</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>30</td>
            <td>London</td>
        </tr>
    </tbody>
</table>
```

**Output:**
```
┌──────────┬─────┬──────────┐
│ Name     │ Age │ City     │  ← Header (th)
├──────────┼─────┼──────────┤
│ John     │ 25  │ New York │  ← Data (td)
├──────────┼─────┼──────────┤
│ Jane     │ 30  │ London   │
└──────────┴─────┴──────────┘
```

**Table Tags:**
| Tag | Purpose |
|-----|---------|
| `<table>` | Container for table |
| `<thead>` | Header section |
| `<tbody>` | Body section |
| `<tr>` | Table row |
| `<th>` | Header cell (bold, centered) |
| `<td>` | Data cell |

---

### 3.8 Forms

```html
<form action="/submit" method="POST">
    <!-- Text input -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your name">
    <br><br>

    <!-- Email input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br><br>

    <!-- Password -->
    <label for="pass">Password:</label>
    <input type="password" id="pass" name="password">
    <br><br>

    <!-- Number -->
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="1" max="120">
    <br><br>

    <!-- Checkbox -->
    <input type="checkbox" id="agree" name="agree">
    <label for="agree">I agree to terms</label>
    <br><br>

    <!-- Radio buttons -->
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
    <br><br>

    <!-- Dropdown -->
    <label for="country">Country:</label>
    <select id="country" name="country">
        <option value="">Select...</option>
        <option value="us">USA</option>
        <option value="uk">UK</option>
        <option value="in">India</option>
    </select>
    <br><br>

    <!-- Textarea -->
    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="4" cols="50"></textarea>
    <br><br>

    <!-- Submit button -->
    <button type="submit">Submit</button>
</form>
```

**Input Types:**
| Type | Purpose | Example |
|------|---------|---------|
| `text` | Single line text | Name, username |
| `email` | Email (validates format) | Email address |
| `password` | Hidden text | Passwords |
| `number` | Numbers only | Age, quantity |
| `tel` | Phone number | Phone |
| `date` | Date picker | Birth date |
| `checkbox` | Multiple choices | Agree to terms |
| `radio` | Single choice | Gender |
| `file` | File upload | Documents |
| `submit` | Submit form | Submit button |

---

### 3.9 Semantic Tags (HTML5)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Semantic HTML</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main>
        <article>
            <h1>Article Title</h1>
            <p>Article content...</p>
        </article>

        <section>
            <h2>Section Title</h2>
            <p>Section content...</p>
        </section>

        <aside>
            <h3>Related Links</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2024 My Website</p>
    </footer>
</body>
</html>
```

**Semantic Tags Explained:**
| Tag | Purpose |
|-----|---------|
| `<header>` | Top section (logo, navigation) |
| `<nav>` | Navigation links |
| `<main>` | Main content area |
| `<article>` | Self-contained content (blog post) |
| `<section>` | Grouped content |
| `<aside>` | Sidebar content |
| `<footer>` | Bottom section (copyright, links) |

**Visual Layout:**
```
┌─────────────────────────────────────┐
│           <header>                   │
│    Logo    Home  About  Contact      │
├─────────────────────────────────────┤
│                          │          │
│        <main>            │ <aside>  │
│    ┌─────────────┐       │          │
│    │ <article>   │       │ Related  │
│    │ Blog post   │       │ Links    │
│    └─────────────┘       │          │
│    ┌─────────────┐       │          │
│    │ <section>   │       │          │
│    └─────────────┘       │          │
├─────────────────────────────────────┤
│           <footer>                   │
│        © 2024 My Website            │
└─────────────────────────────────────┘
```

---

## 4. Void Elements (Self-Closing Tags)

### What are Void Elements?

Void elements are HTML tags that **don't have closing tags** because they don't contain content.

```html
<!-- Regular elements (have opening AND closing tags) -->
<p>Content here</p>
<div>Content here</div>

<!-- Void elements (NO closing tag, NO content) -->
<br>
<hr>
<img src="photo.jpg" alt="Photo">
<input type="text">
```

### Complete List of Void Elements

| Tag | Purpose | Example |
|-----|---------|---------|
| `<br>` | Line break | `Text<br>New line` |
| `<hr>` | Horizontal line | `<hr>` |
| `<img>` | Image | `<img src="pic.jpg" alt="Picture">` |
| `<input>` | Form input | `<input type="text">` |
| `<meta>` | Metadata | `<meta charset="UTF-8">` |
| `<link>` | External resource | `<link rel="stylesheet" href="style.css">` |
| `<area>` | Image map area | `<area shape="rect" coords="...">` |
| `<base>` | Base URL | `<base href="https://...">` |
| `<col>` | Table column | `<col style="...">` |
| `<embed>` | Embed content | `<embed src="video.mp4">` |
| `<source>` | Media source | `<source src="audio.mp3">` |
| `<track>` | Text tracks | `<track src="subtitles.vtt">` |
| `<wbr>` | Word break opportunity | `supercali<wbr>fragilistic` |

### Examples with Output

```html
<!-- Line Break <br> -->
<p>
    Roses are red<br>
    Violets are blue<br>
    HTML is fun<br>
    CSS is too!
</p>

<!-- Output:
Roses are red
Violets are blue
HTML is fun
CSS is too!
-->


<!-- Horizontal Rule <hr> -->
<h2>Section 1</h2>
<p>Content of section 1...</p>
<hr>
<h2>Section 2</h2>
<p>Content of section 2...</p>

<!-- Output:
Section 1
Content of section 1...
────────────────────────  (horizontal line)
Section 2
Content of section 2...
-->


<!-- Image <img> -->
<img src="cat.jpg" alt="A cute cat" width="200">

<!-- Output: Shows the image, or "A cute cat" if image fails -->


<!-- Input <input> -->
<input type="text" placeholder="Enter name">
<input type="email" placeholder="Enter email">
<input type="submit" value="Submit">

<!-- Output: Text box, email box, and submit button -->


<!-- Meta <meta> - in <head>, not visible -->
<meta charset="UTF-8">
<meta name="description" content="My website description">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Self-Closing Syntax (Optional)

```html
<!-- Both are valid in HTML5 -->
<br>        <!-- Without slash -->
<br />      <!-- With slash (XHTML style) -->

<img src="photo.jpg" alt="Photo">      <!-- Without slash -->
<img src="photo.jpg" alt="Photo" />    <!-- With slash -->

<!-- Modern recommendation: Don't use the slash -->
<br>
<hr>
<img src="photo.jpg" alt="Photo">
```

---

## 5. Global Attributes

### What are Global Attributes?

Global attributes can be used on **ANY HTML element**. They work everywhere!

### Most Important Global Attributes

#### 5.1 `id` - Unique Identifier

```html
<!-- BEFORE (no id) -->
<h1>Welcome</h1>
<p>Content here...</p>

<!-- AFTER (with id) -->
<h1 id="main-title">Welcome</h1>
<p id="intro-text">Content here...</p>

<!-- Usage: -->
<!-- 1. CSS targeting -->
<style>
    #main-title { color: blue; }
</style>

<!-- 2. JavaScript access -->
<script>
    document.getElementById('main-title').innerText = 'Hello!';
</script>

<!-- 3. Link to section -->
<a href="#main-title">Go to title</a>
```

**Rules:**
- Must be UNIQUE (only one element with that id)
- No spaces allowed
- Start with letter, not number

---

#### 5.2 `class` - Reusable Styling

```html
<!-- BEFORE (no class) -->
<p>Normal paragraph</p>
<p>Another paragraph</p>
<p>Third paragraph</p>

<!-- AFTER (with class) -->
<p class="highlight">Highlighted paragraph</p>
<p class="highlight">Another highlighted</p>
<p>Normal paragraph</p>

<!-- CSS -->
<style>
    .highlight {
        background-color: yellow;
        font-weight: bold;
    }
</style>

<!-- Multiple classes -->
<p class="highlight large centered">Multiple classes!</p>
```

**Output:**
```
BEFORE:                     AFTER:
Normal paragraph            [Highlighted paragraph]  ← yellow background
Another paragraph           [Another highlighted]    ← yellow background
Third paragraph             Normal paragraph
```

---

#### 5.3 `style` - Inline CSS

```html
<!-- BEFORE -->
<p>Normal text</p>

<!-- AFTER (with style) -->
<p style="color: red; font-size: 20px;">Red, bigger text</p>
<p style="background-color: yellow; padding: 10px;">Yellow background</p>
```

**Output:**
```
Normal text                    ← default black, normal size
Red, bigger text               ← red color, larger
Yellow background              ← yellow highlight
```

---

#### 5.4 `title` - Tooltip

```html
<!-- BEFORE -->
<p>Hover over me</p>

<!-- AFTER (with title) -->
<p title="This is a tooltip!">Hover over me</p>
<a href="#" title="Click to learn more">Learn More</a>
<img src="photo.jpg" alt="Photo" title="Beautiful sunset photo">
```

**Output:**
```
When you hover mouse over element:
┌─────────────────────┐
│ This is a tooltip!  │  ← small popup appears
└─────────────────────┘
```

---

#### 5.5 `hidden` - Hide Element

```html
<!-- BEFORE (visible) -->
<p>This is visible</p>
<p>This is also visible</p>

<!-- AFTER (with hidden) -->
<p>This is visible</p>
<p hidden>This is hidden - won't show!</p>
<p>This is also visible</p>
```

**Output:**
```
BEFORE:                     AFTER:
This is visible             This is visible
This is also visible        This is also visible
                            (middle paragraph gone!)
```

---

#### 5.6 `data-*` - Custom Data

```html
<!-- Store custom data on elements -->
<div data-user-id="123" data-role="admin">
    User: John
</div>

<button data-action="delete" data-item-id="456">
    Delete
</button>

<!-- Access with JavaScript -->
<script>
    const div = document.querySelector('div');
    console.log(div.dataset.userId);  // "123"
    console.log(div.dataset.role);    // "admin"
</script>
```

---

#### 5.7 `tabindex` - Keyboard Navigation

```html
<!-- Control tab order -->
<input type="text" tabindex="1" placeholder="First (tab here first)">
<input type="text" tabindex="3" placeholder="Third">
<input type="text" tabindex="2" placeholder="Second">

<!-- tabindex="0" = normal tab order -->
<!-- tabindex="-1" = skip when tabbing -->
```

---

#### 5.8 `contenteditable` - Make Editable

```html
<!-- BEFORE -->
<p>You cannot edit this text.</p>

<!-- AFTER (with contenteditable) -->
<p contenteditable="true">Click and edit this text!</p>
<div contenteditable="true">
    <h3>Editable Title</h3>
    <p>Editable paragraph...</p>
</div>
```

**Output:**
```
Click on the text → cursor appears → you can type and edit!
```

---

#### 5.9 `draggable` - Drag and Drop

```html
<img src="photo.jpg" draggable="true" alt="Drag me!">
<p draggable="true">You can drag this paragraph!</p>
```

---

### Global Attributes Summary Table

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `id` | Unique identifier | `id="header"` |
| `class` | Reusable styling | `class="btn primary"` |
| `style` | Inline CSS | `style="color: red;"` |
| `title` | Tooltip on hover | `title="More info"` |
| `hidden` | Hide element | `hidden` |
| `data-*` | Custom data | `data-id="123"` |
| `tabindex` | Tab order | `tabindex="1"` |
| `contenteditable` | Make editable | `contenteditable="true"` |
| `draggable` | Enable dragging | `draggable="true"` |
| `lang` | Language | `lang="en"` |
| `dir` | Text direction | `dir="rtl"` |
| `spellcheck` | Spell checking | `spellcheck="true"` |

---

# CSS Section

---

## 6. What is CSS?

### Simple Explanation

CSS (Cascading Style Sheets) makes HTML look **beautiful**. It controls colors, fonts, layouts, spacing, and more.

```
HTML without CSS:          HTML with CSS:
┌─────────────────┐        ┌─────────────────────────┐
│ Plain text      │        │  Beautiful Website      │
│ No colors       │   →    │  Colors, fonts, layout  │
│ No layout       │        │  Responsive design      │
│ Ugly!           │        │  Professional!          │
└─────────────────┘        └─────────────────────────┘
```

### What CSS Controls

```
APPEARANCE:
- Colors (text, background)
- Fonts (size, family, weight)
- Borders, shadows

LAYOUT:
- Width, height
- Margins, padding
- Position
- Flexbox, Grid

EFFECTS:
- Animations
- Transitions
- Transforms
```

---

## 7. Three Ways to Add CSS

### 7.1 Inline CSS (Inside HTML Tag)

```html
<!-- CSS written directly in the style attribute -->
<p style="color: red; font-size: 20px;">This is red text.</p>
<h1 style="background-color: yellow;">Yellow background</h1>
```

**Pros:**
- Quick for single elements
- Highest priority

**Cons:**
- Hard to maintain
- Repeats code
- Mixes HTML and CSS

---

### 7.2 Internal CSS (In `<head>`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Internal CSS</title>
    <style>
        p {
            color: blue;
            font-size: 18px;
        }
        h1 {
            background-color: yellow;
        }
        .highlight {
            background-color: pink;
        }
    </style>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is blue text.</p>
    <p class="highlight">This has pink background.</p>
</body>
</html>
```

**Pros:**
- All CSS in one place
- Good for single-page sites

**Cons:**
- Only works for one HTML file
- Makes HTML file larger

---

### 7.3 External CSS (Separate File)

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>External CSS</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome</h1>
    <p>This is styled text.</p>
    <p class="highlight">Highlighted text.</p>
</body>
</html>
```

```css
/* styles.css */
p {
    color: blue;
    font-size: 18px;
}

h1 {
    background-color: yellow;
}

.highlight {
    background-color: pink;
}
```

**Pros:**
- One CSS file for multiple HTML pages
- Clean separation
- Browser caches CSS file (faster loading)
- **RECOMMENDED METHOD!**

**Cons:**
- Extra HTTP request (minor)

---

### Comparison Table

| Feature | Inline | Internal | External |
|---------|--------|----------|----------|
| Location | In HTML tag | In `<head>` | Separate .css file |
| Reusability | None | Same page only | Multiple pages |
| Maintenance | Hard | Medium | Easy |
| Priority | Highest | Medium | Lowest |
| Best for | Quick fixes | Single page | **Real projects** |

### Visual Example

```
INLINE:
<p style="color: red;">Text</p>
         ↓
    Applies ONLY to this <p>


INTERNAL:
<head>
    <style>
        p { color: red; }
    </style>
</head>
         ↓
    Applies to ALL <p> in this file


EXTERNAL:
<link href="styles.css">
         ↓
    Applies to ALL <p> in ALL files using this CSS
```

---

## 8. CSS Selectors

### 8.1 Element/Tag Selector

Selects ALL elements of that type.

```css
/* Selects ALL <p> elements */
p {
    color: blue;
}

/* Selects ALL <h1> elements */
h1 {
    font-size: 32px;
}
```

```html
<p>This is blue</p>
<p>This is also blue</p>
<h1>This is 32px</h1>
```

---

### 8.2 Class Selector (.)

Selects elements with specific class. **Can be reused!**

```css
/* Selects elements with class="highlight" */
.highlight {
    background-color: yellow;
}

.error {
    color: red;
    font-weight: bold;
}

.success {
    color: green;
}
```

```html
<p class="highlight">Yellow background</p>
<p class="error">Red error message</p>
<p class="success">Green success message</p>
<p>Normal paragraph</p>

<!-- Multiple classes -->
<p class="highlight error">Yellow background AND red text</p>
```

**Output:**
```
Yellow background          ← yellow background
Red error message          ← red, bold
Green success message      ← green
Normal paragraph           ← default
Yellow background AND...   ← yellow background + red + bold
```

---

### 8.3 ID Selector (#)

Selects ONE element with specific ID. **Must be unique!**

```css
/* Selects element with id="header" */
#header {
    background-color: navy;
    color: white;
}

#main-content {
    padding: 20px;
}

#footer {
    border-top: 1px solid black;
}
```

```html
<div id="header">Website Header</div>
<div id="main-content">Main content here</div>
<div id="footer">Footer content</div>
```

---

### 8.4 Attribute Selector

Selects elements based on attributes.

```css
/* Elements with href attribute */
[href] {
    color: blue;
}

/* Elements with specific attribute value */
[type="text"] {
    border: 1px solid gray;
}

/* Attribute starts with */
[href^="https"] {
    color: green;  /* Secure links */
}

/* Attribute ends with */
[href$=".pdf"] {
    color: red;  /* PDF links */
}

/* Attribute contains */
[href*="google"] {
    font-weight: bold;  /* Google links */
}
```

```html
<a href="https://google.com">Google (green, bold)</a>
<a href="http://example.com">Example (blue)</a>
<a href="document.pdf">Download PDF (red)</a>
<input type="text" placeholder="Text input (gray border)">
<input type="email" placeholder="Email input (no border)">
```

---

### 8.5 Descendant Selector (Space)

Selects elements INSIDE other elements.

```css
/* All <p> inside <div> */
div p {
    color: blue;
}

/* All <a> inside <nav> */
nav a {
    text-decoration: none;
}

/* All <li> inside <ul> inside <nav> */
nav ul li {
    display: inline;
}
```

```html
<div>
    <p>This is blue (inside div)</p>
</div>
<p>This is NOT blue (outside div)</p>

<nav>
    <ul>
        <li><a href="#">Link 1 (no underline)</a></li>
    </ul>
</nav>
<a href="#">This link HAS underline (outside nav)</a>
```

---

### 8.6 Child Selector (>)

Selects DIRECT children only.

```css
/* Direct children only */
div > p {
    color: red;
}
```

```html
<div>
    <p>RED (direct child)</p>
    <section>
        <p>NOT red (grandchild)</p>
    </section>
</div>
```

---

### 8.7 Pseudo-class Selectors

Select elements in specific STATES.

```css
/* Mouse hover */
a:hover {
    color: red;
    text-decoration: underline;
}

/* Link states */
a:link { color: blue; }      /* Unvisited */
a:visited { color: purple; } /* Visited */
a:active { color: red; }     /* Being clicked */

/* First/last child */
li:first-child {
    font-weight: bold;
}
li:last-child {
    color: gray;
}

/* Nth child */
tr:nth-child(even) {
    background-color: #f2f2f2;  /* Zebra stripes */
}

/* Focus (for forms) */
input:focus {
    border-color: blue;
    outline: none;
}

/* Disabled/enabled */
input:disabled {
    background-color: #eee;
}
```

---

### 8.8 Pseudo-element Selectors

Style PARTS of elements.

```css
/* First letter */
p::first-letter {
    font-size: 200%;
    color: red;
}

/* First line */
p::first-line {
    font-weight: bold;
}

/* Before element */
h1::before {
    content: "★ ";
    color: gold;
}

/* After element */
h1::after {
    content: " ★";
    color: gold;
}

/* Selection highlight */
::selection {
    background-color: yellow;
    color: black;
}
```

```html
<h1>Welcome</h1>
<!-- Displays: ★ Welcome ★ -->

<p>This is a paragraph with the first letter styled big and red.</p>
<!-- First "T" is 200% size and red -->
```

---

### Selector Summary

| Selector | Syntax | Example | Selects |
|----------|--------|---------|---------|
| Element | `tag` | `p { }` | All `<p>` |
| Class | `.class` | `.highlight { }` | `class="highlight"` |
| ID | `#id` | `#header { }` | `id="header"` |
| Attribute | `[attr]` | `[type="text"] { }` | `type="text"` |
| Descendant | `a b` | `div p { }` | `<p>` inside `<div>` |
| Child | `a > b` | `div > p { }` | Direct `<p>` child |
| Hover | `:hover` | `a:hover { }` | On mouse hover |
| First-child | `:first-child` | `li:first-child { }` | First `<li>` |

---

## 9. CSS Specificity (Priority)

### What is Specificity?

When multiple CSS rules target the same element, **specificity determines which wins**.

### The Specificity Hierarchy

```
PRIORITY (Highest to Lowest):

1. !important              (1000 points) - AVOID!
2. Inline styles           (1000 points)
3. ID selectors            (100 points)
4. Class/attribute/pseudo  (10 points)
5. Element/pseudo-element  (1 point)
6. Universal selector *    (0 points)

Higher points = Higher priority = Wins!
```

### Calculating Specificity

```css
/* Specificity: 0-0-1 (1 element) */
p { color: black; }

/* Specificity: 0-1-0 (1 class) */
.highlight { color: yellow; }

/* Specificity: 1-0-0 (1 id) */
#special { color: red; }

/* Specificity: 0-1-1 (1 class + 1 element) */
p.highlight { color: green; }

/* Specificity: 1-1-1 (1 id + 1 class + 1 element) */
#special.highlight p { color: blue; }
```

### Real Example

```html
<p id="intro" class="highlight" style="color: purple;">
    What color am I?
</p>
```

```css
p { color: black; }                    /* 0-0-1 = 1 point */
.highlight { color: yellow; }          /* 0-1-0 = 10 points */
#intro { color: red; }                 /* 1-0-0 = 100 points */
p.highlight { color: green; }          /* 0-1-1 = 11 points */
#intro.highlight { color: blue; }      /* 1-1-0 = 110 points */
```

**Result:** The text is **PURPLE** because inline style beats all!

```
Priority order for this element:
1. style="color: purple"    → INLINE (wins!)
2. #intro.highlight         → 110 points
3. #intro                   → 100 points
4. p.highlight              → 11 points
5. .highlight               → 10 points
6. p                        → 1 point
```

### !important (Use Sparingly!)

```css
p {
    color: red !important;  /* ALWAYS wins (unless another !important) */
}

#intro {
    color: blue;  /* Loses to !important even though higher specificity */
}
```

**WARNING:** Avoid `!important`! It makes CSS hard to maintain.

### Specificity Visual Guide

```
SPECIFICITY CALCULATION:
Format: (inline) - (IDs) - (classes) - (elements)

Example selectors:

p                    → 0-0-0-1  = 1
.class               → 0-0-1-0  = 10
#id                  → 0-1-0-0  = 100
style=""             → 1-0-0-0  = 1000

div p                → 0-0-0-2  = 2
div.class            → 0-0-1-1  = 11
#id .class p         → 0-1-1-1  = 111
#id1 #id2            → 0-2-0-0  = 200
```

### Specificity Rules Summary

| Rule | Example | Specificity |
|------|---------|-------------|
| Element | `p` | 0-0-0-1 |
| Class | `.box` | 0-0-1-0 |
| ID | `#header` | 0-1-0-0 |
| Inline | `style="..."` | 1-0-0-0 |
| !important | `color: red !important` | Highest |

---

## 10. Font Sizes (px, em, rem, pt)

### 10.1 Pixels (px) - Fixed Size

```css
/* Pixels = exact size, doesn't change */
h1 {
    font-size: 32px;  /* Always 32 pixels */
}

p {
    font-size: 16px;  /* Always 16 pixels */
}
```

**Pros:** Precise, consistent
**Cons:** Doesn't scale with user settings, not responsive

---

### 10.2 Points (pt) - Print Size

```css
/* Points = mainly for print */
p {
    font-size: 12pt;  /* 1pt = 1/72 inch */
}
```

**Pros:** Good for print stylesheets
**Cons:** Not recommended for web

---

### 10.3 Percentage (%) - Relative to Parent

```css
body {
    font-size: 16px;
}

p {
    font-size: 100%;  /* 100% of parent = 16px */
}

.large {
    font-size: 150%;  /* 150% of parent = 24px */
}

.small {
    font-size: 75%;   /* 75% of parent = 12px */
}
```

---

### 10.4 em - Relative to Parent (IMPORTANT!)

**em = Relative to the PARENT element's font size**

```css
body {
    font-size: 16px;  /* Base size */
}

p {
    font-size: 1em;   /* 1 × 16px = 16px */
}

h1 {
    font-size: 2em;   /* 2 × 16px = 32px */
}

small {
    font-size: 0.5em; /* 0.5 × 16px = 8px */
}
```

### The em Compounding Problem!

```css
/* PROBLEM: em compounds (multiplies) with nesting! */
.parent {
    font-size: 20px;
}

.parent .child {
    font-size: 0.8em;  /* 0.8 × 20px = 16px */
}

.parent .child .grandchild {
    font-size: 0.8em;  /* 0.8 × 16px = 12.8px (compounds!) */
}

.parent .child .grandchild .great-grandchild {
    font-size: 0.8em;  /* 0.8 × 12.8px = 10.24px (keeps shrinking!) */
}
```

```html
<div class="parent">
    Parent text (20px)
    <div class="child">
        Child text (16px)
        <div class="grandchild">
            Grandchild text (12.8px - SMALLER!)
            <div class="great-grandchild">
                Great-grandchild (10.24px - EVEN SMALLER!)
            </div>
        </div>
    </div>
</div>
```

**Output:**
```
Parent text (20px)           ← Normal
  Child text (16px)          ← Smaller
    Grandchild (12.8px)      ← Even smaller
      Great-grand (10.24px)  ← Tiny! (compounding problem)
```

---

### 10.5 rem - Relative to ROOT (RECOMMENDED!)

**rem = Relative to the ROOT (html) element's font size**

```css
html {
    font-size: 16px;  /* Root size - rem is based on THIS */
}

p {
    font-size: 1rem;   /* 1 × 16px = 16px */
}

h1 {
    font-size: 2rem;   /* 2 × 16px = 32px */
}

small {
    font-size: 0.75rem; /* 0.75 × 16px = 12px */
}
```

### rem Solves the Compounding Problem!

```css
html {
    font-size: 16px;
}

.parent {
    font-size: 1.25rem;  /* 1.25 × 16px = 20px */
}

.parent .child {
    font-size: 1rem;     /* 1 × 16px = 16px (NOT 20px!) */
}

.parent .child .grandchild {
    font-size: 1rem;     /* 1 × 16px = 16px (stays consistent!) */
}
```

**Output with rem:**
```
Parent text (20px)
  Child text (16px)
    Grandchild (16px)       ← Same as child!
      Great-grandchild (16px) ← Same! No compounding!
```

---

### em vs rem - Complete Comparison

```
em:  Relative to PARENT
rem: Relative to ROOT (html)

Example setup:
html { font-size: 16px; }
.parent { font-size: 20px; }

Inside .parent:
- font-size: 1em   → 20px (1 × parent)
- font-size: 1rem  → 16px (1 × root)

- font-size: 2em   → 40px (2 × parent)
- font-size: 2rem  → 32px (2 × root)
```

### Visual Comparison

```css
html { font-size: 16px; }

.container {
    font-size: 20px;
}

.using-em {
    font-size: 1.5em;   /* 1.5 × 20px = 30px */
    padding: 1em;       /* 1 × 30px = 30px (uses own font-size!) */
}

.using-rem {
    font-size: 1.5rem;  /* 1.5 × 16px = 24px */
    padding: 1rem;      /* 1 × 16px = 16px (always root) */
}
```

### When to Use Which?

| Unit | Use For | Example |
|------|---------|---------|
| `px` | Borders, shadows, precise | `border: 1px solid` |
| `rem` | Font sizes, spacing | `font-size: 1.2rem` |
| `em` | Component-relative sizing | `padding: 0.5em` (scales with font) |
| `%` | Widths, responsive | `width: 50%` |

### Best Practice

```css
/* Set root size */
html {
    font-size: 16px;  /* Or 62.5% for easy math: 10px */
}

/* Use rem for font sizes */
h1 { font-size: 2rem; }      /* 32px */
h2 { font-size: 1.5rem; }    /* 24px */
p { font-size: 1rem; }       /* 16px */

/* Use em for component spacing (scales with font) */
button {
    font-size: 1rem;
    padding: 0.5em 1em;  /* Scales if font-size changes */
}

/* Use px for things that shouldn't scale */
border: 1px solid black;
box-shadow: 0 2px 4px rgba(0,0,0,0.1);
```

---

## 11. The CSS Box Model

### What is the Box Model?

Every HTML element is a rectangular **BOX**. The box model defines how the box is structured.

```
┌─────────────────────────────────────────────────────┐
│                     MARGIN                          │
│   ┌─────────────────────────────────────────────┐   │
│   │               BORDER                        │   │
│   │   ┌─────────────────────────────────────┐   │   │
│   │   │           PADDING                   │   │   │
│   │   │   ┌─────────────────────────────┐   │   │   │
│   │   │   │                             │   │   │   │
│   │   │   │         CONTENT             │   │   │   │
│   │   │   │                             │   │   │   │
│   │   │   └─────────────────────────────┘   │   │   │
│   │   │                                     │   │   │
│   │   └─────────────────────────────────────┘   │   │
│   │                                             │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Box Model Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Content** | The actual content (text, image) | Your text goes here |
| **Padding** | Space INSIDE border (around content) | Like cushion inside a box |
| **Border** | The edge of the element | Like the box walls |
| **Margin** | Space OUTSIDE border (around element) | Distance from other boxes |

### Real-World Analogy

```
Think of a picture frame:

┌─────────────────────────────────┐
│         MARGIN                  │  ← Space between frames on wall
│   ┌─────────────────────────┐   │
│   │       BORDER            │   │  ← The frame itself
│   │   ┌─────────────────┐   │   │
│   │   │    PADDING      │   │   │  ← Mat board inside frame
│   │   │ ┌───────────┐   │   │   │
│   │   │ │  PICTURE  │   │   │   │  ← Content (actual image)
│   │   │ └───────────┘   │   │   │
│   │   └─────────────────┘   │   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```

### Box Model Example

```css
.box {
    /* Content size */
    width: 200px;
    height: 100px;

    /* Padding (inside) */
    padding: 20px;

    /* Border */
    border: 5px solid black;

    /* Margin (outside) */
    margin: 30px;

    background-color: lightblue;
}
```

```html
<div class="box">Content here</div>
```

### Calculating Total Size (Default)

```
By default (box-sizing: content-box):

Total Width = content + padding-left + padding-right + border-left + border-right
Total Width = 200px + 20px + 20px + 5px + 5px = 250px

Total Height = content + padding-top + padding-bottom + border-top + border-bottom
Total Height = 100px + 20px + 20px + 5px + 5px = 150px

+ Margin doesn't count in element size (it's OUTSIDE)
```

### box-sizing: border-box (RECOMMENDED!)

```css
/* The better way! */
* {
    box-sizing: border-box;
}

.box {
    width: 200px;    /* TOTAL width including padding and border */
    height: 100px;   /* TOTAL height including padding and border */
    padding: 20px;
    border: 5px solid black;
}

/*
With border-box:
Total Width = 200px (padding and border FIT INSIDE)
Content Width = 200px - 20px - 20px - 5px - 5px = 150px
*/
```

### Visual Comparison

```
content-box (default):          border-box (recommended):

width: 200px                    width: 200px
padding: 20px                   padding: 20px
border: 5px                     border: 5px

┌─────────────────────────┐     ┌───────────────────┐
│         250px           │     │       200px       │
│  ┌───────────────────┐  │     │  ┌─────────────┐  │
│  │      200px        │  │     │  │   150px     │  │
│  │    (content)      │  │     │  │  (content)  │  │
│  └───────────────────┘  │     │  └─────────────┘  │
└─────────────────────────┘     └───────────────────┘

Content = 200px                  Content = 150px
Total = 250px                    Total = 200px (what you set!)
```

### Setting Padding and Margin

```css
/* All sides same */
padding: 20px;

/* Vertical | Horizontal */
padding: 10px 20px;  /* top/bottom: 10px, left/right: 20px */

/* Top | Horizontal | Bottom */
padding: 10px 20px 30px;

/* Top | Right | Bottom | Left (clockwise!) */
padding: 10px 20px 30px 40px;

/* Individual sides */
padding-top: 10px;
padding-right: 20px;
padding-bottom: 30px;
padding-left: 40px;

/* Same patterns work for margin! */
margin: 20px;
margin: 10px 20px;
margin: 10px 20px 30px 40px;
margin-top: 10px;
```

### Auto Margin (Centering)

```css
/* Center a block element horizontally */
.centered {
    width: 300px;
    margin: 0 auto;  /* 0 top/bottom, auto left/right */
}

/* Or */
.centered {
    width: 300px;
    margin-left: auto;
    margin-right: auto;
}
```

---

## 12. Padding vs Border vs Margin

### Quick Comparison

```
PADDING:
- Space INSIDE the border
- BETWEEN content and border
- Has background color
- Clickable area includes padding

BORDER:
- THE EDGE of the element
- Has its own color and style
- Separates padding from margin

MARGIN:
- Space OUTSIDE the border
- BETWEEN this element and others
- Always TRANSPARENT (no background)
- Creates gaps between elements
```

### Visual Demonstration

```html
<style>
    .demo {
        background-color: lightblue;
        padding: 30px;
        border: 10px solid darkblue;
        margin: 20px;
    }
</style>

<div class="demo">Content</div>
```

**Output:**
```
                    ← 20px margin (transparent, no color)
┌──────────────────────────────────┐
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ ← 10px border (darkblue)
│░┌────────────────────────────┐░░│
│░│                            │░░│ ← 30px padding (lightblue, same as bg)
│░│                            │░░│
│░│         Content            │░░│ ← Content area
│░│                            │░░│
│░│                            │░░│
│░└────────────────────────────┘░░│
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
└──────────────────────────────────┘
                    ← 20px margin (transparent)
```

### When to Use What?

| Use | When |
|-----|------|
| **Padding** | Add space around content, enlarge clickable area, background should extend |
| **Border** | Visual edge, decorative lines, separators |
| **Margin** | Space between elements, push elements apart |

### Code Example

```html
<!DOCTYPE html>
<html>
<head>
<style>
    .card {
        width: 200px;
        background-color: #f0f0f0;

        /* Padding: space inside for content */
        padding: 20px;

        /* Border: visual edge */
        border: 2px solid #333;
        border-radius: 8px;

        /* Margin: space between cards */
        margin: 15px;
    }
</style>
</head>
<body>
    <div class="card">Card 1 content</div>
    <div class="card">Card 2 content</div>
</body>
</html>
```

**Output:**
```
┌─────────────────────────┐
│                         │ ← margin (15px gap from edge)
│  ┌───────────────────┐  │
│  │                   │  │
│  │   Card 1 content  │  │ ← content with 20px padding inside
│  │                   │  │
│  └───────────────────┘  │ ← border (2px solid)
│                         │
│  ← 15px margin gap →    │
│                         │
│  ┌───────────────────┐  │
│  │                   │  │
│  │   Card 2 content  │  │
│  │                   │  │
│  └───────────────────┘  │
│                         │
└─────────────────────────┘
```

---

## 13. Must-Know CSS Properties

### 13.1 Colors

```css
/* Text color */
color: red;
color: #ff0000;
color: rgb(255, 0, 0);
color: rgba(255, 0, 0, 0.5);  /* 50% transparent */

/* Background color */
background-color: blue;
background-color: #0000ff;
background-color: rgb(0, 0, 255);

/* Common color formats */
color: red;                    /* Named color */
color: #ff0000;                /* Hex (6 digits) */
color: #f00;                   /* Hex (3 digits shorthand) */
color: rgb(255, 0, 0);         /* RGB */
color: rgba(255, 0, 0, 0.5);   /* RGB with alpha (transparency) */
color: hsl(0, 100%, 50%);      /* HSL */
```

### 13.2 Text Properties

```css
/* Font family */
font-family: Arial, sans-serif;
font-family: 'Times New Roman', serif;
font-family: 'Courier New', monospace;

/* Font size */
font-size: 16px;
font-size: 1.2rem;
font-size: 1.5em;

/* Font weight */
font-weight: normal;  /* 400 */
font-weight: bold;    /* 700 */
font-weight: 100;     /* thin */
font-weight: 900;     /* extra bold */

/* Font style */
font-style: normal;
font-style: italic;

/* Text alignment */
text-align: left;
text-align: center;
text-align: right;
text-align: justify;

/* Text decoration */
text-decoration: none;         /* Remove underline from links */
text-decoration: underline;
text-decoration: line-through;
text-decoration: overline;

/* Text transform */
text-transform: uppercase;     /* ALL CAPS */
text-transform: lowercase;     /* all lowercase */
text-transform: capitalize;    /* First Letter Caps */

/* Line height */
line-height: 1.5;             /* 1.5x the font size */
line-height: 24px;

/* Letter spacing */
letter-spacing: 2px;

/* Word spacing */
word-spacing: 5px;
```

### 13.3 Background Properties

```css
/* Background color */
background-color: #f0f0f0;

/* Background image */
background-image: url('image.jpg');

/* Background repeat */
background-repeat: no-repeat;
background-repeat: repeat;
background-repeat: repeat-x;   /* Horizontal only */
background-repeat: repeat-y;   /* Vertical only */

/* Background position */
background-position: center;
background-position: top right;
background-position: 50% 50%;

/* Background size */
background-size: cover;        /* Fill entire element */
background-size: contain;      /* Fit inside element */
background-size: 100px 200px;

/* Shorthand */
background: #f0f0f0 url('bg.jpg') no-repeat center/cover;
```

### 13.4 Border Properties

```css
/* Border shorthand */
border: 1px solid black;

/* Individual properties */
border-width: 2px;
border-style: solid;   /* solid, dashed, dotted, double, none */
border-color: #333;

/* Individual sides */
border-top: 1px solid red;
border-right: 2px dashed blue;
border-bottom: 3px dotted green;
border-left: 4px double orange;

/* Border radius (rounded corners) */
border-radius: 5px;            /* All corners */
border-radius: 10px 20px;      /* top-left/bottom-right | top-right/bottom-left */
border-radius: 50%;            /* Circle (on square element) */
```

### 13.5 Width and Height

```css
/* Fixed size */
width: 200px;
height: 100px;

/* Relative size */
width: 50%;          /* 50% of parent */
width: 100vw;        /* 100% of viewport width */
height: 100vh;       /* 100% of viewport height */

/* Min/Max */
min-width: 200px;    /* At least 200px */
max-width: 800px;    /* At most 800px */
min-height: 100px;
max-height: 500px;

/* Common pattern for responsive images */
img {
    max-width: 100%;
    height: auto;
}
```

### 13.6 Display Property

```css
/* Block: takes full width, new line */
display: block;

/* Inline: only content width, same line */
display: inline;

/* Inline-block: inline but accepts width/height */
display: inline-block;

/* None: completely hidden */
display: none;

/* Flex: flexible layout */
display: flex;

/* Grid: grid layout */
display: grid;
```

### 13.7 Position Property

```css
/* Static: normal flow (default) */
position: static;

/* Relative: relative to normal position */
position: relative;
top: 10px;     /* Move down 10px from where it would be */
left: 20px;    /* Move right 20px */

/* Absolute: relative to positioned parent */
position: absolute;
top: 0;
right: 0;      /* Top-right corner of parent */

/* Fixed: relative to viewport (stays on scroll) */
position: fixed;
bottom: 20px;
right: 20px;   /* Floating button in corner */

/* Sticky: switches between relative and fixed */
position: sticky;
top: 0;        /* Sticks to top when scrolling */
```

### 13.8 Flexbox Basics

```css
/* Container */
.flex-container {
    display: flex;

    /* Direction */
    flex-direction: row;          /* Left to right (default) */
    flex-direction: column;       /* Top to bottom */

    /* Justify content (main axis) */
    justify-content: flex-start;   /* Start */
    justify-content: flex-end;     /* End */
    justify-content: center;       /* Center */
    justify-content: space-between; /* Even space between */
    justify-content: space-around;  /* Even space around */

    /* Align items (cross axis) */
    align-items: flex-start;
    align-items: flex-end;
    align-items: center;
    align-items: stretch;         /* Fill height */

    /* Wrap */
    flex-wrap: wrap;              /* Wrap to next line */
}

/* Items */
.flex-item {
    flex: 1;                      /* Grow to fill space */
    flex-grow: 1;                 /* Grow factor */
    flex-shrink: 0;               /* Don't shrink */
    flex-basis: 200px;            /* Initial size */
}
```

### 13.9 Common CSS Patterns

```css
/* Center anything with flexbox */
.center-everything {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Responsive image */
img {
    max-width: 100%;
    height: auto;
}

/* Reset margins/padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Card style */
.card {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    background: white;
}

/* Button style */
.button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
}

.button:hover {
    background-color: #0056b3;
}
```

---

## 14. Quick Reference

### HTML Tags Cheat Sheet

| Tag | Purpose |
|-----|---------|
| `<h1>` - `<h6>` | Headings |
| `<p>` | Paragraph |
| `<a>` | Link |
| `<img>` | Image |
| `<ul>`, `<ol>`, `<li>` | Lists |
| `<div>` | Block container |
| `<span>` | Inline container |
| `<table>`, `<tr>`, `<td>` | Tables |
| `<form>`, `<input>` | Forms |
| `<br>` | Line break |
| `<hr>` | Horizontal line |

### CSS Properties Cheat Sheet

| Property | Values |
|----------|--------|
| `color` | red, #ff0000, rgb() |
| `background` | color, image, gradient |
| `font-size` | px, em, rem, % |
| `font-weight` | normal, bold, 100-900 |
| `text-align` | left, center, right |
| `margin` | px, em, auto |
| `padding` | px, em |
| `border` | width style color |
| `display` | block, inline, flex |
| `position` | static, relative, absolute, fixed |
| `width/height` | px, %, vh/vw |

### Selectors Cheat Sheet

| Selector | Syntax | Specificity |
|----------|--------|-------------|
| Element | `p` | 0-0-1 |
| Class | `.class` | 0-1-0 |
| ID | `#id` | 1-0-0 |
| Descendant | `div p` | Sum |
| Child | `div > p` | Sum |
| Hover | `:hover` | 0-1-0 |

### Box Model Reminder

```
┌─────────────────────────────────┐
│            MARGIN               │
│   ┌─────────────────────────┐   │
│   │        BORDER           │   │
│   │   ┌─────────────────┐   │   │
│   │   │    PADDING      │   │   │
│   │   │ ┌───────────┐   │   │   │
│   │   │ │  CONTENT  │   │   │   │
│   │   │ └───────────┘   │   │   │
│   │   └─────────────────┘   │   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```

### Units Summary

| Unit | Type | Best For |
|------|------|----------|
| `px` | Fixed | Borders, shadows |
| `rem` | Relative to root | Font sizes |
| `em` | Relative to parent | Component spacing |
| `%` | Relative to parent | Widths |
| `vh/vw` | Viewport | Full-screen elements |

---

## Complete Starter Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <style>
        /* Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }

        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background: #333;
            color: white;
            padding: 1rem 0;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-right: 1rem;
        }

        nav a:hover {
            text-decoration: underline;
        }

        /* Main */
        main {
            padding: 2rem 0;
        }

        /* Footer */
        footer {
            background: #333;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <h1>Welcome to My Website</h1>
            <p>This is a starter template with HTML and CSS.</p>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 My Website. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

---

You now have a complete understanding of HTML and CSS basics! Practice by building small projects.
