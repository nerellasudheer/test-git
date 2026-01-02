# Django - Complete Beginner's Guide

## Full-Featured Web Framework for Python

---

# PART 1: WHAT IS DJANGO?

---

## 1.1 Simple Explanation

**Django** is a high-level Python web framework that encourages rapid development with a "batteries included" philosophy.

```
┌─────────────────────────────────────────────────────────────────┐
│                    DJANGO EXPLAINED                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Think of Django like a FULL RESTAURANT KIT:                    │
│                                                                  │
│  Flask = Waiter only (you build everything else)                │
│  Django = Full restaurant (waiter, kitchen, menu, tables)       │
│                                                                  │
│  Django comes with:                                              │
│  - Admin panel (manage data without coding)                     │
│  - User authentication (login, logout, register)                │
│  - Database ORM (talk to database with Python)                  │
│  - Form handling (validate user input)                          │
│  - Security features (CSRF, XSS protection)                     │
│                                                                  │
│  "Batteries Included" = Everything you need out of the box!     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Why Django?

| Feature | Benefit |
|---------|---------|
| **Batteries Included** | Most features built-in |
| **Admin Panel** | Free admin interface for your data |
| **Security** | Protection against common attacks |
| **Scalable** | Powers Instagram, Pinterest, Disqus |
| **ORM** | Database access without SQL |
| **Great Documentation** | Excellent official docs |
| **Large Community** | Thousands of packages available |

---

## 1.3 Django vs Flask

| Feature | Django | Flask |
|---------|--------|-------|
| **Philosophy** | "Batteries included" | "Micro" framework |
| **Built-in Admin** | Yes | No |
| **Built-in ORM** | Yes (Django ORM) | No (use SQLAlchemy) |
| **Built-in Auth** | Yes | No (use Flask-Login) |
| **Learning Curve** | Steeper | Easier |
| **Best For** | Large apps, CMS, e-commerce | Small apps, APIs |

---

# PART 2: INSTALLATION & SETUP

---

## 2.1 Installation

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install Django
pip install django

# Verify installation
django-admin --version
```

---

## 2.2 Create a Project

```bash
# Create new Django project
django-admin startproject myproject

# Navigate into project
cd myproject

# Run development server
python manage.py runserver
```

Open browser → `http://127.0.0.1:8000` → See Django welcome page!

---

## 2.3 Project Structure

```
myproject/                 # Root folder
├── manage.py              # Command-line utility
└── myproject/             # Project package
    ├── __init__.py        # Python package marker
    ├── settings.py        # Project settings
    ├── urls.py            # URL routing
    ├── asgi.py            # ASGI config (async)
    └── wsgi.py            # WSGI config (deployment)
```

---

## 2.4 Create an App

Django projects contain multiple **apps** (modules of functionality).

```bash
# Create a new app
python manage.py startapp blog

# Project structure now:
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   └── urls.py
└── blog/                  # New app!
    ├── __init__.py
    ├── admin.py           # Admin configuration
    ├── apps.py            # App configuration
    ├── migrations/        # Database migrations
    ├── models.py          # Database models
    ├── tests.py           # Tests
    └── views.py           # Views (request handlers)
```

**Register the app in settings.py:**
```python
# myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Add your app here!
]
```

---

# PART 3: MTV ARCHITECTURE

---

## 3.1 Model-Template-View

Django follows the **MTV** pattern (similar to MVC):

```
┌─────────────────────────────────────────────────────────────────┐
│                    DJANGO MTV PATTERN                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Request → URL Router → VIEW → (MODEL + TEMPLATE) → Response│
│                                                                  │
│  MODEL:                                                          │
│  - Defines database structure                                   │
│  - Handles data logic                                           │
│  - File: models.py                                              │
│                                                                  │
│  TEMPLATE:                                                       │
│  - HTML with Django template language                           │
│  - Presentation layer                                           │
│  - Folder: templates/                                           │
│                                                                  │
│  VIEW:                                                           │
│  - Handles requests                                             │
│  - Contains business logic                                      │
│  - File: views.py                                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 4: VIEWS & URLS

---

## 4.1 Function-Based Views

**blog/views.py:**
```python
from django.http import HttpResponse
from django.shortcuts import render

# Simple text response
def home(request):
    return HttpResponse('Hello, World!')

