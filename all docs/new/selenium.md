# Selenium WebDriver - Complete Python Documentation

---

## 1. Overview

### What is Selenium?

Selenium is a powerful Python library for **automating web browsers**. It controls real browsers (Chrome, Firefox, Edge, Safari) programmatically, allowing you to interact with websites exactly like a human user - clicking buttons, filling forms, scrolling pages, and extracting data.

### Main Purpose and Use Cases

- **Web Scraping**: Extract data from dynamic, JavaScript-heavy websites
- **Automated Testing**: Test web applications across different browsers
- **Web Automation**: Automate repetitive browser tasks (form filling, data entry)
- **Bot Development**: Create automated workflows for web interactions
- **Handling Login-Required Sites**: Access content behind authentication

### When to Use Selenium vs Alternatives

| Tool | Use When | Speed | JavaScript Support |
|------|----------|-------|-------------------|
| **Selenium** | Dynamic JS sites, user interaction needed | Slow | Yes |
| **BeautifulSoup + Requests** | Static HTML pages | Fast | No |
| **Scrapy** | Large-scale crawling (1000s of pages) | Very Fast | No |
| **Playwright** | Modern alternative to Selenium | Fast | Yes |
| **API Requests** | When official API exists | Fastest | N/A |

**Use Selenium when:**
- Website uses JavaScript to load content dynamically
- Need to interact with elements (click, scroll, fill forms)
- Content loads after page initially renders (AJAX, Single Page Apps)
- Need to handle authentication or sessions
- Need to handle pop-ups, alerts, or multiple windows

**Use Alternatives when:**
- Page is static HTML (use BeautifulSoup - 10x faster)
- Need to scrape thousands of pages (use Scrapy)
- Website offers an API (always prefer official APIs)

### Installation

```bash
# Install Selenium
pip install selenium

# Install WebDriver Manager (automatic driver management - RECOMMENDED)
pip install webdriver-manager
```

**Browser Drivers:**
- Chrome: ChromeDriver (most common)
- Firefox: GeckoDriver
- Edge: EdgeDriver
- Safari: Built-in (macOS only)

**Verify Installation:**
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# This should open and close Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print(f"Page title: {driver.title}")
driver.quit()

# Output: Page title: Google
```

---

## 2. Core Components Overview

### Main Components

| Component | Description | Import Statement |
|-----------|-------------|------------------|
| `webdriver` | Controls the browser | `from selenium import webdriver` |
| `WebElement` | Represents HTML elements | Auto-returned by find methods |
| `By` | Element locator strategies | `from selenium.webdriver.common.by import By` |
| `Keys` | Keyboard actions (Enter, Tab, etc.) | `from selenium.webdriver.common.keys import Keys` |
| `ActionChains` | Complex mouse/keyboard automation | `from selenium.webdriver.common.action_chains import ActionChains` |
| `WebDriverWait` | Explicit waiting mechanism | `from selenium.webdriver.support.ui import WebDriverWait` |
| `Expected Conditions (EC)` | Wait conditions | `from selenium.webdriver.support import expected_conditions as EC` |
| `Select` | Handle dropdown menus | `from selenium.webdriver.support.select import Select` |

### How They Work Together

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. WebDriver creates browser instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Navigate to page
driver.get("https://www.google.com")

# 3. Wait for element to be ready
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

# 4. Interact with WebElement
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# 5. Extract data
wait.until(EC.presence_of_element_located((By.ID, "search")))
print(f"Current URL: {driver.current_url}")

# 6. Clean up
driver.quit()
```

### Common Workflow

```
Start Browser (webdriver.Chrome())
       ↓
Navigate to URL (driver.get())
       ↓
Wait for Elements (WebDriverWait)
       ↓
Find Elements (find_element/find_elements)
       ↓
Interact (click, send_keys, etc.)
       ↓
Extract Data (text, get_attribute)
       ↓
Close Browser (driver.quit())
```

---

## 3. Fundamentals (Logical Sequence)

### Step 1: Setting Up WebDriver

#### Method 1: Using WebDriver Manager (RECOMMENDED)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads and manages ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
print(driver.title)
# Output: Welcome to Python.org

driver.quit()
```

#### Method 2: Manual Driver Path

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify path to downloaded ChromeDriver
service = Service(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome(service=service)
```

#### Method 3: Different Browsers

```python
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# Firefox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Edge
edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
```

---

### Step 2: Finding Elements (Locator Strategies)

#### All Locator Types

```python
from selenium.webdriver.common.by import By

# By.ID - Fastest and most reliable (if ID exists)
element = driver.find_element(By.ID, "submit-button")

# By.NAME - Common for form inputs
element = driver.find_element(By.NAME, "username")

# By.CLASS_NAME - Single class only (no spaces)
element = driver.find_element(By.CLASS_NAME, "btn-primary")

# By.TAG_NAME - HTML tag type
element = driver.find_element(By.TAG_NAME, "h1")

# By.CSS_SELECTOR - Very flexible (RECOMMENDED for complex selections)
element = driver.find_element(By.CSS_SELECTOR, "div.content > p.intro")

# By.XPATH - Most powerful but slower
element = driver.find_element(By.XPATH, "//div[@class='header']/h1")

# By.LINK_TEXT - Exact text of anchor tag
element = driver.find_element(By.LINK_TEXT, "Click Here")

# By.PARTIAL_LINK_TEXT - Partial text match
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
```

#### Locator Priority (Use in This Order)

1. **By.ID** - Fastest, unique identifier
2. **By.NAME** - Good for form elements
3. **By.CSS_SELECTOR** - Flexible, fast
4. **By.XPATH** - When CSS can't achieve it
5. **By.CLASS_NAME** - Simple class selections
6. **By.TAG_NAME** - Broad selections
7. **By.LINK_TEXT** - Text-based link finding

---

### Step 3: CSS Selectors (Detailed Guide)

CSS Selectors are powerful and faster than XPath. Here's a complete guide:

#### Basic CSS Selectors

