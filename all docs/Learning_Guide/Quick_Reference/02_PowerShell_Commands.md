# PowerShell Commands - Quick Reference

> Modern Windows shell (Default in VS Code)

---

## What is PowerShell?

- **Newer** and more powerful than CMD
- Prompt looks like: `PS C:\Users\Name>`
- Understands **CMD commands + Linux aliases + its own commands**
- Recommended for beginners

---

## Navigation

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `Set-Location` | `cd` | Change directory | `cd Desktop` |
| `Get-Location` | `pwd` | Show current path | `pwd` |
| `Get-ChildItem` | `ls`, `dir` | List contents | `ls` |
| `Get-ChildItem -Force` | `ls -Force` | Show hidden files | `ls -Force` |
| `Get-ChildItem -Recurse` | `ls -Recurse` | List all nested | `ls -Recurse` |
| `Get-ChildItem -Name` | `ls -Name` | List names only | `ls -Name` |

---

## File Operations

### Create

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `mkdir` | - | Create folder | `mkdir my_folder` |
| `New-Item` | `ni` | Create file | `ni file.txt` |
| `New-Item -ItemType Directory` | - | Create folder | `ni -ItemType Directory folder` |
| Multiple files | - | Create several | `ni file1.txt, file2.txt` |

**Create file with content:**
```powershell
"Hello World" | Out-File readme.txt
Set-Content readme.txt "Hello World"
```

### Delete

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `Remove-Item` | `rm`, `del` | Delete file | `rm file.txt` |
| `Remove-Item *.log` | - | Delete by pattern | `rm *.log` |
| `Remove-Item -Recurse` | `rm -r` | Delete folder + contents | `rm -r folder` |
| `Remove-Item -Recurse -Force` | `rm -r -Force` | Force delete | `rm -r -Force folder` |

### Copy

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `Copy-Item` | `cp`, `copy` | Copy file | `cp file.txt backup.txt` |
| `Copy-Item -Recurse` | `cp -r` | Copy folder + contents | `cp -r src dest` |

### Move & Rename

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `Move-Item` | `mv`, `move` | Move file | `mv file.txt folder\` |
| `Rename-Item` | `ren` | Rename | `ren old.txt new.txt` |

### View

| Command | Alias | Description | Example |
|---------|-------|-------------|---------|
| `Get-Content` | `cat`, `type` | View file | `cat file.txt` |
| `Get-Content -Head 10` | - | First 10 lines | `cat file.txt -Head 10` |
| `Get-Content -Tail 10` | - | Last 10 lines | `cat file.txt -Tail 10` |

---

## Environment Variables

| Command | Description |
|---------|-------------|
| `$env:PATH` | View PATH |
| `$env:USERPROFILE` | User home directory |
| `$env:VAR = "value"` | Set temporary variable |
| `Get-ChildItem Env:` | List all variables |

---

## System Commands

| Command | Description |
|---------|-------------|
| `Clear-Host` or `cls` | Clear screen |
| `Get-Help command` | Get help on command |
| `Get-Command *keyword*` | Find commands |
| `Test-Path <path>` | Check if file/folder exists |
| `where <command>` | Find where program is installed |
| `tree` | Show folder structure as tree |
| `exit` | Close PowerShell |

---

## Path Symbols

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\` or `/` | Folder separator | Both work in PowerShell |
| `.` | Current folder | `.\file.txt` |
| `..` | Parent folder | `..\other` |
| `~` | Home directory | `cd ~` |
| `*` | Wildcard | `*.txt` |

---

## Tips

1. **Tab** - Auto-completes names
2. **Up/Down Arrow** - Command history
3. **Ctrl+C** - Cancel command
4. **Ctrl+L** - Clear screen
5. **Get-Help** - Built-in documentation

---

## PowerShell vs CMD vs Git Bash

| Task | PowerShell | CMD | Git Bash |
|------|------------|-----|----------|
| List files | `ls` or `dir` | `dir` | `ls` |
| Clear screen | `cls` or `clear` | `cls` | `clear` |
| Current path | `pwd` | `cd` | `pwd` |
| Create file | `ni file.txt` | `type nul > file.txt` | `touch file.txt` |
| Delete folder | `rm -r folder` | `rmdir /s /q folder` | `rm -rf folder` |

---

## Quick Examples

```powershell
# Navigate to Desktop
cd ~\Desktop

# Create project structure
mkdir my_project
cd my_project
mkdir src, tests, docs
ni src\main.py, src\utils.py
ni tests\test_main.py
ni README.md, requirements.txt

# List all files recursively
ls -Recurse

# View file
cat README.md

# Clean up log files
rm *.log

# Copy project for backup
cp -r my_project my_project_backup

# Go back and delete
cd ..
rm -r my_project
```

---

## Common Cmdlet Pattern

PowerShell uses **Verb-Noun** pattern:

| Verb | Meaning | Examples |
|------|---------|----------|
| `Get-` | Retrieve | `Get-Content`, `Get-ChildItem` |
| `Set-` | Modify | `Set-Content`, `Set-Location` |
| `New-` | Create | `New-Item` |
| `Remove-` | Delete | `Remove-Item` |
| `Copy-` | Copy | `Copy-Item` |
| `Move-` | Move | `Move-Item` |
