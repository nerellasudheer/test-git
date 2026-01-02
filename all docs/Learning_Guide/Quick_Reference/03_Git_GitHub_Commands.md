# Git & GitHub Commands - Complete Quick Reference

> Version control from basic to advanced

---

## PART 1: UNDERSTANDING GIT

### What is Git?

- **Git** = Version Control System (VCS) that tracks code changes
- **GitHub** = Website to store and share Git projects online
- Git works OFFLINE on your computer
- GitHub needs INTERNET for cloud backup and collaboration

### Git vs GitHub

| Git | GitHub |
|-----|--------|
| Software/Tool | Website/Service |
| Runs on YOUR computer | Stores code IN THE CLOUD |
| Works OFFLINE | Needs INTERNET |
| Tracks changes LOCALLY | Backup + sharing + collaboration |
| Created by Linus Torvalds | Owned by Microsoft |

**Simple Rule:** You can use Git WITHOUT GitHub, but cannot use GitHub without Git!

### Key Concepts

| Term | Definition |
|------|------------|
| **Repository (Repo)** | A folder tracked by Git |
| **Commit** | A snapshot/save point of your project |
| **Branch** | A parallel line of development |
| **HEAD** | Pointer to your current position in Git history |
| **Remote** | A version of your repo on a server (like GitHub) |
| **Clone** | Download a copy of a remote repository |
| **Push** | Upload commits to remote |
| **Pull** | Download and merge from remote |

### The Three Areas

```
[Working Directory] --git add--> [Staging Area] --git commit--> [Repository]
     Your files                  Changes ready                 Permanent
   (where you edit)              to be saved                    history
```

---

## PART 2: SETUP (One-time Configuration)

### Initial Setup

```bash
# Set your identity (REQUIRED - do this once!)
git config --global user.name "Your Full Name"
git config --global user.email "your@email.com"

# Verify settings
git config --list

# View specific setting
git config user.name
git config user.email
```

### Configuration Levels

| Level | Scope | Location | Command |
|-------|-------|----------|---------|
| `--system` | All users | Program Files\Git\etc\gitconfig | `git config --system` |
| `--global` | Current user | C:\Users\YOU\.gitconfig | `git config --global` |
| `--local` | Current repo | .git/config | `git config --local` |

**Priority:** Local > Global > System (local overrides others)

```bash
# Edit global config file
git config --global -e

# View all config with locations
git config --list --show-origin
```

---

## PART 3: REPOSITORY BASICS

### Creating/Cloning Repositories

| Command | Description |
|---------|-------------|
| `git init` | Create new repo in current folder |
| `git clone <url>` | Download existing repo |
| `git clone <url> folder-name` | Clone into specific folder |

### Checking Status

| Command | Description |
|---------|-------------|
| `git status` | Check current state (MOST USED!) |
| `git status -s` | Short/compact status |

**Status Output Meanings:**
- `nothing to commit, working tree clean` - All changes saved
- `Untracked files` - New files Git isn't tracking
- `Changes not staged for commit` - Modified files not staged
- `Changes to be committed` - Files staged and ready

---

## PART 4: DAILY WORKFLOW

### The Basic Cycle

```
Edit files --> git status --> git add --> git commit --> git push --> Repeat
```

### 1. Staging Changes (git add)

| Command | Description |
|---------|-------------|
| `git add file.txt` | Stage specific file |
| `git add file1.txt file2.txt` | Stage multiple files |
| `git add .` | Stage ALL changes in current directory |
| `git add -A` | Stage ALL changes everywhere (including deletions) |
| `git add *.py` | Stage by pattern |

**git add . vs git add -A:**
- `git add .` - Stages new and modified files in current folder
- `git add -A` - Stages new, modified, AND deleted files everywhere

### 2. Committing Changes

```bash
git commit -m "Your descriptive message here"
```

**Good Commit Messages:**
- `Add user authentication feature`
- `Fix login button not working on mobile`
- `Update README with installation instructions`

