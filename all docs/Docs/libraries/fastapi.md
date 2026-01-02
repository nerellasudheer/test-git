# FastAPI - Complete Beginner's Guide

## Modern, Fast, Async API Framework for Python

---

# PART 1: WHAT IS FASTAPI?

---

## 1.1 Simple Explanation

**FastAPI** is a modern Python web framework for building APIs quickly with automatic documentation.

```
┌─────────────────────────────────────────────────────────────────┐
│                    FASTAPI EXPLAINED                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  FastAPI is like a SUPER-EFFICIENT WAITER:                      │
│                                                                  │
│  - Takes orders FAST (high performance)                         │
│  - Writes them perfectly (type checking)                        │
│  - Provides a MENU automatically (auto-documentation)           │
│  - Can handle MANY tables at once (async support)               │
│                                                                  │
│  Key Features:                                                   │
│  - Automatic API documentation (Swagger UI & ReDoc)             │
│  - Data validation with Python type hints                       │
│  - Async/await support for high performance                     │
│  - Based on Pydantic for data handling                          │
│  - One of the fastest Python frameworks                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Why FastAPI?

| Feature | Benefit |
|---------|---------|
| **Fast** | One of the fastest Python frameworks |
| **Auto Documentation** | Swagger UI and ReDoc automatically generated |
| **Type Hints** | Editor support, validation, and documentation |
| **Data Validation** | Automatic validation with Pydantic |
| **Async Support** | Native async/await support |
| **Standards-Based** | OpenAPI and JSON Schema |
| **Easy to Learn** | Simple and intuitive |

---

## 1.3 Framework Comparison

| Feature | FastAPI | Flask | Django |
|---------|---------|-------|--------|
| **Performance** | Very Fast | Medium | Medium |
| **Async Support** | Native | Extension | Limited |
| **Auto Documentation** | Yes | No | No |
| **Type Checking** | Built-in | No | No |
| **Best For** | APIs, Microservices | Small apps, APIs | Full web apps |
| **Learning Curve** | Easy | Easy | Steeper |

---

# PART 2: INSTALLATION & SETUP

---

## 2.1 Installation

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install FastAPI and ASGI server
pip install fastapi
pip install "uvicorn[standard]"
```

---

## 2.2 Your First API

**main.py:**
```python
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

**Run the server:**
```bash
uvicorn main:app --reload
```

- `main` = the Python file (main.py)
- `app` = the FastAPI instance
- `--reload` = auto-restart on code changes

**Open browser:**
- API: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 2.3 Project Structure

```
my_fastapi_app/
├── main.py                # Main application
├── routers/               # Route modules
│   ├── __init__.py
│   ├── users.py
│   └── items.py
├── models/                # Pydantic models
│   ├── __init__.py
│   └── schemas.py
├── database/              # Database setup
│   ├── __init__.py
│   └── database.py
├── requirements.txt
└── .env
```

---

# PART 3: PATH PARAMETERS

---

## 3.1 Basic Path Parameters

```python
from fastapi import FastAPI

app = FastAPI()

# Path parameter with type hint
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}

# String parameter
@app.get("/users/{username}")
def get_user(username: str):
    return {"username": username}
```

**URLs:**
- `/items/5` → `{"item_id": 5}`
- `/users/john` → `{"username": "john"}`

---

## 3.2 Path Parameter Validation

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(
        ...,  # Required
        title="Item ID",
        description="The ID of the item",
        ge=1,   # Greater than or equal
        le=100  # Less than or equal
    )
):
    return {"item_id": item_id}
```

---

## 3.3 Predefined Values (Enum)

```python
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    return {"model_name": model_name}
```

---

# PART 4: QUERY PARAMETERS

---

## 4.1 Basic Query Parameters

```python
from fastapi import FastAPI

app = FastAPI()

# Query parameters: /items/?skip=0&limit=10
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Optional query parameter
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

---

## 4.2 Query Parameter Validation

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def get_items(
    q: str | None = Query(
        default=None,
        min_length=3,
        max_length=50,
        regex="^search",  # Must start with "search"
        title="Search Query",
        description="Search query string"
    )
):
    return {"q": q}

# Required query parameter
@app.get("/search/")
def search(q: str = Query(..., min_length=3)):  # ... means required
    return {"q": q}

# List query parameter: /items/?tags=tag1&tags=tag2
@app.get("/items/")
def get_items(tags: list[str] = Query(default=[])):
    return {"tags": tags}
```