```python
# HTML Example:
# <div id="main" class="container active">
#     <p class="intro text-large">Hello</p>
#     <a href="/about" class="link">About</a>
#     <input type="text" name="email" placeholder="Enter email">
#     <button data-testid="submit-btn">Submit</button>
# </div>

# By ID (#)
element = driver.find_element(By.CSS_SELECTOR, "#main")

# By Class (.)
element = driver.find_element(By.CSS_SELECTOR, ".container")

# Multiple classes
element = driver.find_element(By.CSS_SELECTOR, ".intro.text-large")

# By Tag
element = driver.find_element(By.CSS_SELECTOR, "div")

# By Attribute
element = driver.find_element(By.CSS_SELECTOR, "[name='email']")
element = driver.find_element(By.CSS_SELECTOR, "[type='text']")
element = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-btn']")

# Attribute contains (*)
element = driver.find_element(By.CSS_SELECTOR, "[class*='text']")  # class contains "text"

# Attribute starts with (^)
element = driver.find_element(By.CSS_SELECTOR, "[href^='/about']")  # href starts with /about

# Attribute ends with ($)
element = driver.find_element(By.CSS_SELECTOR, "[href$='.pdf']")  # href ends with .pdf
```

#### Hierarchical CSS Selectors

```python
# HTML Example:
# <div class="products">
#     <div class="product">
#         <h3>Laptop</h3>
#         <span class="price">$999</span>
#     </div>
#     <div class="product">
#         <h3>Mouse</h3>
#         <span class="price">$25</span>
#     </div>
# </div>

# Descendant (space) - Any level nested
element = driver.find_element(By.CSS_SELECTOR, "div.products span.price")
# Finds ALL price spans inside products div

# Direct Child (>)
element = driver.find_element(By.CSS_SELECTOR, "div.products > div.product")
# Finds only direct children

# Adjacent Sibling (+) - Immediately following
element = driver.find_element(By.CSS_SELECTOR, "h3 + span")
# Finds span immediately after h3

# General Sibling (~) - Any following sibling
element = driver.find_element(By.CSS_SELECTOR, "h3 ~ span")
# Finds any span after h3

# Combined selectors
element = driver.find_element(By.CSS_SELECTOR, "div.products > div.product > span.price")
```

#### Pseudo-selectors

```python
# First child
element = driver.find_element(By.CSS_SELECTOR, "div.product:first-child")

# Last child
element = driver.find_element(By.CSS_SELECTOR, "div.product:last-child")

# Nth child (1-indexed)
element = driver.find_element(By.CSS_SELECTOR, "div.product:nth-child(2)")

# Nth of type
element = driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(3)")

# Not selector
element = driver.find_element(By.CSS_SELECTOR, "div:not(.hidden)")
```

#### Real-World CSS Selector Examples

```python
driver.get("https://example-shop.com")

# Product cards with specific data attribute
products = driver.find_elements(By.CSS_SELECTOR, "div[data-product-type='electronics']")

# Price elements inside product cards
prices = driver.find_elements(By.CSS_SELECTOR, ".product-card .price-tag")

# Links in navigation menu
nav_links = driver.find_elements(By.CSS_SELECTOR, "nav.main-nav > ul > li > a")

# Input fields in forms
inputs = driver.find_elements(By.CSS_SELECTOR, "form.checkout input[type='text']")

# Images with lazy loading
images = driver.find_elements(By.CSS_SELECTOR, "img[loading='lazy']")

# Buttons with specific text (using data attributes)
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-action='submit']")

print(f"Found {len(products)} products")
# Output: Found 15 products
```

---

### Step 4: XPath Selectors (Detailed Guide)

XPath is more powerful than CSS for complex selections, especially text-based searching.

#### Basic XPath Syntax

```python
# HTML Example:
# <div id="main" class="container">
#     <h1>Welcome</h1>
#     <p class="intro">Hello World</p>
#     <a href="/about">About Us</a>
# </div>

# By ID
element = driver.find_element(By.XPATH, "//*[@id='main']")

# By Class
element = driver.find_element(By.XPATH, "//div[@class='container']")

# By Tag
element = driver.find_element(By.XPATH, "//h1")

# By Attribute
element = driver.find_element(By.XPATH, "//a[@href='/about']")

# By Text Content (POWERFUL - CSS can't do this)
element = driver.find_element(By.XPATH, "//h1[text()='Welcome']")
element = driver.find_element(By.XPATH, "//a[text()='About Us']")

# Contains text (partial match)
element = driver.find_element(By.XPATH, "//p[contains(text(), 'Hello')]")

# Contains attribute value
element = driver.find_element(By.XPATH, "//div[contains(@class, 'container')]")

# Starts with
element = driver.find_element(By.XPATH, "//a[starts-with(@href, '/about')]")
```

#### XPath Axes (Navigation)

```python
# HTML Example:
# <div class="product">
#     <h3>Product Name</h3>
#     <span class="price">$99</span>
#     <button>Buy Now</button>
# </div>
# <div class="review">
#     <p>Great product!</p>
# </div>

# Parent axis
element = driver.find_element(By.XPATH, "//span[@class='price']/parent::div")

# Ancestor axis (any level up)
element = driver.find_element(By.XPATH, "//button/ancestor::div[@class='product']")

# Child axis
elements = driver.find_elements(By.XPATH, "//div[@class='product']/child::*")

# Following sibling
element = driver.find_element(By.XPATH, "//h3/following-sibling::span")

# Preceding sibling
element = driver.find_element(By.XPATH, "//button/preceding-sibling::span")

# Following (any element after, anywhere in document)
element = driver.find_element(By.XPATH, "//div[@class='product']/following::div[@class='review']")
```

#### Advanced XPath Examples

```python
# Multiple conditions with AND
element = driver.find_element(By.XPATH, "//input[@type='text' and @name='email']")

# OR condition
element = driver.find_element(By.XPATH, "//button[@class='primary' or @class='submit']")

# NOT condition
element = driver.find_element(By.XPATH, "//div[not(@class='hidden')]")

# Position-based selection
element = driver.find_element(By.XPATH, "(//div[@class='product'])[1]")  # First product
element = driver.find_element(By.XPATH, "(//div[@class='product'])[last()]")  # Last product
element = driver.find_element(By.XPATH, "(//div[@class='product'])[position()<=3]")  # First 3

# Normalize space (handles extra whitespace)
element = driver.find_element(By.XPATH, "//p[normalize-space(text())='Hello World']")
```

#### Real-World XPath Examples

```python
driver.get("https://example-shop.com")

# Find element by visible text
add_to_cart = driver.find_element(By.XPATH, "//button[text()='Add to Cart']")

# Find product with specific price
cheap_product = driver.find_element(By.XPATH, "//div[@class='product'][.//span[@class='price' and text()='$9.99']]")

# Find input field by placeholder
email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']")

# Find link containing text
learn_more = driver.find_element(By.XPATH, "//a[contains(text(), 'Learn More')]")

# Find element after a label
password_field = driver.find_element(By.XPATH, "//label[text()='Password']/following-sibling::input")

# Find row in table by cell content
row = driver.find_element(By.XPATH, "//tr[td[text()='John Doe']]")

print(f"Add to cart button found: {add_to_cart.text}")
# Output: Add to cart button found: Add to Cart
```

