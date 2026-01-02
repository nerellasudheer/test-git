# Python Virtual Environments & Environment Variables - Complete Guide

## Master Python Project Isolation and Configuration

---

# PART 1: UNDERSTANDING VIRTUAL ENVIRONMENTS

---

## 1.1 What is a Virtual Environment?

A **Virtual Environment** is an isolated Python installation for each project.

```
┌─────────────────────────────────────────────────────────────────┐
│                   WHY VIRTUAL ENVIRONMENTS?                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Problem WITHOUT virtual environments:                          │
│  ────────────────────────────────────                            │
│  Project A needs: requests v2.25.0                              │
│  Project B needs: requests v2.28.0                              │
│  They share same Python installation!                           │
│  Installing one breaks the other!                               │
│                                                                  │
│  Solution WITH virtual environments:                            │
│  ───────────────────────────────────                             │
│  Project A has its OWN Python with its OWN packages             │
│  Project B has its OWN Python with its OWN packages             │
│  They don't interfere with each other!                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Visual Understanding

```
WITHOUT Virtual Environment (BAD):
────────────────────────────────────
                Python (Global)
                     │
    ┌────────────────┼────────────────┐
    │                │                │
 Project A      Project B       Project C
    │                │                │
    └────────────────┴────────────────┘
              │
         Same packages!
         Conflicts happen!


WITH Virtual Environments (GOOD):
────────────────────────────────────
                Python (Global)
                     │
    ┌────────────────┼────────────────┐
    ↓                ↓                ↓
 Project A      Project B       Project C
    │                │                │
    ↓                ↓                ↓
venv/ (A)        venv/ (B)       venv/ (C)
    │                │                │
requests 2.25   requests 2.28   requests 2.31
django 3.2      flask 2.0       fastapi 0.100

Each project = isolated!
```

---

# PART 2: CREATING AND USING VIRTUAL ENVIRONMENTS

---

## 2.1 Creating a Virtual Environment

```bash
# Navigate to your project folder first!
cd my_project

# Create virtual environment named "venv"
python -m venv venv
```

**What happens:**
```
my_project/
├── venv/                    ← NEW! Virtual environment folder
│   ├── Include/
│   ├── Lib/
│   │   └── site-packages/   ← Your packages go here
│   └── Scripts/             ← Activation scripts
│       ├── activate
│       ├── activate.bat
│       ├── Activate.ps1
│       └── python.exe       ← This project's Python
├── main.py
└── requirements.txt
```

---

## 2.2 Activating the Virtual Environment

**You MUST activate the virtual environment before using it!**

| Shell | Activation Command |
|-------|-------------------|
| PowerShell | `.\venv\Scripts\Activate.ps1` |
| CMD | `.\venv\Scripts\activate` |
| Git Bash | `source venv/Scripts/activate` |
| Mac/Linux | `source venv/bin/activate` |

**How to know it's activated:**
```
BEFORE activation:
PS C:\Users\Sudheer\my_project>

AFTER activation:
(venv) PS C:\Users\Sudheer\my_project>
↑
└── "(venv)" appears in your prompt!
```

---

## 2.3 Deactivating the Virtual Environment

```bash
# Just type:
deactivate

# Prompt changes back:
# (venv) PS C:\Users\...>  →  PS C:\Users\...>
```

---

## 2.4 Checking Which Python is Active

```bash
# PowerShell
Get-Command python

# CMD
where python

# Git Bash
which python
```

**GOOD OUTPUT (venv active):**
```
C:\Users\Sudheer\my_project\venv\Scripts\python.exe
```

**WRONG OUTPUT (venv NOT active):**
```
C:\Python312\python.exe
```

---

## 2.5 Check if Virtual Environment Exists

```bash
# PowerShell - Check if venv folder exists
Test-Path .\venv

# Output: True (exists) or False (doesn't exist)
```

---

# PART 3: PACKAGE MANAGEMENT WITH PIP

---

## 3.1 Installing Packages

```bash
# Make sure venv is activated first!
# (venv) should appear in prompt

# Install single package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install requests flask pandas

# Install from requirements file
pip install -r requirements.txt
```

---

## 3.2 Listing and Checking Packages

```bash
# List all installed packages
pip list

# Show package details
pip show requests

# Check for outdated packages
pip list --outdated

# Check Python version
python --version
```

---

## 3.3 Saving and Sharing Package Requirements

```bash
# Save current packages to requirements.txt
pip freeze > requirements.txt

