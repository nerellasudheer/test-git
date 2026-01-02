# Python Requests Library

## Overview

**Requests** is a simple, elegant HTTP library for Python that allows you to send HTTP requests (GET, POST, PUT, DELETE, etc.) to web servers and interact with web APIs. It's often described as "HTTP for Humans" because it simplifies web interactions.

### Main Purpose and Use Cases
- Making HTTP requests to web APIs and websites
- Fetching data from RESTful APIs (JSON, XML, HTML)
- Submitting forms and uploading files
- Authenticating with web services
- Downloading files from the internet
- Web scraping (combined with BeautifulSoup)

### Installation
```bash
pip install requests

# Import convention
import requests
```

---

## Core Components

### HTTP Methods Functions
| Method | Purpose | Example |
|--------|---------|---------|
| `requests.get()` | Retrieve data | Fetch API data |
| `requests.post()` | Send data | Submit forms |
| `requests.put()` | Update/replace data | Update user profile |
| `requests.patch()` | Partial update | Change email only |
| `requests.delete()` | Remove data | Delete account |

### HTTP Status Codes
| Code Range | Meaning | Common Codes |
|------------|---------|--------------|
| 200-299 | Success | 200 (OK), 201 (Created) |
| 300-399 | Redirect | 301 (Moved), 302 (Found) |
| 400-499 | Client Error | 400 (Bad Request), 404 (Not Found), 401 (Unauthorized) |
| 500-599 | Server Error | 500 (Internal Error), 503 (Unavailable) |

---

## GET Requests

### Basic Syntax
```python
requests.get(url, params=None, headers=None, timeout=None, verify=True)
```

### Parameters
- `url` (str): The URL to request - **REQUIRED**
- `params` (dict): URL query parameters - Optional
- `headers` (dict): HTTP headers to send - Optional
- `timeout` (float/tuple): Request timeout in seconds - Optional (recommended)
- `verify` (bool): Verify SSL certificates - Optional (default: True)
- `auth` (tuple): Username/password for authentication - Optional

### Basic Example
```python
import requests

# Simple GET request
response = requests.get('https://api.github.com')
print(response.status_code)
# Output: 200

print(response.text[:100])
# Output: First 100 characters of response
```

### Real-World Example
```python
# Fetch GitHub user information
username = 'torvalds'
url = f'https://api.github.com/users/{username}'

response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    print(f"Name: {user_data['name']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
# Output:
# Name: Linus Torvalds
# Public Repos: 6
# Followers: 195000+
```

### Using Query Parameters
```python
# Search GitHub repositories
url = 'https://api.github.com/search/repositories'
params = {
    'q': 'python requests',
    'sort': 'stars',
    'order': 'desc'
}

response = requests.get(url, params=params)
data = response.json()

print(f"Total results: {data['total_count']}")
print(f"Top repo: {data['items'][0]['name']}")
```

---

## POST Requests

### Basic Syntax
```python
requests.post(url, data=None, json=None, files=None, headers=None, timeout=None)
```

### Parameters
- `url` (str): The URL to send data to - **REQUIRED**
- `data` (dict): Form data to send - Optional
- `json` (dict): JSON data to send - Optional
- `files` (dict): Files to upload - Optional

### Basic Example
```python
# Send form data
url = 'https://httpbin.org/post'
data = {'username': 'john', 'password': 'secret123'}

response = requests.post(url, data=data)
print(response.status_code)
# Output: 200
```

### Sending JSON Data
```python
# API request with JSON
url = 'https://api.example.com/users'
json_data = {'name': 'Alice', 'age': 30}

response = requests.post(url, json=json_data)
# Automatically sets Content-Type: application/json
```

### JSON vs Form Data
```python
# JSON data (Content-Type: application/json)
json_data = {'name': 'Alice', 'age': 30}
response = requests.post(url, json=json_data)

# Form data (Content-Type: application/x-www-form-urlencoded)
form_data = {'name': 'Alice', 'age': '30'}
response = requests.post(url, data=form_data)
```

---

## Other HTTP Methods

### PUT - Replace Resource
```python
url = 'https://api.example.com/users/123'
updated_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.put(url, json=updated_data)
print(response.status_code)
# Output: 200 or 204
```

### DELETE - Remove Resource
```python
url = 'https://api.example.com/items/456'
response = requests.delete(url)

if response.status_code == 204:
    print("Item deleted successfully")
```

### PATCH - Partial Update
```python
url = 'https://api.example.com/users/123'
partial_update = {'email': 'newemail@example.com'}

response = requests.patch(url, json=partial_update)
# Only email is updated, other fields remain unchanged
```

---

## Response Object

### Key Attributes
```python
response = requests.get('https://api.github.com')

# Status information
response.status_code          # 200
response.ok                   # True if status < 400
response.reason               # 'OK'

# Content in different formats
response.text                 # String content
response.content              # Bytes content
response.json()               # Parsed JSON (if applicable)

# Headers and metadata
response.headers              # Response headers dict
response.url                  # Final URL after redirects
response.encoding             # Content encoding
response.elapsed              # Request duration
```