#### CSS Selector vs XPath Comparison

| Feature | CSS Selector | XPath |
|---------|--------------|-------|
| Speed | Faster | Slower |
| Text matching | Not supported | Supported |
| Going up DOM | Not supported | Supported (parent, ancestor) |
| Complex conditions | Limited | Full support (and, or, not) |
| Readability | More readable | Can be complex |
| Browser support | All browsers | All browsers |

**Rule of thumb:** Use CSS Selectors by default, use XPath when you need text-based selection or parent navigation.

---

### Step 5: Interacting with Elements

#### Basic Interactions

```python
from selenium.webdriver.common.keys import Keys

# Click element
button = driver.find_element(By.ID, "submit-btn")
button.click()

# Type text
input_field = driver.find_element(By.NAME, "username")
input_field.send_keys("myusername")

# Clear text field
input_field.clear()

# Type and submit
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Submit form
form = driver.find_element(By.TAG_NAME, "form")
form.submit()

# Check element state
is_displayed = element.is_displayed()
is_enabled = element.is_enabled()
is_selected = element.is_selected()  # For checkboxes/radio buttons
```

#### Keyboard Keys Reference

```python
from selenium.webdriver.common.keys import Keys

# Common keys
element.send_keys(Keys.RETURN)      # Enter key
element.send_keys(Keys.ENTER)       # Same as RETURN
element.send_keys(Keys.TAB)         # Tab key
element.send_keys(Keys.ESCAPE)      # Escape key
element.send_keys(Keys.BACKSPACE)   # Backspace
element.send_keys(Keys.DELETE)      # Delete
element.send_keys(Keys.SPACE)       # Space bar

# Arrow keys
element.send_keys(Keys.ARROW_UP)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ARROW_LEFT)
element.send_keys(Keys.ARROW_RIGHT)

# Modifier keys (for combinations)
element.send_keys(Keys.CONTROL + 'a')  # Select all (Ctrl+A)
element.send_keys(Keys.CONTROL + 'c')  # Copy (Ctrl+C)
element.send_keys(Keys.CONTROL + 'v')  # Paste (Ctrl+V)
element.send_keys(Keys.SHIFT + Keys.TAB)  # Shift+Tab

# Function keys
element.send_keys(Keys.F5)  # Refresh
element.send_keys(Keys.F12) # Dev tools
```

#### Real-World Interaction Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Find and interact with search box
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Type search query
    search_box.send_keys("Selenium WebDriver tutorial")

    # Wait a moment for suggestions
    import time
    time.sleep(1)

    # Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Wait for results page
    wait.until(EC.presence_of_element_located((By.ID, "search")))

    # Get first result title
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    print(f"First result: {first_result.text}")
    # Output: First result: Selenium WebDriver Tutorial - Complete Guide

finally:
    driver.quit()
```

---

### Step 6: Waiting Strategies

#### Why Waits Are Essential

Web pages load dynamically. Without proper waits, your script may try to interact with elements before they exist, causing errors.

#### Method 1: Implicit Wait (Global - NOT Recommended)

```python
# Sets a global wait time for ALL find operations
driver.implicitly_wait(10)  # Waits up to 10 seconds

# Every find_element will now wait up to 10 seconds
element = driver.find_element(By.ID, "dynamic-content")

# Problems:
# - Applies to ALL finds (can slow down script)
# - Can't specify different conditions
# - Can interfere with explicit waits
```

#### Method 2: Explicit Wait (RECOMMENDED)

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create wait object
wait = WebDriverWait(driver, 10)  # Max 10 seconds

# Wait for element to be present in DOM
element = wait.until(EC.presence_of_element_located((By.ID, "content")))

# Wait for element to be visible on page
element = wait.until(EC.visibility_of_element_located((By.ID, "content")))

# Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

# Wait for text to appear in element
wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Complete"))

# Wait for element to disappear
wait.until(EC.invisibility_of_element_located((By.ID, "loading-spinner")))

# Wait for URL to contain text
wait.until(EC.url_contains("/dashboard"))

# Wait for title to contain text
wait.until(EC.title_contains("Dashboard"))

# Wait for alert to be present
alert = wait.until(EC.alert_is_present())
```

#### Complete Expected Conditions Reference

| Expected Condition | Purpose | When to Use |
|-------------------|---------|-------------|
| `presence_of_element_located` | Element exists in DOM | Checking element loaded |
| `visibility_of_element_located` | Element visible on page | Before reading text |
| `element_to_be_clickable` | Element ready to click | Before clicking |
| `text_to_be_present_in_element` | Text appears in element | Waiting for content |
| `invisibility_of_element_located` | Element disappears | After closing modal |
| `staleness_of` | Element removed from DOM | After page navigation |
| `frame_to_be_available_and_switch_to_it` | Frame ready | Before switching to iframe |
| `alert_is_present` | Alert dialog appears | Handling pop-ups |
| `url_contains` | URL changes | After navigation |
| `title_contains` | Page title changes | Page load verification |

#### Method 3: Custom Wait Condition

```python
from selenium.webdriver.support.ui import WebDriverWait

def element_has_css_class(locator, css_class):
    """Wait until element has specific CSS class"""
    def check(driver):
        element = driver.find_element(*locator)
        if css_class in element.get_attribute("class"):
            return element
        return False
    return check

# Usage
wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, "button"), "active"))
```

#### Real-World Waiting Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://example-shop.com/products")

    # Wait for page to fully load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Wait for products to load (JavaScript renders these)
    try:
        products = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card"))
        )
        print(f"Found {len(products)} products")
    except TimeoutException:
        print("Products didn't load within 15 seconds")

    # Click on first product
    first_product = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-card:first-child"))
    )
    first_product.click()

    # Wait for product detail page
    product_title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.product-title"))
    )
    print(f"Product: {product_title.text}")

    # Wait for Add to Cart button to be ready
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart"))
    )
    add_to_cart.click()

    # Wait for cart notification to appear and then disappear
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-notification")))
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "cart-notification")))

    print("Product added to cart successfully!")

except TimeoutException as e:
    print(f"Timeout waiting for element: {e}")

finally:
    driver.quit()
```

---

### Step 7: Extracting Data

#### Getting Text Content

```python
# HTML: <h1 class="title">Welcome to Our Site</h1>

title = driver.find_element(By.CLASS_NAME, "title")

# Get visible text
text = title.text
print(text)
# Output: Welcome to Our Site

