# PowerShell Commands - Complete Quick Reference

> Modern Windows shell - Default in VS Code (Recommended)

---

## What is PowerShell?

- **Modern Windows shell** - More powerful than CMD (since 2006)
- Prompt looks like: `PS C:\Users\Name>`
- **Understands THREE command styles:**
  - PowerShell native commands (Get-ChildItem)
  - CMD commands (dir, copy)
  - Linux-style aliases (ls, cat, rm)
- Microsoft's recommended shell for Windows
- **DEFAULT shell in VS Code**

---

## PART 1: UNDERSTANDING POWERSHELL

### How to Identify PowerShell

```
PS C:\Users\Sudheer>_
↑
└── "PS" at the start means PowerShell
```

### PowerShell Command Pattern

PowerShell uses **Verb-Noun** naming:

| Verb | Meaning | Examples |
|------|---------|----------|
| `Get-` | Retrieve/Read | `Get-Content`, `Get-ChildItem`, `Get-Location` |
| `Set-` | Modify/Change | `Set-Content`, `Set-Location` |
| `New-` | Create | `New-Item` |
| `Remove-` | Delete | `Remove-Item` |
| `Copy-` | Copy | `Copy-Item` |
| `Move-` | Move | `Move-Item` |
| `Test-` | Check/Verify | `Test-Path` |

---

## PART 2: NAVIGATION

### Basic Navigation

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Set-Location` | `cd` | Change directory | `cd Desktop` |
| `Get-Location` | `pwd` | Show current path | `pwd` |
| `cd ..` | - | Go up one level | `cd ..` |
| `cd ..\..` | - | Go up two levels | `cd ..\..` |
| `cd ~` | - | Go to home directory | `cd ~` |
| `cd \` | - | Go to drive root | `cd \` |
| `cd D:\` | - | Change to D: drive | `cd D:\` |

### Listing Files and Folders

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Get-ChildItem` | `ls`, `dir` | List contents | `ls` |
| `Get-ChildItem -Force` | `ls -Force` | Show hidden files | `ls -Force` |
| `Get-ChildItem -Recurse` | `ls -Recurse` | List ALL nested items | `ls -Recurse` |
| `Get-ChildItem -Name` | `ls -Name` | Show names only | `ls -Name` |
| `Get-ChildItem *.txt` | `ls *.txt` | Filter by pattern | `ls *.py` |

---

## PART 3: FILE OPERATIONS

### Creating Files and Folders

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `mkdir folder` | - | Create folder | `mkdir my_project` |
| `New-Item file.txt` | `ni file.txt` | Create empty file | `ni readme.txt` |
| `ni -ItemType Directory folder` | - | Create folder (alternative) | `ni -ItemType Directory src` |
| `ni file1.txt, file2.txt` | - | Create multiple files | `ni main.py, utils.py` |

**Create file with content:**
```powershell
# Method 1: Using Out-File
"Hello World" | Out-File readme.txt

# Method 2: Using Set-Content
Set-Content readme.txt "Hello World"

# Method 3: Append to file
Add-Content readme.txt "New line"
```

