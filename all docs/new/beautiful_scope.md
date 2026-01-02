# BeautifulSoup4 (bs4) - Complete Python Documentation

---

## 1. Overview

### What is BeautifulSoup4?

BeautifulSoup4 (bs4) is a Python library for **parsing HTML and XML documents** and extracting data from them. It creates a parse tree from page source code that can be used to navigate, search, and extract data in a hierarchical and readable manner.

**Key Strengths:**
- Simple, Pythonic interface
- Handles malformed HTML gracefully
- Multiple parser backends for flexibility
- Fast for static HTML content

### Main Purpose and Use Cases

- **Web Scraping**: Extract data from static websites
- **HTML/XML Parsing**: Navigate and search through document structure
- **Data Extraction**: Pull specific information from web pages
- **Web Content Analysis**: Analyze structure and content
- **HTML Cleaning**: Fix or modify HTML documents

### When to Use BeautifulSoup vs Alternatives

| Tool | Use When | Speed | JavaScript | Learning Curve |
|------|----------|-------|------------|----------------|
| **BeautifulSoup** | Static HTML, simple scraping | Fast | No | Easy |
| **Selenium** | Dynamic JS sites, interaction | Slow | Yes | Medium |
| **Scrapy** | Large-scale crawling | Very Fast | No | Hard |
| **lxml** | Maximum speed needed | Fastest | No | Medium |
| **Requests-HTML** | Modern API, some JS | Fast | Limited | Easy |

**Use BeautifulSoup when:**
- Scraping static HTML pages
- Need simple, readable syntax
- Working with poorly formatted HTML
- Quick one-time scraping tasks
- Learning web scraping

**Consider Alternatives when:**
- **Selenium**: JavaScript-heavy sites (SPAs, React, Angular)
- **Scrapy**: Large-scale production scraping
- **lxml directly**: Need maximum parsing speed
- **APIs**: When website offers official API (always prefer this!)

### Installation

```bash
# Install BeautifulSoup
pip install beautifulsoup4

# Install recommended parser (REQUIRED for best results)
pip install lxml

# Install alternative parser (most lenient)
pip install html5lib

# Install requests for fetching web pages
pip install requests
```

**Verify Installation:**
```python
from bs4 import BeautifulSoup
import requests

# Test parsing
html = '<h1>Hello World</h1>'
soup = BeautifulSoup(html, 'lxml')
print(soup.h1.text)
# Output: Hello World
```

---

## 2. Core Components Overview

### Main Components

| Component | Description | Example |
|-----------|-------------|---------|
| **BeautifulSoup** | Main parsed document object | `soup = BeautifulSoup(html, 'lxml')` |
| **Tag** | HTML/XML tag element | `<div>`, `<p>`, `<a>` |
| **NavigableString** | Text content inside tags | `"Hello World"` |
| **Comment** | HTML comments | `<!-- comment -->` |
| **ResultSet** | List of found elements | `soup.find_all('p')` |

### How They Relate

```
HTML String → BeautifulSoup (parse) → Tag Objects → NavigableString/Attributes
                                          ↓
                                      ResultSet (from find_all)
```

### Parser Comparison

```python
from bs4 import BeautifulSoup

html = '<html><body><p>Test</p></body></html>'

# lxml - FASTEST and RECOMMENDED
soup = BeautifulSoup(html, 'lxml')

# html.parser - Built-in, no external dependency
soup = BeautifulSoup(html, 'html.parser')

# html5lib - Most lenient, handles worst HTML
soup = BeautifulSoup(html, 'html5lib')

# lxml-xml - For XML documents only
soup = BeautifulSoup(xml_content, 'lxml-xml')
```

| Parser | Speed | External Dep | Leniency |
|--------|-------|--------------|----------|
| lxml | Fastest | Yes | Good |
| html.parser | Medium | No | Medium |
| html5lib | Slowest | Yes | Best |

**Recommendation:** Always use `lxml` unless you have a specific reason not to.

### Most Common Workflow

```python
import requests
from bs4 import BeautifulSoup

# 1. Fetch HTML content
response = requests.get('https://example.com')
html_content = response.content  # Use .content for proper encoding

# 2. Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

# 3. Find elements
elements = soup.find_all('div', class_='product')

# 4. Extract data
for element in elements:
    title = element.find('h2').text
    price = element.find('span', class_='price').text
    print(f"{title}: {price}")

# 5. (Optional) Save data
import json
with open('data.json', 'w') as f:
    json.dump(data, f)
```

---

## 3. Fundamentals (Logical Sequence)

### Step 1: Creating a BeautifulSoup Object

#### From String

```python
from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>My Page</title></head>
    <body>
        <h1>Welcome</h1>
        <p class="intro">This is a paragraph</p>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
print(soup.title.text)
# Output: My Page
```

#### From Web Request (MOST COMMON)

