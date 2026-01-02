# VS Code - Complete Guide

## Master Visual Studio Code Like a Pro

---

# PART 1: WHAT IS VS CODE?

---

## 1.1 Simple Explanation

**VS Code (Visual Studio Code)** is like Microsoft Word, but for writing code!

```
┌─────────────────────────────────────────────────────────────────┐
│                    VS CODE EXPLAINED                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Microsoft Word              VS Code                            │
│   ──────────────              ───────                            │
│                                                                  │
│   • Write documents           • Write code                       │
│   • Format text               • Syntax highlighting              │
│   • Spell check               • Error detection                  │
│   • Save .docx files          • Save .py, .js, .html files      │
│   • Print documents           • Run code                         │
│                                                                  │
│   VS Code is FREE, made by Microsoft, and used by               │
│   millions of programmers worldwide!                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 VS Code Interface Overview

```
┌────────────────────────────────────────────────────────────────────────────┐
│  VS CODE WINDOW LAYOUT                                                      │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  File  Edit  Selection  View  Go  Run  Terminal  Help               │   │
│  │  ↑                                                                   │   │
│  │  MENU BAR - Access all features                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌────┬───────────────────────────────────────────────────────────────┐   │
│  │    │                                                                │   │
│  │ A  │  ┌────────────────────────────────────────────────────────┐   │   │
│  │ C  │  │  main.py  ×  │  utils.py  │                            │   │   │
│  │ T  │  ├────────────────────────────────────────────────────────┤   │   │
│  │ I  │  │                                                        │   │   │
│  │ V  │  │  1 │ # My Python Code                                  │   │   │
│  │ I  │  │  2 │ print("Hello World")                              │   │   │
│  │ T  │  │  3 │                                                   │   │   │
│  │ Y  │  │  4 │ def greet(name):                                  │   │   │
│  │    │  │  5 │     return f"Hello, {name}!"                      │   │   │
│  │ B  │  │                                                        │   │   │
│  │ A  │  │  EDITOR AREA - Write your code here                    │   │   │
│  │ R  │  │                                                        │   │   │
│  │    │  └────────────────────────────────────────────────────────┘   │   │
│  │    │                                                                │   │
│  │    │  ┌────────────────────────────────────────────────────────┐   │   │
│  │    │  │ TERMINAL │ PROBLEMS │ OUTPUT │ DEBUG CONSOLE          │   │   │
│  │    │  ├────────────────────────────────────────────────────────┤   │   │
│  │    │  │ PS C:\Users\...\test>                                  │   │   │
│  │    │  │ _                                                      │   │   │
│  │    │  │                                                        │   │   │
│  │    │  │ PANEL AREA - Terminal, errors, output                  │   │   │
│  │    │  └────────────────────────────────────────────────────────┘   │   │
│  └────┴───────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Ln 2, Col 25    UTF-8    CRLF    Python    ○                       │   │
│  │  ↑                                                                   │   │
│  │  STATUS BAR - Current file info, line number, language              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

# PART 2: THE ACTIVITY BAR (Left Side Icons)

---

## 2.1 Activity Bar Icons Explained

```
┌─────────────────────────────────────────────────────────────────┐
│                    ACTIVITY BAR ICONS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌────┐                                                         │
│   │ 📄 │  EXPLORER (Ctrl + Shift + E)                           │
│   │    │  • See all files in your project                       │
│   │    │  • Create, rename, delete files                        │
│   │    │  • Navigate folder structure                           │
│   ├────┤                                                         │
│   │ 🔍 │  SEARCH (Ctrl + Shift + F)                             │
│   │    │  • Find text in ALL files                              │
│   │    │  • Find and replace across project                     │
│   ├────┤                                                         │
│   │ 🌿 │  SOURCE CONTROL (Ctrl + Shift + G)                     │
│   │    │  • Git integration                                      │
│   │    │  • See changed files                                    │
│   │    │  • Commit, push, pull                                   │
│   ├────┤                                                         │
│   │ 🐛 │  RUN AND DEBUG (Ctrl + Shift + D)                      │
│   │    │  • Run your code                                        │
│   │    │  • Debug (find errors)                                  │
│   │    │  • Set breakpoints                                      │
│   ├────┤                                                         │
│   │ 🧩 │  EXTENSIONS (Ctrl + Shift + X)                         │
│   │    │  • Add extra features                                   │
│   │    │  • Install themes                                       │
│   │    │  • Language support                                     │
│   └────┘                                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 3: ESSENTIAL KEYBOARD SHORTCUTS

---

## 3.1 Most Important Shortcuts (MUST KNOW!)

| Shortcut | What It Does |
|----------|--------------|
| `Ctrl + S` | **SAVE** file (Use this OFTEN!) |
| `Ctrl + Z` | **UNDO** (Made a mistake? Undo it!) |
| `Ctrl + Y` or `Ctrl + Shift + Z` | **REDO** (Undo your undo) |
| `Ctrl + C` | **COPY** selected text |
| `Ctrl + X` | **CUT** selected text |
| `Ctrl + V` | **PASTE** |
| `Ctrl + A` | **SELECT ALL** |
| `Ctrl + F` | **FIND** in current file |
| `Ctrl + H` | **FIND AND REPLACE** |
| `Ctrl + /` | **COMMENT/UNCOMMENT** line |

---

## 3.2 Panel and Sidebar Shortcuts

| Shortcut | What It Does |
|----------|--------------|
| `Ctrl + B` | Toggle SIDEBAR (show/hide left panel) |
| `Ctrl + `` | Toggle TERMINAL (show/hide bottom) |
| `Ctrl + J` | Toggle PANEL (terminal, problems) |
| `Ctrl + Shift + E` | Open EXPLORER (file list) |
| `Ctrl + Shift + F` | Open SEARCH |
| `Ctrl + Shift + G` | Open SOURCE CONTROL (Git) |
| `Ctrl + Shift + X` | Open EXTENSIONS |