### Deleting Files and Folders

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Remove-Item file.txt` | `rm`, `del` | Delete file | `rm old.txt` |
| `Remove-Item *.log` | `rm *.log` | Delete by pattern | `rm *.tmp` |
| `Remove-Item -Recurse folder` | `rm -r folder` | Delete folder + contents | `rm -r old_folder` |
| `Remove-Item -Recurse -Force folder` | `rm -r -Force folder` | Force delete (no prompt) | `rm -r -Force venv` |
| `rmdir folder` | - | Delete EMPTY folder | `rmdir empty_folder` |

**WARNING:** Terminal deletions are PERMANENT - no Recycle Bin!

### Copying Files and Folders

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Copy-Item src dest` | `cp`, `copy` | Copy file | `cp file.txt backup.txt` |
| `Copy-Item src folder\` | `cp src folder\` | Copy to folder | `cp file.txt backup\` |
| `Copy-Item -Recurse src dest` | `cp -r src dest` | Copy folder + contents | `cp -r project backup` |

### Moving and Renaming

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Move-Item src dest` | `mv`, `move` | Move file | `mv file.txt folder\` |
| `Move-Item old.txt new.txt` | `mv old.txt new.txt` | Rename file | `mv old.txt new.txt` |
| `Rename-Item old new` | `ren old new` | Rename | `ren oldname.txt newname.txt` |

### Viewing File Contents

| Full Command | Alias | Description | Example |
|--------------|-------|-------------|---------|
| `Get-Content file.txt` | `cat`, `type` | View entire file | `cat readme.txt` |
| `Get-Content -Head 10 file.txt` | `cat -Head 10 file.txt` | First 10 lines | `cat -Head 10 log.txt` |
| `Get-Content -Tail 10 file.txt` | `cat -Tail 10 file.txt` | Last 10 lines | `cat -Tail 10 log.txt` |
| `Get-Content -Tail 10 -Wait file.txt` | - | Watch file (like tail -f) | `cat -Tail 10 -Wait log.txt` |

---

## PART 4: ENVIRONMENT VARIABLES

### Viewing Variables

| Command | Description | Example |
|---------|-------------|---------|
| `Get-ChildItem Env:` | List ALL environment variables | `Get-ChildItem Env:` |
| `$env:PATH` | View specific variable | `$env:PATH` |
| `$env:USERPROFILE` | User home directory | `$env:USERPROFILE` |
| `$env:USERNAME` | Current username | `$env:USERNAME` |

### Setting Variables

| Command | Description | Scope |
|---------|-------------|-------|
| `$env:MY_VAR = "value"` | Set temporary variable | Current session only |
| `[Environment]::SetEnvironmentVariable("VAR", "value", "User")` | Set permanent user variable | Permanent |
| `[Environment]::SetEnvironmentVariable("VAR", "value", "Machine")` | Set permanent system variable | Requires admin |

---

## PART 5: SYSTEM COMMANDS

### Screen and Session

| Command | Description |
|---------|-------------|
| `Clear-Host` or `cls` or `clear` | Clear the screen |
| `exit` | Close PowerShell window |

### Finding Programs and Files

| Command | Description | Example |
|---------|-------------|---------|
| `where program` | Find program location | `where python` |
| `Get-Command program` | Get command details | `Get-Command python` |
| `Get-Command *keyword*` | Find commands containing keyword | `Get-Command *item*` |
| `Test-Path path` | Check if file/folder exists | `Test-Path .\venv` |
| `tree` | Display folder structure | `tree` |

### Searching in Files

| Command | Description | Example |
|---------|-------------|---------|
| `Select-String pattern file` | Search text in file | `Select-String "error" log.txt` |
| `Select-String -Recurse pattern *.*` | Search in all files | `Select-String -Recurse "TODO" *.py` |

### Getting Help

| Command | Description |
|---------|-------------|
| `Get-Help command` | Get help for a command |
| `Get-Help command -Examples` | Show examples |
| `Get-Help command -Full` | Full documentation |
| `command --help` | Also works for many commands |

---

## PART 6: PATH SYMBOLS

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\` or `/` | Folder separator (both work!) | `C:\Users\Desktop` or `C:/Users/Desktop` |
| `.` | Current folder | `.\file.txt` |
| `..` | Parent folder | `..\other` |
| `~` | Home directory | `cd ~` |
| `*` | Wildcard (any characters) | `*.txt` |
| `?` | Single character wildcard | `file?.txt` |
| `$env:VAR` | Environment variable | `$env:USERPROFILE` |

---

## PART 7: KEYBOARD SHORTCUTS

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete (cycles through options) |
| `Up/Down Arrow` | Navigate command history |
| `Ctrl + C` | Cancel/stop running command |
| `Ctrl + L` | Clear screen (same as cls) |
| `Ctrl + R` | Search command history |
| `F7` | Show command history popup |

---

## PART 8: COMMON MISTAKES AND FIXES

### Spaces in Names

```powershell
# WRONG
cd My Documents

