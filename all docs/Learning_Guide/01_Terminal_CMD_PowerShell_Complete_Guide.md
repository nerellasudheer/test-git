# Terminal, CMD & PowerShell - Complete Guide

## Understanding and Mastering the Command Line

---

# PART 1: UNDERSTANDING TERMINALS

---

## 1.1 What is a Terminal?

A **Terminal** is a text-based way to control your computer. Instead of clicking icons, you type commands.

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                                 │
│                                                                  │
│   ┌─────────────────────┐       ┌─────────────────────┐         │
│   │   GUI (Visual)      │       │   TERMINAL (Text)   │         │
│   │                     │       │                     │         │
│   │   Click folders     │       │   Type: cd Desktop  │         │
│   │   Double-click      │       │   Type: mkdir test  │         │
│   │   files to open     │       │   Type: dir         │         │
│   │   Drag to move      │       │                     │         │
│   └─────────────────────┘       └─────────────────────┘         │
│                                                                  │
│        BOTH do the SAME thing, just DIFFERENT ways!             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 What is a Shell?

A **Shell** is the translator between you and the computer.

```
┌─────────────────────────────────────────────────────────────────┐
│                     HOW SHELL WORKS                              │
│                                                                  │
│   ┌──────────┐     ┌──────────────┐     ┌──────────────┐        │
│   │   YOU    │────▶│    SHELL     │────▶│   COMPUTER   │        │
│   │ "show    │     │ (Translator) │     │              │        │
│   │  files"  │     │              │     │  Executes    │        │
│   │          │◀────│  Translates  │◀────│  command     │        │
│   └──────────┘     └──────────────┘     └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.3 Windows Shells Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│                    WINDOWS SHELLS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. COMMAND PROMPT (CMD)                                        │
│      • The OLDEST Windows shell (since 1980s)                   │
│      • Basic but reliable                                        │
│      • Looks like: C:\Users\Name>                               │
│      • Uses commands like: dir, copy, del                       │
│                                                                  │
│   2. POWERSHELL                                                  │
│      • NEWER and more powerful (since 2006)                      │
│      • DEFAULT in VS Code on Windows                             │
│      • Looks like: PS C:\Users\Name>                            │
│      • Can use CMD commands + many more                         │
│      • Uses commands like: Get-ChildItem, ls, dir               │
│                                                                  │
│   3. GIT BASH                                                    │
│      • Linux-style commands on Windows                          │
│      • Comes when you install Git                               │
│      • Looks like: user@computer MINGW64 ~                      │
│      • Uses commands like: ls, cat, rm                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.4 How to Identify Your Shell

```
┌─────────────────────────────────────────────────────────────────┐
│                  HOW TO IDENTIFY YOUR SHELL                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  C:\Users\Sudheer>_                                             │
│  ↑ This is CMD (Command Prompt) - Just shows path and >        │
│                                                                  │
│  PS C:\Users\Sudheer>_                                          │
│  ↑ This is POWERSHELL - Starts with "PS"                        │
│                                                                  │
│  sudheer@LAPTOP MINGW64 ~                                        │
│  $                                                               │
│  ↑ This is GIT BASH - Shows username@computer with $            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.5 Which Shell Should You Use?

**Recommendation: USE POWERSHELL**

- It's the DEFAULT in VS Code
- It understands CMD commands (backward compatible)
- It understands some Linux commands (ls, cat)
- It's more powerful for future learning
- Microsoft's recommended shell

**When to use CMD:**
- Very old tutorials that specifically need CMD
- Running .bat (batch) files

**When to use Git Bash:**
- Following Linux/Mac tutorials
- If you plan to learn Linux later

---

# PART 2: TERMINAL IN VS CODE

---

## 2.1 Opening Terminal in VS Code

```
┌─────────────────────────────────────────────────────────────────┐
│              THREE WAYS TO OPEN TERMINAL                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  METHOD 1: KEYBOARD SHORTCUT (Fastest!)                         │
│     Press: Ctrl + `  (backtick key below Esc)                   │
│                                                                  │
│  METHOD 2: MENU                                                  │
│     Click: View → Terminal                                       │
│                                                                  │
│  METHOD 3: COMMAND PALETTE                                       │
│     1. Press: Ctrl + Shift + P                                  │
│     2. Type: "Terminal: Create New Terminal"                    │
│     3. Press: Enter                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2.2 Understanding the Terminal Prompt