---

# PART 5: REQUEST BODY (Pydantic Models)

---

## 5.1 Creating Pydantic Models

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Use in endpoint
@app.post("/items/")
def create_item(item: Item):
    return item

# Access fields
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```

---

## 5.2 Model with Validation

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    username: str = Field(
        ...,  # Required
        min_length=3,
        max_length=50,
        description="Username must be 3-50 characters"
    )
    email: EmailStr
    full_name: str | None = None
    age: int = Field(default=None, ge=18, le=120)

    # Example for documentation
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "email": "john@example.com",
                    "full_name": "John Doe",
                    "age": 25
                }
            ]
        }
    }
```

---

## 5.3 Nested Models

```python
from pydantic import BaseModel
from typing import List

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tags: list[str] = []
    images: list[Image] | None = None

# Request body example:
# {
#     "name": "Phone",
#     "price": 999.99,
#     "tags": ["electronics", "mobile"],
#     "images": [
#         {"url": "http://example.com/img1.jpg", "name": "front"},
#         {"url": "http://example.com/img2.jpg", "name": "back"}
#     ]
# }
```

---

# PART 6: HTTP METHODS

---

## 6.1 All HTTP Methods

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

# GET - Retrieve data
@app.get("/items/")
def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# POST - Create data
@app.post("/items/")
def create_item(item: Item):
    return {"created": item}

# PUT - Update/Replace data
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated": item}

# PATCH - Partial update
@app.patch("/items/{item_id}")
def partial_update(item_id: int, item: Item):
    return {"item_id": item_id, "partial_update": item}

# DELETE - Remove data
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}
```

---

# PART 7: RESPONSE MODELS

---

## 7.1 Response Model

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: str

class UserOut(BaseModel):
    username: str
    email: str
    # password is NOT included!

@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    # Password won't be in response
    return user
```

---

## 7.2 Multiple Response Models

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    owner_id: int

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    # Add id and owner_id
    return {**item.model_dump(), "id": 1, "owner_id": 1}
```

---

## 7.3 Status Codes

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
```

**Common Status Codes:**
| Code | Constant | Meaning |
|------|----------|---------|
| 200 | `HTTP_200_OK` | Success |
| 201 | `HTTP_201_CREATED` | Created |
| 204 | `HTTP_204_NO_CONTENT` | Deleted |
| 400 | `HTTP_400_BAD_REQUEST` | Bad request |
| 401 | `HTTP_401_UNAUTHORIZED` | Not authenticated |
| 403 | `HTTP_403_FORBIDDEN` | Not authorized |
| 404 | `HTTP_404_NOT_FOUND` | Not found |
| 422 | `HTTP_422_UNPROCESSABLE_ENTITY` | Validation error |
| 500 | `HTTP_500_INTERNAL_SERVER_ERROR` | Server error |

---

# PART 8: ERROR HANDLING

---

## 8.1 HTTPException

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-Error": "Not found"}
        )
    return {"item": items[item_id]}
```

---

## 8.2 Custom Exception Handler

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."}
    )

@app.get("/unicorns/{name}")
def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
```

---

# PART 9: DEPENDENCY INJECTION

---

