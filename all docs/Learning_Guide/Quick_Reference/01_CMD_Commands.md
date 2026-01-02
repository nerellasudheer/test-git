# CMD Commands - Quick Reference

> Command Prompt basics for Windows

---

## What is CMD?

- **Oldest** Windows shell (since 1980s)
- Prompt looks like: `C:\Users\Name>`
- Basic but reliable

---

## Navigation

| Command | Description | Example |
|---------|-------------|---------|
| `cd` | Change directory | `cd Desktop` |
| `cd ..` | Go up one level | `cd ..` |
| `cd ..\..` | Go up 2 levels | `cd ..\..` |
| `cd \` | Go to root | `cd \` |
| `cd` (alone) | Show current path | `cd` |
| `D:` | Change drive | `D:` |
| `dir` | List files/folders | `dir` |
| `dir /a` | Show hidden files | `dir /a` |
| `dir /b` | Names only (simple) | `dir /b` |
| `dir /s` | List all subfolders | `dir /s` |

---

## File Operations

### Create

| Command | Description | Example |
|---------|-------------|---------|
| `mkdir` | Create folder | `mkdir my_folder` |
| `type nul >` | Create empty file | `type nul > file.txt` |
| `echo text >` | Create file with text | `echo Hello > file.txt` |

### Delete

| Command | Description | Example |
|---------|-------------|---------|
| `del` | Delete file | `del file.txt` |
| `del *.txt` | Delete by pattern | `del *.log` |
| `rmdir` | Delete empty folder | `rmdir folder` |
| `rmdir /s /q` | Delete folder + contents | `rmdir /s /q folder` |

### Copy & Move

| Command | Description | Example |
|---------|-------------|---------|
| `copy` | Copy file | `copy file.txt backup.txt` |
| `xcopy /E /I` | Copy folder + contents | `xcopy /E /I src dest` |
| `move` | Move/rename file | `move old.txt new.txt` |
| `ren` | Rename | `ren old.txt new.txt` |

### View

| Command | Description | Example |
|---------|-------------|---------|
| `type` | View file contents | `type file.txt` |

---

## System Commands

| Command | Description |
|---------|-------------|
| `cls` | Clear screen |
| `exit` | Close CMD window |
| `echo %PATH%` | Show PATH variable |
| `set` | Show all variables |
| `set VAR=value` | Set temporary variable |
| `where <command>` | Find where program is installed |
| `tree` | Show folder structure as tree |
| `tree /f` | Show tree with files |

---

## Path Symbols

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\` | Folder separator | `C:\Users\Desktop` |
| `.` | Current folder | `.\file.txt` |
| `..` | Parent folder | `..\other` |
| `*` | Wildcard (any chars) | `*.txt` |

---

## Tips

1. **Use Tab** - Auto-completes names
2. **Up Arrow** - Previous command
3. **Ctrl+C** - Cancel running command
4. **Quotes for spaces** - `cd "My Folder"`

---

## Common Mistakes

```cmd
# Wrong - spaces need quotes
cd My Documents

# Correct
cd "My Documents"
```

---

## Quick Examples

```cmd
# Navigate to Desktop
cd %USERPROFILE%\Desktop

# Create project folder
mkdir my_project
cd my_project

# Create files
type nul > main.py
type nul > readme.txt

# List contents
dir

# Go back
cd ..

# Delete project
rmdir /s /q my_project
```