---

## 3.3 File Navigation Shortcuts

| Shortcut | What It Does |
|----------|--------------|
| `Ctrl + P` | **QUICK OPEN** - Find and open any file (Very useful!) |
| `Ctrl + Tab` | Switch between OPEN files |
| `Ctrl + W` | CLOSE current file |
| `Ctrl + Shift + T` | REOPEN closed file (Accidentally closed? Get it back!) |
| `Ctrl + N` | Create NEW file |
| `Ctrl + O` | OPEN file from computer |
| `Ctrl + K, Ctrl + O` | OPEN FOLDER |

---

## 3.4 Code Editing Shortcuts

| Shortcut | What It Does |
|----------|--------------|
| `Ctrl + D` | SELECT next occurrence of word |
| `Ctrl + L` | SELECT entire line |
| `Alt + Up/Down` | MOVE line up or down |
| `Shift + Alt + Up/Down` | COPY line up or down (Duplicate!) |
| `Ctrl + Shift + K` | DELETE entire line |
| `Ctrl + Enter` | INSERT line below |
| `Ctrl + Shift + Enter` | INSERT line above |
| `Home` | Go to BEGINNING of line |
| `End` | Go to END of line |
| `Ctrl + Home` | Go to BEGINNING of file |
| `Ctrl + End` | Go to END of file |
| `Ctrl + K Ctrl + C` | Comment selected lines |
| `Ctrl + K Ctrl + U` | Uncomment selected lines |
| `F2` | Rename symbol (variable/function name) |

---

## 3.5 Multiple Cursors (Magic Feature!)

