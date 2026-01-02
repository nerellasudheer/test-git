# All Commands - Master Quick Reference Card

> Everything in one place for fast lookup - From Basic to Advanced

---

## Table of Contents

1. [CMD Commands](#cmd-commands)
2. [PowerShell Commands](#powershell-commands)
3. [Git Commands](#git-commands)
4. [VS Code Shortcuts](#vs-code-shortcuts)
5. [Python Virtual Environment](#python-virtual-environment)
6. [Environment Variables](#environment-variables)
7. [Common Tasks & Workflows](#common-tasks--workflows)
8. [Quick Troubleshooting](#quick-troubleshooting)

---

## CMD Commands

### Navigation

| Command | Description |
|---------|-------------|
| `cd folder` | Change directory |
| `cd ..` | Go up one level |
| `cd \` | Go to root of drive |
| `cd` (alone) | Show current path |
| `D:` | Change to D: drive |
| `dir` | List files and folders |
| `dir /a` | Show hidden files |
| `dir /s` | List all in subfolders |
| `tree` | Show folder structure |
| `tree /f` | Show tree with files |

### File Operations

| Command | Description |
|---------|-------------|
| `mkdir folder` | Create folder |
| `type nul > file.txt` | Create empty file |
| `echo text > file.txt` | Create file with text |
| `del file.txt` | Delete file |
| `rmdir /s /q folder` | Delete folder + contents |
| `copy src dest` | Copy file |
| `xcopy /E /I src dest` | Copy folder + contents |
| `move src dest` | Move/rename file |
| `ren old new` | Rename |
| `type file.txt` | View file contents |
| `cls` | Clear screen |
| `where program` | Find program location |

---

## PowerShell Commands

### Navigation

| Command | Alias | Description |
|---------|-------|-------------|
| `Set-Location` | `cd` | Change directory |
| `Get-Location` | `pwd` | Show current path |
| `cd ~` | - | Go to home directory |
| `Get-ChildItem` | `ls`, `dir` | List contents |
| `Get-ChildItem -Force` | `ls -Force` | Show hidden files |
| `Get-ChildItem -Recurse` | `ls -Recurse` | List all nested |

### File Operations

| Command | Alias | Description |
|---------|-------|-------------|
| `mkdir folder` | - | Create folder |
| `New-Item file.txt` | `ni file.txt` | Create file |
| `ni file1, file2` | - | Create multiple files |
| `Remove-Item` | `rm`, `del` | Delete file |
| `Remove-Item -Recurse` | `rm -r` | Delete folder + contents |
| `Copy-Item` | `cp`, `copy` | Copy file |
| `Copy-Item -Recurse` | `cp -r` | Copy folder + contents |
| `Move-Item` | `mv`, `move` | Move/rename |
| `Rename-Item` | `ren` | Rename |
| `Get-Content` | `cat`, `type` | View file |
| `Get-Content -Head 10` | - | First 10 lines |
| `Get-Content -Tail 10` | - | Last 10 lines |
| `Clear-Host` | `cls`, `clear` | Clear screen |
| `Test-Path` | - | Check if exists |
| `where` | - | Find program location |

---

## Git Commands

### Setup (One-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list                       # View settings
```

### Repository Basics

| Command | Description |
|---------|-------------|
| `git init` | Create new repo |
| `git clone <url>` | Download repo |
| `git status` | Check current state |
| `git status -s` | Short status |

### Daily Workflow

| Command | Description |
|---------|-------------|
| `git add .` | Stage all changes |
| `git add file` | Stage specific file |
| `git add -A` | Stage everything (including deletions) |
| `git commit -m "msg"` | Commit with message |
| `git push` | Upload to remote |
| `git push -u origin main` | First push (set upstream) |
| `git pull` | Download and merge |
| `git fetch` | Download only (safe) |

### Branching

| Command | Description |
|---------|-------------|
| `git branch` | List branches |
| `git branch -a` | List all (local + remote) |
| `git branch name` | Create branch |
| `git checkout name` | Switch branch |
| `git switch name` | Switch branch (newer) |
| `git checkout -b name` | Create and switch |
| `git switch -c name` | Create and switch (newer) |
| `git merge name` | Merge branch into current |
| `git branch -d name` | Delete merged branch |
| `git branch -D name` | Force delete branch |
| `git branch -m newname` | Rename current branch |

### History & Viewing

| Command | Description |
|---------|-------------|
| `git log --oneline` | View compact history |
| `git log --oneline --graph --all` | Visual branch graph |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git blame file` | See who changed each line |
| `git reflog` | View all HEAD movements |

### Undoing Changes

| Command | Description |
|---------|-------------|
| `git restore file` | Discard file changes |
| `git restore --staged file` | Unstage file |
| `git reset --soft HEAD~1` | Undo commit (keep staged) |
| `git reset HEAD~1` | Undo commit (keep unstaged) |
| `git reset --hard HEAD~1` | Undo commit (DELETE changes) |
| `git revert HEAD` | Undo pushed commit (safe) |
| `git commit --amend -m "msg"` | Change last commit message |

### Stash

| Command | Description |
|---------|-------------|
| `git stash` | Save work temporarily |
| `git stash list` | List all stashes |
| `git stash pop` | Apply and remove stash |
| `git stash apply` | Apply but keep stash |
| `git stash drop` | Delete stash |

### Remote Operations

| Command | Description |
|---------|-------------|
| `git remote -v` | View remotes |
| `git remote add origin <url>` | Add remote |
| `git remote set-url origin <url>` | Change remote URL |
| `git push origin --delete branch` | Delete remote branch |

### .gitignore Patterns

| Pattern | Matches |
|---------|---------|
| `file.txt` | Any file.txt |
| `*.log` | All .log files |
| `folder/` | Entire folder |
| `**/temp/` | temp anywhere |
| `!keep.txt` | Don't ignore |

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
| `Ctrl + Shift + F` | Find in all files |

### Panels & Navigation

| Shortcut | Action |
|----------|--------|
| `Ctrl + `` ` | Toggle Terminal |
| `Ctrl + B` | Toggle Sidebar |
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + P` | Quick Open File |
| `Ctrl + G` | Go to line number |
| `Ctrl + Shift + E` | Explorer |
| `Ctrl + Shift + G` | Git panel |
| `Ctrl + Shift + X` | Extensions |

### Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl + D` | Select next match |
| `Ctrl + Shift + L` | Select ALL matches |
| `Alt + Up/Down` | Move line |
| `Shift + Alt + Up/Down` | Copy line |
| `Ctrl + Shift + K` | Delete line |
| `Shift + Alt + F` | Format document |
| `Ctrl + K, Ctrl + C` | Comment block |
| `Ctrl + K, Ctrl + U` | Uncomment block |
| `F2` | Rename symbol |

### Multi-Cursor

| Shortcut | Action |
|----------|--------|
| `Alt + Click` | Add cursor at click |
| `Ctrl + Alt + Up/Down` | Add cursor above/below |
| `Esc` | Exit multi-cursor |

### Files

| Shortcut | Action |
|----------|--------|
| `Ctrl + N` | New file |
| `Ctrl + W` | Close file |
| `Ctrl + Tab` | Switch files |
| `Ctrl + Shift + T` | Reopen closed file |

### View

| Shortcut | Action |
|----------|--------|
| `Ctrl + =` | Zoom in |
| `Ctrl + -` | Zoom out |
| `Ctrl + 0` | Reset zoom |
| `Ctrl + \` | Split editor |

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

### Package Management

| Command | Description |
|---------|-------------|
| `pip install package` | Install package |
| `pip install package==1.2.3` | Install specific version |
| `pip install -r requirements.txt` | Install from file |
| `pip freeze > requirements.txt` | Save dependencies |
| `pip list` | List packages |
| `pip list --outdated` | Show outdated packages |
| `pip show package` | Package details |
| `pip uninstall package` | Remove package |

### Verification

| Command | Description |
|---------|-------------|
| `where python` | Check Python location |
| `python --version` | Check Python version |
| `Test-Path venv\Scripts\python.exe` | Check if venv exists |

### Cleanup

| Command | Description |
|---------|-------------|
| `deactivate` | Exit venv first! |
| `rm -r -Force venv` | Delete venv (PowerShell) |
| `rmdir /s /q venv` | Delete venv (CMD) |

---

## Environment Variables

### View Variables

| Shell | Command |
|-------|---------|
| PowerShell | `$env:PATH` |
| PowerShell | `Get-ChildItem Env:` |
| CMD | `echo %PATH%` |
| CMD | `set` |

### Set Temporary Variables

| Shell | Command |
|-------|---------|
| PowerShell | `$env:VAR = "value"` |
| CMD | `set VAR=value` |

### Set Permanent Variables

| Method | Command |
|--------|---------|
| CMD (User) | `setx VAR "value"` |
| CMD (System) | `setx VAR "value" /M` (admin) |
| PowerShell (User) | `[Environment]::SetEnvironmentVariable("VAR", "value", "User")` |

### Python .env Files

```python
# Install: pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()                            # Load .env file
value = os.getenv("VAR_NAME")            # Get variable
value = os.getenv("VAR", "default")      # With default
```

**.env File Format:**
```env
API_KEY=your-key-here
DEBUG=True
DATABASE_URL=localhost
```

---

## Common Tasks & Workflows

### Create Python Project

```powershell
mkdir my_project
cd my_project
python -m venv venv
.\venv\Scripts\Activate.ps1
ni main.py, requirements.txt, .gitignore, .env
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

### Clone & Setup Project

```bash
git clone <url>
cd project
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Copy .env.example to .env and fill values
```

### Clean Up Files

```powershell
rm *.log              # Delete log files
rm -r __pycache__     # Delete Python cache
rm -r node_modules    # Delete npm packages
```

---

## Path Symbols

| Symbol | Meaning |
|--------|---------|
| `.` | Current folder |
| `..` | Parent folder |
| `~` | Home folder (PowerShell) |
| `\` or `/` | Folder separator |
| `*` | Wildcard (any) |
| `%VAR%` | Env variable (CMD) |
| `$env:VAR` | Env variable (PowerShell) |

---

## Terminal Tips

1. **Tab** - Auto-complete file/folder names
2. **Up Arrow** - Previous command
3. **Ctrl + C** - Cancel/stop command
4. **Ctrl + L** - Clear screen
5. **Use quotes** for names with spaces

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Check spelling, install program, check PATH |
| Permission denied | Run as administrator |
| Git: branch behind | `git pull origin main` |
| Git: push rejected | `git pull` first, then push |
| File not tracking | Check .gitignore |
| Env var not found | Restart terminal |
| Script execution disabled | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Python: module not found | Activate venv, install package |
| venv not activating | Check path, use correct shell command |
| .env not loading | Check file location, call `load_dotenv()` |

---

## Shell Comparison

| Task | CMD | PowerShell | Git Bash |
|------|-----|------------|----------|
| List files | `dir` | `ls` or `dir` | `ls` |
| Clear screen | `cls` | `cls` or `clear` | `clear` |
| Current path | `cd` (alone) | `pwd` | `pwd` |
| Create file | `type nul > file` | `ni file` | `touch file` |
| Delete folder | `rmdir /s /q` | `rm -r -Force` | `rm -rf` |
| View file | `type file` | `cat file` | `cat file` |
| Find program | `where` | `where` | `which` |
| Check exists | - | `Test-Path` | `test -e` |

---

## Key Points Summary

### Git
1. `git status` is your best friend
2. Commit often with clear messages
3. Pull before push
4. Never force push on shared branches
5. Use .gitignore for secrets

### Virtual Environment
1. Always use venv for Python projects
2. Activate before installing packages
3. Use requirements.txt
4. Add venv/ to .gitignore

### Environment Variables
1. Never commit secrets to Git
2. Use .env files for project secrets
3. Add .env to .gitignore
4. Use os.getenv() with defaults

### VS Code
1. `Ctrl + Shift + P` can do everything
2. `Ctrl + P` for quick file opening
3. `Ctrl + D` for multi-cursor editing
4. `Shift + Alt + F` to format code

---

*For detailed explanations, see individual Quick Reference files in this folder.*

---