# Get ALL text including hidden elements
all_text = title.get_attribute("textContent")

# Get inner HTML
inner_html = title.get_attribute("innerHTML")

# Get outer HTML (includes the element itself)
outer_html = title.get_attribute("outerHTML")
print(outer_html)
# Output: <h1 class="title">Welcome to Our Site</h1>
```

#### Getting Attributes

```python
# HTML: <a href="https://example.com" class="link primary" data-id="123">Click Me</a>

link = driver.find_element(By.TAG_NAME, "a")

# Get specific attribute
href = link.get_attribute("href")
print(href)
# Output: https://example.com

classes = link.get_attribute("class")
print(classes)
# Output: link primary

data_id = link.get_attribute("data-id")
print(data_id)
# Output: 123

# Check if attribute exists (returns None if not)
target = link.get_attribute("target")
print(target)
# Output: None
```

#### Getting Element Properties

```python
element = driver.find_element(By.ID, "my-element")

# Get tag name
tag = element.tag_name
print(tag)
# Output: div

# Get element size
size = element.size
print(size)
# Output: {'height': 100, 'width': 200}

# Get element location
location = element.location
print(location)
# Output: {'x': 100, 'y': 250}

# Get rectangle (location + size)
rect = element.rect
print(rect)
# Output: {'height': 100, 'width': 200, 'x': 100, 'y': 250}

# Get CSS value
color = element.value_of_css_property("color")
print(color)
# Output: rgba(0, 0, 0, 1)
```

#### Real-World Data Extraction Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://news.ycombinator.com")

    # Wait for stories to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "athing")))

    # Get all story rows
    stories = driver.find_elements(By.CLASS_NAME, "athing")

    scraped_data = []

    for story in stories[:10]:  # First 10 stories
        try:
            # Get story ID
            story_id = story.get_attribute("id")

            # Get title and link
            title_element = story.find_element(By.CSS_SELECTOR, ".titleline > a")
            title = title_element.text
            url = title_element.get_attribute("href")

            # Get score (in subtext row)
            try:
                score_element = driver.find_element(By.ID, f"score_{story_id}")
                score = score_element.text
            except:
                score = "0 points"

            scraped_data.append({
                "id": story_id,
                "title": title,
                "url": url,
                "score": score
            })

        except Exception as e:
            continue

    # Print results
    for item in scraped_data[:5]:
        print(f"\n{item['title']}")
        print(f"  URL: {item['url']}")
        print(f"  Score: {item['score']}")

    # Output:
    # Show HN: My Weekend Project
    #   URL: https://github.com/user/project
    #   Score: 142 points
    #
    # Understanding Neural Networks
    #   URL: https://blog.example.com/neural-networks
    #   Score: 89 points

finally:
    driver.quit()
```

---

## 4. Functions/Methods Documentation

### WebDriver Methods

#### driver.get()

**Purpose:** Navigate browser to specified URL

**Syntax:**
```python
driver.get(url)
```

