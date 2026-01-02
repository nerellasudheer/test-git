# VS Code Shortcuts - Complete Quick Reference

> Master Visual Studio Code from basic to advanced

---

## PART 1: WHAT IS VS CODE?

- **Visual Studio Code** - A free code editor by Microsoft
- Like Microsoft Word, but for writing code
- Features: Syntax highlighting, error detection, extensions
- Used by millions of developers worldwide
- **FREE** and constantly updated

---

## PART 2: INTERFACE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────┐
│  File  Edit  Selection  View  Go  Run  Terminal  Help          │ ← Menu Bar
├────┬────────────────────────────────────────────────────────────┤
│    │  main.py  ×  │  utils.py  │                   ← Tab Bar   │
│ A  ├────────────────────────────────────────────────────────────┤
│ C  │  1 │ # My Python Code                                      │
│ T  │  2 │ print("Hello World")            ← Editor Area         │
│ I  │  3 │                                                       │
│ V  │  4 │ def greet(name):                                      │
│ I  │  5 │     return f"Hello, {name}!"                          │
│ T  ├────────────────────────────────────────────────────────────┤
│ Y  │ TERMINAL │ PROBLEMS │ OUTPUT │        ← Panel Area         │
│    │ PS C:\Users\...\test>                                      │
│ B  │ _                                                          │
│ A  ├────────────────────────────────────────────────────────────┤
│ R  │  Ln 2, Col 25    UTF-8    Python         ← Status Bar      │
└────┴────────────────────────────────────────────────────────────┘
```

### Activity Bar Icons (Left Side)

| Icon | Name | Shortcut | Purpose |
|------|------|----------|---------|
| 📄 | Explorer | `Ctrl + Shift + E` | See all files in project |
| 🔍 | Search | `Ctrl + Shift + F` | Find text in ALL files |
| 🌿 | Source Control | `Ctrl + Shift + G` | Git integration |
| 🐛 | Run and Debug | `Ctrl + Shift + D` | Debug your code |
| 🧩 | Extensions | `Ctrl + Shift + X` | Add extra features |

---

## PART 3: ESSENTIAL SHORTCUTS (MUST KNOW!)

### File Operations

| Shortcut | Action |
|----------|--------|
| `Ctrl + S` | **SAVE** file (Use this OFTEN!) |
| `Ctrl + Shift + S` | Save As |
| `Ctrl + N` | New file |
| `Ctrl + O` | Open file |
| `Ctrl + W` | Close current file |
| `Ctrl + Shift + T` | **Reopen closed file** (Lifesaver!) |
| `Ctrl + Tab` | Switch between open files |
| `Ctrl + P` | **Quick Open** - Find and open any file by name |
| `Ctrl + K, Ctrl + O` | Open folder |

### Basic Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl + Z` | **UNDO** |
| `Ctrl + Y` | **REDO** (or `Ctrl + Shift + Z`) |
| `Ctrl + C` | Copy (or copy entire line if nothing selected) |
| `Ctrl + X` | Cut (or cut entire line if nothing selected) |
| `Ctrl + V` | Paste |
| `Ctrl + A` | Select all |

### Find and Replace

| Shortcut | Action |
|----------|--------|
| `Ctrl + F` | Find in current file |
| `Ctrl + H` | Find and Replace |
| `Ctrl + Shift + F` | **Find in ALL files** |
| `Ctrl + Shift + H` | Replace in ALL files |
| `F3` | Find next occurrence |
| `Shift + F3` | Find previous occurrence |

---

## PART 4: PANELS AND SIDEBAR

| Shortcut | Action |
|----------|--------|
| `Ctrl + B` | Toggle Sidebar (show/hide) |
| `Ctrl + `` ` | Toggle Terminal |
| `Ctrl + J` | Toggle bottom Panel |
| `Ctrl + Shift + E` | Open Explorer |
| `Ctrl + Shift + F` | Open Search |
| `Ctrl + Shift + G` | Open Source Control (Git) |
| `Ctrl + Shift + D` | Open Debug panel |
| `Ctrl + Shift + X` | Open Extensions |

---

## PART 5: CODE EDITING - ESSENTIAL

### Line Operations

| Shortcut | Action |
|----------|--------|
| `Ctrl + /` | **Comment/Uncomment line** |
| `Ctrl + L` | Select entire line |
| `Ctrl + Shift + K` | **Delete entire line** |
| `Alt + Up` | **Move line up** |
| `Alt + Down` | **Move line down** |
| `Shift + Alt + Up` | **Copy line up** (Duplicate!) |
| `Shift + Alt + Down` | **Copy line down** |
| `Ctrl + Enter` | Insert blank line below |
| `Ctrl + Shift + Enter` | Insert blank line above |

### Selection

| Shortcut | Action |
|----------|--------|
| `Ctrl + D` | **Select next occurrence** of word |
| `Ctrl + Shift + L` | **Select ALL occurrences** at once |
| `Shift + Alt + Right` | Expand selection |
| `Shift + Alt + Left` | Shrink selection |
| `Ctrl + L` | Select entire line |