# Render template
def about(request):
    return render(request, 'about.html')

# With context data
def profile(request):
    context = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    return render(request, 'profile.html', context)
```

---

## 4.2 URL Configuration

**blog/urls.py:** (create this file)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]
```

**myproject/urls.py:** (main URL config)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include app URLs
]
```

---

## 4.3 Dynamic URLs

```python
# blog/urls.py
urlpatterns = [
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('category/<slug:slug>/', views.category, name='category'),
]
```

```python
# blog/views.py
def post_detail(request, id):
    return HttpResponse(f'Post ID: {id}')

def user_profile(request, username):
    return HttpResponse(f'User: {username}')
```

**URL Converters:**
| Converter | Description |
|-----------|-------------|
| `str` | Any non-empty string (default) |
| `int` | Integer |
| `slug` | Slug (letters, numbers, hyphens) |
| `uuid` | UUID |
| `path` | Any string including slashes |

---

# PART 5: TEMPLATES

---

## 5.1 Template Setup

Create templates folder in your app:
```
blog/
├── templates/
│   └── blog/
│       ├── base.html
│       ├── home.html
│       └── post_detail.html
```

---

## 5.2 Template Syntax

**blog/templates/blog/home.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}!</h1>

    <!-- If/Else -->
    {% if user.is_authenticated %}
        <p>You are logged in.</p>
    {% else %}
        <p>Please log in.</p>
    {% endif %}

    <!-- For Loop -->
    <ul>
    {% for post in posts %}
        <li>{{ post.title }} - {{ post.date }}</li>
    {% empty %}
        <li>No posts yet.</li>
    {% endfor %}
    </ul>

    <!-- URL Tag -->
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'post_detail' id=post.id %}">View Post</a>
</body>
</html>
```

---

## 5.3 Template Inheritance

**blog/templates/blog/base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
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

**blog/templates/blog/home.html:**
```html
{% extends 'blog/base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h1>Welcome!</h1>
    <p>This is the home page.</p>
{% endblock %}
```

---

## 5.4 Template Filters

```html
<!-- String filters -->
{{ name|upper }}              <!-- JOHN -->
{{ name|lower }}              <!-- john -->
{{ name|title }}              <!-- John Doe -->
{{ text|truncatewords:30 }}   <!-- First 30 words... -->
{{ text|truncatechars:100 }}  <!-- First 100 chars... -->

<!-- Date filters -->
{{ date|date:"F j, Y" }}      <!-- January 1, 2024 -->
{{ date|timesince }}          <!-- 2 days ago -->

<!-- Default values -->
{{ value|default:"N/A" }}     <!-- Shows "N/A" if empty -->

<!-- List filters -->
{{ items|length }}            <!-- Count of items -->
{{ items|first }}             <!-- First item -->
{{ items|last }}              <!-- Last item -->
{{ items|join:", " }}         <!-- "a, b, c" -->

<!-- Safe HTML -->
{{ html_content|safe }}       <!-- Render as HTML -->
```

---

# PART 6: MODELS (DATABASE)

---

## 6.1 Defining Models

**blog/models.py:**
```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

---

## 6.2 Field Types

| Field Type | Description | Example |
|------------|-------------|---------|
| `CharField` | Short text | `CharField(max_length=100)` |
| `TextField` | Long text | `TextField()` |
| `IntegerField` | Integer | `IntegerField()` |
| `FloatField` | Decimal | `FloatField()` |
| `BooleanField` | True/False | `BooleanField(default=False)` |
| `DateField` | Date | `DateField()` |
| `DateTimeField` | Date + Time | `DateTimeField()` |
| `EmailField` | Email | `EmailField()` |
| `URLField` | URL | `URLField()` |
| `SlugField` | URL-safe string | `SlugField()` |
| `ImageField` | Image file | `ImageField(upload_to='images/')` |
| `FileField` | Any file | `FileField(upload_to='files/')` |
| `ForeignKey` | Many-to-One | `ForeignKey(User, on_delete=CASCADE)` |
| `ManyToManyField` | Many-to-Many | `ManyToManyField(Tag)` |
| `OneToOneField` | One-to-One | `OneToOneField(Profile)` |

---

## 6.3 Migrations

```bash
# Create migrations (after model changes)
python manage.py makemigrations

# Apply migrations (create tables)
python manage.py migrate