**Key Parameters:**
- `url` (str): Complete URL including protocol (https://) - **REQUIRED**

**Returns:** None

**Example:**
```python
driver.get("https://www.google.com")
print(driver.current_url)
# Output: https://www.google.com/
```

**When to Use:** Starting point for any navigation

---

#### driver.find_element()

**Purpose:** Locate single element on page

**Syntax:**
```python
element = driver.find_element(by, value)
```

**Key Parameters:**
- `by` (By): Locator strategy - **REQUIRED**
- `value` (str): Locator value - **REQUIRED**

**Returns:** WebElement object (first match)

**Raises:** `NoSuchElementException` if not found

**Example:**
```python
from selenium.webdriver.common.by import By

# Find by ID
button = driver.find_element(By.ID, "submit-btn")

# Find by CSS selector
price = driver.find_element(By.CSS_SELECTOR, "span.price")

# Find by XPath
heading = driver.find_element(By.XPATH, "//h1[text()='Welcome']")
```

**When to Use:** When you need exactly one element

---

#### driver.find_elements()

**Purpose:** Locate multiple elements matching criteria

**Syntax:**
```python
elements = driver.find_elements(by, value)
```

**Key Parameters:**
- `by` (By): Locator strategy - **REQUIRED**
- `value` (str): Locator value - **REQUIRED**

**Returns:** List of WebElement objects (empty list if none found - never raises exception)

**Example:**
```python
# Get all links
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Found {len(links)} links")

# Get all products
products = driver.find_elements(By.CLASS_NAME, "product-card")
for product in products:
    print(product.text)
```

**When to Use:** When extracting lists of items

---

#### driver.execute_script()

**Purpose:** Run JavaScript code in browser context

**Syntax:**
```python
result = driver.execute_script(script, *args)
```

**Key Parameters:**
- `script` (str): JavaScript code to execute - **REQUIRED**
- `*args`: Arguments passed to script (accessed via `arguments[0]`, `arguments[1]`, etc.) - **Optional**

**Returns:** Whatever the JavaScript returns

**Examples:**
```python
# Scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll element into view
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Get page height
height = driver.execute_script("return document.body.scrollHeight;")
print(f"Page height: {height}px")

# Click element (bypasses some click issues)
button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", button)

# Set value directly (faster than send_keys)
input_field = driver.find_element(By.ID, "email")
driver.execute_script("arguments[0].value = 'user@example.com';", input_field)

# Remove element (useful for removing overlays)
overlay = driver.find_element(By.CLASS_NAME, "modal-backdrop")
driver.execute_script("arguments[0].remove();", overlay)

# Get computed style
element = driver.find_element(By.ID, "box")
color = driver.execute_script(
    "return window.getComputedStyle(arguments[0]).backgroundColor;",
    element
)
print(f"Background color: {color}")
```

**When to Use:**
- Scrolling pages
- Clicking hidden or covered elements
- Accessing browser APIs not available through Selenium
- Performance optimization

---

#### driver.switch_to.frame()

**Purpose:** Switch context to iframe or frame element

**Syntax:**
```python
driver.switch_to.frame(frame_reference)
```

**Key Parameters:**
- `frame_reference`: Can be int (index), str (name/id), or WebElement - **REQUIRED**

**Returns:** None

**Example:**
```python
# HTML: <iframe id="content-frame" name="contentFrame" src="..."></iframe>

# Switch by index (0 = first frame)
driver.switch_to.frame(0)

# Switch by name or ID
driver.switch_to.frame("content-frame")
driver.switch_to.frame("contentFrame")

# Switch by WebElement
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Interact with iframe content
iframe_content = driver.find_element(By.TAG_NAME, "body").text
print(iframe_content)

# IMPORTANT: Switch back to main content
driver.switch_to.default_content()

# For nested iframes, switch to parent frame
driver.switch_to.parent_frame()
```

**When to Use:** Accessing content inside iframes (common in ads, payment forms, embedded content)

---

#### driver.switch_to.window()

**Purpose:** Switch between browser windows/tabs

**Syntax:**
```python
driver.switch_to.window(window_handle)
```

**Key Parameters:**
- `window_handle` (str): Window handle identifier - **REQUIRED**

**Returns:** None

**Example:**
```python
# Store main window handle
main_window = driver.current_window_handle

# Click link that opens new tab
link = driver.find_element(By.LINK_TEXT, "Open New Tab")
link.click()

# Wait for new window
import time
time.sleep(1)

# Get all window handles
all_windows = driver.window_handles
print(f"Open windows: {len(all_windows)}")

# Switch to new window
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Do something in new window
print(f"New window title: {driver.title}")

# Close new window
driver.close()

# Switch back to main window
driver.switch_to.window(main_window)
print(f"Back to: {driver.title}")
```

**When to Use:** Handling pop-ups, new tabs, or multi-window workflows

---

#### driver.get_screenshot_as_file()

**Purpose:** Save screenshot of current page

**Syntax:**
```python
success = driver.get_screenshot_as_file(filename)
```

**Key Parameters:**
- `filename` (str): Path where screenshot will be saved (.png) - **REQUIRED**

**Returns:** Boolean (True if successful)

**Example:**
```python
# Full page screenshot
driver.get_screenshot_as_file("homepage.png")

# Screenshot specific element
element = driver.find_element(By.ID, "product-image")
element.screenshot("product.png")

# Screenshot with timestamp
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
driver.get_screenshot_as_file(f"screenshot_{timestamp}.png")

# Get screenshot as base64 (for storing in database)
screenshot_base64 = driver.get_screenshot_as_base64()

# Get screenshot as PNG bytes
screenshot_png = driver.get_screenshot_as_png()
with open("screenshot.png", "wb") as f:
    f.write(screenshot_png)
```

**When to Use:** Debugging, documenting page states, creating reports

---

### WebElement Methods

#### element.send_keys()

**Purpose:** Type text into element or send keyboard keys

**Syntax:**
```python
element.send_keys(*value)
```

**Key Parameters:**
- `*value` (str/Keys): Text or special keys to send - **REQUIRED**

**Returns:** None

**Example:**
```python
from selenium.webdriver.common.keys import Keys

# Type text
username = driver.find_element(By.ID, "username")
username.send_keys("myusername")

# Clear and type new text
username.clear()
username.send_keys("newusername")

# Send special keys
password = driver.find_element(By.ID, "password")
password.send_keys("mypassword")
password.send_keys(Keys.TAB)  # Move to next field

# Submit with Enter
search = driver.find_element(By.NAME, "q")
search.send_keys("search term", Keys.RETURN)

# Keyboard shortcuts
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 'a')  # Select all
```

**When to Use:** Filling forms, typing search queries, keyboard interaction

---

#### element.click()

**Purpose:** Click on element

**Syntax:**
```python
element.click()
```

**Returns:** None

**Example:**
```python
# Click button
button = driver.find_element(By.ID, "submit-btn")
button.click()

# Click with wait
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
button.click()

# If regular click doesn't work, use JavaScript
driver.execute_script("arguments[0].click();", button)
```

**Common Issues:**
- Element not visible → scroll into view first
- Element covered by another element → wait or use JavaScript click
- Element not clickable yet → use `element_to_be_clickable` wait

---

#### element.text

**Purpose:** Get visible text content of element

**Syntax:**
```python
text = element.text
```

**Returns:** String containing visible text

**Example:**
```python
# Get heading text
heading = driver.find_element(By.TAG_NAME, "h1")
print(heading.text)
# Output: Welcome to Our Website

# Get all text from paragraph
paragraph = driver.find_element(By.CLASS_NAME, "description")
print(paragraph.text)

# Note: .text only returns VISIBLE text
# For hidden text, use:
all_text = element.get_attribute("textContent")
```

**When to Use:** Extracting displayed content from pages

---

#### element.get_attribute()

**Purpose:** Get value of HTML attribute

**Syntax:**
```python
value = element.get_attribute(name)
```

**Key Parameters:**
- `name` (str): Attribute name - **REQUIRED**

**Returns:** String value or None if attribute doesn't exist

**Example:**
```python
# HTML: <a href="https://example.com" class="link" data-id="123">Link</a>

link = driver.find_element(By.TAG_NAME, "a")

href = link.get_attribute("href")
print(href)  # https://example.com

class_attr = link.get_attribute("class")
print(class_attr)  # link

data_id = link.get_attribute("data-id")
print(data_id)  # 123

# Special attributes
inner_html = link.get_attribute("innerHTML")
outer_html = link.get_attribute("outerHTML")
text_content = link.get_attribute("textContent")

# Check if attribute exists
target = link.get_attribute("target")
if target:
    print(f"Opens in: {target}")
else:
    print("Opens in same window")
```

**When to Use:** Extracting URLs, data attributes, form values

---

### Handling Dropdowns (Select)

```python
from selenium.webdriver.support.select import Select

# HTML:
# <select id="country">
#     <option value="">Select Country</option>
#     <option value="us">United States</option>
#     <option value="uk">United Kingdom</option>
#     <option value="ca">Canada</option>
# </select>

# Find the select element
dropdown = driver.find_element(By.ID, "country")
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("United States")

# Select by value attribute
select.select_by_value("uk")

# Select by index (0-based)
select.select_by_index(2)  # Selects "United Kingdom"

# Get all options
all_options = select.options
for option in all_options:
    print(f"Value: {option.get_attribute('value')}, Text: {option.text}")

# Get currently selected option
selected = select.first_selected_option
print(f"Selected: {selected.text}")

# For multi-select dropdowns
select.deselect_all()
select.select_by_value("us")
select.select_by_value("ca")
selected_options = select.all_selected_options
```

---

### ActionChains (Complex Interactions)

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

# Hover over element
menu = driver.find_element(By.ID, "dropdown-menu")
actions.move_to_element(menu).perform()

# Double click
element = driver.find_element(By.ID, "double-click-me")
actions.double_click(element).perform()

# Right click (context menu)
element = driver.find_element(By.ID, "right-click-me")
actions.context_click(element).perform()

# Drag and drop
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(source, target).perform()

# Click and hold
slider = driver.find_element(By.ID, "slider")
actions.click_and_hold(slider).move_by_offset(100, 0).release().perform()

# Chain multiple actions
actions.move_to_element(element1)\
       .click()\
       .move_to_element(element2)\
       .click()\
       .perform()

# Key down/up (modifier keys)
from selenium.webdriver.common.keys import Keys
actions.key_down(Keys.CONTROL)\
       .click(link1)\
       .click(link2)\
       .key_up(Keys.CONTROL)\
       .perform()
```

---

### Handling Alerts and Pop-ups

```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException

# Wait for alert to appear
wait = WebDriverWait(driver, 10)

try:
    alert = wait.until(EC.alert_is_present())

    # Get alert text
    alert_text = alert.text
    print(f"Alert says: {alert_text}")

    # Accept alert (click OK)
    alert.accept()

    # Or dismiss alert (click Cancel)
    # alert.dismiss()

except NoAlertPresentException:
    print("No alert present")

# For prompt dialogs (with input)
alert = wait.until(EC.alert_is_present())
alert.send_keys("My input text")
alert.accept()
```

---

### File Upload

```python
# HTML: <input type="file" id="upload">

# Simple file upload (send_keys with file path)
upload_input = driver.find_element(By.ID, "upload")
upload_input.send_keys("/absolute/path/to/file.pdf")

# Multiple files
upload_input.send_keys("/path/to/file1.pdf\n/path/to/file2.pdf")

# Windows path example
upload_input.send_keys("C:\\Users\\user\\Documents\\file.pdf")
```

---

### File Download

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Configure download directory
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
driver.get("https://example.com/download-page")

# Click download button
download_btn = driver.find_element(By.ID, "download-btn")
download_btn.click()

# Wait for download to complete
import time
import glob

timeout = 30
downloaded = False
start_time = time.time()

while time.time() - start_time < timeout:
    files = glob.glob(os.path.join(download_dir, "*"))
    if files and not any(f.endswith('.crdownload') for f in files):
        downloaded = True
        break
    time.sleep(1)

if downloaded:
    print(f"Downloaded: {files[-1]}")
else:
    print("Download timed out")

driver.quit()
```

---

## 5. Exception Handling

### Common Exceptions

| Exception | Cause | Solution |
|-----------|-------|----------|
| `NoSuchElementException` | Element not found | Use explicit wait, check selector |
| `TimeoutException` | Wait timeout exceeded | Increase timeout, check element exists |
| `StaleElementReferenceException` | Element no longer in DOM | Re-find element after page changes |
| `ElementNotInteractableException` | Element exists but can't interact | Wait for clickable, scroll into view |
| `ElementClickInterceptedException` | Another element blocking click | Wait for overlay to disappear, use JS click |
| `WebDriverException` | Browser/driver issues | Check driver version, restart browser |

### Robust Exception Handling Pattern

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_with_error_handling(url, selector):
    """Scrape data with comprehensive error handling"""
    driver = None

    try:
        # Initialize driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.set_page_load_timeout(30)

        # Navigate to page
        logger.info(f"Navigating to {url}")
        driver.get(url)

        # Wait for element
        wait = WebDriverWait(driver, 15)
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

        data = element.text
        logger.info(f"Successfully extracted: {data[:50]}...")
        return data

    except TimeoutException:
        logger.error(f"Timeout: Element '{selector}' not found within 15 seconds")
        return None

    except NoSuchElementException:
        logger.error(f"Element not found: {selector}")
        return None

    except StaleElementReferenceException:
        logger.error("Element became stale - page may have updated")
        return None

    except WebDriverException as e:
        logger.error(f"WebDriver error: {e}")
        return None

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None

    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed")

# Usage
result = scrape_with_error_handling(
    "https://example.com",
    "h1.main-title"
)

if result:
    print(f"Success: {result}")
else:
    print("Failed to scrape data")
```

### Handling Stale Elements with Retry

```python
from selenium.common.exceptions import StaleElementReferenceException
import time

def click_with_retry(driver, locator, max_attempts=3):
    """Click element with retry logic for stale elements"""
    for attempt in range(max_attempts):
        try:
            element = driver.find_element(*locator)
            element.click()
            return True
        except StaleElementReferenceException:
            if attempt < max_attempts - 1:
                time.sleep(0.5)
                continue
            raise
    return False

# Usage
from selenium.webdriver.common.by import By

success = click_with_retry(driver, (By.ID, "submit-btn"))
```

---

## 6. Best Practices

### 1. Always Use WebDriver Manager

```python
# Good - Automatic driver management
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

### 2. Use Explicit Waits (Never time.sleep for waiting)

```python
# Good - Explicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "button")))

# Bad - Fixed sleep
import time
time.sleep(5)  # Don't do this!
element = driver.find_element(By.ID, "button")
```

### 3. Always Close Browser in Finally Block

```python
driver = None
try:
    driver = webdriver.Chrome()
    # Your code here
finally:
    if driver:
        driver.quit()
```

### 4. Use CSS Selectors Over XPath When Possible

```python
# Good - CSS (faster)
element = driver.find_element(By.CSS_SELECTOR, "div.product > span.price")

# Use XPath only when CSS can't do it (text matching, parent selection)
element = driver.find_element(By.XPATH, "//button[text()='Submit']")
```

### 5. Use Headless Mode for Production

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
```

### 6. Add Reasonable Delays Between Actions

```python
import time

# Be respectful to servers
for url in urls:
    driver.get(url)
    # Scrape data
    time.sleep(1)  # 1 second between requests
```

### 7. Handle Elements Safely

```python
# Good - Check if elements exist
elements = driver.find_elements(By.CLASS_NAME, "product")
if elements:
    for element in elements:
        print(element.text)
else:
    print("No products found")

# Good - Safe attribute access
element = driver.find_element(By.TAG_NAME, "a")
href = element.get_attribute("href") or "No URL"
```

---

## 7. Common Mistakes

### Mistake 1: Not Waiting for Elements

**Wrong:**
```python
driver.get("https://example.com")
element = driver.find_element(By.ID, "dynamic-content")  # May fail!
```

**Correct:**
```python
driver.get("https://example.com")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "dynamic-content")))
```

---

### Mistake 2: Not Closing Browser

**Wrong:**
```python
driver = webdriver.Chrome()
driver.get("https://example.com")
# Script ends - browser stays open!
```

**Correct:**
```python
driver = None
try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")
finally:
    if driver:
        driver.quit()
