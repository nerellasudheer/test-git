# Flask - Complete Beginner's Guide

## Lightweight Web Framework for Python

---

# PART 1: WHAT IS FLASK?

---

## 1.1 Simple Explanation

**Flask** is a lightweight Python web framework that helps you build websites and web applications.

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLASK EXPLAINED                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Think of Flask like a RESTAURANT:                              │
│                                                                  │
│  User (Customer) → Browser Request → Flask (Waiter) → Response  │
│                                                                  │
│  1. Customer orders food (User visits URL)                      │
│  2. Waiter takes order to kitchen (Flask routes request)        │
│  3. Kitchen prepares food (Your Python code runs)               │
│  4. Waiter delivers food (Flask sends response)                 │
│                                                                  │
│  Flask is the "waiter" connecting users to your code!           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Why Flask?

| Feature | Benefit |
|---------|---------|
| **Lightweight** | Minimal setup, no unnecessary features |
| **Flexible** | Add only what you need |
| **Easy to Learn** | Simple syntax, beginner-friendly |
| **Great Documentation** | Well-documented with many tutorials |
| **Large Community** | Lots of extensions and support |
| **Scalable** | From small projects to large applications |

---

## 1.3 Flask vs Django

| Feature | Flask | Django |
|---------|-------|--------|
| **Philosophy** | "Micro" framework | "Batteries included" |
| **Learning Curve** | Easier | Steeper |
| **Flexibility** | High - choose your tools | Lower - comes with tools |
| **Built-in Admin** | No | Yes |
| **ORM** | No (use SQLAlchemy) | Yes (Django ORM) |
| **Best For** | Small to medium apps, APIs | Large, complex applications |

---

# PART 2: INSTALLATION & SETUP

---

## 2.1 Installation

```bash
# Create virtual environment (recommended!)
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Install Flask
pip install flask
```

---

## 2.2 Verify Installation

```python
import flask
print(flask.__version__)  # Output: 3.0.0 (or similar)
```

---

## 2.3 Project Structure

```
my_flask_app/
├── venv/                  # Virtual environment
├── app.py                 # Main application file
├── templates/             # HTML templates
│   ├── base.html
│   └── index.html
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt       # Dependencies
└── .env                   # Environment variables
```

---

# PART 3: YOUR FIRST FLASK APP

---

## 3.1 Minimal Flask Application

```python
# app.py
from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define a route (URL endpoint)
@app.route('/')
def home():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Run it:**
```bash
python app.py
```

**Output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

Open browser → `http://127.0.0.1:5000` → See "Hello, World!"

---

## 3.2 Understanding the Code

```python
from flask import Flask          # Import Flask class

app = Flask(__name__)            # Create app instance
                                 # __name__ tells Flask where to find resources

@app.route('/')                  # Decorator: URL that triggers this function
def home():                      # View function (handles the request)
    return 'Hello, World!'       # Response sent to browser

if __name__ == '__main__':       # Only run if this file is executed directly
    app.run(debug=True)          # Start development server
                                 # debug=True enables auto-reload & error details
```

---

# PART 4: ROUTING

---

## 4.1 Basic Routes

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
```

**URLs:**
- `http://127.0.0.1:5000/` → "Home Page"
- `http://127.0.0.1:5000/about` → "About Page"
- `http://127.0.0.1:5000/contact` → "Contact Page"

---

## 4.2 Dynamic Routes (URL Parameters)

```python
# Single parameter
@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'

# Multiple parameters
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# Multiple parameters
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f'{username}\'s post #{post_id}'
```

**URL Parameter Types:**

| Converter | Description | Example |
|-----------|-------------|---------|
| `string` | Default, any text without slash | `/user/<username>` |
| `int` | Integers only | `/post/<int:id>` |
| `float` | Floating point numbers | `/price/<float:amount>` |
| `path` | Like string but includes slashes | `/path/<path:subpath>` |

---

## 4.3 HTTP Methods

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
        return f'Logging in {username}'
    return 'Login Form'  # GET request

# Multiple methods
@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_data():
    if request.method == 'GET':
        return 'Getting data'
    elif request.method == 'POST':
        return 'Creating data'
    elif request.method == 'PUT':
        return 'Updating data'
    elif request.method == 'DELETE':
        return 'Deleting data'
