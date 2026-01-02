# Python Virtual Environment - Complete Quick Reference

> Isolate project dependencies from basic to advanced

---

## PART 1: WHAT IS A VIRTUAL ENVIRONMENT?

### Simple Explanation

A **Virtual Environment** is an isolated Python installation for each project.

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
         (Project A needs requests 2.25,
          Project B needs requests 2.28)


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

### Why Use Virtual Environments?

1. **Project Isolation** - Each project has its own packages
2. **Version Control** - Different projects can use different package versions
3. **Clean System** - Keep global Python clean
4. **Reproducibility** - Easily recreate environments on other machines
5. **Professional Standard** - Required for any Python development

---

## PART 2: CREATING VIRTUAL ENVIRONMENTS

### Create a Virtual Environment

```bash
# Navigate to your project folder first!
cd my_project

# Create virtual environment named "venv"
python -m venv venv
```

### What Gets Created

```
my_project/
├── venv/                      ← NEW! Virtual environment folder
│   ├── Include/               ← Header files for building packages
│   ├── Lib/
│   │   └── site-packages/     ← Your packages get installed here
│   ├── Scripts/ (Windows)     ← Activation scripts and executables
│   │   ├── activate           ← Activation script
│   │   ├── activate.bat       ← CMD activation
│   │   ├── Activate.ps1       ← PowerShell activation
│   │   ├── python.exe         ← This project's Python
│   │   └── pip.exe            ← This project's pip
│   └── pyvenv.cfg             ← Configuration file
├── main.py                    ← Your code
└── requirements.txt           ← Your dependencies list
```

### Alternative Naming

```bash
# Standard name (recommended)
python -m venv venv

# Other common names
python -m venv .venv          # Hidden folder (starts with dot)
python -m venv env            # Shorter name
```

---

## PART 3: ACTIVATING AND DEACTIVATING

### Activating the Virtual Environment

**You MUST activate before installing packages or running code!**

| Shell | Activation Command |
|-------|-------------------|
| **PowerShell** | `.\venv\Scripts\Activate.ps1` |
| **CMD** | `.\venv\Scripts\activate` |
| **Git Bash** | `source venv/Scripts/activate` |
| **Mac/Linux** | `source venv/bin/activate` |

### How to Know It's Activated

```
BEFORE activation:
PS C:\Users\Sudheer\my_project>

AFTER activation:
(venv) PS C:\Users\Sudheer\my_project>
↑
└── "(venv)" appears in your prompt!
```

### Deactivating

```bash
# Just type:
deactivate

# Prompt changes back:
# (venv) PS C:\...>  →  PS C:\...>
```

---

## PART 4: PACKAGE MANAGEMENT WITH PIP

### Installing Packages

```bash
# Make sure venv is activated first!
# (venv) should appear in prompt

# Install single package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install minimum version
pip install requests>=2.25.0

# Install multiple packages
pip install requests flask pandas

# Install from requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Install from GitHub
pip install git+https://github.com/user/repo.git
```

### Listing and Checking Packages

```bash
# List all installed packages
pip list

# List in requirements format
pip freeze

# Show package details
pip show requests

# Check for outdated packages
pip list --outdated

# Check Python version
python --version

# Check pip version
pip --version
```

### Uninstalling Packages

```bash
# Uninstall single package
pip uninstall requests

# Uninstall multiple packages
pip uninstall requests flask pandas

# Uninstall without confirmation
pip uninstall -y requests
```

---

## PART 5: REQUIREMENTS FILE

### Creating requirements.txt

```bash
# Save ALL installed packages to requirements.txt
pip freeze > requirements.txt
```

**Example requirements.txt:**
```
certifi==2023.7.22
charset-normalizer==3.3.2
flask==2.0.1
idna==3.6
requests==2.28.0
urllib3==2.1.0
```

### Installing from requirements.txt

```bash
# Install all packages from file
pip install -r requirements.txt
```

### Best Practices for requirements.txt

```
# Good - Pin exact versions for production
requests==2.28.0
flask==2.0.1

# OK - Minimum version for development
requests>=2.25.0

# Include comments for clarity
# Web framework
flask==2.0.1
# HTTP client
requests==2.28.0
```

---

## PART 6: VERIFYING YOUR ENVIRONMENT

### Check Which Python is Active

```bash
# PowerShell
Get-Command python
(Get-Command python).Source

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

### Check if Virtual Environment Exists

```bash
# PowerShell - Check if venv folder exists
Test-Path .\venv

# Check if venv python exists
Test-Path .\venv\Scripts\python.exe

# Output: True (exists) or False (doesn't exist)
```

---

## PART 7: DELETING VIRTUAL ENVIRONMENTS

### How to Delete

```bash
# IMPORTANT: Make sure it's deactivated first!
deactivate

# PowerShell - Delete venv folder
rm -r -Force venv

# CMD
rmdir /s /q venv