```

---

### Mistake 3: Using find_element for Lists

**Wrong:**
```python
# Only gets first product
product = driver.find_element(By.CLASS_NAME, "product")
```

**Correct:**
```python
# Gets all products
products = driver.find_elements(By.CLASS_NAME, "product")
for product in products:
    print(product.text)
```

---

### Mistake 4: Not Handling Iframes

**Wrong:**
```python
# Trying to find element inside iframe from main context
element = driver.find_element(By.ID, "element-in-iframe")  # Fails!
```

**Correct:**
```python
# Switch to iframe first
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Now find element
element = driver.find_element(By.ID, "element-in-iframe")

# Switch back
driver.switch_to.default_content()
```

---

### Mistake 5: Using close() Instead of quit()

**Wrong:**
```python
driver.close()  # Closes window but driver process remains
```

**Correct:**
```python
driver.quit()  # Closes all windows AND terminates driver process
```

---

### Mistake 6: Mixing Implicit and Explicit Waits

**Wrong:**
```python
driver.implicitly_wait(10)  # Global wait
wait = WebDriverWait(driver, 10)  # Explicit wait
# Can cause unpredictable wait times!
```

**Correct:**
```python
# Use ONLY explicit waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element")))
```

---

## 8. Commonly Confused Concepts

### find_element() vs find_elements()

| | find_element() | find_elements() |
|--|----------------|-----------------|
| Returns | Single WebElement | List of WebElements |
| If not found | Raises NoSuchElementException | Returns empty list |
| Use when | Need exactly one element | Need multiple elements |

```python
# find_element - single element
button = driver.find_element(By.ID, "submit")  # One element or exception

