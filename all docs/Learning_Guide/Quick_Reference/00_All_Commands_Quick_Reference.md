# All Commands - Quick Reference Card

> Everything in one place for fast lookup

---

## CMD Commands

| Command | Description |
|---------|-------------|
| `cd folder` | Change directory |
| `cd ..` | Go up one level |
| `cd` | Show current path |
| `dir` | List files |
| `mkdir folder` | Create folder |
| `type nul > file.txt` | Create empty file |
| `echo text > file.txt` | Create file with text |
| `del file.txt` | Delete file |
| `rmdir /s /q folder` | Delete folder + contents |
| `copy src dest` | Copy file |
| `move src dest` | Move file |
| `ren old new` | Rename |
| `type file.txt` | View file |
| `cls` | Clear screen |
| `where <cmd>` | Find program location |
| `tree` | Show folder structure |

---

## PowerShell Commands

| Command | Alias | Description |
|---------|-------|-------------|
| `Set-Location` | `cd` | Change directory |
| `Get-Location` | `pwd` | Show current path |
| `Get-ChildItem` | `ls`, `dir` | List files |
| `New-Item` | `ni` | Create file |
| `mkdir` | - | Create folder |
| `Remove-Item` | `rm`, `del` | Delete |
| `Remove-Item -r` | `rm -r` | Delete folder + contents |
| `Copy-Item` | `cp` | Copy |
| `Copy-Item -r` | `cp -r` | Copy folder |
| `Move-Item` | `mv` | Move |
| `Rename-Item` | `ren` | Rename |
| `Get-Content` | `cat` | View file |
| `Clear-Host` | `cls` | Clear screen |
| `Test-Path` | - | Check if file exists |
| `where` | - | Find program location |

---

## Git Commands

### Setup
```bash
git config --global user.name "Name"
git config --global user.email "email"
git config --list                       # View settings
```

### Daily Commands

| Command | Description |
|---------|-------------|
| `git init` | Create new repo |
| `git clone <url>` | Download repo |
| `git status` | Check status |
| `git add .` | Stage all changes |
| `git add file` | Stage specific file |
| `git commit -m "msg"` | Commit with message |
| `git commit --amend -m "msg"` | Change last commit |
| `git push` | Upload to remote |
| `git pull` | Download and merge |
| `git fetch` | Download only |

### Branching

| Command | Description |
|---------|-------------|
| `git branch` | List branches |
| `git branch -v` | List with last commit |
| `git branch name` | Create branch |
| `git checkout name` | Switch branch |
| `git switch name` | Switch branch (newer) |
| `git checkout -b name` | Create and switch |
| `git switch -c name` | Create and switch (newer) |
| `git merge name` | Merge branch |
| `git branch -d name` | Delete branch |
| `git branch -m newname` | Rename current branch |
| `git branch -M main` | Force rename to main |

### History & Undo