# Contents of requirements.txt:
# requests==2.28.0
# flask==2.0.1
# pandas==1.5.3
```

---

## 3.4 Installing from requirements.txt

```bash
# Install all packages from file (on another machine or fresh venv)
pip install -r requirements.txt
```

---

## 3.5 Removing Packages

```bash
# Uninstall single package
pip uninstall requests

# Uninstall multiple packages
pip uninstall requests flask pandas
```

---

## 3.6 Copy Packages Between Environments

```bash
# On machine A (source)
pip freeze > requirements.txt

# Copy requirements.txt to machine B

# On machine B
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

# PART 4: DELETING VIRTUAL ENVIRONMENTS

---

## 4.1 How to Delete a Virtual Environment

```bash
# Make sure it's deactivated first!
deactivate

# Then simply delete the folder

# PowerShell
rm -r -Force venv

# CMD
rmdir /s /q venv

# Git Bash
rm -rf venv
```

**Note:** Deleting `venv` folder removes ALL packages installed in that environment!

---

# PART 5: VS CODE INTEGRATION

---

## 5.1 Auto-Activate in VS Code

VS Code can automatically activate your virtual environment when you open a terminal!

**Setup:**
1. Open project folder in VS Code
2. Open Command Palette: `Ctrl + Shift + P`
3. Type: "Python: Select Interpreter"
4. Choose the Python from your venv folder

**Result:** New terminals will show `(venv)` automatically!

---

## 5.2 VS Code Settings for Auto-Activation

In VS Code Settings (`Ctrl + ,`), search for:
- `Python: Activate Environment in Terminal` → Enable (check)

---

# PART 6: UNDERSTANDING ENVIRONMENT VARIABLES

---

## 6.1 What are Environment Variables?

**Environment Variables** = Settings stored by your computer that programs can read.

```
Real-life example:
- A box labeled "API_KEY" → stores your secret key
- A box labeled "PATH" → stores locations of programs
- A box labeled "DEBUG" → stores True or False

Programs can read these "boxes" to get settings without
the settings being written directly in the code.
```

---

## 6.2 Why Use Environment Variables?

```
WITHOUT environment variables:
─────────────────────────────
api_key = "sk_secret_123456789"  # Secret exposed in code!
# If you push to GitHub → Everyone sees your secret!

WITH environment variables:
───────────────────────────
api_key = os.getenv("API_KEY")   # Secret stays hidden
# Secret is stored in .env file or Windows settings
# Code is safe to share
```

---

## 6.3 Types of Environment Variables

| Type | Stored Where | Lifetime | Scope |
|------|-------------|----------|-------|
| **System** | Windows Registry | Permanent | All users |
| **User** | Windows Registry | Permanent | Your account only |
| **Process** | RAM | While program runs | One program |
| **.env file** | Text file | While file exists | One project |

---

# PART 7: WORKING WITH ENVIRONMENT VARIABLES

---

## 7.1 Viewing Environment Variables

**PowerShell:**
```powershell
# View ALL environment variables
Get-ChildItem Env:

# View specific variable
$env:PATH
$env:USERNAME
```

**CMD:**
```cmd
# View ALL
set

# View specific
echo %PATH%
echo %USERNAME%
```

---

## 7.2 Setting Temporary Variables (Process Level)

These exist only in the current window - close the window, they're gone!

**PowerShell:**
```powershell
$env:MY_VAR = "HelloWorld"
echo $env:MY_VAR  # Output: HelloWorld
```

**CMD:**
```cmd
set MY_VAR=HelloWorld
echo %MY_VAR%  # Output: HelloWorld
```

---

## 7.3 Setting Permanent Variables

**For User Variables (no admin needed):**
```cmd
setx MY_VAR "MyValue"
# IMPORTANT: Open NEW terminal to see the change!
```

**For System Variables (admin needed):**
```cmd
setx MY_VAR "MyValue" /M
# Run CMD as Administrator!
```

---

# PART 8: .env FILES - PROJECT-SPECIFIC CONFIGURATION

---

## 8.1 What is a .env File?

A `.env` file is a **plain text file** that stores settings for ONE project.

```
Project Structure:
📁 MyProject/
├── main.py
├── .env          ← Your actual secrets (DON'T commit!)
├── .env.example  ← Template to share (safe to commit)
└── .gitignore    ← Contains ".env" to not push secrets
```