```python
import requests
from bs4 import BeautifulSoup

# Basic request
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')  # Use .content not .text

# With headers (recommended to avoid blocking)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.content, 'lxml')

print(soup.title.text)
# Output: Example Domain
```

#### From File

```python
from bs4 import BeautifulSoup

# Using context manager (recommended)
with open('page.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

print(soup.prettify()[:100])  # Print formatted HTML
```

---

### Step 2: Finding Elements

#### find() - Get First Match

```python
from bs4 import BeautifulSoup

html = '''
<div>
    <p class="intro">First paragraph</p>
    <p class="content">Second paragraph</p>
    <p class="content">Third paragraph</p>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# Find by tag name
first_p = soup.find('p')
print(first_p.text)
# Output: First paragraph

# Find by class (note: class_ with underscore)
intro = soup.find('p', class_='intro')
print(intro.text)
# Output: First paragraph

# Find by id
# html: <div id="main">Content</div>
# main_div = soup.find(id='main')

# Find by attributes dict
element = soup.find('p', attrs={'class': 'intro'})
print(element.text)
# Output: First paragraph

# Returns None if not found (doesn't raise exception)
missing = soup.find('span')
print(missing)
# Output: None
```

#### find_all() - Get All Matches

```python
from bs4 import BeautifulSoup

html = '''
<ul>
    <li class="item">Apple</li>
    <li class="item">Banana</li>
    <li class="item special">Cherry</li>
    <li class="item">Date</li>
</ul>
'''
soup = BeautifulSoup(html, 'lxml')

# Find all by tag
all_items = soup.find_all('li')
print(f"Found {len(all_items)} items")
# Output: Found 4 items

for item in all_items:
    print(item.text)
# Output:
# Apple
# Banana
# Cherry
# Date

# Find all by class
special = soup.find_all('li', class_='special')
print(special[0].text)
# Output: Cherry

# Limit results
first_two = soup.find_all('li', limit=2)
print(len(first_two))
# Output: 2

# Find multiple tag types
headings = soup.find_all(['h1', 'h2', 'h3'])

# Returns empty list if none found (doesn't raise exception)
spans = soup.find_all('span')
print(spans)
# Output: []
```

---

### Step 3: CSS Selectors (POWERFUL)

CSS selectors provide a more familiar and powerful way to find elements.

#### Basic CSS Selectors

```python
from bs4 import BeautifulSoup

html = '''
<div id="container" class="main-content">
    <h1 class="title">Welcome</h1>
    <p class="intro highlight">First paragraph</p>
    <div class="products">
        <div class="product" data-id="123">
            <h3>Laptop</h3>
            <span class="price">$999</span>
        </div>
        <div class="product featured" data-id="456">
            <h3>Phone</h3>
            <span class="price">$699</span>
        </div>
    </div>
    <a href="/about" class="link">About</a>
    <a href="https://external.com" class="link external">External</a>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# By ID (#)
container = soup.select_one('#container')
print(container.name)
# Output: div

# By Class (.)
title = soup.select_one('.title')
print(title.text)
# Output: Welcome

# Multiple classes (AND)
intro = soup.select_one('.intro.highlight')
print(intro.text)
# Output: First paragraph

# By Tag
h1 = soup.select_one('h1')
print(h1.text)
# Output: Welcome

# By Attribute
product = soup.select_one('[data-id="123"]')
print(product.find('h3').text)
# Output: Laptop

# Attribute contains (*)
links = soup.select('a[href*="external"]')
print(len(links))
# Output: 1

# Attribute starts with (^)
external_links = soup.select('a[href^="https"]')
print(external_links[0].text)
# Output: External

# Attribute ends with ($)
# soup.select('a[href$=".pdf"]')  # Links ending with .pdf
```

#### Hierarchical CSS Selectors

```python
from bs4 import BeautifulSoup

html = '''
<div class="container">
    <div class="products">
        <div class="product">
            <h3>Product 1</h3>
            <span class="price">$100</span>
        </div>
        <div class="product">
            <h3>Product 2</h3>
            <span class="price">$200</span>
        </div>
    </div>
    <div class="sidebar">
        <span class="price">Ad Price</span>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# Descendant selector (space) - any level nested
all_prices = soup.select('div.container span.price')
print(f"All prices: {len(all_prices)}")
# Output: All prices: 3

# Direct child (>)
product_prices = soup.select('div.products > div.product > span.price')
print(f"Product prices only: {len(product_prices)}")
# Output: Product prices only: 2

for price in product_prices:
    print(price.text)
# Output:
# $100
# $200

# Adjacent sibling (+)
# Finds element immediately after
titles_with_price = soup.select('h3 + span.price')
print(f"Prices after titles: {len(titles_with_price)}")
# Output: Prices after titles: 2

# General sibling (~)
# Finds any sibling after
```

#### Pseudo-selectors

