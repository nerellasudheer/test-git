# Environment Variables - Complete Quick Reference

> Store configuration and secrets outside your code

---

## PART 1: WHAT ARE ENVIRONMENT VARIABLES?

### Simple Explanation

**Environment Variables** = Settings stored by your operating system that programs can read.

Think of them as labeled boxes:
- A box labeled "API_KEY" → stores your secret key
- A box labeled "PATH" → stores locations of programs
- A box labeled "DEBUG" → stores True or False

Programs read these "boxes" to get settings WITHOUT the settings being written directly in code.

### Why Use Environment Variables?

```python
# WITHOUT environment variables (BAD - Secret exposed!)
api_key = "sk_secret_123456789"
# If you push to GitHub → Everyone sees your secret!

# WITH environment variables (GOOD - Secret hidden!)
api_key = os.getenv("API_KEY")
# Secret stored separately - code is safe to share
```

---

## PART 2: TYPES OF ENVIRONMENT VARIABLES

| Type | Stored Where | Lifetime | Scope | Needs Admin? |
|------|-------------|----------|-------|--------------|
| **System** | Windows Registry | Permanent | All users | Yes |
| **User** | Windows Registry | Permanent | Your account only | No |
| **Process** | RAM | While program runs | One program | No |
| **.env file** | Text file | While file exists | One project | No |

### Priority Order

```
Process variables → User variables → System variables
(Most specific wins - Process overrides User, User overrides System)
```

---

## PART 3: VIEWING ENVIRONMENT VARIABLES

### PowerShell

```powershell
# View ALL environment variables
Get-ChildItem Env:

# View specific variable
$env:PATH
$env:USERPROFILE
$env:USERNAME
$env:TEMP

# List all in table format
Get-ChildItem Env: | Sort-Object Name
```

### CMD

```cmd
# View ALL
set

# View specific
echo %PATH%
echo %USERPROFILE%
echo %USERNAME%
echo %TEMP%
```

### Common System Variables

| Variable | Contains |
|----------|----------|
| `PATH` | Folders to search for programs |
| `USERPROFILE` | Your home folder (C:\Users\Name) |
| `USERNAME` | Current user's name |
| `TEMP` / `TMP` | Temporary files folder |
| `APPDATA` | Application data folder |
| `PROGRAMFILES` | Program Files folder |
| `HOMEPATH` | Home path without drive |
| `COMPUTERNAME` | Computer name |

---

## PART 4: SETTING ENVIRONMENT VARIABLES

### Temporary Variables (Current Session Only)

These exist only in the current terminal window - close it, they're gone!

**PowerShell:**
```powershell
$env:MY_VAR = "HelloWorld"
echo $env:MY_VAR                    # Output: HelloWorld

# Multiple variables
$env:API_KEY = "your-key-here"
$env:DEBUG = "True"
```

**CMD:**
```cmd
set MY_VAR=HelloWorld
echo %MY_VAR%                       REM Output: HelloWorld

set API_KEY=your-key-here
set DEBUG=True
```

### Permanent Variables

**Method 1: Using setx (User Level)**
```cmd
setx MY_VAR "MyValue"
# IMPORTANT: Open NEW terminal to see the change!
```

**Method 2: Using setx (System Level - Admin Required)**
```cmd
setx MY_VAR "MyValue" /M
# Run CMD as Administrator!
```

**Method 3: PowerShell (User Level)**
```powershell
[Environment]::SetEnvironmentVariable("MY_VAR", "MyValue", "User")
# Open NEW terminal to see the change!
```

**Method 4: PowerShell (System Level - Admin Required)**
```powershell
[Environment]::SetEnvironmentVariable("MY_VAR", "MyValue", "Machine")
```

**Method 5: GUI (Windows)**
1. Press `Win + R`
2. Type `sysdm.cpl` and Enter
3. Click "Advanced" tab
4. Click "Environment Variables"
5. Add under "User variables" or "System variables"
6. Click OK → OK → OK
7. **Restart any open terminals**