---

## 8.2 .env File Format

```env
# Database settings
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_database

# API Keys (SECRETS!)
API_KEY=sk_test_1234567890
OPENAI_KEY=sk-proj-xyz123

# Application settings
DEBUG=True
MAX_CONNECTIONS=100
```

**Format Rules:**
- One variable per line
- Format: KEY=VALUE
- No spaces around = sign
- No quotes needed (usually)
- Comments start with #
- Case-sensitive (API_KEY ≠ api_key)

---

## 8.3 Installing python-dotenv

```bash
pip install python-dotenv
```

---

## 8.4 Using .env in Python

```python
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access variables
api_key = os.getenv('API_KEY')
db_host = os.getenv('DB_HOST', 'localhost')  # With default
debug = os.getenv('DEBUG', 'False').lower() == 'true'  # Convert to bool

print(f"API Key: {api_key}")
print(f"Database: {db_host}")
print(f"Debug Mode: {debug}")
```

---

## 8.5 Python Methods for Environment Variables

| Method | When to Use | Returns if Missing |
|--------|-------------|-------------------|
| `os.environ['VAR']` | VAR MUST exist | Raises KeyError |
| `os.environ.get('VAR')` | VAR is optional | None |
| `os.environ.get('VAR', 'default')` | You have a fallback | 'default' |
| `os.getenv('VAR')` | Same as get() | None |
| `os.getenv('VAR', 'default')` | Same as get() with default | 'default' |

**Recommended:** Always use `os.getenv()` with a default or validation!

---

## 8.6 Complete Example

**.env file:**
```env
API_KEY=sk_test_XXXXXX
DB_HOST=production-server.com
DB_PORT=5432
DEBUG=False
```

**.gitignore:**
```gitignore
.env
.env.local
venv/
__pycache__/
```

**.env.example:** (safe to share)
```env
# Copy this to .env and fill in your values
API_KEY=your_api_key_here
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```

**config.py:**
```python
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_KEY = os.getenv('API_KEY')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

    @classmethod
    def validate(cls):
        if not cls.API_KEY:
            raise ValueError("API_KEY is required! Set it in .env file.")
```

**main.py:**
```python
from config import Config

# Validate configuration
Config.validate()

# Use configuration
print(f"Database: {Config.DB_HOST}:{Config.DB_PORT}")
print(f"Debug Mode: {Config.DEBUG}")
```

---

# PART 9: BEST PRACTICES

---

## 9.1 Virtual Environment Best Practices

1. **One venv per project** - Don't share between projects
2. **Name it "venv"** - Standard convention, add to .gitignore
3. **Don't commit venv/** - Add to .gitignore
4. **Always use requirements.txt** - Document your dependencies
5. **Activate before installing** - `(venv)` should be in prompt

---

## 9.2 Environment Variables Best Practices

1. **NEVER commit .env to Git** - Add to .gitignore!
2. **Create .env.example** - Template for teammates
3. **Use descriptive names** - `DATABASE_URL` not `VAR1`
4. **Always use safe access** - `os.getenv()` not `os.environ[]`
5. **Restart programs after setting** - New permanent variables need restart

---

## 9.3 Complete .gitignore for Python Projects

```gitignore
# Virtual environment
venv/
.venv/
env/

# Environment variables
.env
.env.local
.env.*.local

# Python cache
__pycache__/
*.py[cod]
*.pyo

# Distribution
dist/
build/
*.egg-info/

# IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```

---

# PART 10: COMMON MISTAKES AND FIXES

---

## 10.1 Virtual Environment Mistakes

| Mistake | Fix |
|---------|-----|
| Installing without activating venv | Always activate first! Check for `(venv)` in prompt |
| Committing venv/ to git | Add `venv/` to .gitignore |
| Using wrong Python | Use `where python` to verify |
| PowerShell execution policy error | Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

## 10.2 Environment Variable Mistakes

| Mistake | Fix |
|---------|-----|
| Committing .env to git | Add `.env` to .gitignore immediately |
| Using `os.environ['VAR']` directly | Use `os.getenv('VAR')` with validation |
| setx doesn't work immediately | Open NEW terminal window |
| Quotes in .env values | Don't use quotes: `KEY=value` not `KEY="value"` |

---

# PART 11: COMPLETE PROJECT SETUP WORKFLOW

---