```
PS C:\Users\Sudheer.Nerella\Desktop\test>
││ │      │                        │    │
││ │      │                        │    └── ">" means ready for command
││ │      │                        └── Current folder (you are HERE)
││ │      └── Your username folder
││ └── C: is your main hard drive
│└── Backslash separates folders (Windows style)
└── "PS" = PowerShell
```

---

## 2.3 Essential Terminal Shortcuts

| Shortcut | What It Does |
|----------|--------------|
| `Ctrl + `` | Open/Close terminal panel |
| `Ctrl + Shift + `` | Create NEW terminal |
| `Ctrl + C` | STOP/Cancel current command |
| `↑` (Up Arrow) | Previous command (history) |
| `↓` (Down Arrow) | Next command in history |
| `Tab` | Auto-complete file/folder names |
| `Ctrl + L` or `cls` | Clear the terminal screen |

---

## 2.4 Changing Your Shell in VS Code

1. Look at the terminal panel
2. Click the dropdown arrow (∨) next to the + sign
3. Select "Select Default Profile"
4. Choose your preferred shell (PowerShell, CMD, Git Bash)

---

# PART 3: FILE SYSTEM CONCEPTS

---

## 3.1 Understanding the Folder Tree

```
┌─────────────────────────────────────────────────────────────────┐
│                 FILE SYSTEM STRUCTURE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                         C:\                                      │
│                    (Root - Top Level)                            │
│                          │                                       │
│          ┌───────────────┼───────────────┐                      │
│          │               │               │                       │
│       Users          Program Files    Windows                    │
│          │                                                       │
│          └── Sudheer.Nerella (Your home folder)                 │
│                    │                                             │
│       ┌────────────┼────────────┬────────────┐                  │
│       │            │            │            │                   │
│    Desktop     Documents    Downloads    Pictures                │
│       │                                                          │
│       └── my_project                                             │
│              │                                                   │
│              └── Learning_Guide                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.2 Key Terminology

| Term | Meaning |
|------|---------|
| **Root** | The topmost folder (C:\ on Windows) |
| **Directory** | Same as FOLDER |
| **Parent Folder** | The folder that contains you |
| **Child/Subdirectory** | A folder inside another folder |
| **Current Directory** | The folder you are currently in |
| **Path** | The full address/location of a file |
| **Absolute Path** | Complete path from root (C:\Users\...) |
| **Relative Path** | Path relative to where you are (..\folder) |

---

## 3.3 Special Path Symbols

| Symbol | Meaning | Example |
|--------|---------|---------|
| `.` | Current folder | `.\file.txt` = file.txt here |
| `..` | Parent folder (go back one level) | `cd ..` |
| `\` | Folder separator (Windows) | `C:\Users\Desktop` |
| `/` | Folder separator (Linux/Git Bash) | `/home/user` |
| `~` | Home folder (Git Bash/PowerShell) | `cd ~` |
| `C:\` | Root of C: drive | `cd \` goes to root |

---

# PART 4: NAVIGATION COMMANDS

---

## 4.1 pwd / cd - Where Am I?

Shows your current location (full path).

**PowerShell / Git Bash:**
```powershell
pwd
```

**CMD:**
```cmd
cd
```

---

## 4.2 ls / dir - What's Here?

Lists all files and folders in current location.

```
┌─────────────────────────────────────────────────────────────────┐
│                    ls / dir COMMANDS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  ls                     List files and folders                  │
│  ls -Force              Include hidden files                    │
│  ls -Name               Show only names (simple)                │
│  ls -Recurse            List ALL files in ALL subfolders       │
│                                                                  │
│  CMD:                                                            │
│  dir                    List files and folders                  │
│  dir /a                 Include hidden files                    │
│  dir /b                 Show only names (simple)                │
│  dir /s                 List ALL files in ALL subfolders       │
│                                                                  │
│  GIT BASH:                                                       │
│  ls                     List files (simple)                     │
│  ls -l                  Long format (detailed)                  │
│  ls -a                  Show hidden files (starting with .)    │
│  ls -la                 Long format + hidden (most common)      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.3 cd - Change Directory