```

---

# PART 5: TEMPLATES (HTML)

---

## 5.1 Rendering Templates

Flask uses **Jinja2** template engine to render HTML.

**Folder structure:**
```
my_app/
├── app.py
└── templates/
    └── index.html
```

**app.py:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
</body>
</html>
```

---

## 5.2 Template Variables

**app.py:**
```python
@app.route('/profile')
def profile():
    user = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 25
    }
    return render_template('profile.html', user=user)
```

**templates/profile.html:**
```html
<!DOCTYPE html>
<html>
<body>
    <h1>{{ user.name }}</h1>
    <p>Email: {{ user.email }}</p>
    <p>Age: {{ user.age }}</p>
</body>
</html>
```

---

## 5.3 Template Control Structures

**If/Else:**
```html
{% if user.is_admin %}
    <p>Welcome, Admin!</p>
{% elif user.is_member %}
    <p>Welcome, Member!</p>
{% else %}
    <p>Welcome, Guest!</p>
{% endif %}
```

**For Loop:**
```html
<ul>
{% for item in items %}
    <li>{{ item.name }} - ${{ item.price }}</li>
{% endfor %}
</ul>
```

**With Loop Index:**
```html
{% for item in items %}
    <p>{{ loop.index }}. {{ item }}</p>
{% endfor %}
```

---

## 5.4 Template Inheritance (Base Template)

**templates/base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 My Site</p>
    </footer>
</body>
</html>
```

**templates/home.html:**
```html
{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h1>Welcome Home!</h1>
    <p>This is the home page.</p>
{% endblock %}
```

---

# PART 6: STATIC FILES

---

## 6.1 Serving Static Files

**Folder structure:**
```
my_app/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
└── templates/
    └── index.html
```

**In templates:**
```html
<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- JavaScript -->
<script src="{{ url_for('static', filename='js/script.js') }}"></script>

<!-- Images -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

---

# PART 7: REQUEST DATA

---

## 7.1 Getting Request Data

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    # Query parameters: /search?q=flask&page=1
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    return f'Query: {query}, Page: {page}'

@app.route('/submit', methods=['POST'])
def submit():
    # Form data
    name = request.form.get('name')
    email = request.form.get('email')
    return f'Name: {name}, Email: {email}'

@app.route('/api/data', methods=['POST'])
def api_data():
    # JSON data
    data = request.get_json()
    return f'Received: {data}'
```

---

## 7.2 Request Object Properties

| Property | Description | Example |
|----------|-------------|---------|
| `request.args` | Query string parameters | `?name=john` |
| `request.form` | Form data (POST) | form fields |
| `request.json` | JSON data | API requests |
| `request.files` | Uploaded files | file uploads |
| `request.method` | HTTP method | GET, POST, etc. |
| `request.headers` | Request headers | Auth tokens |
| `request.cookies` | Cookies | session data |

---

# PART 8: RESPONSES

---

## 8.1 Different Response Types

```python
from flask import Flask, jsonify, redirect, url_for, make_response

app = Flask(__name__)

# Plain text
@app.route('/text')
def text_response():
    return 'Plain text response'

# HTML (from template)
@app.route('/html')
def html_response():
    return render_template('page.html')

# JSON (for APIs)
@app.route('/api/users')
def json_response():
    users = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'}
    ]
    return jsonify(users)

# Redirect
@app.route('/old-page')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return 'This is the new page'

# Custom response with status code
@app.route('/error')
def error_response():
    return 'Not Found', 404

# Custom response with headers
@app.route('/custom')
def custom_response():
    response = make_response('Custom response')
    response.headers['X-Custom-Header'] = 'Value'
    return response
```

---

# PART 9: FORMS & VALIDATION

---

## 9.1 Basic HTML Forms

**templates/contact.html:**
```html
<form method="POST" action="{{ url_for('contact') }}">
    <label>Name:</label>
    <input type="text" name="name" required>

    <label>Email:</label>
    <input type="email" name="email" required>

    <label>Message:</label>
    <textarea name="message" required></textarea>

    <button type="submit">Send</button>
