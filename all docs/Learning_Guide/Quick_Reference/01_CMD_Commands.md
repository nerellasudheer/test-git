# CMD Commands - Complete Quick Reference

> Command Prompt essentials from basic to advanced

---

## What is CMD?

- **Command Prompt** - The oldest Windows shell (since 1980s)
- Prompt looks like: `C:\Users\Name>`
- Basic but reliable for Windows operations
- Best for running `.bat` (batch) files and legacy commands

---

## PART 1: NAVIGATION - Getting Around

### Basic Navigation

| Command | Description | Example |
|---------|-------------|---------|
| `cd` | Show current directory path | `cd` |
| `cd folder` | Change to a folder | `cd Desktop` |
| `cd ..` | Go up one level (parent folder) | `cd ..` |
| `cd ..\..` | Go up two levels | `cd ..\..` |
| `cd \` | Go to root of current drive | `cd \` |
| `D:` | Change to different drive | `D:` |

### Listing Files and Folders

| Command | Description | Example |
|---------|-------------|---------|
| `dir` | List files and folders | `dir` |
| `dir /a` | Show ALL files (including hidden) | `dir /a` |
| `dir /b` | Show names only (bare format) | `dir /b` |
| `dir /s` | List ALL files in ALL subfolders | `dir /s` |
| `dir /o:n` | List sorted by name | `dir /o:n` |
| `dir /o:d` | List sorted by date | `dir /o:d` |
| `dir /o:s` | List sorted by size | `dir /o:s` |
| `dir *.txt` | List only .txt files | `dir *.txt` |

---

## PART 2: FILE OPERATIONS

### Creating Files and Folders

| Command | Description | Example |
|---------|-------------|---------|
| `mkdir folder` | Create a folder | `mkdir my_project` |
| `mkdir "folder name"` | Create folder with spaces | `mkdir "My Project"` |
| `type nul > file.txt` | Create empty file | `type nul > readme.txt` |
| `echo text > file.txt` | Create file with content | `echo Hello > readme.txt` |
| `echo text >> file.txt` | Append text to file | `echo World >> readme.txt` |

### Deleting Files and Folders

| Command | Description | Example |
|---------|-------------|---------|
| `del file.txt` | Delete a file | `del old.txt` |
| `del *.txt` | Delete all .txt files | `del *.log` |
| `del /q file.txt` | Delete quietly (no prompt) | `del /q temp.txt` |
| `rmdir folder` | Delete EMPTY folder | `rmdir old_folder` |
| `rmdir /s folder` | Delete folder + ALL contents | `rmdir /s old_folder` |
| `rmdir /s /q folder` | Delete folder quietly | `rmdir /s /q old_folder` |

**WARNING:** Terminal deletions are PERMANENT - no Recycle Bin!

### Copying Files and Folders

| Command | Description | Example |
|---------|-------------|---------|
| `copy src dest` | Copy a file | `copy file.txt backup.txt` |
| `copy src folder\` | Copy file to folder | `copy file.txt backup\` |
| `copy *.txt folder\` | Copy all .txt files | `copy *.txt archive\` |
| `xcopy /E /I src dest` | Copy folder with contents | `xcopy /E /I project backup` |

**xcopy flags:**
- `/E` - Copy subdirectories including empty ones
- `/I` - If destination doesn't exist, assume it's a directory
- `/H` - Copy hidden and system files

### Moving and Renaming

| Command | Description | Example |
|---------|-------------|---------|
| `move src dest` | Move file to new location | `move file.txt folder\` |
| `move old.txt new.txt` | Rename a file | `move old.txt new.txt` |
| `ren old new` | Rename file or folder | `ren oldname.txt newname.txt` |

### Viewing File Contents

| Command | Description | Example |
|---------|-------------|---------|
| `type file.txt` | Display entire file | `type readme.txt` |
| `more file.txt` | View file page by page | `more longfile.txt` |

---

## PART 3: SYSTEM COMMANDS

### Screen and Session

| Command | Description |
|---------|-------------|
| `cls` | Clear the screen |
| `exit` | Close CMD window |
| `title My Window` | Set window title |
| `color 0A` | Change text color (0=black bg, A=green text) |

### Finding Programs and Files

| Command | Description | Example |
|---------|-------------|---------|
| `where program` | Find where program is installed | `where python` |
| `tree` | Display folder structure as tree | `tree` |
| `tree /f` | Display tree with files | `tree /f` |
| `findstr text file` | Search for text in file | `findstr "error" log.txt` |
| `findstr /s text *.*` | Search in all files | `findstr /s "TODO" *.py` |

### Environment Variables

| Command | Description | Example |
|---------|-------------|---------|
| `set` | Show all environment variables | `set` |
| `echo %PATH%` | Show specific variable | `echo %PATH%` |
| `echo %USERPROFILE%` | Show user home directory | `echo %USERPROFILE%` |
| `set VAR=value` | Set temporary variable | `set MY_VAR=hello` |
| `setx VAR value` | Set permanent user variable | `setx MY_VAR hello` |

### Getting Help

| Command | Description |
|---------|-------------|
| `command /?` | Get help for any command |
| `help` | List all available commands |

---

## PART 4: PATH SYMBOLS

| Symbol | Meaning | Example |
|--------|---------|---------|
| `\` | Folder separator | `C:\Users\Desktop` |
| `.` | Current folder | `.\file.txt` |
| `..` | Parent folder (go up one) | `..\other` |
| `*` | Wildcard (any characters) | `*.txt` |
| `?` | Single character wildcard | `file?.txt` |
| `%VAR%` | Environment variable | `%USERPROFILE%` |

---

## PART 5: KEYBOARD SHORTCUTS

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete file/folder names |
| `Up Arrow` | Previous command from history |
| `Down Arrow` | Next command in history |
| `Ctrl + C` | Cancel/stop running command |
| `F7` | Show command history |
| `F3` | Repeat last command |

---

## PART 6: COMMON MISTAKES AND FIXES

### Spaces in Names

```cmd
# WRONG - spaces cause errors
cd My Documents

