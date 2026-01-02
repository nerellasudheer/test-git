# Flask - Web Framework for ML Model Deployment

> **What is it?** Lightweight web framework for building APIs and web apps
> **Install:** `pip install flask`
> **Import as:** `from flask import Flask`

---

## Table of Contents

1. [What is Flask?](#1-what-is-flask)
2. [Installation](#2-installation)
3. [Your First Flask App](#3-your-first-flask-app)
4. [Routes and URLs](#4-routes-and-urls)
5. [HTTP Methods (GET, POST)](#5-http-methods-get-post)
6. [Request and Response](#6-request-and-response)
7. [JSON APIs](#7-json-apis)
8. [Templates (HTML)](#8-templates-html)
9. [Deploying ML Models](#9-deploying-ml-models)
10. [File Uploads](#10-file-uploads)
11. [Error Handling](#11-error-handling)
12. [Real-World ML API Example](#12-real-world-ml-api-example)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is Flask?

### Simple Explanation

Flask is a tool that lets you **turn your Python code into a web application or API**.

```
Why Flask for AI/ML?

You trained a model:
- Image classifier (cat vs dog)
- Sentiment analyzer
- Price predictor

But how do others use it?
- They can't run your Python code
- They don't have Python installed
- They need a simple interface

Flask solution:
- Create a web API
- User sends data (image, text)
- Your model processes it
- API returns prediction
- Works from any device/language!

Example:
User → sends image → Flask API → your model → "This is a cat" → User
```

### Flask vs Django

| Flask | Django |
|-------|--------|
| Lightweight | Full-featured |
| Simple | Complex |
| Flexible | Opinionated |
| Best for APIs, small apps | Best for large apps |
| Learn in hours | Learn in weeks |

**For ML deployment: Flask is the better choice!**

---

## 2. Installation

```bash
# Install Flask
pip install flask

# Verify
python -c "import flask; print(flask.__version__)"
```

### Project Structure

```
my_flask_app/
├── app.py              # Main application
├── templates/          # HTML files
│   └── index.html
├── static/             # CSS, JS, images
│   └── style.css
├── models/             # ML models
│   └── model.pkl
└── requirements.txt    # Dependencies
```

---

## 3. Your First Flask App

### 3.1 Hello World

```python
# app.py
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Run the App

```bash
# In terminal
python app.py

# Output:
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
```

### Open in Browser

```
Open: http://127.0.0.1:5000/
You'll see: Hello, World!
```

### 3.2 Understanding the Code

```python
from flask import Flask

# Create app instance
# __name__ tells Flask where to find resources
app = Flask(__name__)

# @app.route('/') is a decorator
# It maps URL '/' to this function
@app.route('/')
def home():
    return 'Hello, World!'  # This is returned to browser

# Only run if this file is executed directly
if __name__ == '__main__':
    # debug=True: Auto-reload on code changes, show errors
    app.run(debug=True)
```

---

## 4. Routes and URLs

### 4.1 Basic Routes

```python
from flask import Flask

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return 'Home Page'

# About page
@app.route('/about')
def about():
    return 'About Page'

# Contact page
@app.route('/contact')
def contact():
    return 'Contact Page'

if __name__ == '__main__':
    app.run(debug=True)

# URLs:
# http://127.0.0.1:5000/         → Home Page
# http://127.0.0.1:5000/about    → About Page
# http://127.0.0.1:5000/contact  → Contact Page
```

### 4.2 Dynamic Routes (URL Parameters)

```python
from flask import Flask

app = Flask(__name__)

# Dynamic route with variable
@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'

# With type conversion
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# Multiple parameters
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f'{username}\'s post #{post_id}'

if __name__ == '__main__':
    app.run(debug=True)

# URLs:
# /user/john          → Hello, john!
# /post/123           → Post ID: 123
# /user/john/post/1   → john's post #1
```

### 4.3 URL Converters

| Converter | Description | Example |
|-----------|-------------|---------|
| `string` | Default, any text | `/user/<username>` |
| `int` | Integer | `/post/<int:id>` |
| `float` | Float | `/price/<float:amount>` |
| `path` | String with slashes | `/file/<path:filepath>` |

---

## 5. HTTP Methods (GET, POST)

### 5.1 Understanding HTTP Methods

```
GET:  Request data (view page, fetch info)
POST: Send data (submit form, upload file)

Example:
- View product page → GET /product/123
- Submit order → POST /order
```

### 5.2 Handling Different Methods

```python
from flask import Flask, request

app = Flask(__name__)

# GET only (default)
@app.route('/search')
def search():
    query = request.args.get('q', '')  # Get query parameter
    return f'Searching for: {query}'

# GET and POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Logging in {username}...'
    else:
        return '''
            <form method="post">
                <input name="username" placeholder="Username">
                <input name="password" type="password" placeholder="Password">
                <button type="submit">Login</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)

# URLs:
# GET /search?q=python    → Searching for: python
# GET /login              → Shows form
# POST /login             → Processes form
```

---

## 6. Request and Response

### 6.1 Accessing Request Data

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    # GET parameters (URL query string)
    # URL: /example?name=John&age=25
    name = request.args.get('name')
    age = request.args.get('age', type=int)

    # POST form data
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

    # JSON data
    if request.is_json:
        data = request.get_json()
        value = data.get('key')

    # Headers
    user_agent = request.headers.get('User-Agent')
    content_type = request.headers.get('Content-Type')

    # Files
    if 'file' in request.files:
        file = request.files['file']
        filename = file.filename

    return 'OK'
```

### 6.2 Creating Responses

```python
from flask import Flask, jsonify, make_response, redirect, url_for

app = Flask(__name__)

# Simple text response
@app.route('/text')
def text_response():
    return 'Plain text response'

# JSON response
@app.route('/json')
def json_response():
    data = {'name': 'John', 'age': 25, 'active': True}
    return jsonify(data)

# Custom status code
@app.route('/error')
def error_response():
    return 'Not Found', 404

# Custom response with headers
@app.route('/custom')
def custom_response():
    response = make_response('Custom response')
    response.headers['X-Custom-Header'] = 'Custom Value'
    response.status_code = 201
    return response

# Redirect
@app.route('/old-page')
def old_page():
    return redirect(url_for('home'))  # Redirect to home()

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 7. JSON APIs

### 7.1 Creating a JSON API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
]

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

# GET single user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# POST create user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data.get('email', '')
    }
    users.append(new_user)

    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### 7.2 Testing with curl

```bash
# GET all users
curl http://127.0.0.1:5000/api/users

# GET single user
curl http://127.0.0.1:5000/api/users/1

# POST new user
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Charlie", "email": "charlie@example.com"}'
```

### 7.3 Testing with Python requests

```python
import requests

# GET all users
response = requests.get('http://127.0.0.1:5000/api/users')
print(response.json())

# POST new user
data = {'name': 'Charlie', 'email': 'charlie@example.com'}
response = requests.post('http://127.0.0.1:5000/api/users', json=data)
print(response.json())
```

---

## 8. Templates (HTML)

### 8.1 Basic Template

```
Project structure:
my_app/
├── app.py
└── templates/
    └── index.html
```

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
    <p>This is a simple Flask application.</p>
</body>
</html>
```

```html
<!-- templates/greet.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

### 8.2 Template with Variables

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user_profile(username):
    user = {
        'name': username,
        'age': 25,
        'hobbies': ['reading', 'gaming', 'coding']
    }
    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/profile.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ user.name }}'s Profile</title>
</head>
<body>
    <h1>{{ user.name }}</h1>
    <p>Age: {{ user.age }}</p>

    <h2>Hobbies:</h2>
    <ul>
    {% for hobby in user.hobbies %}
        <li>{{ hobby }}</li>
    {% endfor %}
    </ul>

    {% if user.age >= 18 %}
        <p>You are an adult.</p>
    {% else %}
        <p>You are a minor.</p>
    {% endif %}
</body>
</html>
```

---

## 9. Deploying ML Models

### 9.1 Simple Model Deployment

```python
# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return 'ML Model API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data
    data = request.get_json()

    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400

    # Convert to numpy array
    features = np.array(data['features']).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Return result
    return jsonify({
        'prediction': int(prediction[0]),
        'features': data['features']
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### 9.2 Train and Save Model First

```python
# train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print(f"Model accuracy: {model.score(X_test, y_test):.2f}")

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved to model.pkl")
```

### 9.3 Test the API

```python
# test_api.py
import requests

# API endpoint
url = 'http://127.0.0.1:5000/predict'

# Test data (iris features: sepal length, sepal width, petal length, petal width)
data = {
    'features': [5.1, 3.5, 1.4, 0.2]  # Should predict setosa (0)
}

# Send request
response = requests.post(url, json=data)
print(response.json())
# Output: {'prediction': 0, 'features': [5.1, 3.5, 1.4, 0.2]}
```

---

## 10. File Uploads

### 10.1 Image Upload for ML

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'path': filepath
        })

    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### 10.2 Image Classification API

```python
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow import keras
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs('uploads', exist_ok=True)

# Load pre-trained model
model = keras.models.load_model('image_classifier.keras')
class_names = ['cat', 'dog']  # Your classes

def preprocess_image(filepath):
    """Preprocess image for model"""
    img = Image.open(filepath)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Preprocess and predict
        img_array = preprocess_image(filepath)
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))

        # Clean up
        os.remove(filepath)

        return jsonify({
            'prediction': predicted_class,
            'confidence': f'{confidence:.2%}',
            'all_predictions': {
                name: f'{prob:.2%}'
                for name, prob in zip(class_names, predictions[0])
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 11. Error Handling

### 11.1 Custom Error Pages

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Handle 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Handle 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Handle specific exceptions
@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({'error': str(error)}), 400

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return jsonify({'result': a / b})

if __name__ == '__main__':
    app.run(debug=True)
```

### 11.2 Try-Except in Routes

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        if 'features' not in data:
            return jsonify({'error': 'Missing features'}), 400

        # Process prediction
        features = data['features']
        # prediction = model.predict(features)

        return jsonify({'prediction': 'success'})

    except KeyError as e:
        return jsonify({'error': f'Missing key: {e}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid value: {e}'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 12. Real-World ML API Example

### Complete Sentiment Analysis API

```python
# app.py
from flask import Flask, request, jsonify, render_template
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download required data
nltk.download('vader_lexicon', quiet=True)

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return '''
    <h1>Sentiment Analysis API</h1>
    <h2>Endpoints:</h2>
    <ul>
        <li>POST /api/analyze - Analyze single text</li>
        <li>POST /api/analyze/batch - Analyze multiple texts</li>
    </ul>
    <h2>Try it:</h2>
    <form action="/api/analyze" method="post" id="form">
        <textarea name="text" rows="4" cols="50" placeholder="Enter text to analyze..."></textarea><br>
        <button type="submit">Analyze</button>
    </form>
    <script>
        document.getElementById('form').onsubmit = async (e) => {
            e.preventDefault();
            const text = document.querySelector('textarea').value;
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            });
            const result = await response.json();
            alert(JSON.stringify(result, null, 2));
        };
    </script>
    '''

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze sentiment of a single text"""
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    scores = sia.polarity_scores(text)

    # Determine sentiment
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'scores': {
            'positive': scores['pos'],
            'negative': scores['neg'],
            'neutral': scores['neu'],
            'compound': scores['compound']
        }
    })

@app.route('/api/analyze/batch', methods=['POST'])
def analyze_batch():
    """Analyze sentiment of multiple texts"""
    data = request.get_json()

    if not data or 'texts' not in data:
        return jsonify({'error': 'No texts provided'}), 400

    results = []
    for text in data['texts']:
        scores = sia.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            sentiment = 'positive'
        elif compound <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        results.append({
            'text': text,
            'sentiment': sentiment,
            'compound': compound
        })

    # Summary
    sentiments = [r['sentiment'] for r in results]
    summary = {
        'total': len(results),
        'positive': sentiments.count('positive'),
        'negative': sentiments.count('negative'),
        'neutral': sentiments.count('neutral')
    }

    return jsonify({
        'results': results,
        'summary': summary
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Test the API

```python
# test_sentiment_api.py
import requests

BASE_URL = 'http://127.0.0.1:5000'

# Test single analysis
print("Single text analysis:")
response = requests.post(
    f'{BASE_URL}/api/analyze',
    json={'text': 'I absolutely love this product! It is amazing!'}
)
print(response.json())

# Test batch analysis
print("\nBatch analysis:")
response = requests.post(
    f'{BASE_URL}/api/analyze/batch',
    json={
        'texts': [
            'Great product, highly recommend!',
            'Terrible experience, waste of money.',
            'It is okay, nothing special.',
            'Best purchase I ever made!'
        ]
    }
)
print(response.json())
```

---

## 13. Quick Reference

### Basic App Structure

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello!'

@app.route('/api/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'result': 'success'})
    return jsonify({'message': 'GET request'})

if __name__ == '__main__':
    app.run(debug=True)
```

### Common Imports

```python
from flask import (
    Flask,
    request,          # Access request data
    jsonify,          # Create JSON response
    render_template,  # Render HTML
    redirect,         # Redirect to URL
    url_for,          # Build URL
    make_response,    # Custom response
    abort             # Abort with error
)
```

### Request Object

| Property | Description | Example |
|----------|-------------|---------|
| `request.args` | URL parameters | `request.args.get('q')` |
| `request.form` | Form data | `request.form['name']` |
| `request.json` | JSON data | `request.get_json()` |
| `request.files` | Uploaded files | `request.files['file']` |
| `request.method` | HTTP method | `'GET'` or `'POST'` |
| `request.headers` | HTTP headers | `request.headers['Content-Type']` |

### Response Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful request |
| 201 | Created | Resource created |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Auth required |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Something went wrong |

### ML Deployment Template

```python
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0].tolist()})

if __name__ == '__main__':
    app.run(debug=True)
```

### Run Commands

```bash
# Development
python app.py

# Production (use gunicorn)
pip install gunicorn
gunicorn app:app -w 4 -b 0.0.0.0:5000
```

---

## Summary

Flask is essential for deploying ML models:

1. **Create app** - `app = Flask(__name__)`
2. **Define routes** - `@app.route('/path')`
3. **Handle methods** - `methods=['GET', 'POST']`
4. **Get data** - `request.get_json()`
5. **Return JSON** - `jsonify(data)`
6. **Load model** - `pickle.load()` or `keras.models.load_model()`
7. **Make predictions** - `model.predict()`
8. **Return results** - JSON response

Master these basics and you can deploy any ML model as an API!
