# Python Virtual Environment - Quick Reference

> Isolate project dependencies

---

## What is Virtual Environment?

- **Isolated Python** per project
- Separate packages from system Python
- Different projects can use different versions
- Recommended for ALL Python projects

---

## Create Virtual Environment

```bash
python -m venv venv
```

*This creates a `venv` folder with isolated Python*

---

## Activate

| Shell | Command |
|-------|---------|
| PowerShell | `.\venv\Scripts\Activate.ps1` |
| CMD | `.\venv\Scripts\activate` |
| Git Bash | `source venv/Scripts/activate` |

**When activated:**
- `(venv)` appears in your prompt
- `pip install` goes to this environment only

---

## Deactivate

```bash
deactivate
```

---

## Package Management

| Command | Description |
|---------|-------------|
| `pip install package` | Install package |
| `pip install package==1.2.3` | Install specific version |
| `pip uninstall package` | Remove package |
| `pip list` | Show installed packages |
| `pip show package` | Package details |

---

## Requirements File

### Save Dependencies
```bash
pip freeze > requirements.txt
```

### Install from File
```bash
pip install -r requirements.txt
```

---

## Check Which Python

```bash
where python                    # Windows - find Python location
python --version                # Version check
pip --version                   # Pip check
(Get-Command python).Source     # PowerShell - full path
```

---

## Check if venv Exists

```powershell
Test-Path venv\Scripts\python.exe    # Returns True/False
dir venv\Scripts\python.exe          # Shows file if exists
```

---

## Common Workflow

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
.\venv\Scripts\Activate.ps1    # PowerShell

# 4. Install packages
pip install requests pandas

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Work on project...

# 7. Deactivate when done
deactivate
```

---

## .gitignore for venv

Always ignore virtual environment in Git:

```gitignore
venv/
.venv/
ENV/
```

---

## Delete Virtual Environment

Simply delete the folder:

```powershell
rm -r venv           # PowerShell
rmdir /s /q venv     # CMD
```

---

## Copy Packages to New Project

```bash
# In OLD project (with venv activated)
pip freeze > requirements.txt

# In NEW project
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## VS Code Auto-Activate venv

1. Press `Ctrl + ,` (Settings)
2. Search: `python.terminal.activateEnvironment`
3. Check/enable the setting

*VS Code will auto-activate venv when opening terminal*

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Script execution disabled | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Wrong Python version | Use `python3 -m venv venv` |
| venv not activating | Check path, use correct shell command |
| Package not found | Make sure venv is activated |

---

## Key Points

1. **Always use venv** for projects
2. **Activate before installing** packages
3. **Save requirements.txt** for sharing
4. **Add venv/ to .gitignore**
5. **Deactivate** when done