# CORRECT - use quotes
cd "My Documents"
```

### Case Sensitivity

- CMD is NOT case sensitive
- `DIR`, `dir`, `Dir` all work the same

### File vs Folder

```cmd
# WRONG - can't cd into a file!
cd file.txt

# You can only cd into FOLDERS
cd folder_name
```

---

## PART 7: PRACTICAL EXAMPLES

### Create Project Structure

```cmd
# Navigate to Desktop
cd %USERPROFILE%\Desktop

# Create project folder
mkdir my_project
cd my_project

# Create subfolders
mkdir src
mkdir tests
mkdir docs

# Create files
type nul > src\main.py
type nul > README.md
type nul > requirements.txt

# View structure
tree /f
```

### Backup and Clean

```cmd
# Copy project to backup
xcopy /E /I my_project my_project_backup

# Delete log files
del /q *.log

# Delete temp folder
rmdir /s /q temp
```

### Navigate and Explore

```cmd
# Go to user profile
cd %USERPROFILE%

# List all Python files
dir /s *.py

# Find text in files
findstr /s "import" *.py
```

---

## PART 8: COMMAND COMPARISON

| Task | CMD | PowerShell | Git Bash |
|------|-----|------------|----------|
| List files | `dir` | `ls` or `dir` | `ls` |
| Clear screen | `cls` | `cls` or `clear` | `clear` |
| Where am I? | `cd` (alone) | `pwd` | `pwd` |
| Create file | `type nul > file` | `ni file` | `touch file` |
| Delete folder | `rmdir /s /q` | `rm -r -Force` | `rm -rf` |
| View file | `type file` | `cat file` | `cat file` |
| Find program | `where` | `where` | `which` |

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| 'command' is not recognized | Check spelling, install program, or add to PATH |
| Access denied | Run CMD as Administrator |
| File not found | Check spelling and current directory |
| Can't delete folder | Close programs using it, use `/s /q` flags |
| Path has spaces | Use quotes: `"path with spaces"` |

---

## Key Points to Remember

1. **Use Tab** for auto-completion - saves time and avoids typos
2. **Use quotes** for names with spaces
3. **Deletions are permanent** - no Recycle Bin!
4. **Use `/?`** after any command for help
5. **`dir`** is your friend - use it often to see what's around you
6. **Case doesn't matter** in CMD (unlike Linux)

---