```python
from bs4 import BeautifulSoup

html = '''
<ul>
    <li>First</li>
    <li>Second</li>
    <li>Third</li>
    <li>Fourth</li>
</ul>
'''
soup = BeautifulSoup(html, 'lxml')

# First child
first = soup.select_one('li:first-child')
print(first.text)
# Output: First

# Last child
last = soup.select_one('li:last-child')
print(last.text)
# Output: Fourth

# Nth child (1-indexed)
second = soup.select_one('li:nth-child(2)')
print(second.text)
# Output: Second

# Nth from end
third_from_end = soup.select_one('li:nth-last-child(2)')
print(third_from_end.text)
# Output: Third

# Not selector
not_first = soup.select('li:not(:first-child)')
print(f"Not first: {len(not_first)} items")
# Output: Not first: 3 items
```

#### select() vs select_one()

```python
# select() - returns list of all matches
all_products = soup.select('div.product')
print(type(all_products))  # <class 'list'>

# select_one() - returns first match or None
first_product = soup.select_one('div.product')
print(type(first_product))  # <class 'bs4.element.Tag'>
```

---

### Step 4: Extracting Data

#### Getting Text Content

```python
from bs4 import BeautifulSoup

html = '''
<div class="article">
    <h1>   Article Title   </h1>
    <p>First paragraph with <strong>bold text</strong>.</p>
    <p>Second paragraph.</p>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# .text - Get all text (includes whitespace)
article = soup.find('div', class_='article')
print(repr(article.text))
# Output: '\n   Article Title   \nFirst paragraph with bold text.\nSecond paragraph.\n'

# .get_text() with strip - Clean text
clean_text = article.get_text(strip=True)
print(clean_text)
# Output: Article TitleFirst paragraph with bold text.Second paragraph.

# .get_text() with separator
text_with_sep = article.get_text(separator=' ', strip=True)
print(text_with_sep)
# Output: Article Title First paragraph with bold text. Second paragraph.

# For single tag
h1 = soup.find('h1')
title = h1.get_text(strip=True)
print(title)
# Output: Article Title

# .string - Only works for single text content (no nested tags)
simple_html = '<p>Just text</p>'
simple_soup = BeautifulSoup(simple_html, 'lxml')
print(simple_soup.p.string)
# Output: Just text

# Returns None for nested tags
print(soup.find('p').string)
# Output: None (because it has <strong> nested)
```

#### Getting Attributes

```python
from bs4 import BeautifulSoup

html = '''
<a href="https://example.com" class="link external" id="main-link" data-id="123">
    Click Here
</a>
<img src="image.jpg" alt="Description" width="300">
'''
soup = BeautifulSoup(html, 'lxml')

link = soup.find('a')

# Dictionary-style access (may raise KeyError)
href = link['href']
print(href)
# Output: https://example.com

# Safe access with .get() (returns None or default if missing)
href = link.get('href')
print(href)
# Output: https://example.com

target = link.get('target', '_self')  # Default value
print(target)
# Output: _self

# Get all attributes as dictionary
print(link.attrs)
# Output: {'href': 'https://example.com', 'class': ['link', 'external'], 'id': 'main-link', 'data-id': '123'}

# Note: class is always a list
classes = link['class']
print(classes)
# Output: ['link', 'external']

# Check if attribute exists
has_id = 'id' in link.attrs
print(has_id)
# Output: True

# Image attributes
img = soup.find('img')
print(f"Source: {img['src']}")
print(f"Alt: {img.get('alt', 'No alt text')}")
print(f"Width: {img.get('width', 'Not specified')}")
# Output:
# Source: image.jpg
# Alt: Description
# Width: 300
```

---

### Step 5: Navigating the DOM Tree

#### Parent Navigation

```python
from bs4 import BeautifulSoup

html = '''
<div class="container">
    <div class="product">
        <h3>Product Name</h3>
        <span class="price">$99</span>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# Find price and navigate to parent
price = soup.find('span', class_='price')

# .parent - immediate parent
parent = price.parent
print(parent.name)
# Output: div

print(parent['class'])
# Output: ['product']

# .parents - all ancestors (generator)
for ancestor in price.parents:
    if ancestor.name:
        print(ancestor.name)
# Output:
# div
# div
# body
# html
# [document]

# find_parent() - find specific parent
product_div = price.find_parent('div', class_='product')
print(product_div.find('h3').text)
# Output: Product Name
```

#### Child Navigation

```python
from bs4 import BeautifulSoup

html = '''
<div id="parent">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

parent = soup.find('div', id='parent')

# .children - direct children only (generator)
print("Direct children:")
for child in parent.children:
    if child.name:  # Skip text nodes (whitespace)
        print(f"  {child.name}")
# Output:
# Direct children:
#   h1
#   p
#   p
#   ul

# .descendants - ALL nested elements (generator)
print("\nAll descendants:")
for desc in parent.descendants:
    if desc.name:
        print(f"  {desc.name}")
# Output:
# All descendants:
#   h1
#   p
#   p
#   ul
#   li
#   li

# .contents - direct children as list
children_list = parent.contents
print(f"\nNumber of children (including text): {len(children_list)}")
```