| Command | Description |
|---------|-------------|
| `git log --oneline` | View history |
| `git log --oneline --graph --all` | Visual history |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git stash` | Save work temporarily |
| `git stash pop` | Restore stashed work |
| `git reset HEAD file` | Unstage file |
| `git checkout -- file` | Discard changes |
| `git restore file` | Discard changes (newer) |
| `git clean -fd` | Delete untracked files ⚠️ |
| `git reset --soft HEAD~1` | Undo last commit (keep changes) |
| `git revert HEAD` | Undo pushed commit (safe) |
| `git reflog` | View all HEAD movements |
| `git blame <file>` | See who changed each line |

### .gitignore Patterns

| Pattern | Matches |
|---------|---------|
| `file.txt` | Any file.txt |
| `*.log` | All .log files |
| `folder/` | Entire folder |
| `**/temp/` | temp anywhere |
| `!keep.txt` | Don't ignore |

### Remote Operations

| Command | Description |
|---------|-------------|
| `git remote -v` | View remotes |
| `git remote add origin <url>` | Add remote |
| `git push -u origin main` | First push |
| `git push origin --delete branch` | Delete remote branch |

---

## Python Virtual Environment

### Create & Activate

| Command | Description |
|---------|-------------|
| `python -m venv venv` | Create virtual env |
| `.\venv\Scripts\Activate.ps1` | Activate (PowerShell) |
| `.\venv\Scripts\activate` | Activate (CMD) |
| `source venv/Scripts/activate` | Activate (Git Bash) |
| `deactivate` | Exit virtual env |

### Packages

| Command | Description |
|---------|-------------|
| `pip install package` | Install package |
| `pip install -r requirements.txt` | Install from file |
| `pip freeze > requirements.txt` | Save dependencies |
| `pip list` | List packages |
| `pip uninstall package` | Remove package |
| `where python` | Check active Python |
| `rm -r venv` | Delete virtual env |
| `Test-Path venv\Scripts\python.exe` | Check if venv exists |

---

## VS Code Shortcuts

### Essential

| Shortcut | Action |
|----------|--------|
| `Ctrl + S` | Save |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |
| `Ctrl + /` | Comment line |
| `Ctrl + F` | Find |
| `Ctrl + H` | Find & Replace |

### Panels

| Shortcut | Action |
|----------|--------|
| `Ctrl + `` ` | Terminal |
| `Ctrl + B` | Sidebar |
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + P` | Quick Open File |
| `Ctrl + Shift + E` | Explorer |
| `Ctrl + Shift + G` | Git |

### Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl + D` | Select next match |
| `Alt + Up/Down` | Move line |
| `Shift + Alt + Up/Down` | Copy line |
| `Ctrl + Shift + K` | Delete line |
| `Shift + Alt + F` | Format document |
| `Ctrl + K, Ctrl + C` | Comment block |
| `Ctrl + K, Ctrl + U` | Uncomment block |
| `F2` | Rename symbol |
| `Ctrl + Shift + L` | Select ALL matches |

### Files

| Shortcut | Action |
|----------|--------|
| `Ctrl + N` | New file |
| `Ctrl + W` | Close file |
| `Ctrl + Tab` | Switch files |
| `Ctrl + Shift + T` | Reopen closed |

---

## Environment Variables

### View

| Shell | Command |
|-------|---------|
| PowerShell | `$env:PATH` |
| CMD | `echo %PATH%` |

### Set (Temporary)

| Shell | Command |
|-------|---------|
| PowerShell | `$env:VAR = "value"` |
| CMD | `set VAR=value` |

### Python

```python
import os
from dotenv import load_dotenv

load_dotenv()
value = os.environ.get("VAR_NAME")
```

### .env File

```
API_KEY=your-key
DEBUG=True
```

---

## Common Tasks

### Create Project Structure
```powershell
mkdir my_project
cd my_project
mkdir src, tests, docs
ni src\main.py, README.md, requirements.txt
```

### Initialize Git Repo
```bash
git init
ni .gitignore
git add .
git commit -m "Initial commit"
```

### Daily Git Workflow
```bash
git pull origin main
git checkout -b feature-x
# make changes
git add .
git commit -m "Add feature"
git push -u origin feature-x
```

### Clean Up Files
```powershell
rm *.log          # Delete log files
rm *.tmp          # Delete temp files
rm -r old_folder  # Delete folder
```

---

## Path Symbols

| Symbol | Meaning |
|--------|---------|
| `.` | Current folder |
| `..` | Parent folder |
| `~` | Home folder |
| `\` or `/` | Folder separator |
| `*` | Wildcard (any) |

---

## Tips

1. **Tab** - Auto-complete file/folder names
2. **Up Arrow** - Previous command
3. **Ctrl + C** - Cancel command
4. **Ctrl + L** - Clear screen
5. **Use quotes** for names with spaces

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Check spelling, install program |
| Permission denied | Run as administrator |
| Git: branch behind | `git pull origin main` |
| File not tracking | Check .gitignore |
| Env var not found | Restart terminal |