## 11.1 New Project Checklist

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Initialize Git
git init

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
.\venv\Scripts\Activate.ps1  # PowerShell

# 5. Create .gitignore
# (create file with content from section 9.3)

# 6. Create .env and .env.example
# .env - your actual secrets
# .env.example - template for others

# 7. Install packages
pip install python-dotenv requests

# 8. Save requirements
pip freeze > requirements.txt

# 9. Create your Python files
# main.py, config.py, etc.

# 10. First commit
git add .
git commit -m "Initial project setup"
```

---

## 11.2 Daily Workflow

```bash
# 1. Navigate to project
cd my_project

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Check venv is active
# (venv) should appear in prompt

# 4. Work on your code

# 5. If you install new packages
pip install new_package
pip freeze > requirements.txt

# 6. Deactivate when done (optional)
deactivate
```

---

## 11.3 Cloning Someone's Project

```bash
# 1. Clone the repository
git clone <url>
cd project-name

# 2. Create virtual environment
python -m venv venv

# 3. Activate
.\venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create your .env file from template
# Copy .env.example to .env
# Fill in your own values

# 6. Run the project
python main.py
```

---

# PART 12: QUICK REFERENCE

---

```
┌─────────────────────────────────────────────────────────────────┐
│              VIRTUAL ENVIRONMENT COMMANDS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CREATE:                                                         │
│  python -m venv venv            Create virtual environment      │
│                                                                  │
│  ACTIVATE:                                                       │
│  .\venv\Scripts\Activate.ps1    PowerShell                      │
│  .\venv\Scripts\activate        CMD                             │
│  source venv/Scripts/activate   Git Bash                        │
│                                                                  │
│  DEACTIVATE:                                                     │
│  deactivate                     Exit virtual environment        │
│                                                                  │
│  PACKAGES:                                                       │
│  pip install package            Install package                 │
│  pip install -r requirements.txt Install from file              │
│  pip freeze > requirements.txt  Save packages to file           │
│  pip list                       List installed packages         │
│  pip uninstall package          Remove package                  │
│                                                                  │
│  CHECK:                                                          │
│  where python                   See which Python is active      │
│  python --version               Check Python version            │
│  Test-Path .\venv               Check if venv exists            │
│                                                                  │
│  DELETE:                                                         │
│  rm -r -Force venv              Delete venv (PowerShell)        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              ENVIRONMENT VARIABLES                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  VIEW:                                                           │
│  Get-ChildItem Env:             View all (PowerShell)           │
│  $env:VAR_NAME                  View specific (PowerShell)      │
│  set                            View all (CMD)                  │
│  echo %VAR_NAME%                View specific (CMD)             │
│                                                                  │
│  SET TEMPORARY:                                                  │
│  $env:VAR = "value"             PowerShell                      │
│  set VAR=value                  CMD                             │
│                                                                  │
│  SET PERMANENT:                                                  │
│  setx VAR "value"               User level (open new terminal)  │
│  setx VAR "value" /M            System level (admin required)   │
│                                                                  │
│  PYTHON:                                                         │
│  os.getenv('VAR')               Read variable (returns None)    │
│  os.getenv('VAR', 'default')    Read with default               │
│  os.environ['VAR']              Read (raises KeyError)          │
│                                                                  │
│  .env FILES:                                                     │
│  pip install python-dotenv      Install library                 │
│  load_dotenv()                  Load .env file                  │
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
│  VIRTUAL ENVIRONMENTS:                                           │
│  1. Create one venv per project (python -m venv venv)           │
│  2. Always activate before installing packages                  │
│  3. Look for (venv) in your prompt                              │
│  4. Use requirements.txt to track dependencies                  │
│  5. Add venv/ to .gitignore                                     │
│                                                                  │
│  ENVIRONMENT VARIABLES:                                          │
│  1. Use .env files for project-specific secrets                 │
│  2. NEVER commit .env to Git                                    │
│  3. Create .env.example as a template                           │
│  4. Use os.getenv() with defaults or validation                 │
│  5. Restart programs after setting permanent variables          │
│                                                                  │
│  WORKFLOW:                                                       │
│  Create venv → Activate → Install packages → Create .env        │
│  → Write code → Save requirements → Commit (not venv or .env)   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Previous:** [03_Git_Complete_Guide.md](./03_Git_Complete_Guide.md)
**Next:** [00_Learning_Guide_Index.md](./00_Learning_Guide_Index.md)