# find_elements - multiple elements
items = driver.find_elements(By.CLASS_NAME, "item")  # List (maybe empty)
if items:
    for item in items:
        print(item.text)
```

---

### driver.close() vs driver.quit()

| | close() | quit() |
|--|---------|--------|
| Closes | Current window only | All windows |
| Driver process | Keeps running | Terminates |
| Use when | Closing one of many tabs | Done with automation |

```python
# close() - just closes current window
driver.close()

# quit() - closes everything and ends session (USE THIS)
driver.quit()
```

---

### element.text vs element.get_attribute("textContent")

| | .text | get_attribute("textContent") |
|--|-------|------------------------------|
| Returns | Visible text only | All text including hidden |
| Respects CSS | Yes (display:none hidden) | No (returns all) |

```python
# HTML: <div>Visible <span style="display:none">Hidden</span></div>

div = driver.find_element(By.TAG_NAME, "div")
print(div.text)  # "Visible"
print(div.get_attribute("textContent"))  # "Visible Hidden"
```

---

### implicitly_wait() vs WebDriverWait

| | implicitly_wait() | WebDriverWait |
|--|-------------------|---------------|
| Scope | Global (all finds) | Specific element |
| Conditions | Just presence | Many conditions |
| Flexibility | Low | High |
| Recommended | No | Yes |

```python
# implicitly_wait - global, less control
driver.implicitly_wait(10)

# WebDriverWait - specific, more control (RECOMMENDED)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "btn")))
```

---

## 9. Browser Options and Configuration

### Headless Mode (No GUI)

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)
```

### Common Chrome Options

```python
options = Options()

# Headless mode
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Window size
options.add_argument('--window-size=1920,1080')
options.add_argument('--start-maximized')

# Disable features
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')

# Incognito mode
options.add_argument('--incognito')

# Custom user agent
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

# Disable images (faster loading)
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# Disable automation flags (avoid detection)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Run in sandbox
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
```

### Mobile Emulation

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Emulate specific device
mobile_emulation = {
    "deviceName": "iPhone 12 Pro"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

# Or custom dimensions
mobile_emulation = {
    "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=options)
```

### Proxy Configuration

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--proxy-server=http://proxy.example.com:8080')

# For authenticated proxy
# options.add_argument('--proxy-server=http://user:pass@proxy.example.com:8080')

driver = webdriver.Chrome(options=options)
```

---

## 10. Complete Real-World Examples

### Example 1: E-commerce Product Scraper

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

def scrape_products(url, max_products=20):
    """Scrape product data from e-commerce site"""

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = None
    products = []

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        wait = WebDriverWait(driver, 15)

        print(f"Navigating to {url}")
        driver.get(url)

        # Wait for products to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card")))

        # Scroll to load more products (for lazy loading)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while len(products) < max_products:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Extract product data
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".product-card")[:max_products]

        for card in product_cards:
            try:
                product = {
                    'name': card.find_element(By.CSS_SELECTOR, ".product-name").text,
                    'price': card.find_element(By.CSS_SELECTOR, ".product-price").text,
                    'url': card.find_element(By.CSS_SELECTOR, "a").get_attribute("href"),
                }

                # Optional: get image
                try:
                    product['image'] = card.find_element(By.TAG_NAME, "img").get_attribute("src")
                except:
                    product['image'] = None

                # Optional: get rating
                try:
                    product['rating'] = card.find_element(By.CSS_SELECTOR, ".rating").text
                except:
                    product['rating'] = None

                products.append(product)

            except Exception as e:
                print(f"Error extracting product: {e}")
                continue

        print(f"Successfully scraped {len(products)} products")
        return products

    except Exception as e:
        print(f"Scraping error: {e}")
        return []

    finally:
        if driver:
            driver.quit()

# Usage
if __name__ == "__main__":
    products = scrape_products(
        "https://example-shop.com/products",
        max_products=10
    )

    # Save to JSON
    with open("products.json", "w") as f:
        json.dump(products, f, indent=2)

    # Print results
    for product in products:
        print(f"\n{product['name']}")
        print(f"  Price: {product['price']}")
        print(f"  URL: {product['url']}")
```

**Sample Output:**
```
Navigating to https://example-shop.com/products
Successfully scraped 10 products

Laptop Pro 15"
  Price: $1299.99
  URL: https://example-shop.com/products/laptop-pro

Wireless Mouse
  Price: $29.99
  URL: https://example-shop.com/products/wireless-mouse
...
```

---

### Example 2: Login and Form Automation

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time

def login_and_submit_form(login_url, credentials, form_data):
    """Login to website and submit a form"""

    driver = None

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 15)

        # 1. Navigate to login page
        print("Navigating to login page...")
        driver.get(login_url)

        # 2. Fill login form
        print("Filling login credentials...")
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys(credentials['email'])

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(credentials['password'])

        # 3. Submit login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # 4. Wait for dashboard (login success)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))
            print("Login successful!")
        except TimeoutException:
            print("Login failed - dashboard not found")
            return False

        # 5. Navigate to form page
        print("Navigating to form page...")
        driver.get("https://example.com/submit-form")

        # 6. Fill form
        print("Filling form...")

        name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_field.send_keys(form_data['name'])

        company_field = driver.find_element(By.ID, "company")
        company_field.send_keys(form_data['company'])

        message_field = driver.find_element(By.ID, "message")
        message_field.send_keys(form_data['message'])

        # Handle dropdown
        from selenium.webdriver.support.select import Select
        category = Select(driver.find_element(By.ID, "category"))
        category.select_by_visible_text(form_data['category'])

        # Handle checkbox
        terms_checkbox = driver.find_element(By.ID, "terms")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # 7. Take screenshot before submit
        driver.get_screenshot_as_file("form_filled.png")

        # 8. Submit form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # 9. Wait for success message
        success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))
        print(f"Form submitted successfully: {success.text}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        if driver:
            driver.get_screenshot_as_file("error_screenshot.png")
        return False

    finally:
        if driver:
            driver.quit()

# Usage
if __name__ == "__main__":
    credentials = {
        'email': 'user@example.com',
        'password': 'password123'
    }

    form_data = {
        'name': 'John Doe',
        'company': 'ACME Corp',
        'message': 'This is a test submission',
        'category': 'Sales Inquiry'
    }

    success = login_and_submit_form(
        "https://example.com/login",
        credentials,
        form_data
    )

    print(f"\nForm submission: {'Success' if success else 'Failed'}")
```

---

### Example 3: Infinite Scroll Scraper

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_infinite_scroll(url, max_items=50, scroll_pause=2):
    """Scrape content from infinite scroll page"""

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = None
    items = []

    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        print(f"Loading {url}")
        driver.get(url)
        time.sleep(3)  # Initial load

        last_height = driver.execute_script("return document.body.scrollHeight")

        while len(items) < max_items:
            # Extract current items
            item_elements = driver.find_elements(By.CSS_SELECTOR, ".item-card")

            for elem in item_elements:
                try:
                    item = {
                        'title': elem.find_element(By.CSS_SELECTOR, ".title").text,
                        'description': elem.find_element(By.CSS_SELECTOR, ".description").text,
                    }
                    if item not in items:
                        items.append(item)
                except:
                    continue

            print(f"Collected {len(items)} items...")

            if len(items) >= max_items:
                break

            # Scroll down
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)

            # Check if reached bottom
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Reached end of page")
                break
            last_height = new_height

        return items[:max_items]

    finally:
        if driver:
            driver.quit()