### Checking Status
```python
response = requests.get(url)

# Method 1: Direct comparison
if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print("Not found")

# Method 2: Check if successful (2xx range)
if response.ok:  # True for 200-299
    print("Request successful")

# Method 3: Raise exception for errors
try:
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx
    print("Success")
except requests.HTTPError as e:
    print(f"Error: {e}")
```

---

## Headers and Authentication

### Custom Headers
```python
url = 'https://api.example.com/data'
headers = {
    'Authorization': 'Bearer your-api-key-here',
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
```

### Basic Authentication
```python
from requests.auth import HTTPBasicAuth

url = 'https://api.example.com/protected'

# Method 1: Using auth tuple
response = requests.get(url, auth=('username', 'password'))

# Method 2: Using HTTPBasicAuth
response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
```

### Bearer Token Authentication
```python
url = 'https://api.example.com/user'
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

response = requests.get(url, headers=headers)
```

---

## File Operations

### Downloading Files
```python
# Download an image
url = 'https://example.com/image.jpg'
response = requests.get(url)

with open('downloaded_image.jpg', 'wb') as f:
    f.write(response.content)

print("File downloaded successfully")
```

### Downloading Large Files (Memory Efficient)
```python
url = 'https://example.com/large_dataset.zip'
local_filename = 'dataset.zip'

response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(local_filename, 'wb') as f:
    downloaded = 0
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            downloaded += len(chunk)
            progress = (downloaded / total_size) * 100
            print(f"Downloaded: {progress:.1f}%", end='\r')

print("\nDownload complete!")
```

### Uploading Files
```python
# Upload single file
url = 'https://httpbin.org/post'
files = {'file': open('document.pdf', 'rb')}

response = requests.post(url, files=files)

# Upload with additional form data
files = {'document': open('report.pdf', 'rb')}
data = {
    'title': 'Monthly Report',
    'category': 'Finance'
}

response = requests.post(url, files=files, data=data)
```

---

## Session Object

### Purpose
- Maintains cookies automatically
- Reuses TCP connections (faster)
- Can set default headers for all requests
- Useful for authenticated workflows

### Basic Usage
```python
session = requests.Session()

# Set default headers for all requests
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Make multiple requests
response1 = session.get('https://httpbin.org/cookies/set/sessionid/123')
response2 = session.get('https://httpbin.org/cookies')

print(response2.json())
# Output: {'cookies': {'sessionid': '123'}}
# Cookie automatically persisted!
```

### Login Workflow Example
```python
session = requests.Session()

# Step 1: Login
login_url = 'https://example.com/api/login'
credentials = {'username': 'user@example.com', 'password': 'secret'}
login_response = session.post(login_url, json=credentials)

if login_response.status_code == 200:
    print("Login successful")

    # Step 2: Access protected resources
    profile_url = 'https://example.com/api/profile'
    profile = session.get(profile_url)

    # Step 3: Logout
    logout_url = 'https://example.com/api/logout'
    session.post(logout_url)
```

---

## Timeout Configuration

### Setting Timeouts
```python
# Single timeout value (5 seconds)
response = requests.get('https://httpbin.org/delay/3', timeout=5)

# Different timeouts for connect vs read
# 3 seconds to connect, 10 seconds to read response
response = requests.get(url, timeout=(3, 10))
```

### Handling Timeouts
```python
try:
    response = requests.get(url, timeout=5)
    data = response.json()
except requests.ConnectTimeout:
    print("Could not connect to server")
except requests.ReadTimeout:
    print("Server took too long to respond")
except requests.Timeout:
    print("Request timed out")
```

---

## Exception Handling

### Common Exceptions
```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError

url = 'https://api.example.com/data'

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise error for 4xx/5xx
    data = response.json()
    print(f"Success: Retrieved {len(data)} items")

except Timeout:
    print("Request timed out - server too slow")

except ConnectionError:
    print("Connection failed - check internet or DNS")

except HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print(f"Status code: {response.status_code}")

except RequestException as e:
    print(f"General request error: {e}")

except ValueError:
    print("Response is not valid JSON")
```

### Robust Function with Retries
```python
def fetch_api_data(url, max_retries=3):
    """Robust API data fetching with retries"""

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()

        except Timeout:
            print(f"Attempt {attempt + 1}: Timeout")
            if attempt == max_retries - 1:
                return None

        except ConnectionError:
            print(f"Attempt {attempt + 1}: Connection failed")
            if attempt == max_retries - 1:
                return None

        except HTTPError as e:
            if response.status_code == 404:
                print("Resource not found")
                return None  # Don't retry for 404
            elif response.status_code >= 500:
                print(f"Attempt {attempt + 1}: Server error")
            else:
                return None

    return None

# Usage
data = fetch_api_data('https://api.example.com/users')
if data:
    print(f"Retrieved {len(data)} users")
```

---