# Git Bash
rm -rf venv
```

**Note:** This deletes ALL packages installed in that environment, but NOT your code files!

### When to Delete and Recreate

- When the environment is corrupted
- When switching Python versions
- When starting fresh with new requirements
- When the venv folder is too large

---

## PART 8: VS CODE INTEGRATION

### Auto-Activate in VS Code

VS Code can automatically activate your virtual environment!

**Setup:**
1. Open project folder in VS Code
2. Open Command Palette: `Ctrl + Shift + P`
3. Type: "Python: Select Interpreter"
4. Choose the Python from your venv folder:
   `.\venv\Scripts\python.exe`

**Result:** New terminals will show `(venv)` automatically!

### Settings for Auto-Activation

In VS Code Settings (`Ctrl + ,`), search for:

| Setting | Value |
|---------|-------|
| `python.terminal.activateEnvironment` | `true` (check this) |
| `python.defaultInterpreterPath` | `./venv/Scripts/python.exe` |

Or add to `.vscode/settings.json`:
```json
{
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe"
}
```

---

## PART 9: COMMON WORKFLOWS

### New Project Workflow

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Initialize Git (optional but recommended)
git init

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
.\venv\Scripts\Activate.ps1    # PowerShell

# 5. Create .gitignore (add venv/)
ni .gitignore
# Add: venv/ to the file

# 6. Install packages
pip install requests flask

# 7. Save requirements
pip freeze > requirements.txt

# 8. Create your Python files
ni main.py

# 9. Work on project...

# 10. When done, deactivate
deactivate
```

### Daily Work Workflow

```bash
# 1. Navigate to project
cd my_project

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Check venv is active
# (venv) should appear in prompt

# 4. Work on your code...

# 5. If you install new packages
pip install new_package
pip freeze > requirements.txt

# 6. Commit changes (including updated requirements.txt)

# 7. Deactivate when done (optional)
deactivate
```

### Clone Someone's Project Workflow

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
# (Copy .env.example to .env and fill in values)

# 6. Run the project
python main.py
```

### Copy Packages to New Environment

```bash
# In OLD project (with venv activated)
pip freeze > requirements.txt

# In NEW project
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## PART 10: COMPLETE .gitignore FOR PYTHON

```gitignore
# Virtual environment
venv/
.venv/
ENV/
env/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.pyo

# Distribution
dist/
build/
*.egg-info/
*.egg

# Environment variables
.env
.env.local
.env.*.local

# IDE settings
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Jupyter notebooks
.ipynb_checkpoints/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log
logs/
```

---

## PART 11: TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Script execution disabled | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Wrong Python version | Use `python3 -m venv venv` or check PATH |
| venv not activating | Check path, use correct shell command |
| Package not found after install | Make sure venv is activated first |
| (venv) not showing | Check if activation worked, try again |
| "python is not recognized" | Install Python, add to PATH |
| pip install fails | Try `python -m pip install package` |
| Permission denied | Don't use sudo/admin, use --user flag if needed |
| venv folder too large | Delete and recreate |

### PowerShell Execution Policy Error

```powershell
# Error: "running scripts is disabled on this system"

# Fix: Run this once
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activation again
.\venv\Scripts\Activate.ps1
```

### Can't Find venv Python

```bash
# Verify venv exists
Test-Path .\venv\Scripts\python.exe

# If not, create it
python -m venv venv

# If Python not found, check installation
python --version
where python
```

---

## PART 12: QUICK REFERENCE CHEAT SHEET

### Create and Activate

| Command | Description |
|---------|-------------|
| `python -m venv venv` | Create virtual environment |
| `.\venv\Scripts\Activate.ps1` | Activate (PowerShell) |
| `.\venv\Scripts\activate` | Activate (CMD) |
| `source venv/Scripts/activate` | Activate (Git Bash) |
| `deactivate` | Exit virtual environment |

### Package Management

| Command | Description |
|---------|-------------|
| `pip install package` | Install package |
| `pip install package==1.2.3` | Install specific version |
| `pip install -r requirements.txt` | Install from file |
| `pip freeze > requirements.txt` | Save packages to file |
| `pip list` | List installed packages |
| `pip list --outdated` | Show outdated packages |
| `pip show package` | Package details |
| `pip uninstall package` | Remove package |

### Verification

| Command | Description |
|---------|-------------|
| `where python` | Find Python location |
| `python --version` | Check Python version |
| `pip --version` | Check pip version |
| `Test-Path .\venv` | Check if venv exists |

### Cleanup

| Command | Description |
|---------|-------------|
| `deactivate` | Exit venv first! |
| `rm -r -Force venv` | Delete venv (PowerShell) |
| `rmdir /s /q venv` | Delete venv (CMD) |

---

## PART 13: KEY POINTS TO REMEMBER

1. **Always create venv** for every Python project
2. **Always activate** before installing packages
3. **Look for (venv)** in your prompt to confirm activation
4. **Use requirements.txt** to track dependencies
5. **Add venv/ to .gitignore** - never commit it
6. **Deactivate** when switching projects
7. **Delete and recreate** if environment gets corrupted
8. **VS Code integration** saves time - set it up!
9. **Clone workflow**: Create venv → Activate → Install from requirements.txt
10. **Different Python versions** need different venvs

---

## PART 14: COMPARISON WITH OTHER TOOLS

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **venv** | Built-in Python virtual environments | Standard choice, always available |
| **virtualenv** | Third-party venv (more features) | Need extra features |
| **conda** | Package + environment manager | Data science, complex dependencies |
| **pipenv** | Pip + venv combined | Automated dependency management |
| **poetry** | Modern dependency management | Advanced project management |

**Recommendation:** Start with `venv` - it's built into Python and works for most cases!

---