# CORRECT - use quotes
cd "My Documents"

# OR use Tab to auto-complete (adds quotes automatically)
cd My[Tab]
```

### Execution Policy Error

```powershell
# Error: "running scripts is disabled on this system"
# Fix: Run this once
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Slashes

```powershell
# Both work in PowerShell!
cd C:\Users\Desktop
cd C:/Users/Desktop
```

---

## PART 9: PRACTICAL EXAMPLES

### Create Project Structure

```powershell
# Navigate to Desktop
cd ~\Desktop

# Create project folder and structure
mkdir my_project
cd my_project
mkdir src, tests, docs

# Create files
ni src\main.py, src\utils.py
ni tests\test_main.py
ni README.md, requirements.txt, .gitignore

# View structure
ls -Recurse
```

### Backup and Clean

```powershell
# Copy project for backup
cp -r my_project my_project_backup

# Delete log files
rm *.log

# Delete temp folder
rm -r -Force temp

# Clean up Python cache
rm -r -Force __pycache__
```

### File Content Operations

```powershell
# View file
cat README.md

# View first 20 lines
cat -Head 20 large_file.txt

# Watch log file in real-time
cat -Tail 10 -Wait app.log

# Search in file
Select-String "error" log.txt

# Search in all Python files
Select-String -Recurse "import" *.py
```

### Check and Verify

```powershell
# Check if file exists
Test-Path .\requirements.txt

# Check if folder exists
Test-Path .\venv

# Check which Python is active
Get-Command python

# List all Python files
ls -Recurse *.py
```

---

## PART 10: COMMAND COMPARISON TABLE

| Task | PowerShell | CMD | Git Bash |
|------|------------|-----|----------|
| List files | `ls` or `dir` | `dir` | `ls` |
| List with details | `ls -la` | `dir` | `ls -la` |
| Show hidden | `ls -Force` | `dir /a` | `ls -a` |
| Clear screen | `cls` or `clear` | `cls` | `clear` |
| Current path | `pwd` | `cd` (alone) | `pwd` |
| Create file | `ni file.txt` | `type nul > file.txt` | `touch file.txt` |
| Create folder | `mkdir folder` | `mkdir folder` | `mkdir folder` |
| Delete file | `rm file.txt` | `del file.txt` | `rm file.txt` |
| Delete folder | `rm -r folder` | `rmdir /s /q folder` | `rm -rf folder` |
| Copy file | `cp src dest` | `copy src dest` | `cp src dest` |
| Copy folder | `cp -r src dest` | `xcopy /E /I src dest` | `cp -r src dest` |
| Move/Rename | `mv old new` | `move old new` | `mv old new` |
| View file | `cat file` | `type file` | `cat file` |
| Find text | `Select-String` | `findstr` | `grep` |
| Find program | `where` | `where` | `which` |
| Check exists | `Test-Path` | - | `test -e` |

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Script execution disabled | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Command not found | Check spelling, install program |
| Access denied | Run PowerShell as Administrator |
| File not found | Check `pwd` and use `ls` to verify location |
| Tab not completing | Press Tab multiple times to cycle options |

---

## Key Points to Remember

1. **PowerShell is RECOMMENDED** - It's the default in VS Code
2. **Use Tab** - Auto-completes and cycles through options
3. **Both slashes work** - `\` and `/` are interchangeable
4. **Use `ls -Force`** to see hidden files
5. **Aliases make life easy** - `ls`, `cat`, `rm`, `cp`, `mv` all work
6. **`Test-Path`** is great for checking if files/folders exist
7. **Deletions are permanent** - no Recycle Bin!
8. **Set execution policy once** if you get script errors

---