## Best Practices

### 1. Always Use Timeout
```python
# Good
response = requests.get(url, timeout=5)

# Bad - Can hang forever!
response = requests.get(url)
```

### 2. Check Response Status
```python
# Good
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")

# Or use raise_for_status()
response.raise_for_status()
```

### 3. Use Sessions for Multiple Requests
```python
# Good - Reuses connection
session = requests.Session()
for url in urls:
    response = session.get(url)

# Bad - Creates new connection each time
for url in urls:
    response = requests.get(url)  # Slower!
```

### 4. Stream Large Files
```python
# Good - Memory efficient
response = requests.get(url, stream=True)
for chunk in response.iter_content(chunk_size=8192):
    f.write(chunk)

# Bad - Loads entire file into memory
response = requests.get(url)
f.write(response.content)  # May cause MemoryError!
```

### 5. Use json Parameter for JSON Data
```python
# Good - Automatic JSON encoding
data = {'name': 'Alice', 'age': 30}
response = requests.post(url, json=data)

# Bad - Manual encoding
import json
data_str = json.dumps({'name': 'Alice', 'age': 30})
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=data_str, headers=headers)
```

### 6. Set User-Agent Header
```python
# Good
headers = {'User-Agent': 'MyApp/1.0 (contact@example.com)'}
response = requests.get(url, headers=headers)

# Bad - Default: python-requests/X.X.X
response = requests.get(url)  # May be blocked
```

---

## Common Mistakes

### Mistake 1: No Exception Handling
```python
# Wrong - Crashes if network fails
response = requests.get('https://api.example.com/data')
data = response.json()

# Correct - Handles errors gracefully
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

### Mistake 2: No Timeout
```python
# Wrong - Can hang forever
response = requests.get('https://slow-server.com/data')

# Correct - Fails gracefully
try:
    response = requests.get('https://slow-server.com/data', timeout=5)
except requests.Timeout:
    print("Server took too long to respond")
```

### Mistake 3: Not Checking Status Code
```python
# Wrong - Assumes success
response = requests.get('https://api.example.com/users/99999')
data = response.json()
print(data['name'])  # KeyError if user doesn't exist!

# Correct - Checks status
response = requests.get('https://api.example.com/users/99999')
if response.status_code == 200:
    data = response.json()
    print(data['name'])
elif response.status_code == 404:
    print("User not found")
```

### Mistake 4: Using GET for Modifications
```python
# Wrong - Using GET to delete
requests.get('https://api.example.com/delete?id=123')

# Correct - Use appropriate method
requests.delete('https://api.example.com/items/123')
```

### Mistake 5: Disabling SSL Verification
```python
# Wrong - Security risk!
response = requests.get('https://api.example.com', verify=False)

# Correct - Always verify certificates
response = requests.get('https://api.example.com', verify=True)
```

---

## Commonly Confused Concepts

### response.text vs response.content vs response.json()

| Attribute | Returns | Use For |
|-----------|---------|---------|
| `.text` | string (decoded) | HTML, XML, text |
| `.content` | bytes (raw) | Binary files (images, PDFs) |
| `.json()` | dict/list (parsed) | API responses |

```python
# Text (string)
html = response.text
print(type(html))  # <class 'str'>

# Content (bytes)
image_bytes = response.content
print(type(image_bytes))  # <class 'bytes'>

# JSON (dict)
data = response.json()
print(type(data))  # <class 'dict'>
```

### data vs json vs files Parameters

| Parameter | Content-Type | Use For |
|-----------|--------------|---------|
| `data` | application/x-www-form-urlencoded | HTML forms |
| `json` | application/json | REST APIs |
| `files` | multipart/form-data | File uploads |

---

## Automatic Retries with urllib3

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

# Configure automatic retries
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Automatically retries on failure
response = session.get(url, timeout=5)
```

---

## Quick Reference Summary

| Category | Methods/Functions | Purpose | Example |
|----------|------------------|---------|---------|
| **Basic Requests** | `get()`, `post()` | Fetch/send data | `requests.get(url)` |
| **Response Access** | `.text`, `.json()` | Get response data | `response.json()` |
| **Sessions** | `Session()` | Persistent connections | `session = Session()` |
| **Error Handling** | `.raise_for_status()` | Check status | `response.raise_for_status()` |
| **File Operations** | `stream=True` | Download files | `get(url, stream=True)` |
| **Authentication** | `auth` parameter | Login | `get(url, auth=(...))` |

---

## Status Codes Quick Reference

| Code | Meaning | How to Handle |
|------|---------|---------------|
| **200** | OK | Process normally |
| **201** | Created | Confirm creation |
| **204** | No Content | Check status only |
| **400** | Bad Request | Check your data |
| **401** | Unauthorized | Add authentication |
| **403** | Forbidden | Check permissions |
| **404** | Not Found | Verify URL |
| **429** | Too Many Requests | Implement retry |
| **500** | Server Error | Retry later |
| **503** | Unavailable | Wait and retry |