**Bad Commit Messages:**
- `Fixed stuff` (too vague)
- `asdfasdf` (meaningless)
- `Changes` (what changes?)

**Message Format:** `[Action verb] + [What you did]`
- Add, Fix, Update, Remove, Refactor, Improve

### 3. Push/Pull with Remote

| Command | Description |
|---------|-------------|
| `git push` | Upload commits to remote |
| `git push origin main` | Push to specific branch |
| `git push -u origin main` | First push (sets upstream tracking) |
| `git pull` | Download and merge from remote |
| `git pull origin main` | Pull from specific branch |
| `git fetch` | Download only (don't merge) - safer |
| `git pull --rebase` | Pull with rebase (cleaner history) |

---

## PART 5: BRANCHING

### Viewing Branches

| Command | Description |
|---------|-------------|
| `git branch` | List local branches |
| `git branch -a` | List all branches (local + remote) |
| `git branch -v` | List with last commit info |
| `git branch -r` | List remote branches only |

The `*` indicates your current branch.

### Creating Branches

| Command | Description |
|---------|-------------|
| `git branch name` | Create branch (stay on current) |
| `git checkout -b name` | Create AND switch to new branch |
| `git switch -c name` | Create AND switch (newer syntax) |

### Switching Branches

| Command | Description |
|---------|-------------|
| `git checkout name` | Switch to branch |
| `git switch name` | Switch to branch (newer syntax) |

### Merging Branches

```bash
# First, go to the branch you want to merge INTO
git checkout main

# Then merge the feature branch
git merge feature-branch
```

### Deleting Branches

| Command | Description |
|---------|-------------|
| `git branch -d name` | Delete merged branch (safe) |
| `git branch -D name` | Force delete (even if not merged) |
| `git push origin --delete name` | Delete remote branch |

### Renaming Branches

| Command | Description |
|---------|-------------|
| `git branch -m new-name` | Rename current branch |
| `git branch -m old-name new-name` | Rename specific branch |
| `git branch -M main` | Force rename (often used for master→main) |

---

## PART 6: VIEWING HISTORY

| Command | Description |
|---------|-------------|
| `git log` | Full commit history |
| `git log --oneline` | Compact one-line format (RECOMMENDED) |
| `git log --oneline -5` | Last 5 commits |
| `git log --oneline --graph --all` | Visual branch graph |
| `git log branch-name` | View specific branch history |
| `git log -1` | View only the last commit |
| `git log -1 --format='%an %ae'` | View last commit author info |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |
| `git diff --cached` | Same as --staged |
| `git diff branch1..branch2` | Compare branches |
| `git blame file` | See who changed each line |
| `git show commit-id` | Show commit details |
| `git reflog` | View all HEAD movements (recovery tool) |

Press `q` to exit log view.

---

## PART 7: UNDOING CHANGES

### Quick Decision Guide

| What You Want | Command |
|---------------|---------|
| See old version | `git checkout <commit>` |
| Undo local commits (not pushed) | `git reset` |
| Undo pushed commits | `git revert` |
| Discard uncommitted file changes | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Save changes temporarily | `git stash` |

### Discard File Changes

```bash
# Discard changes in working directory
git restore file.txt
git checkout -- file.txt    # Older syntax

# Unstage a file (keep changes)
git restore --staged file.txt
git reset HEAD file.txt     # Older syntax
```

### Delete Untracked Files

```bash
git clean -n                # Preview what will be deleted (dry run)
git clean -fd               # Delete untracked files/folders (DANGEROUS!)
```

### Undo Commits with git reset

| Mode | Command | What Happens |
|------|---------|--------------|
| **--soft** | `git reset --soft HEAD~1` | Undo commit, keep changes STAGED |
| **--mixed** | `git reset HEAD~1` | Undo commit, keep changes UNSTAGED (default) |
| **--hard** | `git reset --hard HEAD~1` | Undo commit, DELETE changes (DANGEROUS!) |

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged (default)
git reset HEAD~1
git reset --mixed HEAD~1

# Undo last commit, DELETE all changes (DANGEROUS!)
git reset --hard HEAD~1

# Go back to specific commit
git reset --hard abc1234
```

**WARNING:** `--hard` PERMANENTLY DELETES changes! Don't use on pushed commits!

### Undo Pushed Commits with git revert

Creates a NEW commit that undoes an old commit (preserves history - SAFE for shared code).

```bash
git revert HEAD              # Revert last commit
git revert <commit-id>       # Revert specific commit
git revert HEAD --no-edit    # Revert without editing message
git push                     # Push the revert commit
```

**GOLDEN RULE:**
- **PUSHED to GitHub?** → Use **REVERT** (safe)
- **Only LOCAL?** → Can use **RESET**

### Amend Last Commit

```bash
# Change last commit message
git commit --amend -m "New message"

# Add more files to last commit
git add forgotten_file.py
git commit --amend --no-edit
```

**Note:** Only use amend if you haven't pushed yet!

---

## PART 8: STASH - TEMPORARY STORAGE

| Command | Description |
|---------|-------------|
| `git stash` | Save current work temporarily |
| `git stash save "message"` | Save with description |
| `git stash list` | List all stashes |
| `git stash pop` | Apply and remove top stash |
| `git stash apply` | Apply but keep stash |
| `git stash apply stash@{0}` | Apply specific stash |
| `git stash drop` | Delete top stash |
| `git stash drop stash@{0}` | Delete specific stash |
| `git stash clear` | Clear ALL stashes |

---

## PART 9: REMOTE OPERATIONS

### Managing Remotes

| Command | Description |
|---------|-------------|
| `git remote -v` | Show remote URLs |
| `git remote add origin <url>` | Add remote |
| `git remote remove origin` | Remove remote |
| `git remote set-url origin <url>` | Change remote URL |

### Push Operations

| Command | Description |
|---------|-------------|
| `git push -u origin main` | First push (sets upstream) |
| `git push` | Push to tracked remote |
| `git push origin branch-name` | Push specific branch |
| `git push origin --delete branch` | Delete remote branch |
| `git push --tags` | Push all tags |
| `git push origin main --force` | Force push (DANGEROUS!) |

### Pull Operations

| Command | Description |
|---------|-------------|
| `git pull` | Download and merge |
| `git pull origin main` | Pull from specific branch |
| `git pull --rebase` | Pull with rebase (cleaner) |
| `git fetch` | Download only (safe) |
| `git fetch --all` | Fetch from all remotes |

**Pull vs Fetch:**
- `git fetch` = Downloads only (safe, lets you review first)
- `git pull` = Downloads AND merges automatically

---

## PART 10: .gitignore

### Creating .gitignore

Create a `.gitignore` file in your repo root to exclude files from Git.

### Pattern Reference

| Pattern | What it Ignores |
|---------|-----------------|
| `file.txt` | Any file.txt anywhere |
| `/file.txt` | Only file.txt in root folder |
| `folder/` | Entire folder and contents |
| `*.log` | All .log files |
| `**/temp/` | temp folder anywhere |
| `!important.log` | Exception - DON'T ignore this |

### Sample Python .gitignore

```gitignore
# Virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]
*.pyo

# Environment variables (SECRETS!)
.env
.env.local

# IDE settings
.vscode/
.idea/

# Distribution
dist/
build/
*.egg-info/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

### Untrack Already Pushed Files

If a file was pushed before adding to .gitignore:

```bash
# Add to .gitignore first, then:
git rm --cached filename.txt        # Single file
git rm --cached -r foldername/      # Folder
git commit -m "Stop tracking file"
git push
```

### Debugging .gitignore

```bash
git check-ignore -v filename.txt    # Check why file is ignored
git status --ignored                # See all ignored files
git add -f ignored_file.txt         # Force add an ignored file
```

---

## PART 11: ADVANCED COMMANDS

| Command | Description |
|---------|-------------|
| `git cherry-pick <commit>` | Copy specific commit to current branch |
| `git tag v1.0.0` | Create lightweight tag |
| `git tag -a v1.0.0 -m "Release"` | Create annotated tag |
| `git tag` | List all tags |
| `git tag -d v1.0.0` | Delete tag |
| `git push --tags` | Push tags to remote |

---

## PART 12: HANDLING COMMON ISSUES

### Push Rejected - Remote Has Changes

```bash
# Error: "Updates were rejected because the remote contains work..."
git pull origin main              # Pull first
git push origin main              # Then push
```

### Unrelated Histories Error

```bash
# Error: "refusing to merge unrelated histories"
git pull origin main --allow-unrelated-histories
```

### Unfinished Merge

```bash
# Error: "You have not concluded your merge"
# Option 1: Complete the merge
git add .
git commit -m "Merge completed"

# Option 2: Abort the merge
git merge --abort
```

### Merge Conflicts

```bash
# When you see conflict markers in file:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> branch-name

# 1. Edit file to resolve conflicts (remove markers, keep wanted code)
# 2. Stage resolved file
git add resolved_file.txt
# 3. Commit
git commit -m "Resolve merge conflict"
```

### Removing Secrets from Git History

```bash
# If you accidentally committed secrets:
# Step 1: Replace secrets with placeholders in files
# Step 2: Rewrite history
git filter-branch --force --tree-filter \
  "find . -name '*.md' -exec sed -i 's/sk_live_[A-Za-z0-9]*/sk_test_XXXXXX/g' {} + 2>/dev/null || true" \
  --prune-empty HEAD
# Step 3: Force push
git push origin main --force
```

---

## PART 13: TYPICAL WORKFLOWS

### Start New Project

```bash
mkdir my-project
cd my-project
git init
ni README.md                          # Create README
git add .
git commit -m "Initial commit"
# Create repo on GitHub, then:
git remote add origin <url>
git push -u origin main
```

### Clone and Work

```bash
git clone https://github.com/user/repo.git
cd repo
git checkout -b my-feature
# Make changes...
git add .
git commit -m "Add feature"
git push -u origin my-feature
# Create PR on GitHub
```

### Daily Development

```bash
git pull origin main              # Sync with remote
git checkout -b feature-x         # New branch
# Work on files...
git status                        # Check changes
git add .                         # Stage
git commit -m "Add feature x"     # Commit
git push -u origin feature-x      # Push
# Create PR on GitHub
# After PR is merged:
git checkout main
git pull origin main
git branch -d feature-x           # Cleanup local branch
```

---

## PART 14: QUICK TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "git is not recognized" | Install Git, restart terminal |
| "not a git repository" | Run `git init` or cd to correct folder |
| "Your branch is behind" | `git pull origin main` |
| "Updates were rejected" | `git pull` first, then `git push` |
| "Merge conflict" | Edit file, `git add`, `git commit` |
| "HEAD detached" | `git checkout main` to return to branch |
| Wrong commit message | `git commit --amend -m "new message"` |
| Accidentally committed | `git reset --soft HEAD~1` |
| Need to switch but have changes | `git stash`, then switch, then `git stash pop` |
| Execution policy error | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

## PART 15: KEY POINTS TO REMEMBER

1. **`git status`** is your best friend - use it constantly!
2. **Commit often** with small, logical commits
3. **Write clear messages** describing the "why" not just "what"
4. **Pull before push** to avoid conflicts
5. **Branch for features** - keep main/master stable
6. **Never force push** on shared branches
7. **Use .gitignore** - don't commit secrets or temp files
8. **PUSHED to GitHub?** → Use REVERT (safe)
9. **Only LOCAL?** → Can use RESET
10. **Never commit secrets** - they stay in history forever!

---