# Usage
if __name__ == "__main__":
    items = scrape_infinite_scroll(
        "https://example.com/feed",
        max_items=30
    )

    print(f"\nScraped {len(items)} items:")
    for i, item in enumerate(items[:5], 1):
        print(f"{i}. {item['title']}")
```

---

## 11. Method Comparison Table

| Method | Key Parameters | Returns | Use When | Confusing With |
|--------|---------------|---------|----------|----------------|
| `find_element()` | **by**, **value** | WebElement | Need single element | `find_elements()` |
| `find_elements()` | **by**, **value** | List | Need multiple elements | `find_element()` |
| `get()` | **url** | None | Navigate to page | - |
| `click()` | None | None | Click element | `submit()` |
| `send_keys()` | **value** | None | Type text | `execute_script()` |
| `text` | Property | String | Get visible text | `get_attribute()` |
| `get_attribute()` | **name** | String/None | Get HTML attribute | `text` |
| `close()` | None | None | Close current window | `quit()` |
| `quit()` | None | None | End session | `close()` |
| `switch_to.frame()` | **frame** | None | Access iframe | `switch_to.window()` |
| `switch_to.window()` | **handle** | None | Switch tabs | `switch_to.frame()` |
| `execute_script()` | **script** | Any | Run JavaScript | `send_keys()` |

---

## 12. Quick Reference Summary

| Category | Methods | Purpose | Example |
|----------|---------|---------|---------|
| **Setup** | `webdriver.Chrome()` | Start browser | `driver = webdriver.Chrome()` |
| **Navigation** | `get()`, `back()`, `forward()` | Page control | `driver.get(url)` |
| **Finding** | `find_element()`, `find_elements()` | Locate elements | `driver.find_element(By.ID, "btn")` |
| **Interaction** | `click()`, `send_keys()`, `clear()` | User actions | `element.click()` |
| **Extraction** | `text`, `get_attribute()` | Get content | `element.text` |
| **Waiting** | `WebDriverWait`, `EC` | Handle loading | `wait.until(EC.presence_of...)` |
| **Context** | `switch_to.frame()`, `switch_to.window()` | Change context | `driver.switch_to.frame(iframe)` |
| **JavaScript** | `execute_script()` | Run JS code | `driver.execute_script("...")` |
| **Cleanup** | `quit()` | End session | `driver.quit()` |

---

## 13. Legal and Ethical Guidelines

### Before Scraping, Always:

1. **Check robots.txt**: `https://example.com/robots.txt`
2. **Read Terms of Service**: Many sites prohibit scraping
3. **Check for APIs**: Use official APIs when available
4. **Respect rate limits**: Add delays between requests
5. **Don't overload servers**: Be a good internet citizen

### Ethical Scraping Practices

```python
import time

# Add delays between requests
for url in urls:
    driver.get(url)
    # Scrape data
    time.sleep(2)  # 2 second delay

# Use reasonable User-Agent
options.add_argument('user-agent=Mozilla/5.0 (compatible; MyBot/1.0; +https://mysite.com/bot)')

# Handle robots.txt
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://example.com/robots.txt")
rp.read()
if rp.can_fetch("*", "/page-to-scrape"):
    # OK to scrape
    pass
```

---

## 14. Troubleshooting

### Problem: Element not found

**Solutions:**
1. Use explicit wait
2. Check if element is in iframe
3. Verify selector is correct
4. Check if page finished loading

### Problem: Element not clickable

**Solutions:**
1. Wait for element to be clickable
2. Scroll element into view
3. Use JavaScript click
4. Wait for overlays to disappear

### Problem: Stale element

**Solutions:**
1. Re-find element after page changes
2. Use retry logic
3. Don't store element references across page loads

### Problem: Slow performance

**Solutions:**
1. Use headless mode
2. Disable images
3. Use CSS selectors (faster than XPath)
4. Reuse driver instance

---

## 15. Additional Resources

- **Official Documentation**: https://selenium-python.readthedocs.io/
- **WebDriver Manager**: https://github.com/SergeyPirogov/webdriver_manager
- **Practice Sites**:
  - http://books.toscrape.com/
  - http://quotes.toscrape.com/
  - https://the-internet.herokuapp.com/

---

**End of Documentation**
