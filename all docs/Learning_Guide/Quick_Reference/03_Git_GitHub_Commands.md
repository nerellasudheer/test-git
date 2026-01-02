# Git & GitHub Commands - Quick Reference

> Version control essentials

---

## Setup (One-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list                           # View all settings
```

### Config Levels

| Level | Scope | Location |
|-------|-------|----------|
| `--system` | All users | Program Files\Git\etc\gitconfig |
| `--global` | Current user | C:\Users\YOU\.gitconfig |
| `--local` | Current repo | .git/config |

*Local overrides Global overrides System*

---

## Repository Basics

| Command | Description |
|---------|-------------|
| `git init` | Create new repo in current folder |
| `git clone <url>` | Download existing repo |
| `git status` | Check current state |
| `git status -s` | Short status |

---

## Daily Workflow

### 1. Check Status
```bash
git status
```

### 2. Stage Changes
| Command | Description |
|---------|-------------|
| `git add file.txt` | Stage specific file |
| `git add .` | Stage all changes |
| `git add *.py` | Stage by pattern |
| `git add -A` | Stage everything |

### 3. Commit
```bash
git commit -m "Your message here"
```

### 4. Push to Remote
```bash
git push origin main
git push -u origin main    # First time (sets upstream)
```

### 5. Pull Latest
```bash
git pull origin main
```

---

## Branching

| Command | Description |
|---------|-------------|
| `git branch` | List branches |
| `git branch -a` | List all (including remote) |
| `git branch -v` | List with last commit info |
| `git branch name` | Create new branch |
| `git checkout name` | Switch to branch |
| `git switch name` | Switch to branch (newer) |
| `git checkout -b name` | Create AND switch |
| `git switch -c name` | Create AND switch (newer) |
| `git branch -d name` | Delete merged branch |
| `git branch -D name` | Force delete branch |
| `git branch -m newname` | Rename current branch |
| `git branch -M main` | Force rename to main |

---

## Merging

```bash
# Switch to target branch first
git checkout main

# Merge feature branch into main
git merge feature-branch
```

---

## View History

| Command | Description |
|---------|-------------|
| `git log` | Full commit history |
| `git log --oneline` | Compact history |
| `git log --oneline -5` | Last 5 commits |
| `git log --graph` | Visual branch graph |
| `git log --oneline --graph --all` | Full visual history |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git diff branch1..branch2` | Compare branches |
| `git log <branch> --oneline` | View specific branch history |
| `git blame <file>` | See who changed each line |
| `git show <commit>` | Show commit details |

---

## Undo Changes

### Unstage File
```bash
git reset HEAD file.txt
```

### Discard File Changes
```bash
git checkout -- file.txt
git restore file.txt           # Newer command
```

### Delete Untracked Files
```bash
git clean -n                   # Preview what will be deleted
git clean -fd                  # Delete untracked files/folders ⚠️
```

### Undo Last Commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (discard changes)
```bash
git reset --hard HEAD~1    # DANGEROUS!
```

### Revert Pushed Commit (safe)
```bash
git revert HEAD
git push
```

### Amend Last Commit
```bash
git commit --amend -m "New message"    # Change message
git commit --amend                      # Add staged files to last commit
```

---

## Stash (Temporary Storage)

| Command | Description |
|---------|-------------|
| `git stash` | Save current work |
| `git stash save "message"` | Save with description |
| `git stash list` | List all stashes |
| `git stash pop` | Apply and remove top stash |
| `git stash apply` | Apply but keep stash |
| `git stash drop` | Delete top stash |

---

## Remote

| Command | Description |
|---------|-------------|
| `git remote -v` | Show remotes |
| `git remote add origin <url>` | Add remote |
| `git fetch origin` | Download without merge |
| `git pull origin main` | Download and merge |
| `git push origin main` | Upload commits |
| `git push origin --delete branch` | Delete remote branch |
| `git remote set-url origin <url>` | Change remote URL |
| `git remote remove origin` | Remove remote |

---

## .gitignore

Create `.gitignore` file to exclude files:

```gitignore
# Python
__pycache__/
*.pyc
venv/
.env

# IDE
.vscode/
.idea/

# Logs
*.log
logs/

# OS
.DS_Store
Thumbs.db
```

### Untrack Already Pushed Files
```bash
# Add to .gitignore first, then:
git rm --cached filename.txt
git rm --cached -r foldername/
git commit -m "Stop tracking file"
git push
```

---

## Common Patterns

### .gitignore Patterns

| Pattern | Matches |
|---------|---------|
| `file.txt` | Any file.txt |
| `/file.txt` | Only root file.txt |
| `folder/` | Folder and contents |
| `*.log` | All .log files |
| `**/temp/` | temp folder anywhere |
| `!important.log` | Exception - don't ignore |

---

## Typical Workflows

### Start New Project
```bash
mkdir my-project
cd my-project
git init
ni README.md
git add .
git commit -m "Initial commit"
```

### Clone and Work
```bash
git clone https://github.com/user/repo.git
cd repo
git checkout -b my-feature
# make changes
git add .
git commit -m "Add feature"
git push -u origin my-feature
```

### Daily Development
```bash
git pull origin main              # Sync
git checkout -b feature-x         # New branch
# work on files
git status                        # Check
git add .                         # Stage
git commit -m "Add feature x"     # Commit
git push -u origin feature-x      # Push
# Create PR on GitHub
# After merge:
git checkout main
git pull origin main
git branch -d feature-x           # Cleanup
```

---

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Your branch is behind" | `git pull origin main` |
| Merge conflict | Edit file, `git add`, `git commit` |
| Wrong commit message | `git commit --amend -m "new message"` |
| Accidentally committed | `git reset --soft HEAD~1` |
| Need to switch but have changes | `git stash` then `git checkout` |

---

## Pull vs Fetch

| Command | What it does |
|---------|--------------|
| `git fetch` | Downloads only (safe) |
| `git pull` | Downloads AND merges |

Use `fetch` when you want to review first.

---

## git add . vs git add -A

| Command | What it does |
|---------|--------------|
| `git add .` | Stage new + modified in current dir |
| `git add -A` | Stage new + modified + deleted everywhere |

*Use `git add -A` to include deleted files*

---

## Advanced Commands

| Command | Description |
|---------|-------------|
| `git cherry-pick <commit>` | Copy specific commit to current branch |
| `git tag v1.0` | Create version tag |
| `git tag -a v1.0 -m "msg"` | Create annotated tag |
| `git pull --rebase` | Pull with rebase (cleaner history) |
| `git reflog` | View all HEAD movements (recovery) |

---

## Key Points

1. **Commit often** - Small, logical commits
2. **Write clear messages** - Describe the "why"
3. **Pull before push** - Avoid conflicts
4. **Branch for features** - Keep main stable
5. **Never force push** on shared branches
6. **Use .gitignore** - Don't commit secrets/temp files