#### Sibling Navigation

```python
from bs4 import BeautifulSoup

html = '''
<div>
    <h1>Title</h1>
    <p class="first">First</p>
    <p class="second">Second</p>
    <p class="third">Third</p>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

first_p = soup.find('p', class_='first')

# find_next_sibling() - RECOMMENDED (skips text nodes)
next_p = first_p.find_next_sibling('p')
print(next_p.text)
# Output: Second

# find_previous_sibling()
prev = next_p.find_previous_sibling('p')
print(prev.text)
# Output: First

# find_all_next_siblings()
all_next = first_p.find_next_siblings('p')
print(f"Found {len(all_next)} siblings after")
# Output: Found 2 siblings after

# .next_sibling - may return whitespace (less reliable)
raw_next = first_p.next_sibling
print(repr(raw_next))
# Output: '\n    ' (whitespace text node)

# To get actual element
raw_next = first_p.next_sibling.next_sibling
print(raw_next.text if raw_next else "None")
# Output: Second
```

---

## 4. Functions/Methods Documentation

### Finding Methods

#### find()

**Purpose:** Find the first element matching criteria

**Syntax:**
```python
element = soup.find(name, attrs, recursive, string, **kwargs)
```

**Key Parameters:**
- `name` (str/list/re): Tag name(s) to search - **Optional**
- `attrs` (dict): Attributes to match - **Optional**
- `class_` (str): CSS class - **Optional** (underscore required!)
- `id` (str): ID attribute - **Optional**
- `string` (str/re): Match text content - **Optional**
- `recursive` (bool): Search descendants (default: True) - **Optional**

**Returns:** Tag object or `None`

**Examples:**
```python
from bs4 import BeautifulSoup

html = '''
<div class="container">
    <h1 id="title">Welcome</h1>
    <p class="intro text-large">Hello World</p>
    <a href="/about">About</a>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# By tag name
h1 = soup.find('h1')
print(h1.text)  # Welcome

# By class (note underscore)
intro = soup.find('p', class_='intro')
print(intro.text)  # Hello World

# By ID
title = soup.find(id='title')
print(title.text)  # Welcome

# By attribute
link = soup.find('a', href='/about')
print(link.text)  # About

# By attrs dict
element = soup.find(attrs={'class': 'intro'})

# Multiple conditions
element = soup.find('p', class_='intro', id='some-id')
```

**When to Use:** When you need exactly one element (first match)

---

#### find_all()

**Purpose:** Find all elements matching criteria

**Syntax:**
```python
elements = soup.find_all(name, attrs, recursive, string, limit, **kwargs)
```

**Key Parameters:**
- `name` (str/list/re): Tag name(s) - **Optional**
- `attrs` (dict): Attributes - **Optional**
- `class_` (str): CSS class - **Optional**
- `limit` (int): Max results - **Optional**
- `recursive` (bool): Search depth - **Optional** (default: True)

**Returns:** ResultSet (list-like) - empty list if no matches

**Examples:**
```python
from bs4 import BeautifulSoup

html = '''
<ul>
    <li class="item">Apple</li>
    <li class="item">Banana</li>
    <li class="item featured">Cherry</li>
</ul>
'''
soup = BeautifulSoup(html, 'lxml')

# Find all by tag
items = soup.find_all('li')
print(f"Found {len(items)} items")  # Found 3 items

# Iterate results
for item in items:
    print(item.text)

# Limit results
first_two = soup.find_all('li', limit=2)

# Find multiple tags
headings = soup.find_all(['h1', 'h2', 'h3'])

# With class
featured = soup.find_all('li', class_='featured')
```

**When to Use:** When you need multiple elements

---

#### select() / select_one()

**Purpose:** Find elements using CSS selectors

**Syntax:**
```python
elements = soup.select(css_selector)
element = soup.select_one(css_selector)
```

**Key Parameters:**
- `css_selector` (str): CSS selector string - **REQUIRED**

**Returns:**
- `select()`: List of Tag objects
- `select_one()`: Single Tag or None

**Examples:**
```python
from bs4 import BeautifulSoup

html = '''
<div id="content">
    <div class="product featured">
        <h3>Product 1</h3>
        <span class="price">$100</span>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

# By ID
content = soup.select_one('#content')

# By class
products = soup.select('.product')

# Nested selection
price = soup.select_one('#content .product.featured .price')
print(price.text)  # $100

# Multiple selectors (OR)
elements = soup.select('h1, h2, h3')
```

**When to Use:** Complex queries, familiar with CSS selectors

---

### Data Extraction Methods

#### .text / .get_text()

**Purpose:** Extract text content from elements

**Syntax:**
```python
text = element.text
text = element.get_text(separator='', strip=False)
```

