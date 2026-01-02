# Git & GitHub - Complete Guide

## Master Version Control from Beginner to Advanced

---

# PART 1: WHAT IS GIT?

---

## 1.1 The Problem Git Solves

Without Git, you end up with files like:
- essay_v1.doc
- essay_v2.doc
- essay_final.doc
- essay_final_REALLY_FINAL.doc

**Git solves this!** With Git, you have ONE file, but Git remembers EVERY version automatically!

```
┌─────────────────────────────────────────────────────────────────┐
│                 WITHOUT GIT vs WITH GIT                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WITHOUT GIT:                                                    │
│  📁 my_project                                                   │
│  ├── main_v1.py                                                  │
│  ├── main_v2.py                                                  │
│  ├── main_final.py                                               │
│  └── main_DONT_DELETE.py                                         │
│                                                                  │
│  Problems: Which is latest? Takes disk space. Confusing!        │
│                                                                  │
│  WITH GIT:                                                       │
│  📁 my_project                                                   │
│  ├── main.py          ← Just ONE file!                          │
│  └── .git/            ← Git stores ALL versions here            │
│                                                                  │
│  Git remembers: Every version, what changed, who, when          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Git Definition

**Git** is a **Version Control System (VCS)**:
- **VERSION** = A snapshot of your files at a specific time
- **CONTROL** = You decide when to save snapshots
- **SYSTEM** = Software that manages all of this

Think of Git as:
- 📸 A **CAMERA** for your code (takes snapshots)
- ⏰ A **TIME MACHINE** (go back to any point)
- 📝 A **DIARY** (records every change, who, when, why)

---

## 1.3 Git vs GitHub

**VERY IMPORTANT:** Git and GitHub are NOT the same thing!

| GIT | GITHUB |
|-----|--------|
| A SOFTWARE/TOOL | A WEBSITE/SERVICE |
| Runs on YOUR COMPUTER | Stores code IN THE CLOUD |
| Works OFFLINE | Needs INTERNET |
| Tracks changes LOCALLY | Backup + sharing + collaboration |
| Created by Linus Torvalds (2005) | Owned by Microsoft |
| Like Microsoft Word | Like Google Drive |

**Simple Summary:**
- **GIT** = The tool that tracks your code (on your computer)
- **GITHUB** = A website to store and share your Git projects

You can use Git WITHOUT GitHub!
You CANNOT use GitHub without Git!

---

## 1.4 Why Use Git?

1. **HISTORY** - See what code looked like before, find when bugs were introduced
2. **BACKUP** - Code is safe even if your computer dies
3. **EXPERIMENTATION** - Create branches to try new features safely
4. **COLLABORATION** - Multiple people can work on same project
5. **PROFESSIONAL** - Every software company uses Git; it's a required skill

---

# PART 2: GIT CONCEPTS

---

## 2.1 What is a Repository (Repo)?

A **Repository** is a folder that Git is tracking.

```
my_project\                    ← This whole folder is the REPO
├── .git\                      ← Hidden folder (Git's brain)
│   ├── objects\               ← All versions stored here
│   ├── refs\                  ← Branch pointers
│   ├── HEAD                   ← Current position pointer
│   └── config                 ← Repository settings
├── main.py                    ← Your code files
├── utils.py
└── README.md
```

**Types of Repositories:**
- **LOCAL REPO** = On your computer (created with `git init` or `git clone`)
- **REMOTE REPO** = On a server like GitHub (backup + sharing)

---

## 2.2 What is a Commit?

A **COMMIT** is a snapshot of your project at a specific moment.

Think of it like:
- Taking a photo 📸
- Saving your game progress 🎮
- Creating a restore point 💾

**What a commit contains:**
- Snapshot of all tracked files
- Commit message (your description)
- Author name and email
- Date and time
- Parent commit (previous snapshot)
- Unique ID (hash like abc1234)

**Commits form a chain (History):**
```
┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐
│Commit 1│───▶│Commit 2│───▶│Commit 3│───▶│Commit 4│
│Initial │    │Added   │    │Fixed   │    │Added   │
│setup   │    │login   │    │bug     │    │logout  │
└────────┘    └────────┘    └────────┘    └────────┘
```

---

## 2.3 What is HEAD?

**HEAD** is like a "YOU ARE HERE" marker - it points to where you currently are in Git history.

```
Normally: HEAD → main → latest commit

DETACHED HEAD: When HEAD points directly to a commit (not a branch)
This happens when you checkout an old commit
```

---

## 2.4 What is a Branch?

A **BRANCH** is a separate line of development - like a parallel universe for your code.

```
                        feature-login
                            ↓
                       ┌────────┐
                      ╱│Add form│
                     ╱ └────────┘
  ┌────────┐    ┌────────┐    ┌────────┐
  │Commit 1│───▶│Commit 2│───▶│Commit 3│
  └────────┘    └────────┘    └────────┘
                                   ↑
                                  main
```

**Common Branch Names:**
- `main` / `master` - Main production code
- `develop` - Development version
- `feature-xxx` - New feature being worked on
- `bugfix-xxx` - Bug fix
- `hotfix-xxx` - Urgent fix

---

## 2.5 The Three Areas

```
┌─────────────────────────────────────────────────────────────────┐
│               GIT'S THREE AREAS                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Working Directory]  ──git add──▶  [Staging Area]              │
│         │                                │                       │
│    Your files                      Changes ready                 │
│    (where you edit)                to be saved                   │
│                                          │                       │
│                                    ──git commit──▶               │
│                                          │                       │
│                                   [Repository]                   │
│                                          │                       │
│                                   Permanent history              │
│                                   (committed snapshots)          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 3: INSTALLING AND SETTING UP GIT

---

## 3.1 Checking if Git is Installed

```bash
git --version
```

**If installed:** `git version 2.43.0.windows.1`
**If NOT installed:** `'git' is not recognized...` → Install from git-scm.com

---

## 3.2 Initial Configuration (Do This ONCE!)

```bash
# STEP 1: Set your name
git config --global user.name "Your Full Name"

# STEP 2: Set your email (use same as GitHub!)
git config --global user.email "your@email.com"

# STEP 3: Verify settings
git config --list
```

**Why is this important?** Every commit is "signed" with this info.

---

## 3.3 Git Configuration Levels

| Level | Scope | File Location | Command |
|-------|-------|---------------|---------|
| `--system` | All users | `C:\Program Files\Git\etc\gitconfig` | `git config --system` |
| `--global` | Current user | `C:\Users\YOU\.gitconfig` | `git config --global` |
| `--local` | Current repo | `.git/config` in repo | `git config --local` |

**Priority:** Local > Global > System (local overrides others)

```bash
# View all config
git config --list

# View specific level
git config --global --list

# Edit global config file
git config --global -e
```

---

# PART 4: BASIC GIT COMMANDS

---

## 4.1 git init - Start a New Repository

```bash
# Navigate to your project folder
cd C:\Users\Sudheer\Desktop\my_project

# Initialize Git
git init
```

**Output:** `Initialized empty Git repository in .../my_project/.git/`

This creates the hidden `.git` folder. **You only do this ONCE per project!**

---

## 4.2 git status - Check Current State

```bash
git status
```

This is the **most used command** - use it ALL THE TIME!

**Output meanings:**
- `nothing to commit, working tree clean` - All changes saved
- `Untracked files` - New files Git isn't tracking yet
- `Changes not staged for commit` - Modified files not staged
- `Changes to be committed` - Files staged and ready to commit

---

## 4.3 git add - Stage Changes

```bash
# Add ONE specific file
git add filename.py

# Add multiple specific files
git add file1.py file2.py

# Add ALL changes (most common!)
git add .

# Add all changes in entire repository (including deletions)
git add -A
git add --all
```

**git add . vs git add -A:**
- `git add .` - Stages new and modified files in current folder
- `git add -A` - Stages new, modified, AND deleted files everywhere

---

## 4.4 git commit - Save Changes

```bash
git commit -m "Your message describing the changes"
```

**Good Commit Messages:**
- ✓ "Add user authentication feature"
- ✓ "Fix login button not working on mobile"
- ✓ "Update README with installation instructions"

**Bad Commit Messages:**
- ✗ "Fixed stuff" (too vague)
- ✗ "asdfasdf" (meaningless)
- ✗ "Changes" (what changes?)

**Message Format:** `[Action verb] + [What you did]`
- Add, Fix, Update, Remove, Refactor

---

## 4.5 git log - View History

```bash
# Full log
git log

# One line per commit (most useful!)
git log --oneline

# Show visual graph of branches
git log --oneline --graph --all

# Show last N commits
git log -3
git log --oneline -5

# Show commits on specific branch
git log branch-name
```

Press `q` to exit the log view.

---

## 4.6 git diff - See Changes

```bash
# See unstaged changes
git diff

# See staged changes
git diff --staged
git diff --cached

# See changes between commits
git diff commit1 commit2

# See changes in specific file
git diff filename.py
```

---

# PART 5: DAILY GIT WORKFLOW

---

## 5.1 The Basic Cycle

```
Edit files → git status → git add → git commit → Repeat
```

**Step by Step:**
1. **Make changes** to your files
2. `git status` - See what changed
3. `git add .` - Stage changes
4. `git commit -m "message"` - Save snapshot
5. **Repeat!**

---

## 5.2 Complete New Project Workflow

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Initialize Git
git init

# 3. Create your files (main.py, etc.)
# 4. Check status
git status

# 5. Stage files
git add .

# 6. First commit
git commit -m "Initial commit"

# 7. Create repo on GitHub (web)

# 8. Connect to GitHub
git remote add origin <url>

# 9. Push to GitHub
git push -u origin main
```

---

## 5.3 Daily Work Workflow

```bash
# 1. Go to project
cd my_project

# 2. Get latest changes (if working with team)
git pull

# 3. Make your changes (edit code)

# 4. Check what changed
git status

# 5. Stage changes
git add .

# 6. Commit
git commit -m "Describe what you did"

# 7. Push to GitHub
git push
```

---

# PART 6: BRANCHES

---

## 6.1 Viewing Branches

```bash
# List local branches
git branch

# List all branches (local + remote)
git branch -a

# List with last commit info
git branch -v
```

The `*` indicates your current branch.

---

## 6.2 Creating Branches

```bash
# Create branch (stay on current)
git branch branch-name

# Create AND switch to new branch
git checkout -b branch-name
git switch -c branch-name    # newer syntax
```

---

## 6.3 Switching Branches

```bash
# Switch to existing branch
git checkout branch-name
git switch branch-name       # newer syntax
```

---

## 6.4 Merging Branches

```bash
# First, go to the branch you want to merge INTO
git checkout main

# Then merge the feature branch
git merge feature-branch
```

---

## 6.5 Deleting Branches

```bash
# Delete merged branch (safe)
git branch -d branch-name

# Force delete branch (even if not merged)
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

---

## 6.6 Renaming Branches

```bash
# Rename current branch
git branch -m new-name

# Rename specific branch
git branch -m old-name new-name

# Rename master to main
git branch -M main
```

---

# PART 7: GITHUB & REMOTE OPERATIONS

---

## 7.1 Connecting to GitHub

```bash
# Add remote (after creating repo on GitHub)
git remote add origin <url>

# View remotes
git remote -v

# Remove remote
git remote remove origin

# Change remote URL
git remote set-url origin <new-url>
```

---

## 7.2 Push (Upload to GitHub)

```bash
# First push (sets upstream)
git push -u origin main

# After first push
git push

# Push specific branch
git push origin branch-name

# Push new branch to GitHub
git push -u origin new-branch
```

---

## 7.3 Pull (Download from GitHub)

```bash
# Get latest changes and merge
git pull

# Fetch without merging (safer)
git fetch

# Pull with rebase (cleaner history)
git pull --rebase
```

---

## 7.4 Clone (Download Repository)

```bash
# Clone repo
git clone <url>

# Clone into specific folder
git clone <url> folder-name
```

---

# PART 8: UNDOING CHANGES

---

## 8.1 Quick Decision Guide

| What You Want | Command |
|---------------|---------|
| See old version | `git checkout <commit>` |
| Undo local commits (not pushed) | `git reset` |
| Undo pushed commits | `git revert` |
| Discard uncommitted file changes | `git restore <file>` |
| Save changes temporarily | `git stash` |

---

## 8.2 git checkout - View Old Versions

```bash
# View old commit (DETACHED HEAD)
git checkout <commit-id>

# Go back to main branch
git checkout main

# Switch to branch
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch
```

---

## 8.3 git reset - Undo Commits (LOCAL ONLY!)

**Three modes:**

| Mode | Command | What Happens |
|------|---------|--------------|
| **--soft** | `git reset --soft HEAD~1` | Undo commit, keep changes STAGED |
| **--mixed** (default) | `git reset HEAD~1` | Undo commit, keep changes UNSTAGED |
| **--hard** | `git reset --hard HEAD~1` | Undo commit, DELETE changes ⚠️ |

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1

# Undo last commit, DELETE all changes (DANGEROUS!)
git reset --hard HEAD~1

# Unstage a file
git reset HEAD filename.txt

# Go back to specific commit
git reset --hard abc1234
```

**WARNING:** `--hard` PERMANENTLY DELETES changes! Don't use on pushed commits!

---

## 8.4 git revert - Safe Undo (For Pushed Commits)

Creates a NEW commit that undoes an old commit (preserves history).

```bash
# Revert specific commit
git revert <commit-id>

# Revert last commit
git revert HEAD

# Revert without editing message
git revert <commit> --no-edit
```

**GOLDEN RULE:**
- PUSHED to GitHub? → Use **REVERT**
- Only LOCAL? → Can use **RESET**

---

## 8.5 git restore - Discard Changes

```bash
# Discard changes in working directory
git restore filename.txt

# Unstage a file
git restore --staged filename.txt
```

---

## 8.6 git stash - Save for Later

```bash
# Save changes temporarily
git stash

# Save with a message
git stash save "Work in progress on feature X"

# List all stashes
git stash list

# Restore last stash (and remove from stash)
git stash pop

# Restore specific stash (keep in stash)
git stash apply stash@{0}

# Delete a stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

---

## 8.7 git reflog - Recovery Tool

Shows history of all HEAD movements (helpful to recover "lost" commits).

```bash
# View reflog
git reflog

# Recover to a point in reflog
git reset --hard HEAD@{2}
```

---

# PART 9: .gitignore - IGNORING FILES

---

## 9.1 What is .gitignore?

A `.gitignore` file tells Git which files/folders to **ignore** (not track).

**Common files to ignore:**
- Secret files (.env, credentials)
- Generated files (__pycache__, node_modules)
- Personal settings (.vscode/, .idea/)
- Large files (logs, uploads)

---

## 9.2 Basic Syntax

```gitignore
# Comments start with #

# Ignore specific file
secret.txt

# Ignore folder (note trailing /)
node_modules/
__pycache__/

# Ignore by extension
*.log
*.tmp

# Ignore all files in folder
temp/*
```

---

## 9.3 Pattern Reference

| Pattern | What it Ignores |
|---------|-----------------|
| `test.py` | All `test.py` files anywhere |
| `/test.py` | Only `test.py` in root folder |
| `src/test.py` | Only `test.py` in src/ folder |
| `**/test.py` | All `test.py` everywhere (explicit) |
| `*.log` | All .log files |
| `dir/` | Entire directory |
| `dir/*` | Contents of directory |
| `!file.txt` | Exception: DO NOT ignore this |

---

## 9.4 Sample Python .gitignore

```gitignore
# Virtual environment
venv/
.venv/

# Compiled files
__pycache__/
*.py[cod]

# Environment variables
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
```

---

## 9.5 Untracking Already Pushed Files

If a file was pushed before adding to .gitignore:

```bash
# Remove single file from tracking (keep locally)
git rm --cached filename.txt

# Remove folder from tracking
git rm --cached -r foldername/

# Commit the change
git commit -m "Stop tracking filename.txt"

# Push
git push
```

---

## 9.6 Debugging .gitignore

```bash
# Check why a file is ignored
git check-ignore -v filename.txt

# See all ignored files
git status --ignored

# Force add an ignored file
git add -f ignored_file.txt
```

---

# PART 10: ADVANCED COMMANDS

---

## 10.1 git blame - Who Changed What

```bash
# See who changed each line
git blame filename.py

# Blame specific lines
git blame -L 10,20 filename.py
```

---

## 10.2 git show - View Commit Details

```bash
# Show last commit details
git show

# Show specific commit
git show abc1234

# Show file at specific commit
git show abc1234:filename.py
```

---

## 10.3 git cherry-pick - Copy Specific Commits

```bash
# Apply a specific commit to current branch
git cherry-pick <commit-id>
```

---

## 10.4 git tag - Mark Important Versions

```bash
# Create lightweight tag
git tag v1.0.0

# Create annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# List tags
git tag

# Push tags to remote
git push --tags

# Delete tag
git tag -d v1.0.0
```

---

## 10.5 git commit --amend - Fix Last Commit

```bash
# Change last commit message
git commit --amend -m "New message"

# Add more files to last commit
git add forgotten_file.py
git commit --amend --no-edit
```

**Note:** Only use if you haven't pushed yet!

---

# PART 11: DECISION TREE - WHICH COMMAND?

---

```
┌─────────────────────────────────────────────────────────────────┐
│              WHICH GIT COMMAND SHOULD I USE?                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  "I want to see old code"                                        │
│  └─▶ git checkout <commit>                                      │
│                                                                  │
│  "I want to undo my last commit (not pushed)"                   │
│  └─▶ git reset --soft HEAD~1    (keep changes staged)          │
│  └─▶ git reset HEAD~1           (keep changes unstaged)        │
│  └─▶ git reset --hard HEAD~1    (delete changes ⚠️)            │
│                                                                  │
│  "I want to undo a pushed commit"                               │
│  └─▶ git revert <commit>                                        │
│                                                                  │
│  "I want to switch branches"                                     │
│  └─▶ git checkout <branch>   OR   git switch <branch>          │
│                                                                  │
│  "I want to create a new branch"                                │
│  └─▶ git checkout -b <name>  OR   git switch -c <name>         │
│                                                                  │
│  "I want to discard uncommitted changes"                        │
│  └─▶ git restore <file>                                         │
│                                                                  │
│  "I want to save changes temporarily"                           │
│  └─▶ git stash                                                   │
│                                                                  │
│  "I want to combine branches"                                    │
│  └─▶ git merge <branch>                                         │
│                                                                  │
│  "I want to see who changed a line"                             │
│  └─▶ git blame <file>                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 12: COMMON ERRORS & FIXES

---

| Error | Solution |
|-------|----------|
| "git is not recognized" | Install Git, restart terminal |
| "not a git repository" | Run `git init` or cd to correct folder |
| "Updates were rejected" | Run `git pull` first, then `git push` |
| "Please commit your changes before merging" | `git add . && git commit -m "message"` |
| "HEAD detached" | `git checkout main` to go back to branch |
| Merge conflicts | Open file, fix conflicts, `git add`, `git commit` |
| PowerShell script execution disabled | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

# PART 13: QUICK REFERENCE CHEAT SHEET

---

```
┌─────────────────────────────────────────────────────────────────┐
│              GIT COMMANDS QUICK REFERENCE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SETUP                                                           │
│  git init                        Initialize new repo             │
│  git clone <url>                 Clone repository                │
│  git config --global user.name   Set username                    │
│  git config --global user.email  Set email                       │
│                                                                  │
│  BASIC WORKFLOW                                                  │
│  git status                      Check state                     │
│  git add .                       Stage all changes               │
│  git add -A                      Stage all (including deletes)   │
│  git commit -m "message"         Commit changes                  │
│  git push                        Push to remote                  │
│  git pull                        Pull from remote                │
│                                                                  │
│  BRANCHES                                                        │
│  git branch                      List branches                   │
│  git branch name                 Create branch                   │
│  git checkout -b name            Create and switch               │
│  git checkout name               Switch branch                   │
│  git merge branch                Merge branch                    │
│  git branch -d name              Delete branch                   │
│  git branch -M new-name          Rename branch                   │
│                                                                  │
│  HISTORY                                                         │
│  git log --oneline               View history                    │
│  git log --oneline --graph --all Visual branch graph             │
│  git diff                        See changes                     │
│  git blame file                  See who changed what            │
│  git show commit                 Show commit details             │
│  git reflog                      Recovery history                │
│                                                                  │
│  UNDO                                                            │
│  git reset --soft HEAD~1         Undo, keep staged               │
│  git reset HEAD~1                Undo, keep unstaged             │
│  git reset --hard HEAD~1         Undo, DELETE changes ⚠️         │
│  git revert <commit>             Safe undo (new commit)          │
│  git restore <file>              Discard file changes            │
│  git stash                       Save temporarily                │
│  git stash pop                   Restore stash                   │
│                                                                  │
│  REMOTE                                                          │
│  git remote add origin <url>     Add remote                      │
│  git remote -v                   View remotes                    │
│  git push -u origin main         First push                      │
│  git pull --rebase               Pull with rebase                │
│  git fetch                       Fetch only                      │
│                                                                  │
│  ADVANCED                                                        │
│  git cherry-pick <commit>        Copy specific commit            │
│  git tag v1.0.0                  Create tag                      │
│  git commit --amend              Fix last commit                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# SUMMARY

```
┌─────────────────────────────────────────────────────────────────┐
│                    KEY TAKEAWAYS                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Git is a version control system (tracks code changes)       │
│  2. GitHub is a website to store Git projects online            │
│  3. Repository (repo) = folder tracked by Git                   │
│  4. Commit = snapshot/save point of your project                │
│  5. Branch = parallel line of development                       │
│                                                                  │
│  ESSENTIAL WORKFLOW:                                             │
│  git status → git add . → git commit -m "msg" → git push       │
│                                                                  │
│  GOLDEN RULES:                                                   │
│  • Commit often with meaningful messages                        │
│  • Pull before you push (when working with team)                │
│  • Use branches for new features                                │
│  • PUSHED to GitHub? → Use REVERT                               │
│  • Only LOCAL? → Can use RESET                                  │
│  • Never use --hard on pushed commits                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Previous:** [02_VSCode_Complete_Guide.md](./02_VSCode_Complete_Guide.md)
**Next:** [04_Virtual_Environment_Guide.md](./04_Virtual_Environment_Guide.md)