| Action | Command | Example |
|--------|---------|---------|
| Go INTO a folder | `cd foldername` | `cd Desktop` |
| Go BACK (parent) | `cd ..` | Goes up one level |
| Go up 2 levels | `cd ..\..` | Goes up two levels |
| Go to specific path | `cd C:\path\to\folder` | Full path |
| Go to drive root | `cd \` | Goes to C:\ |
| Go to home | `cd ~` | PowerShell/Git Bash |
| Change drive (CMD) | `D:` | Just type drive letter |
| Change drive (PS) | `cd D:\` | Use cd with path |

**Handling Spaces in Folder Names:**
```powershell
# WRONG
cd My Documents

# CORRECT - Use quotes
cd "My Documents"

# OR use Tab completion - it auto-adds quotes!
cd My[TAB]
```

---

## 4.4 clear / cls - Clear Screen

| Shell | Command |
|-------|---------|
| PowerShell | `cls` or `clear` |
| CMD | `cls` |
| Git Bash | `clear` |

---

# PART 5: FILE OPERATIONS

---

## 5.1 Creating Folders - mkdir

**Works in ALL shells:**
```powershell
# Create single folder
mkdir my_project

# Create folder with spaces (use quotes)
mkdir "My Project"

# Create nested folders (PowerShell)
mkdir -Path projects\python\flask_app

# Create multiple folders
mkdir folder1, folder2, folder3
```

---

## 5.2 Creating Files

```
┌─────────────────────────────────────────────────────────────────┐
│              CREATING FILES - BY SHELL                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  New-Item filename.txt          Create empty file               │
│  ni filename.txt                Short form                      │
│  ni file1.txt, file2.txt        Create multiple files           │
│  "Hello" | Out-File readme.txt  Create file with content        │
│                                                                  │
│  CMD:                                                            │
│  type nul > filename.txt        Create empty file               │
│  echo Hello World > readme.txt  Create file with content        │
│                                                                  │
│  GIT BASH:                                                       │
│  touch filename.txt             Create empty file               │
│  touch file1.txt file2.txt      Create multiple files           │
│  echo "Hello" > readme.txt      Create file with content        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.3 Deleting Files

**WARNING: Terminal deletions usually DON'T go to Recycle Bin! They're PERMANENT!**

```
┌─────────────────────────────────────────────────────────────────┐
│              DELETING FILES                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  rm filename.txt                Delete single file              │
│  del filename.txt               Also works                      │
│  rm file1.txt, file2.txt        Delete multiple files           │
│  rm *.txt                       Delete all .txt files           │
│  rm test*                       Delete files starting with test │
│                                                                  │
│  CMD:                                                            │
│  del filename.txt               Delete single file              │
│  del *.txt                      Delete all .txt files           │
│                                                                  │
│  GIT BASH:                                                       │
│  rm filename.txt                Delete single file              │
│  rm *.txt                       Delete all .txt files           │
│  rm -i filename.txt             Ask for confirmation            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.4 Deleting Folders

```
┌─────────────────────────────────────────────────────────────────┐
│              DELETING FOLDERS                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  rmdir foldername               Delete EMPTY folder             │
│  rm -r foldername               Delete folder WITH contents     │
│  rm -r -Force foldername        Force delete (no confirmation)  │
│                                                                  │
│  CMD:                                                            │
│  rmdir foldername               Delete EMPTY folder             │
│  rmdir /s /q foldername         Delete folder WITH contents     │
│    /s = Remove subdirectories and files                         │
│    /q = Quiet mode (no confirmation)                            │
│                                                                  │
│  GIT BASH:                                                       │
│  rmdir foldername               Delete EMPTY folder             │
│  rm -r foldername               Delete folder WITH contents     │
│  rm -rf foldername              Force delete (no prompts)       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.5 Copying Files and Folders