**Key Parameters (get_text):**
- `separator` (str): Insert between text pieces - **Optional**
- `strip` (bool): Remove whitespace - **Optional**

**Examples:**
```python
from bs4 import BeautifulSoup

html = '<div>  Hello  <span>World</span>  </div>'
soup = BeautifulSoup(html, 'lxml')

div = soup.find('div')

# .text - simple extraction
print(repr(div.text))
# Output: '  Hello  World  '

# get_text with strip
print(div.get_text(strip=True))
# Output: 'HelloWorld'

# get_text with separator
print(div.get_text(separator=' ', strip=True))
# Output: 'Hello World'
```

---

#### .get() / ['attr']

**Purpose:** Get attribute values

**Syntax:**
```python
value = element['attribute']  # Raises KeyError if missing
value = element.get('attribute', default)  # Safe access
```

**Examples:**
```python
link = soup.find('a')

# Dictionary access (may raise error)
href = link['href']

# Safe access (recommended)
href = link.get('href', '#')
target = link.get('target', '_self')

# Get all attributes
all_attrs = link.attrs
```

---

### Navigation Methods

| Method | Returns | Use When |
|--------|---------|----------|
| `.parent` | Parent Tag | Navigate up one level |
| `.parents` | Generator of ancestors | Navigate up tree |
| `.children` | Generator of direct children | Process immediate children |
| `.descendants` | Generator of all nested | Process all nested elements |
| `.find_next_sibling()` | Next sibling Tag | Navigate to next element |
| `.find_previous_sibling()` | Previous sibling Tag | Navigate to previous element |
| `.find_parent()` | Ancestor Tag matching criteria | Find specific parent |

---

## 5. Exception Handling

### The Problem with Unhandled find()

```python
from bs4 import BeautifulSoup

html = '<div><span>No paragraph here</span></div>'
soup = BeautifulSoup(html, 'lxml')

# DANGEROUS: Crashes if element not found
paragraph = soup.find('p').text  # AttributeError: 'NoneType' has no attribute 'text'
```

### Safe Pattern for find()

```python
from bs4 import BeautifulSoup

html = '<div><span>No paragraph here</span></div>'
soup = BeautifulSoup(html, 'lxml')

# Pattern 1: Check before accessing
paragraph = soup.find('p')
if paragraph:
    text = paragraph.text
else:
    text = "Not found"
print(text)
# Output: Not found

# Pattern 2: One-liner with conditional
text = soup.find('p').text if soup.find('p') else "Not found"

# Pattern 3: Assign and check
if (p := soup.find('p')):  # Walrus operator (Python 3.8+)
    text = p.text
else:
    text = "Not found"
```

### Safe Attribute Access

```python
from bs4 import BeautifulSoup

html = '<a class="link">No href attribute</a>'
soup = BeautifulSoup(html, 'lxml')

link = soup.find('a')

# DANGEROUS: May raise KeyError
# href = link['href']

# SAFE: Use .get() with default
href = link.get('href', '#')
print(href)
# Output: #

# SAFE: Check first
if 'href' in link.attrs:
    href = link['href']
else:
    href = '#'
```

### Complete Error Handling for Web Scraping

```python
import requests
from bs4 import BeautifulSoup
import time

def safe_scrape(url, max_retries=3):
    """Scrape a URL with comprehensive error handling"""

    for attempt in range(max_retries):
        try:
            # Add headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            # Make request with timeout
            response = requests.get(url, headers=headers, timeout=10)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.content, 'lxml')

            return soup

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            time.sleep(2)

        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            if response.status_code == 404:
                return None  # Page not found
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(2)

    print("Max retries reached")
    return None

def extract_data(soup, selector):
    """Safely extract data from soup"""
    if soup is None:
        return None

    element = soup.select_one(selector)
    return element.get_text(strip=True) if element else None

# Usage
soup = safe_scrape('https://example.com')
if soup:
    title = extract_data(soup, 'h1')
    print(f"Title: {title or 'Not found'}")
```

---

## 6. Best Practices

### 1. Always Specify a Parser

```python
# Good - Explicit parser
soup = BeautifulSoup(html, 'lxml')

# Bad - No parser (warning + inconsistent behavior)
soup = BeautifulSoup(html)
```

### 2. Use .content Not .text for Requests

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(url)

# Good - Let BS4 handle encoding
soup = BeautifulSoup(response.content, 'lxml')

# Can have encoding issues
soup = BeautifulSoup(response.text, 'lxml')
```

### 3. Use .get() for Safe Attribute Access

```python
# Good - Safe access
href = link.get('href', '#')

# Risky - May raise KeyError
href = link['href']
```

### 4. Check Elements Before Accessing

```python
# Good
element = soup.find('p')
text = element.text if element else "Not found"

# Bad - Crashes if element is None
text = soup.find('p').text
```

### 5. Use get_text(strip=True) for Clean Text

```python
# Good - Clean text
text = element.get_text(strip=True)