</form>
```

**app.py:**
```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the form (save to database, send email, etc.)

        return f'Thanks {name}! We received your message.'

    return render_template('contact.html')
```

---

## 9.2 Using Flask-WTF (Recommended)

```bash
pip install flask-wtf
```

**forms.py:**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')
```

**app.py:**
```python
from flask import Flask, render_template
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for CSRF protection

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Process form...
        return f'Thanks {name}!'
    return render_template('contact.html', form=form)
```

**templates/contact.html:**
```html
<form method="POST">
    {{ form.hidden_tag() }}  <!-- CSRF token -->

    <p>{{ form.name.label }}<br>
       {{ form.name(size=32) }}
       {% for error in form.name.errors %}
           <span style="color: red;">{{ error }}</span>
       {% endfor %}
    </p>

    <p>{{ form.email.label }}<br>
       {{ form.email(size=32) }}</p>

    <p>{{ form.message.label }}<br>
       {{ form.message(rows=5, cols=40) }}</p>

    <p>{{ form.submit() }}</p>
</form>
```

---

# PART 10: DATABASE (SQLAlchemy)

---

## 10.1 Setup Flask-SQLAlchemy

```bash
pip install flask-sqlalchemy
```

**app.py:**
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create tables
with app.app_context():
    db.create_all()
```

---

## 10.2 CRUD Operations

```python
# CREATE - Add new user
@app.route('/user/create')
def create_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return f'User {user.username} created!'

# READ - Get all users
@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])

