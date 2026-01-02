# Environment Variables - Quick Reference

> Store configuration outside your code

---

## What Are Environment Variables?

Variables stored by your operating system that programs can read.
- Store sensitive data (API keys, passwords)
- Store configuration (paths, settings)
- Keep secrets OUT of code

---

## Types of Variables

| Type | Scope | Stored In | Lasts |
|------|-------|-----------|-------|
| System | All users | Registry | Forever |
| User | Current user | Registry | Forever |
| Process | Current session | RAM | Until closed |

---

## View Variables

### PowerShell
```powershell
# View all
Get-ChildItem Env:

# View specific
$env:PATH
$env:USERPROFILE
```

### CMD
```cmd
# View all
set

# View specific
echo %PATH%
echo %USERPROFILE%
```

---

## Set Variables

### Temporary (Session Only)

**PowerShell:**
```powershell
$env:MY_VAR = "value"
```

**CMD:**
```cmd
set MY_VAR=value
```

### Permanent (GUI Method)

1. Press `Win + R`
2. Type `sysdm.cpl` and Enter
3. Click "Environment Variables"
4. Add under "User variables" or "System variables"

### Permanent (PowerShell - User)
```powershell
[Environment]::SetEnvironmentVariable("MY_VAR", "value", "User")
```

---

## Common Variables

| Variable | Contains |
|----------|----------|
| `PATH` | Folders to search for programs |
| `USERPROFILE` | Your home folder (C:\Users\Name) |
| `TEMP` | Temporary files folder |
| `APPDATA` | Application data folder |
| `PROGRAMFILES` | Program Files folder |

---

## Using in Python

### Read Variables
```python
import os

# Get variable (returns None if not found)
api_key = os.environ.get("API_KEY")

# Get variable (raises error if not found)
api_key = os.environ["API_KEY"]

# Get with default value
debug = os.environ.get("DEBUG", "False")
```

### Set Variables (Temporary)
```python
import os
os.environ["MY_VAR"] = "value"
```

---

## .env Files

Store variables in a file (NOT in code, NOT in Git).

### Create .env File
```
# .env file
API_KEY=your-secret-key
DATABASE_URL=postgres://localhost:5432/mydb
DEBUG=True
```

### Load with python-dotenv
```python
# Install: pip install python-dotenv

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Now use variables
api_key = os.environ.get("API_KEY")
```

---

## Security Rules

1. **Never commit secrets to Git**
   ```gitignore
   # Add to .gitignore
   .env
   .env.local
   *.key
   ```

2. **Never hardcode secrets**
   ```python
   # Wrong
   api_key = "sk-abc123secret"

   # Correct
   api_key = os.environ.get("API_KEY")
   ```

3. **Use different values per environment**
   - Development: `.env.development`
   - Production: `.env.production`

---

## VS Code Setup

### Create .env file
1. Create `.env` in project root
2. Add variables: `KEY=value`
3. Install "Python" extension (auto-detects .env)

### For Python debugging
In `.vscode/launch.json`:
```json
{
  "envFile": "${workspaceFolder}/.env"
}
```

---

## Quick Examples

### API Key Setup
```bash
# .env file
OPENAI_API_KEY=sk-your-key-here
```

```python
# Python code
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
```

### Database URL
```bash
# .env file
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

```python
# Python code
import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.environ.get("DATABASE_URL")
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Variable not found | Check spelling, restart terminal |
| .env not loading | Check file location, call `load_dotenv()` |
| Changes not showing | Restart terminal/VS Code |
| PATH not working | Separate paths with `;` on Windows |

---

## Key Points

1. **Never commit secrets** - Use .env files
2. **Add .env to .gitignore** - Always
3. **Use os.environ.get()** - Safer than direct access
4. **Restart terminal** after permanent changes
5. **Different values per environment** - Dev vs Prod