# Contains whitespace
text = element.text
```

### 6. Limit Search Scope

```python
# Good - Search within container
container = soup.find('div', id='products')
items = container.find_all('div', class_='product')

# Less efficient - Searches entire document
items = soup.find_all('div', class_='product')
```

### 7. Add Delays When Scraping Multiple Pages

```python
import time

for url in urls:
    soup = safe_scrape(url)
    # Process...
    time.sleep(1)  # Be respectful
```

### 8. Use User-Agent Headers

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
```

---

## 7. Common Mistakes

### Mistake 1: Not Handling None from find()

**Wrong:**
```python
text = soup.find('p').text  # Crashes if no <p> exists
```

**Correct:**
```python
p = soup.find('p')
text = p.text if p else "Not found"
```

---

### Mistake 2: Using class Instead of class_

**Wrong:**
```python
element = soup.find('div', class='container')  # SyntaxError!
```

**Correct:**
```python
element = soup.find('div', class_='container')  # Use underscore
# Or
element = soup.find('div', attrs={'class': 'container'})
```

---

### Mistake 3: Using .string for Nested Tags

**Wrong:**
```python
html = '<p>Text with <strong>bold</strong></p>'
soup = BeautifulSoup(html, 'lxml')
print(soup.p.string)  # Returns None!
```

**Correct:**
```python
print(soup.p.text)  # "Text with bold"
print(soup.p.get_text())  # "Text with bold"
```

---

### Mistake 4: Forgetting Whitespace in Siblings

**Wrong:**
```python
first_p = soup.find('p')
next_p = first_p.next_sibling  # Often returns whitespace '\n'
```

**Correct:**
```python
first_p = soup.find('p')
next_p = first_p.find_next_sibling('p')  # Skips whitespace
```

---

### Mistake 5: Using .text Instead of .content for Requests

**Wrong (may have encoding issues):**
```python
soup = BeautifulSoup(response.text, 'lxml')
```

**Correct:**
```python
soup = BeautifulSoup(response.content, 'lxml')
```

---

### Mistake 6: Searching from Root Every Time

**Wrong - Inefficient:**
```python
title = soup.find('div', id='product').find('h2').text
price = soup.find('div', id='product').find('span', class_='price').text
```

**Correct - Reuse parent:**
```python
product = soup.find('div', id='product')
title = product.find('h2').text
price = product.find('span', class_='price').text
```

---

## 8. Commonly Confused Concepts

### find() vs find_all()

| | find() | find_all() |
|--|--------|------------|
| Returns | First match or None | List of all matches (can be empty) |
| Error on no match | No (returns None) | No (returns []) |
| Use when | Need single element | Need multiple elements |

```python
# find() - single element
first_p = soup.find('p')  # Returns Tag or None

# find_all() - list of elements
all_p = soup.find_all('p')  # Returns list (possibly empty)
```

---

### select() vs find_all()

| | select() | find_all() |
|--|----------|------------|
| Syntax | CSS selectors | Method parameters |
| Power | More powerful for complex queries | Simpler for basic queries |
| Readability | Familiar to web developers | More Pythonic |

```python
# select - CSS syntax
products = soup.select('div.products > div.item')

# find_all - Method parameters
products = soup.find_all('div', class_='item')
```

---

### .text vs .string vs .get_text()

| | .text | .string | .get_text() |
|--|-------|---------|-------------|
| Nested tags | Returns all text | Returns None | Returns all text |
| Options | None | None | separator, strip |
| Use when | Quick extraction | Single text child only | Need formatting control |

```python
html = '<p>Hello <b>World</b></p>'
soup = BeautifulSoup(html, 'lxml')
p = soup.p

print(p.text)           # "Hello World"
print(p.string)         # None (has nested <b>)
print(p.get_text(' ', strip=True))  # "Hello World"
```

---

### .children vs .descendants

| | .children | .descendants |
|--|-----------|--------------|
| Depth | Direct children only | All nested elements |
| Returns | Generator | Generator |

```python
html = '<div><p><span>Text</span></p></div>'
soup = BeautifulSoup(html, 'lxml')
div = soup.div

# children - only <p>
for child in div.children:
    if child.name:
        print(child.name)  # p

# descendants - <p> and <span>
for desc in div.descendants:
    if desc.name:
        print(desc.name)  # p, span
```

---

## 9. Real-World Examples

### Example 1: Product Scraper