### Block Comments

| Shortcut | Action |
|----------|--------|
| `Ctrl + /` | Toggle line comment |
| `Ctrl + K, Ctrl + C` | Add block comment |
| `Ctrl + K, Ctrl + U` | Remove block comment |

### Code Formatting

| Shortcut | Action |
|----------|--------|
| `Shift + Alt + F` | **Format entire document** |
| `Ctrl + K, Ctrl + F` | Format selected code |
| `F2` | **Rename symbol** (variable/function) |

---

## PART 6: MULTIPLE CURSORS (POWER FEATURE!)

Multiple cursors let you edit many places at once!

### Adding Cursors

| Shortcut | Action |
|----------|--------|
| `Alt + Click` | Add cursor at click position |
| `Ctrl + Alt + Up` | Add cursor above |
| `Ctrl + Alt + Down` | Add cursor below |
| `Ctrl + D` | Select next match and add cursor |
| `Ctrl + Shift + L` | Select ALL matches and add cursors |
| `Esc` | Exit multi-cursor mode |

### How to Use Multiple Cursors

1. **Method 1: Alt + Click**
   - Hold `Alt` and click where you want extra cursors
   - Type to edit all locations at once

2. **Method 2: Ctrl + D**
   - Select a word
   - Press `Ctrl + D` repeatedly to select next occurrences
   - Type to replace ALL selected at once

3. **Method 3: Ctrl + Alt + Up/Down**
   - Press to add cursor on line above/below
   - Great for editing multiple lines

---

## PART 7: NAVIGATION

### Within File

| Shortcut | Action |
|----------|--------|
| `Ctrl + G` | Go to specific line number |
| `Home` | Go to beginning of line |
| `End` | Go to end of line |
| `Ctrl + Home` | Go to beginning of file |
| `Ctrl + End` | Go to end of file |
| `Ctrl + Shift + O` | Go to symbol (function/class) |

### Between Files

| Shortcut | Action |
|----------|--------|
| `Ctrl + P` | Quick open any file |
| `Ctrl + Tab` | Cycle through open files |
| `Ctrl + Shift + Tab` | Cycle backwards |
| `F12` | Go to definition |
| `Alt + F12` | Peek definition |
| `Alt + Left` | Navigate back |
| `Alt + Right` | Navigate forward |

---

## PART 8: VIEW AND ZOOM

| Shortcut | Action |
|----------|--------|
| `Ctrl + =` | Zoom in (make text bigger) |
| `Ctrl + -` | Zoom out (make text smaller) |
| `Ctrl + 0` | Reset zoom to default |
| `Ctrl + \` | Split editor (side by side) |
| `Ctrl + 1/2/3` | Focus on editor group 1/2/3 |

---

## PART 9: TERMINAL

| Shortcut | Action |
|----------|--------|
| `Ctrl + `` ` | Open/close terminal |
| `Ctrl + Shift + `` ` | Create new terminal |
| `Ctrl + Shift + 5` | Split terminal |
| `Ctrl + C` | Stop running process |

---

## PART 10: COMMAND PALETTE

The **Command Palette** is like a search box for EVERYTHING VS Code can do!

**Open with:** `Ctrl + Shift + P`

### Useful Commands to Search

| Type This | To Do This |
|-----------|------------|
| `theme` | Change color theme |
| `format` | Format document |
| `terminal` | Terminal options |
| `zoom` | Zoom in/out/reset |
| `settings` | Open settings |
| `keyboard` | Keyboard shortcuts |
| `Python: Select Interpreter` | Choose Python version |
| `Git: Clone` | Clone a repository |
| `Toggle Word Wrap` | Wrap long lines |

**PRO TIP:** If you forget any shortcut, search for it in Command Palette!

---

## PART 11: SETTINGS

### Opening Settings

| Method | How |
|--------|-----|
| Keyboard | `Ctrl + ,` |
| Menu | File → Preferences → Settings |
| Command Palette | `Ctrl + Shift + P` → "Settings" |

### Finding Shortcuts

| Method | How |
|--------|-----|
| Keyboard | `Ctrl + K, Ctrl + S` |
| Command Palette | Search "Keyboard Shortcuts" |

### Recommended Settings for Beginners

| Setting | Value | Why |
|---------|-------|-----|
| Editor: Font Size | 14-16 | Easy to read |
| Editor: Tab Size | 4 | Standard indentation |
| Editor: Word Wrap | on | No horizontal scrolling |
| Files: Auto Save | afterDelay | Auto saves your work |
| Editor: Format On Save | true | Auto format when saving |
| Terminal: Default Profile | PowerShell | Best for Windows |

---

## PART 12: EXTENSIONS

### Managing Extensions

| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + X` | Open Extensions panel |

### Must-Have Extensions

**For Python:**
- **Python** (Microsoft) - MUST HAVE
- **Pylance** - Better Python language support
- **Python Indent** - Fixes indentation issues