```
┌─────────────────────────────────────────────────────────────────┐
│              COPYING FILES AND FOLDERS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  cp source.txt dest.txt         Copy file (same folder)         │
│  cp file.txt C:\destination\    Copy to different folder        │
│  cp -r folder1 folder2          Copy folder with contents       │
│                                                                  │
│  CMD:                                                            │
│  copy source.txt dest.txt       Copy file                       │
│  xcopy /E /I src_folder dest    Copy folder with contents       │
│                                                                  │
│  GIT BASH:                                                       │
│  cp source.txt dest.txt         Copy file                       │
│  cp -r folder1 folder2          Copy folder with contents       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.6 Moving and Renaming

**Note: Moving and Renaming use the same command!**

```
┌─────────────────────────────────────────────────────────────────┐
│              MOVING AND RENAMING                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  mv file.txt newfolder\         Move file to folder             │
│  mv oldname.txt newname.txt     Rename file                     │
│  ren oldname.txt newname.txt    Also works for rename           │
│                                                                  │
│  CMD:                                                            │
│  move file.txt C:\destination\  Move file to folder             │
│  ren oldname.txt newname.txt    Rename file                     │
│                                                                  │
│  GIT BASH:                                                       │
│  mv file.txt newfolder/         Move file to folder             │
│  mv oldname.txt newname.txt     Rename file                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.7 Viewing File Contents

```
┌─────────────────────────────────────────────────────────────────┐
│              VIEWING FILE CONTENTS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  POWERSHELL:                                                     │
│  cat filename.txt               View entire file                │
│  type filename.txt              Also works                      │
│  Get-Content filename.txt       Full command                    │
│  cat -Head 10 filename.txt      First 10 lines                  │
│  cat -Tail 10 filename.txt      Last 10 lines                   │
│                                                                  │
│  CMD:                                                            │
│  type filename.txt              View entire file                │
│                                                                  │
│  GIT BASH:                                                       │
│  cat filename.txt               View entire file                │
│  head -10 filename.txt          First 10 lines                  │
│  tail -10 filename.txt          Last 10 lines                   │
│  less filename.txt              Scroll through (q to exit)     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 6: ADDITIONAL USEFUL COMMANDS

---

## 6.1 Finding Files and Programs

| Command | Shell | Purpose |
|---------|-------|---------|
| `where python` | CMD/PowerShell | Find program location |
| `Get-Command python` | PowerShell | Find command details |
| `which python` | Git Bash | Find program location |
| `tree` | CMD/PowerShell | Display folder structure |
| `tree /f` | CMD | Display with files included |
| `Test-Path file.txt` | PowerShell | Check if file/folder exists |

---

## 6.2 Command History and Help

| Command | Purpose |
|---------|---------|
| `↑` / `↓` Arrow Keys | Navigate command history |
| `history` | Show command history (PowerShell) |
| `Get-Help command` | Get help for a command (PowerShell) |
| `command --help` | Get help (Git Bash) |
| `command /?` | Get help (CMD) |

---

# PART 7: COMMAND COMPARISON TABLE

---

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    COMMAND COMPARISON TABLE                                 │
├────────────────────┬──────────────────┬────────────────┬───────────────────┤
│       TASK         │      CMD         │   POWERSHELL   │    GIT BASH       │
├────────────────────┼──────────────────┼────────────────┼───────────────────┤
│ List files         │ dir              │ dir OR ls      │ ls                │
│ List with details  │ dir              │ ls -la         │ ls -la            │
│ Show hidden files  │ dir /a           │ ls -Force      │ ls -a             │
│ Clear screen       │ cls              │ cls OR clear   │ clear             │
│ Where am I?        │ cd (alone)       │ pwd            │ pwd               │
│ Change directory   │ cd               │ cd             │ cd                │
│ Create folder      │ mkdir            │ mkdir          │ mkdir             │
│ Create file        │ type nul >       │ ni OR New-Item │ touch             │
│ Delete file        │ del              │ del OR rm      │ rm                │
│ Delete folder      │ rmdir /s         │ rm -r          │ rm -r             │
│ Copy file          │ copy             │ copy OR cp     │ cp                │
│ Copy folder        │ xcopy /E /I      │ cp -r          │ cp -r             │
│ Move file          │ move             │ move OR mv     │ mv                │
│ Rename             │ ren              │ ren OR mv      │ mv                │
│ View file content  │ type             │ cat OR type    │ cat               │
│ Find text in files │ findstr          │ Select-String  │ grep              │
│ Find program       │ where            │ where          │ which             │
│ Show tree          │ tree             │ tree           │ tree              │
├────────────────────┴──────────────────┴────────────────┴───────────────────┤
│ NOTICE: PowerShell understands BOTH CMD and some Linux commands!           │
└────────────────────────────────────────────────────────────────────────────┘
```