```python
import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_products(url):
    """Scrape product information from e-commerce page"""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')

        products = []

        # Find all product cards
        product_cards = soup.select('div.product-card')

        for card in product_cards:
            product = {}

            # Extract name
            name_elem = card.select_one('h3.product-name')
            product['name'] = name_elem.get_text(strip=True) if name_elem else None

            # Extract price
            price_elem = card.select_one('span.price')
            product['price'] = price_elem.get_text(strip=True) if price_elem else None

            # Extract rating
            rating_elem = card.select_one('div.rating')
            product['rating'] = rating_elem.get('data-rating') if rating_elem else None

            # Extract link
            link_elem = card.select_one('a.product-link')
            product['url'] = link_elem.get('href') if link_elem else None

            # Extract image
            img_elem = card.select_one('img.product-image')
            product['image'] = img_elem.get('src') if img_elem else None

            products.append(product)

        return products

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# Demo with sample HTML
sample_html = '''
<div class="products-container">
    <div class="product-card">
        <img class="product-image" src="laptop.jpg" alt="Laptop">
        <h3 class="product-name">Gaming Laptop</h3>
        <span class="price">$1299.99</span>
        <div class="rating" data-rating="4.5">4.5 stars</div>
        <a class="product-link" href="/products/laptop-123">View Details</a>
    </div>
    <div class="product-card">
        <img class="product-image" src="mouse.jpg" alt="Mouse">
        <h3 class="product-name">Wireless Mouse</h3>
        <span class="price">$49.99</span>
        <div class="rating" data-rating="4.2">4.2 stars</div>
        <a class="product-link" href="/products/mouse-456">View Details</a>
    </div>
</div>
'''

soup = BeautifulSoup(sample_html, 'lxml')
product_cards = soup.select('div.product-card')

print(f"Found {len(product_cards)} products:\n")

for card in product_cards:
    name = card.select_one('h3.product-name').get_text(strip=True)
    price = card.select_one('span.price').get_text(strip=True)
    rating = card.select_one('div.rating').get('data-rating')
    link = card.select_one('a.product-link').get('href')

    print(f"Product: {name}")
    print(f"  Price: {price}")
    print(f"  Rating: {rating}")
    print(f"  Link: {link}")
    print()

# Output:
# Found 2 products:
#
# Product: Gaming Laptop
#   Price: $1299.99
#   Rating: 4.5
#   Link: /products/laptop-123
#
# Product: Wireless Mouse
#   Price: $49.99
#   Rating: 4.2
#   Link: /products/mouse-456
```

---

### Example 2: Table Data Extraction

```python
from bs4 import BeautifulSoup
import csv

html = '''
<table class="data-table">
    <thead>
        <tr>
            <th>Name</th>
            <th>Department</th>
            <th>Salary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Doe</td>
            <td>Engineering</td>
            <td>$85,000</td>
        </tr>
        <tr>
            <td>Jane Smith</td>
            <td>Marketing</td>
            <td>$72,000</td>
        </tr>
        <tr>
            <td>Bob Johnson</td>
            <td>Sales</td>
            <td>$68,000</td>
        </tr>
    </tbody>
</table>
'''

soup = BeautifulSoup(html, 'lxml')

# Extract headers
headers = []
for th in soup.select('table.data-table thead th'):
    headers.append(th.get_text(strip=True))

print("Headers:", headers)
# Output: Headers: ['Name', 'Department', 'Salary']

# Extract rows
rows = []
for tr in soup.select('table.data-table tbody tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.get_text(strip=True))
    rows.append(row)

print("\nRows:")
for row in rows:
    print(row)
# Output:
# Rows:
# ['John Doe', 'Engineering', '$85,000']
# ['Jane Smith', 'Marketing', '$72,000']
# ['Bob Johnson', 'Sales', '$68,000']

# Convert to list of dictionaries
data = []
for row in rows:
    row_dict = dict(zip(headers, row))
    data.append(row_dict)

print("\nAs Dictionaries:")
for item in data:
    print(item)
# Output:
# As Dictionaries:
# {'Name': 'John Doe', 'Department': 'Engineering', 'Salary': '$85,000'}
# {'Name': 'Jane Smith', 'Department': 'Marketing', 'Salary': '$72,000'}
# {'Name': 'Bob Johnson', 'Department': 'Sales', 'Salary': '$68,000'}

# Save to CSV
with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
print("\nSaved to employees.csv")
```

---

### Example 3: Extracting All Links

```python
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = '''
<html>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
    <main>
        <a href="/blog/post-1">Blog Post 1</a>
        <a href="https://external.com" target="_blank">External Link</a>
    </main>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
base_url = 'https://example.com'

# Extract all links
links = []
for a in soup.find_all('a', href=True):
    text = a.get_text(strip=True)
    href = a['href']

    # Convert relative URLs to absolute
    absolute_url = urljoin(base_url, href)

    # Check if external
    is_external = not absolute_url.startswith(base_url)

    links.append({
        'text': text,
        'url': absolute_url,
        'external': is_external
    })

print("All Links:")
for link in links:
    ext_mark = " [EXTERNAL]" if link['external'] else ""
    print(f"  {link['text']}: {link['url']}{ext_mark}")

# Output:
# All Links:
#   Home: https://example.com/
#   About: https://example.com/about
#   Contact: https://example.com/contact
#   Blog Post 1: https://example.com/blog/post-1
#   External Link: https://external.com [EXTERNAL]

# Filter internal links only
internal_links = [l for l in links if not l['external']]
print(f"\nFound {len(internal_links)} internal links")
```