# READ - Get single user
@app.route('/user/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return f'User: {user.username}'

# UPDATE - Modify user
@app.route('/user/<int:id>/update')
def update_user(id):
    user = User.query.get_or_404(id)
    user.username = 'john_updated'
    db.session.commit()
    return f'User updated to {user.username}'

# DELETE - Remove user
@app.route('/user/<int:id>/delete')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return 'User deleted!'
```

---

## 10.3 Query Methods

```python
# Get all
users = User.query.all()

# Get first
user = User.query.first()

# Get by ID
user = User.query.get(1)
user = User.query.get_or_404(1)  # Returns 404 if not found

# Filter
users = User.query.filter_by(username='john').all()
users = User.query.filter(User.email.like('%@gmail.com')).all()

# Order
users = User.query.order_by(User.username).all()
users = User.query.order_by(User.id.desc()).all()

# Limit
users = User.query.limit(10).all()

# Count
count = User.query.count()

# Pagination
page = User.query.paginate(page=1, per_page=10)
```

---

# PART 11: SESSIONS & COOKIES

---

## 11.1 Using Sessions

```python
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for sessions

@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    session['logged_in'] = True
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return f'Welcome, {session["username"]}!'

@app.route('/logout')
def logout():
    session.clear()
    return 'Logged out!'
```

---

## 11.2 Using Cookies

```python
from flask import Flask, request, make_response

@app.route('/set-cookie')
def set_cookie():
    response = make_response('Cookie set!')
    response.set_cookie('username', 'john', max_age=3600)  # 1 hour
    return response

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username', 'Guest')
    return f'Hello, {username}!'

@app.route('/delete-cookie')
def delete_cookie():
    response = make_response('Cookie deleted!')
    response.delete_cookie('username')
    return response
```

---

# PART 12: ERROR HANDLING

---

## 12.1 Custom Error Pages

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403
```

**templates/404.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Page Not Found</h1>
    <p>Sorry, the page you're looking for doesn't exist.</p>
    <a href="{{ url_for('home') }}">Go Home</a>
{% endblock %}
```

---

# PART 13: BLUEPRINTS (Organizing Large Apps)

---

## 13.1 What are Blueprints?

Blueprints let you organize your app into modules.

**Project structure:**
```
my_app/
├── app.py
├── auth/
│   ├── __init__.py
│   └── routes.py
└── blog/
    ├── __init__.py
    └── routes.py
```

**auth/routes.py:**
```python
from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return 'Login Page'

@auth_bp.route('/register')
def register():
    return 'Register Page'
```

**app.py:**
```python
from flask import Flask
from auth.routes import auth_bp
from blog.routes import blog_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run(debug=True)
```

**URLs:**
- `/auth/login`
- `/auth/register`

---

# PART 14: REST API WITH FLASK

---

## 14.1 Building a Simple API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
todos = [
    {'id': 1, 'task': 'Learn Flask', 'done': False},
    {'id': 2, 'task': 'Build API', 'done': False}
]

# GET all todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET single todo
@app.route('/api/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if todo:
        return jsonify(todo)
    return jsonify({'error': 'Not found'}), 404

# POST create todo
@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        'id': len(todos) + 1,
        'task': data['task'],
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# PUT update todo
@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if not todo:
        return jsonify({'error': 'Not found'}), 404

    data = request.get_json()
    todo['task'] = data.get('task', todo['task'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo)

# DELETE todo
@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t['id'] != id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__':
    app.run(debug=True)
```

---

# PART 15: USEFUL FLASK EXTENSIONS

---

| Extension | Purpose | Install |
|-----------|---------|---------|
| **Flask-SQLAlchemy** | Database ORM | `pip install flask-sqlalchemy` |
| **Flask-WTF** | Forms & validation | `pip install flask-wtf` |
| **Flask-Login** | User authentication | `pip install flask-login` |
| **Flask-Migrate** | Database migrations | `pip install flask-migrate` |
| **Flask-Mail** | Email sending | `pip install flask-mail` |
| **Flask-CORS** | Cross-origin requests | `pip install flask-cors` |
| **Flask-RESTful** | REST API building | `pip install flask-restful` |

---

# PART 16: QUICK REFERENCE

---

```
┌─────────────────────────────────────────────────────────────────┐
│              FLASK QUICK REFERENCE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  BASIC APP:                                                      │
│  from flask import Flask                                        │
│  app = Flask(__name__)                                          │
│  app.run(debug=True)                                            │
│                                                                  │
│  ROUTES:                                                         │
│  @app.route('/')                    Basic route                 │
│  @app.route('/user/<name>')         Dynamic route               │
│  @app.route('/api', methods=['GET', 'POST'])  HTTP methods      │
│                                                                  │
│  TEMPLATES:                                                      │
│  render_template('page.html', var=value)                        │
│  {{ variable }}                     Print variable              │
│  {% if %} {% endif %}               Conditionals                │
│  {% for %} {% endfor %}             Loops                       │
│  {% extends 'base.html' %}          Inheritance                 │
│  {% block content %}{% endblock %}  Block                       │
│                                                                  │
│  REQUEST DATA:                                                   │
│  request.args.get('key')            Query params                │
│  request.form.get('key')            Form data                   │
│  request.get_json()                 JSON data                   │
│  request.method                     HTTP method                 │
│                                                                  │
│  RESPONSES:                                                      │
│  return 'text'                      Text                        │
│  return render_template('x.html')   HTML                        │
│  return jsonify(data)               JSON                        │
│  return redirect(url_for('view'))   Redirect                    │
│  return 'error', 404                With status code            │
│                                                                  │
│  URL BUILDING:                                                   │
│  url_for('view_function')           Get URL for view            │
│  url_for('static', filename='x')    Static file URL             │
│                                                                  │
│  DATABASE (SQLAlchemy):                                          │
│  db.session.add(obj)                Add record                  │
│  db.session.commit()                Save changes                │
│  Model.query.all()                  Get all                     │
│  Model.query.get(id)                Get by ID                   │
│  Model.query.filter_by(x=y)         Filter                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# SUMMARY

```
┌─────────────────────────────────────────────────────────────────┐
│                    KEY TAKEAWAYS                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Flask is a lightweight, flexible web framework              │
│  2. Create routes with @app.route() decorator                   │
│  3. Use render_template() for HTML pages                        │
│  4. Access request data with request object                     │
│  5. Return responses as text, HTML, JSON, or redirects          │
│  6. Use Flask-SQLAlchemy for databases                          │
│  7. Organize large apps with Blueprints                         │
│  8. Always use virtual environment for Flask projects           │
│                                                                  │
│  LEARNING PATH:                                                  │
│  Basics → Templates → Forms → Database → Auth → APIs            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Installation:** `pip install flask`

**Documentation:** https://flask.palletsprojects.com/