# Show migrations status
python manage.py showmigrations

# Show SQL for a migration
python manage.py sqlmigrate blog 0001
```

---

## 6.4 QuerySet API (CRUD)

```python
from blog.models import Post, Category

# CREATE
post = Post.objects.create(
    title='My First Post',
    content='Hello World!',
    author=user
)
# Or
post = Post(title='My Post', content='Hello')
post.save()

# READ - Get all
posts = Post.objects.all()

# READ - Get one
post = Post.objects.get(id=1)
post = Post.objects.get(slug='my-post')

# READ - Filter
published = Post.objects.filter(status='published')
recent = Post.objects.filter(created_at__gte=date)
by_author = Post.objects.filter(author__username='john')

# READ - Exclude
not_draft = Post.objects.exclude(status='draft')

# READ - Order
posts = Post.objects.order_by('-created_at')  # Descending
posts = Post.objects.order_by('title')        # Ascending

# READ - Limit/Slice
first_5 = Post.objects.all()[:5]
posts_5_to_10 = Post.objects.all()[5:10]

# READ - Count
count = Post.objects.count()
count = Post.objects.filter(status='published').count()

# READ - Exists
exists = Post.objects.filter(title='Test').exists()

# UPDATE
post = Post.objects.get(id=1)
post.title = 'Updated Title'
post.save()

# UPDATE - Bulk
Post.objects.filter(status='draft').update(status='published')

# DELETE
post = Post.objects.get(id=1)
post.delete()

# DELETE - Bulk
Post.objects.filter(status='draft').delete()
```

---

## 6.5 Query Lookups

```python
# Exact match
Post.objects.filter(title='Hello')
Post.objects.filter(title__exact='Hello')

# Case-insensitive
Post.objects.filter(title__iexact='hello')

# Contains
Post.objects.filter(title__contains='python')
Post.objects.filter(title__icontains='python')  # Case-insensitive

# Starts/Ends with
Post.objects.filter(title__startswith='How')
Post.objects.filter(title__endswith='?')

# In list
Post.objects.filter(status__in=['draft', 'published'])

# Range
Post.objects.filter(created_at__range=[start_date, end_date])

# Comparisons
Post.objects.filter(views__gt=100)    # Greater than
Post.objects.filter(views__gte=100)   # Greater than or equal
Post.objects.filter(views__lt=100)    # Less than
Post.objects.filter(views__lte=100)   # Less than or equal

# Date parts
Post.objects.filter(created_at__year=2024)
Post.objects.filter(created_at__month=1)
Post.objects.filter(created_at__day=15)

# Null check
Post.objects.filter(category__isnull=True)

# Related fields (double underscore)
Post.objects.filter(author__username='john')
Post.objects.filter(category__name='Python')
```

---

# PART 7: ADMIN PANEL

---

## 7.1 Create Superuser

```bash
python manage.py createsuperuser
# Enter username, email, password
```

Access admin at: `http://127.0.0.1:8000/admin/`

---

## 7.2 Register Models

**blog/admin.py:**
```python
from django.contrib import admin
from .models import Post, Category

# Basic registration
admin.site.register(Category)

# Customized registration
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_editable = ['status']
    list_per_page = 25
```

---

# PART 8: FORMS

---

## 8.1 Django Forms

**blog/forms.py:**
```python
from django import forms
from .models import Post

# Regular form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# Model form (auto-generates fields from model)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']
        # Or exclude certain fields:
        # exclude = ['author', 'slug']
```

---

## 8.2 Using Forms in Views

```python
from django.shortcuts import render, redirect
from .forms import ContactForm, PostForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send email, save to DB, etc.
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
```

---

## 8.3 Forms in Templates

```html
<form method="post">
    {% csrf_token %}

    <!-- Render entire form -->
    {{ form.as_p }}

    <!-- Or render as table -->
    {{ form.as_table }}

    <!-- Or manually -->
    <div>
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>

    <button type="submit">Submit</button>
</form>
```

---

# PART 9: USER AUTHENTICATION

---

## 9.1 Built-in Auth Views

**myproject/urls.py:**
```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password change
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
```

---

## 9.2 Login Required Decorator

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/custom-login/')
def profile(request):
    return render(request, 'profile.html')
```

---

## 9.3 User Registration

**blog/views.py:**
```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

---