---

### Example 4: Saving Data to JSON

```python
from bs4 import BeautifulSoup
import json

html = '''
<div class="articles">
    <article class="post">
        <h2>Introduction to Python</h2>
        <span class="author">Jane Doe</span>
        <time datetime="2024-12-01">Dec 1, 2024</time>
        <p class="excerpt">Learn the basics of Python programming...</p>
        <a href="/articles/python-intro">Read More</a>
    </article>
    <article class="post">
        <h2>Web Scraping Guide</h2>
        <span class="author">John Smith</span>
        <time datetime="2024-12-15">Dec 15, 2024</time>
        <p class="excerpt">Master web scraping with BeautifulSoup...</p>
        <a href="/articles/web-scraping">Read More</a>
    </article>
</div>
'''

soup = BeautifulSoup(html, 'lxml')

articles = []

for article in soup.select('article.post'):
    data = {
        'title': article.select_one('h2').get_text(strip=True),
        'author': article.select_one('.author').get_text(strip=True),
        'date': article.select_one('time').get('datetime'),
        'excerpt': article.select_one('.excerpt').get_text(strip=True),
        'url': article.select_one('a').get('href')
    }
    articles.append(data)

# Save to JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print("Saved to articles.json")
print(json.dumps(articles, indent=2))

# Output:
# Saved to articles.json
# [
#   {
#     "title": "Introduction to Python",
#     "author": "Jane Doe",
#     "date": "2024-12-01",
#     "excerpt": "Learn the basics of Python programming...",
#     "url": "/articles/python-intro"
#   },
#   {
#     "title": "Web Scraping Guide",
#     "author": "John Smith",
#     "date": "2024-12-15",
#     "excerpt": "Master web scraping with BeautifulSoup...",
#     "url": "/articles/web-scraping"
#   }
# ]
```

---

## 10. Method Comparison Table

| Method | Parameters | Returns | Use When |
|--------|------------|---------|----------|
| `find()` | name, class_, id, attrs | Tag or None | Need first match |
| `find_all()` | name, class_, limit | List (ResultSet) | Need all matches |
| `select()` | CSS selector | List | Complex CSS queries |
| `select_one()` | CSS selector | Tag or None | CSS + first match |
| `.text` | None | String | Quick text extraction |
| `.get_text()` | separator, strip | String | Formatted text |
| `.get()` | attr, default | Value or default | Safe attribute access |
| `.parent` | None | Tag | Navigate up one level |
| `.children` | None | Generator | Direct children only |
| `.descendants` | None | Generator | All nested elements |
| `find_next_sibling()` | name | Tag or None | Next element |

---

## 11. Quick Reference Summary

| Task | Code | Example |
|------|------|---------|
| Create soup | `soup = BeautifulSoup(html, 'lxml')` | Parse HTML |
| Find one | `soup.find('tag', class_='class')` | First match |
| Find all | `soup.find_all('tag')` | All matches |
| CSS select | `soup.select('div.class')` | CSS selector |
| Get text | `element.get_text(strip=True)` | Clean text |
| Get attribute | `element.get('href', '#')` | Safe access |
| Navigate up | `element.parent` | Parent element |
| Navigate down | `element.children` | Child elements |
| Next sibling | `element.find_next_sibling()` | Next element |

---

## 12. Legal and Ethical Guidelines

### Before Scraping:

1. **Check robots.txt**: `https://example.com/robots.txt`
2. **Read Terms of Service**: Many sites prohibit scraping
3. **Look for APIs**: Always prefer official APIs
4. **Respect rate limits**: Add delays between requests
5. **Identify your bot**: Use descriptive User-Agent

### Ethical Practices:

```python
import time
import requests

# Add delays between requests
for url in urls:
    response = requests.get(url)
    # Process...
    time.sleep(2)  # 2 second delay

# Identify your bot
headers = {
    'User-Agent': 'MyScraperBot/1.0 (contact@example.com)'
}
```

---

## 13. Troubleshooting

### Element Not Found

**Solutions:**
1. Print `soup.prettify()` to see actual HTML
2. Try different selectors
3. Check if content is JavaScript-rendered (needs Selenium)
4. Verify HTML structure hasn't changed

### Encoding Issues

**Solution:** Use `response.content` instead of `response.text`

```python
soup = BeautifulSoup(response.content, 'lxml')
```

### JavaScript Content

**Solution:** Use Selenium + BeautifulSoup

```python
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
driver.quit()
```

---

## 14. Additional Resources

- **Official Docs**: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Practice Sites**:
  - http://books.toscrape.com/
  - http://quotes.toscrape.com/
  - https://the-internet.herokuapp.com/

---

**End of Documentation**