```
┌─────────────────────────────────────────────────────────────────┐
│              MULTIPLE CURSORS - EDIT MANY PLACES AT ONCE        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What are multiple cursors?                                      │
│  ─────────────────────────                                       │
│  Instead of one cursor, you can have MANY cursors!              │
│  When you type, it types in ALL cursor positions at once!       │
│                                                                  │
│  METHOD 1: Alt + Click                                           │
│  ─────────────────────                                           │
│  Hold Alt and click where you want extra cursors                │
│                                                                  │
│  METHOD 2: Ctrl + Alt + Up/Down                                  │
│  ───────────────────────────────                                 │
│  Add cursor above or below current line                         │
│                                                                  │
│  METHOD 3: Ctrl + D (Select Next Match)                          │
│  ───────────────────────────────────────                         │
│  1. Select a word                                                │
│  2. Press Ctrl + D repeatedly                                    │
│  3. Each press selects the next occurrence                      │
│  4. Type to replace ALL selected at once!                       │
│                                                                  │
│  TO EXIT multiple cursors: Press Esc                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 4: COMMAND PALETTE (The Magic Box!)

---

## 4.1 What is Command Palette?

The **Command Palette** is like a search box for EVERYTHING VS Code can do!

**Open with:** `Ctrl + Shift + P`

| Search This | To Do This |
|-------------|------------|
| "Preferences: Color Theme" | Change VS Code colors |
| "Format Document" | Auto-format/beautify code |
| "Toggle Word Wrap" | Wrap long lines |
| "Zoom In/Out" | Make text bigger/smaller |
| "Keyboard Shortcuts" | See/change all shortcuts |
| "Python: Select Interpreter" | Choose Python version |
| "Git: Clone" | Clone a repository |
| "Settings" | Open settings |

**PRO TIP:** You don't need to remember every shortcut. Just open Command Palette and search!

---

# PART 5: SETTINGS

---

## 5.1 How to Open Settings

| Method | How |
|--------|-----|
| Keyboard | `Ctrl + ,` |
| Menu | File → Preferences → Settings |
| Command Palette | `Ctrl + Shift + P` → type "Settings" → Enter |

---

## 5.2 Recommended Settings for Beginners

| Setting | Recommended Value | Why |
|---------|-------------------|-----|
| Editor: Font Size | 14-16 | Easy to read |
| Editor: Tab Size | 4 | Standard indentation |
| Editor: Word Wrap | on | No scroll for long lines |
| Files: Auto Save | afterDelay | Auto saves your work! |
| Editor: Format On Save | true | Auto format when save |
| Terminal: Default Profile | PowerShell | Best for Windows |
| Python: Activate Env in Terminal | true | Auto activate venv |

---

## 5.3 How to Find Any Shortcut

1. **Open Keyboard Shortcuts**: Press `Ctrl + K`, then `Ctrl + S`
2. **Search** for the command you want
3. **Change a shortcut**: Click the pencil icon, press new shortcut, Enter

---

# PART 6: EXTENSIONS

---

## 6.1 What are Extensions?

Extensions are like **apps for VS Code**. They add extra features!

```
Your Phone                VS Code
──────────                ───────
App Store          →      Extension Marketplace
Download apps      →      Download extensions
Add features       →      Add features
```

---

## 6.2 How to Install Extensions

1. **Open Extensions**: `Ctrl + Shift + X`
2. **Search** for extension name
3. **Click Install**
4. **Reload** if needed

---

## 6.3 Must-Have Extensions

**FOR PYTHON DEVELOPERS:**
| Extension | Purpose |
|-----------|---------|
| Python (Microsoft) | MUST HAVE - syntax, debugging, autocomplete |
| Pylance | Better Python language support |
| Python Indent | Fixes indentation issues |

**FOR EVERYONE:**
| Extension | Purpose |
|-----------|---------|
| GitLens | Enhanced Git features |
| Prettier | Auto-format code beautifully |
| Auto Rename Tag | When you rename HTML tag, other updates too |
| Material Icon Theme | Beautiful file icons |
| Live Server | For web dev - auto-refresh browser |
| Code Spell Checker | Catches spelling mistakes |

---

# PART 7: WORKING WITH FILES

---

## 7.1 Creating New Files

| Method | How |
|--------|-----|
| Keyboard | `Ctrl + N` (creates untitled file) |
| Explorer Panel | Right-click → New File |
| Explorer Icon | Click the 📄 icon next to folder name |
| Terminal (PS) | `ni filename.py` or `New-Item filename.py` |
| Terminal (Bash) | `touch filename.py` |

---

## 7.2 File Extensions and Languages

| Extension | Language | Example |
|-----------|----------|---------|
| .py | Python | main.py, app.py |
| .js | JavaScript | script.js, index.js |
| .html | HTML | index.html, page.html |
| .css | CSS | style.css, main.css |
| .json | JSON | package.json, data.json |
| .md | Markdown | README.md, notes.md |
| .txt | Plain Text | notes.txt |
| .yml/.yaml | YAML | config.yml |

VS Code automatically highlights syntax based on extension!

---

# PART 8: PRACTICAL SCENARIOS

---

## Scenario 1: "I accidentally closed a file!"
**Solution:** `Ctrl + Shift + T` - Reopens last closed file

## Scenario 2: "My code looks messy!"
**Solution:** `Shift + Alt + F` - Format Document

## Scenario 3: "I need to rename a variable everywhere"
**Solution 1:** `Ctrl + H` (Find and Replace) → Replace All
**Solution 2:** Select word → `Ctrl + D` repeatedly → type new name

## Scenario 4: "The text is too small!"
**Solution:** `Ctrl + =` (Zoom In), `Ctrl + -` (Zoom Out), `Ctrl + 0` (Reset)

## Scenario 5: "I want to compare two files"
**Solution:** Open first file → `Ctrl + \` (Split) → Open second file in new pane

---

# PART 9: COMPLETE SHORTCUTS CHEAT SHEET

---

```
┌─────────────────────────────────────────────────────────────────┐
│              VS CODE SHORTCUTS - COMPLETE CHEAT SHEET            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GENERAL                                                         │
│  Ctrl + Shift + P       Command Palette                         │
│  Ctrl + P               Quick Open File                         │
│  Ctrl + ,               Open Settings                           │
│  Ctrl + `               Toggle Terminal                         │
│  Ctrl + B               Toggle Sidebar                          │
│                                                                  │
│  FILE OPERATIONS                                                 │
│  Ctrl + N               New File                                │
│  Ctrl + O               Open File                               │
│  Ctrl + S               Save                                    │
│  Ctrl + Shift + S       Save As                                 │
│  Ctrl + W               Close File                              │
│  Ctrl + Shift + T       Reopen Closed File                      │
│  Ctrl + Tab             Switch Between Open Files               │
│                                                                  │
│  EDITING                                                         │
│  Ctrl + X               Cut Line                                │
│  Ctrl + C               Copy Line                               │
│  Ctrl + V               Paste                                   │
│  Ctrl + Z               Undo                                    │
│  Ctrl + Y               Redo                                    │
│  Ctrl + /               Comment Line                            │
│  Ctrl + D               Select Next Occurrence                  │
│  Ctrl + L               Select Line                             │
│  Ctrl + Shift + K       Delete Line                             │
│  Alt + Up/Down          Move Line                               │
│  Shift + Alt + Up/Down  Copy Line                               │
│  Ctrl + Enter           Insert Line Below                       │
│  Ctrl + Shift + Enter   Insert Line Above                       │
│  Ctrl + K Ctrl + C      Comment Selection                       │
│  Ctrl + K Ctrl + U      Uncomment Selection                     │
│  F2                     Rename Symbol                           │
│                                                                  │
│  SEARCH                                                          │
│  Ctrl + F               Find                                    │
│  Ctrl + H               Find and Replace                        │
│  Ctrl + Shift + F       Find in All Files                       │
│  F3                     Find Next                               │
│  Shift + F3             Find Previous                           │
│                                                                  │
│  MULTI-CURSOR                                                    │
│  Alt + Click            Add Cursor                              │
│  Ctrl + Alt + Up/Down   Add Cursor Above/Below                  │
│  Ctrl + D               Add Selection to Next Match             │
│  Esc                    Exit Multi-Cursor                       │
│                                                                  │
│  NAVIGATION                                                      │
│  Ctrl + G               Go to Line                              │
│  Ctrl + Home            Go to Beginning of File                 │
│  Ctrl + End             Go to End of File                       │
│                                                                  │
│  VIEW                                                            │
│  Ctrl + =               Zoom In                                 │
│  Ctrl + -               Zoom Out                                │
│  Ctrl + 0               Reset Zoom                              │
│  Ctrl + \               Split Editor                            │
│  Shift + Alt + F        Format Document                         │
│                                                                  │
│  TERMINAL                                                        │
│  Ctrl + `               Toggle Terminal                         │
│  Ctrl + Shift + `       New Terminal                            │
│                                                                  │
│  ACTIVITY BAR                                                    │
│  Ctrl + Shift + E       Explorer                                │
│  Ctrl + Shift + F       Search                                  │
│  Ctrl + Shift + G       Source Control (Git)                    │
│  Ctrl + Shift + D       Debug                                   │
│  Ctrl + Shift + X       Extensions                              │
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
│  1. VS Code is your code editor - learn it well!                │
│                                                                  │
│  2. Most important shortcuts to memorize:                        │
│     • Ctrl + S (Save)                                            │
│     • Ctrl + ` (Terminal)                                        │
│     • Ctrl + Shift + P (Command Palette)                        │
│     • Ctrl + P (Quick Open)                                      │
│     • Ctrl + B (Toggle Sidebar)                                  │
│     • Ctrl + / (Comment)                                         │
│     • Ctrl + D (Select Next)                                     │
│                                                                  │
│  3. Command Palette (Ctrl + Shift + P) can do EVERYTHING        │
│     If you forget a shortcut, search there!                     │
│                                                                  │
│  4. Install essential extensions:                                │
│     • Python (for Python coding)                                 │
│     • GitLens (for Git)                                          │
│     • Prettier (for formatting)                                  │
│                                                                  │
│  5. Use Tab completion and multiple cursors to save time        │
│                                                                  │
│  6. Settings (Ctrl + ,) lets you customize everything           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Previous:** [01_Terminal_CMD_PowerShell_Complete_Guide.md](./01_Terminal_CMD_PowerShell_Complete_Guide.md)
**Next:** [03_Git_Complete_Guide.md](./03_Git_Complete_Guide.md)