## 9.4 Access User in Views/Templates

```python
# In views
def profile(request):
    user = request.user
    if user.is_authenticated:
        # User is logged in
        pass
```

```html
<!-- In templates -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

---

# PART 10: STATIC FILES

---

## 10.1 Configuration

**settings.py:**
```python
STATIC_URL = '/static/'

# For development
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# For production
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## 10.2 Using Static Files

Create `static` folder:
```
myproject/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
```

In templates:
```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

---

# PART 11: CLASS-BASED VIEWS

---

## 11.1 Basic CBVs

```python
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

# Single post detail
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

# Delete post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
```

---

## 11.2 URL Configuration for CBVs

```python
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
```

---

# PART 12: COMMON COMMANDS

---

```bash
# Project management
django-admin startproject projectname    # Create project
python manage.py startapp appname        # Create app
python manage.py runserver               # Run dev server
python manage.py runserver 0.0.0.0:8000  # Run on all interfaces

# Database
python manage.py makemigrations          # Create migrations
python manage.py migrate                 # Apply migrations
python manage.py showmigrations          # Show migration status
python manage.py sqlmigrate app 0001     # Show SQL

# Admin
python manage.py createsuperuser         # Create admin user
python manage.py changepassword admin    # Change password

# Shell
python manage.py shell                   # Django shell
python manage.py dbshell                 # Database shell

# Static files
python manage.py collectstatic           # Collect static files

# Testing
python manage.py test                    # Run tests
python manage.py test appname            # Test specific app

# Other
python manage.py check                   # Check for issues
python manage.py flush                   # Clear database
```

---

# PART 13: QUICK REFERENCE

---

```
┌─────────────────────────────────────────────────────────────────┐
│              DJANGO QUICK REFERENCE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROJECT SETUP:                                                  │
│  django-admin startproject myproject                            │
│  python manage.py startapp myapp                                │
│  python manage.py runserver                                     │
│                                                                  │
│  DATABASE:                                                       │
│  python manage.py makemigrations                                │
│  python manage.py migrate                                       │
│  python manage.py createsuperuser                               │
│                                                                  │
│  URLS:                                                           │
│  path('', views.home, name='home')                              │
│  path('post/<int:id>/', views.detail, name='detail')            │
│  path('', include('app.urls'))                                  │
│                                                                  │
│  VIEWS:                                                          │
│  return HttpResponse('text')                                    │
│  return render(request, 'template.html', context)               │
│  return redirect('view_name')                                   │
│  return JsonResponse(data)                                      │
│                                                                  │
│  TEMPLATES:                                                      │
│  {{ variable }}                   Print variable                │
│  {% if %} {% endif %}             Conditional                   │
│  {% for %} {% endfor %}           Loop                          │
│  {% url 'name' %}                 URL tag                       │
│  {% static 'file' %}              Static file                   │
│  {% extends 'base.html' %}        Inheritance                   │
│  {% block name %}{% endblock %}   Block                         │
│  {% csrf_token %}                 CSRF protection               │
│                                                                  │
│  QUERYSETS:                                                      │
│  Model.objects.all()              Get all                       │
│  Model.objects.get(id=1)          Get one                       │
│  Model.objects.filter(x=y)        Filter                        │
│  Model.objects.exclude(x=y)       Exclude                       │
│  Model.objects.create(x=y)        Create                        │
│  obj.save()                       Save                          │
│  obj.delete()                     Delete                        │
│                                                                  │
│  FORMS:                                                          │
│  form = MyForm(request.POST)                                    │
│  if form.is_valid():                                            │
│      data = form.cleaned_data                                   │
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
│  1. Django is a "batteries included" framework                  │
│  2. MTV: Model (data), Template (HTML), View (logic)            │
│  3. Admin panel comes free - register your models!              │
│  4. Use migrations for database changes                         │
│  5. QuerySet API for database operations                        │
│  6. Built-in authentication system                              │
│  7. Class-Based Views for common patterns                       │
│  8. Always use {% csrf_token %} in forms                        │
│                                                                  │
│  LEARNING PATH:                                                  │
│  Setup → Views/URLs → Templates → Models → Admin → Forms        │
│  → Auth → Class-Based Views → REST API (Django REST Framework)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Installation:** `pip install django`

**Documentation:** https://docs.djangoproject.com/