**For Everyone:**
- **GitLens** - Enhanced Git features
- **Prettier** - Auto-format code beautifully
- **Material Icon Theme** - Beautiful file icons
- **Code Spell Checker** - Catches typos
- **Auto Rename Tag** - For HTML/XML editing
- **Live Server** - For web development

---

## PART 13: PRACTICAL SCENARIOS

### Scenario 1: Accidentally closed a file?
**Solution:** `Ctrl + Shift + T` - Reopens last closed file!

### Scenario 2: Code looks messy?
**Solution:** `Shift + Alt + F` - Format entire document

### Scenario 3: Need to rename a variable everywhere?
**Solutions:**
1. `F2` while on variable name - Rename symbol
2. `Ctrl + H` - Find and Replace all
3. `Ctrl + D` repeatedly - Select all occurrences then type

### Scenario 4: Text too small?
**Solution:** `Ctrl + =` to zoom in, `Ctrl + 0` to reset

### Scenario 5: Compare two files?
**Solution:**
1. Open first file
2. `Ctrl + \` to split editor
3. Open second file in new pane

### Scenario 6: Need to edit same thing on multiple lines?
**Solution:**
1. Select the text
2. `Ctrl + Shift + L` to select all matches
3. Type new text - updates everywhere!

### Scenario 7: Quick file navigation?
**Solution:** `Ctrl + P` - Type filename to open instantly

---

## PART 14: COMPLETE CHEAT SHEET

### General

| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + P` | Quick Open File |
| `Ctrl + ,` | Settings |
| `Ctrl + K, Ctrl + S` | Keyboard Shortcuts |
| `Ctrl + `` ` | Toggle Terminal |
| `Ctrl + B` | Toggle Sidebar |

### Files

| Shortcut | Action |
|----------|--------|
| `Ctrl + N` | New File |
| `Ctrl + O` | Open File |
| `Ctrl + S` | Save |
| `Ctrl + Shift + S` | Save As |
| `Ctrl + W` | Close File |
| `Ctrl + Shift + T` | Reopen Closed |
| `Ctrl + Tab` | Switch Files |

### Editing

| Shortcut | Action |
|----------|--------|
| `Ctrl + X` | Cut Line |
| `Ctrl + C` | Copy Line |
| `Ctrl + V` | Paste |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` | Redo |
| `Ctrl + /` | Comment Line |
| `Ctrl + D` | Select Next Match |
| `Ctrl + L` | Select Line |
| `Ctrl + Shift + K` | Delete Line |
| `Alt + Up/Down` | Move Line |
| `Shift + Alt + Up/Down` | Copy Line |
| `Ctrl + Enter` | Insert Line Below |
| `Ctrl + Shift + Enter` | Insert Line Above |
| `Ctrl + K, Ctrl + C` | Comment Block |
| `Ctrl + K, Ctrl + U` | Uncomment Block |
| `F2` | Rename Symbol |

### Search

| Shortcut | Action |
|----------|--------|
| `Ctrl + F` | Find |
| `Ctrl + H` | Find and Replace |
| `Ctrl + Shift + F` | Find in All Files |
| `F3` | Find Next |
| `Shift + F3` | Find Previous |

### Multi-Cursor

| Shortcut | Action |
|----------|--------|
| `Alt + Click` | Add Cursor |
| `Ctrl + Alt + Up/Down` | Add Cursor Above/Below |
| `Ctrl + D` | Select Next Match |
| `Ctrl + Shift + L` | Select ALL Matches |
| `Esc` | Exit Multi-Cursor |

### Navigation

| Shortcut | Action |
|----------|--------|
| `Ctrl + G` | Go to Line |
| `Ctrl + Home` | Go to File Start |
| `Ctrl + End` | Go to File End |
| `F12` | Go to Definition |

### View

| Shortcut | Action |
|----------|--------|
| `Ctrl + =` | Zoom In |
| `Ctrl + -` | Zoom Out |
| `Ctrl + 0` | Reset Zoom |
| `Ctrl + \` | Split Editor |
| `Shift + Alt + F` | Format Document |

### Activity Bar

| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + E` | Explorer |
| `Ctrl + Shift + F` | Search |
| `Ctrl + Shift + G` | Source Control |
| `Ctrl + Shift + D` | Debug |
| `Ctrl + Shift + X` | Extensions |

---

## PART 15: KEY POINTS TO REMEMBER

1. **`Ctrl + Shift + P`** (Command Palette) can do EVERYTHING - if you forget a shortcut, search there!
2. **`Ctrl + S`** (Save) - Use constantly!
3. **`Ctrl + P`** (Quick Open) - Fastest way to open files
4. **`Ctrl + D`** and **`Ctrl + Shift + L`** - Master these for multi-cursor editing
5. **`Ctrl + /`** - Comment/uncomment code quickly
6. **`Shift + Alt + F`** - Format messy code instantly
7. **`Ctrl + Shift + T`** - Recover accidentally closed files
8. **Tab completion** works in terminal - saves time!
9. **Extensions** add superpowers - install Python extension first!
10. **Multiple cursors** are a game-changer - practice them!

---