---

# PART 8: COMMON MISTAKES AND FIXES

---

## 8.1 Spaces in Names

```
WRONG:  cd My Documents
ERROR:  "My" is not recognized...

CORRECT: cd "My Documents"
     OR: cd My[TAB]  (Tab auto-completes with quotes)
```

**Best Practice:** When naming files/folders, avoid spaces! Use: `my_documents`, `my-documents`, `MyDocuments`

---

## 8.2 Wrong Slashes

| Shell | Slash Type | Example |
|-------|------------|---------|
| Windows (CMD/PS) | Backslash `\` | `C:\Users\Desktop` |
| Git Bash/Linux | Forward slash `/` | `/c/Users/Desktop` |

**Note:** PowerShell often accepts both!

---

## 8.3 Command Not Found

```
ERROR: 'xyz' is not recognized as an internal or external command

POSSIBLE CAUSES:
1. TYPO in command       → Check spelling
2. Program NOT INSTALLED → Install it
3. Wrong SHELL's command → Use correct command for your shell
4. Not in PATH           → Add program to PATH or reinstall
```

---

## 8.4 Trying to cd Into a File

```
WRONG: cd test.txt   (test.txt is a FILE, not a folder!)

You can only cd into FOLDERS, not files!
```

---

# SUMMARY - QUICK REFERENCE

---

```
┌─────────────────────────────────────────────────────────────────┐
│              FILE OPERATIONS QUICK REFERENCE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  NAVIGATE:                                                       │
│  pwd                          Where am I?                        │
│  ls                           What's here?                       │
│  cd foldername                Go into folder                     │
│  cd ..                        Go back (parent)                   │
│  cd ..\..                     Go back 2 levels                   │
│  cd C:\path\to\folder         Jump to specific location          │
│                                                                  │
│  CREATE:                                                         │
│  mkdir foldername             Create folder                      │
│  ni filename.txt              Create file (PowerShell)          │
│  touch filename.txt           Create file (Git Bash)            │
│                                                                  │
│  DELETE:                                                         │
│  rm filename.txt              Delete file                        │
│  rm *.log                     Delete all .log files             │
│  rm -r foldername             Delete folder with contents       │
│                                                                  │
│  COPY:                                                           │
│  cp source.txt dest.txt       Copy file                         │
│  cp -r folder1 folder2        Copy folder with contents         │
│                                                                  │
│  MOVE/RENAME:                                                    │
│  mv file.txt newfolder\       Move file to folder               │
│  mv oldname.txt newname.txt   Rename file                       │
│                                                                  │
│  VIEW:                                                           │
│  cat filename.txt             View file contents                │
│  cat -Head 10 file.txt        First 10 lines                    │
│  cat -Tail 10 file.txt        Last 10 lines                     │
│                                                                  │
│  TIPS:                                                           │
│  TAB                          Auto-complete names                │
│  ↑ Arrow                      Previous command                   │
│  cls / clear                  Clear screen                       │
│  Ctrl + C                     Stop/Cancel command                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Key Takeaways:**
1. Terminal = Text-based control of your computer
2. Shell = Translator (CMD, PowerShell, Git Bash)
3. PowerShell recommended for Windows beginners
4. Use Tab for auto-completion to save time and avoid typos
5. Use quotes for paths with spaces
6. Terminal deletions are PERMANENT (no Recycle Bin!)

---

**Next:** [02_VSCode_Complete_Guide.md](./02_VSCode_Complete_Guide.md)