### Deleting Environment Variables

**PowerShell (Temporary):**
```powershell
Remove-Item Env:MY_VAR
```

**PowerShell (Permanent User):**
```powershell
[Environment]::SetEnvironmentVariable("MY_VAR", $null, "User")
```

**CMD:**
```cmd
set MY_VAR=
setx MY_VAR ""
```

---

## PART 5: .env FILES - PROJECT-SPECIFIC CONFIGURATION

### What is a .env File?

A `.env` file is a **plain text file** that stores settings for ONE project.

```
Project Structure:
📁 MyProject/
├── main.py
├── .env              ← Your actual secrets (DON'T commit to Git!)
├── .env.example      ← Template to share (safe to commit)
└── .gitignore        ← Contains ".env" to not push secrets
```

### .env File Format

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
SECRET_KEY=your-secret-key-here
```

**Format Rules:**
- One variable per line
- Format: `KEY=VALUE` (no spaces around `=`)
- No quotes needed (usually)
- Comments start with `#`
- Case-sensitive (`API_KEY` ≠ `api_key`)
- Blank lines are ignored

---

## PART 6: USING ENVIRONMENT VARIABLES IN PYTHON

### Installing python-dotenv

```bash
pip install python-dotenv
```

### Basic Usage

```python
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access variables
api_key = os.getenv('API_KEY')
db_host = os.getenv('DB_HOST', 'localhost')  # With default value
debug = os.getenv('DEBUG', 'False').lower() == 'true'  # Convert to bool
port = int(os.getenv('DB_PORT', 5432))  # Convert to int

print(f"API Key: {api_key}")
print(f"Database: {db_host}")
print(f"Debug Mode: {debug}")
```

### Python Access Methods Comparison

| Method | When to Use | Returns if Missing |
|--------|-------------|-------------------|
| `os.environ['VAR']` | VAR MUST exist | Raises KeyError |
| `os.environ.get('VAR')` | VAR is optional | None |
| `os.environ.get('VAR', 'default')` | You have a fallback | 'default' |
| `os.getenv('VAR')` | Same as get() | None |
| `os.getenv('VAR', 'default')` | Same as get() with default | 'default' |

**Recommended:** Always use `os.getenv()` with a default or validation!

### Setting Variables from Python

```python
import os

# Set temporary variable (only in current process)
os.environ['MY_VAR'] = 'value'

# Access it
print(os.environ.get('MY_VAR'))
```

---

## PART 7: COMPLETE EXAMPLE SETUP

### Step 1: Create .env file

```env
# .env file (DO NOT commit to Git!)
API_KEY=sk_test_XXXXXXXXXXXX
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
SECRET_KEY=my-secret-key-12345
```

### Step 2: Create .env.example (safe to share)

```env
# .env.example - Copy this to .env and fill in your values
API_KEY=your_api_key_here
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
SECRET_KEY=generate-your-own-key
```

### Step 3: Add to .gitignore

```gitignore
# Environment variables
.env
.env.local
.env.*.local
*.key
credentials.json
```

### Step 4: Create config.py

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Config:
    """Application configuration from environment variables"""

    API_KEY = os.getenv('API_KEY')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY')

    @classmethod
    def validate(cls):
        """Check that required variables are set"""
        required = ['API_KEY', 'SECRET_KEY']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {missing}")
```

### Step 5: Use in main.py

```python
from config import Config

# Validate configuration at startup
Config.validate()

# Use configuration
print(f"Debug Mode: {Config.DEBUG}")
print(f"Database: {Config.DB_HOST}:{Config.DB_PORT}")