## 9.1 Basic Dependencies

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency function
def common_parameters(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def get_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
def get_users(commons: dict = Depends(common_parameters)):
    return commons
```

---

## 9.2 Database Dependency

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```

---

## 9.3 Authentication Dependency

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token and get user
    if token != "valid_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return {"username": "johndoe"}

@app.get("/users/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
```

---

# PART 10: DATABASE (SQLAlchemy)

---

## 10.1 Database Setup

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

---

## 10.2 Models

```python
# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
```

---

## 10.3 Schemas (Pydantic)

```python
# schemas.py
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    items: list[Item] = []

    class Config:
        from_attributes = True
```

---

## 10.4 CRUD Operations

```python
# crud.py
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "_hashed"  # Use proper hashing!
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user
```

---

## 10.5 Main Application

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
```

---

# PART 11: ASYNC/AWAIT

---

## 11.1 Async Endpoints

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

# Sync function (regular)
@app.get("/sync")
def sync_endpoint():
    return {"message": "This is sync"}

# Async function
@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(1)  # Simulate async operation
    return {"message": "This is async"}

# Async with external calls
import httpx

@app.get("/external")
async def call_external():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()
```

---

# PART 12: ROUTERS (Organizing Code)

---

## 12.1 Creating Routers

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_users():
    return [{"username": "john"}, {"username": "jane"}]

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/")
def create_user(user: dict):
    return user
```

```python
# routers/items.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
```

---

## 12.2 Including Routers

```python
# main.py
from fastapi import FastAPI
from routers import users, items

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
```

**URLs:**
- `/users/` - Users list
- `/users/{id}` - User detail
- `/items/` - Items list

---

# PART 13: MIDDLEWARE & CORS

---

## 13.1 CORS (Cross-Origin Resource Sharing)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow specific origins
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://myapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],        # Or ["GET", "POST"]
    allow_headers=["*"]
)
```

---

## 13.2 Custom Middleware

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

---

# PART 14: FILE UPLOADS

---

## 14.1 Single File Upload

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

# Save file
@app.post("/savefile/")
async def save_file(file: UploadFile):
    with open(f"uploads/{file.filename}", "wb") as f:
        contents = await file.read()
        f.write(contents)
    return {"filename": file.filename}
```

---

## 14.2 Multiple Files

```python
from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/uploadfiles/")
async def upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}
```

---

# PART 15: TESTING

---

## 15.1 Testing with TestClient

```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test", "price": 9.99}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test"

def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404
```

**Run tests:**
```bash
pip install pytest
pytest
```

---

# PART 16: QUICK REFERENCE

---

```
┌─────────────────────────────────────────────────────────────────┐
│              FASTAPI QUICK REFERENCE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SETUP:                                                          │
│  pip install fastapi uvicorn                                    │
│  uvicorn main:app --reload                                      │
│                                                                  │
│  ROUTES:                                                         │
│  @app.get("/")                      GET request                 │
│  @app.post("/")                     POST request                │
│  @app.put("/")                      PUT request                 │
│  @app.delete("/")                   DELETE request              │
│                                                                  │
│  PARAMETERS:                                                     │
│  @app.get("/items/{id}")            Path parameter              │
│  @app.get("/items/?skip=0")         Query parameter             │
│  def func(item: Item):              Request body                │
│                                                                  │
│  PYDANTIC MODELS:                                                │
│  class Item(BaseModel):                                         │
│      name: str                                                  │
│      price: float                                               │
│      tax: float | None = None                                   │
│                                                                  │
│  VALIDATION:                                                     │
│  Field(..., min_length=3)           Required, min 3 chars       │
│  Field(default=0, ge=0)             Default 0, >= 0             │
│  Query(..., max_length=50)          Query param validation      │
│  Path(..., gt=0)                    Path param > 0              │
│                                                                  │
│  RESPONSES:                                                      │
│  return {"key": "value"}            Dict/JSON response          │
│  response_model=Schema              Filter response             │
│  status_code=201                    Set status code             │
│                                                                  │
│  ERRORS:                                                         │
│  raise HTTPException(404, "Not found")                          │
│                                                                  │
│  DEPENDENCIES:                                                   │
│  def get_db(): yield db                                         │
│  def func(db = Depends(get_db)):                                │
│                                                                  │
│  DOCUMENTATION:                                                  │
│  /docs        → Swagger UI                                      │
│  /redoc       → ReDoc                                           │
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
│  1. FastAPI is fast, modern, and has auto-documentation         │
│  2. Type hints provide validation and editor support            │
│  3. Pydantic models define request/response schemas             │
│  4. Use Path() and Query() for parameter validation             │
│  5. Dependency Injection for shared logic (DB, auth)            │
│  6. Native async/await support for high performance             │
│  7. Routers organize code into modules                          │
│  8. /docs gives you free Swagger documentation                  │
│                                                                  │
│  LEARNING PATH:                                                  │
│  Basics → Pydantic Models → Validation → Dependencies           │
│  → Database → Authentication → Testing → Deployment             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Installation:** `pip install fastapi uvicorn`

**Run Server:** `uvicorn main:app --reload`

**Documentation:** https://fastapi.tiangolo.com/