# Use API key (safely)
api_key = Config.API_KEY
```

---

## PART 8: VS CODE INTEGRATION

### Auto-detect .env file

1. Install the **Python** extension (Microsoft)
2. Create `.env` in project root
3. VS Code automatically detects it

### For Python Debugging

In `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```

### For Terminal

In `.vscode/settings.json`:
```json
{
    "python.envFile": "${workspaceFolder}/.env"
}
```

---

## PART 9: SECURITY BEST PRACTICES

### DO's

1. **Use .env files** for project-specific secrets
2. **Add .env to .gitignore** immediately
3. **Create .env.example** as a template for teammates
4. **Use os.getenv()** with defaults or validation
5. **Use descriptive names** - `DATABASE_URL` not `VAR1`
6. **Restart terminals** after setting permanent variables
7. **Use different values per environment** (dev/staging/prod)

### DON'Ts

1. **NEVER commit secrets to Git**
2. **NEVER hardcode secrets in code**
3. **NEVER print secrets in logs**
4. **NEVER share .env files** (share .env.example instead)

### Example of What NOT to Do

```python
# BAD - Secret in code!
api_key = "sk-abc123secret456"

# BAD - Printing secrets!
print(f"Using API key: {os.getenv('API_KEY')}")

# GOOD - Use environment variable
api_key = os.getenv("API_KEY")

# GOOD - Print safely (masked)
print(f"API key loaded: {'*' * 10 + api_key[-4:] if api_key else 'NOT SET'}")
```

---

## PART 10: TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Variable not found | Check spelling, case matters |
| .env not loading | Check file location, call `load_dotenv()` |
| Changes not showing | Restart terminal/VS Code |
| setx not working immediately | Open NEW terminal window |
| PATH not working | Separate paths with `;` on Windows |
| Permission denied | Need admin for system variables |
| Variable is None | Check if .env file exists and has correct format |
| KeyError with os.environ[] | Use os.getenv() with default instead |

### Debugging Environment Variables

```python
# Check if variable exists
import os
from dotenv import load_dotenv

load_dotenv()

# List all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Check specific variable
var = os.getenv('MY_VAR')
if var:
    print(f"MY_VAR is set to: {var}")
else:
    print("MY_VAR is NOT set!")
```

---

## PART 11: QUICK REFERENCE CHEAT SHEET

### View Variables

| Shell | Command |
|-------|---------|
| PowerShell | `Get-ChildItem Env:` |
| PowerShell | `$env:VAR_NAME` |
| CMD | `set` |
| CMD | `echo %VAR_NAME%` |

### Set Temporary Variables

| Shell | Command |
|-------|---------|
| PowerShell | `$env:VAR = "value"` |
| CMD | `set VAR=value` |

### Set Permanent Variables

| Level | Command |
|-------|---------|
| User (CMD) | `setx VAR "value"` |
| System (CMD) | `setx VAR "value" /M` (admin) |
| User (PS) | `[Environment]::SetEnvironmentVariable("VAR", "value", "User")` |
| System (PS) | `[Environment]::SetEnvironmentVariable("VAR", "value", "Machine")` |

### Python

```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read variable (safe)
value = os.getenv('VAR_NAME')
value = os.getenv('VAR_NAME', 'default')

# Read variable (raises error if missing)
value = os.environ['VAR_NAME']

# Set variable (temporary)
os.environ['VAR_NAME'] = 'value'
```

### .env File Format

```env
# Comment
KEY=value
API_KEY=your-secret-key
DEBUG=True
PORT=5432
```

---

## PART 12: KEY POINTS TO REMEMBER

1. **Never commit secrets** - Add `.env` to `.gitignore` immediately
2. **Use .env.example** - Create a template for teammates
3. **Use os.getenv()** - Safer than os.environ[]
4. **Restart terminal** after setting permanent variables
5. **Different values per environment** - Dev vs Production
6. **Case sensitive** - `API_KEY` ≠ `api_key`
7. **No spaces around `=`** in .env files
8. **Always validate** required variables at startup
9. **Load .env first** - Call `load_dotenv()` before accessing variables
10. **Process variables override** system and user variables

---
