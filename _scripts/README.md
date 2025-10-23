---
title: "Organization Scripts Documentation"
tags: [scripts, automation, reference]
date: 2025-10-23
---

# Organization Scripts
*Automate file organization for your Obsidian vault*

---

## 📚 Available Scripts

### 1. `organize_lectures.py`
**Purpose:** Import lecture .md files with proper formatting

**Use when:** You have lecture markdown files to import from Desktop

**What it does:**
- Reads .md files from Desktop lecture folders
- Adds YAML frontmatter (title, module, tags, date)
- Renames with descriptive titles: `lecture-w02-topic-name-content.md`
- Moves to Obsidian lectures folder
- Preserves original content

**Example mapping:**
```
"CS814 AI for Autonomous Systems week 2.md"
  ↓
"lecture-w02-autonomous-intelligent-agents-content.md"
```

**Run:**
```bash
cd ~/Documents/UniCourse/_scripts
python3 organize_lectures.py
```

**Configure:** Edit `CS814_LECTURES` and `CS982_LECTURES` dictionaries in the script

---

### 2. `organize_cs982_labs.py`
**Purpose:** Import CS982 lab instruction .md files

**Use when:** You have lab instruction markdown files

**What it does:**
- Imports lab instructions as full content
- Adds proper frontmatter
- Renames: `lab-w02-exploring-data-content.md`
- Moves to Obsidian labs folder

**Example:**
```
"CS989_ Big Data Fundamentals Lab (week 2).md"
  ↓
"lab-w02-exploring-data-content.md"
```

**Run:**
```bash
python3 organize_cs982_labs.py
```

**Adapt for other modules:**
1. Copy script: `cp organize_cs982_labs.py organize_cs814_labs.py`
2. Change `CS982` → `CS814` throughout
3. Update `CS982_LABS` dictionary with CS814 filenames
4. Update source/dest paths

---

### 3. `create_link_notes.py`
**Purpose:** Create link-notes for PDFs and documents on Desktop

**Use when:**
- New PDFs added to Desktop folders
- Weekly check for new materials
- After downloading course documents

**What it does:**
- Scans Desktop module folders for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`
- **Skips .md files** (those should be imported with other scripts)
- Creates link-notes in appropriate Obsidian folders
- Uses `file://` URLs for clickable links
- Idempotent (safe to run multiple times)

**Run:**
```bash
python3 create_link_notes.py
```

**Configure:** Edit `MODULE_MAP` in script if folders change

---

### 4. `create_solution_links.py`
**Purpose:** Create link-notes for official solution notebooks

**Use when:** You have solution .ipynb files to reference

**What it does:**
- Creates link-notes for solution notebooks
- Includes topics covered, dataset info
- Adds space for your notes/questions
- Links to related lab instructions

**Example link-note created:**
```markdown
---
title: "Lab 2 Solutions"
module: "CS982"
tags: [module/CS982, type/labs, solutions, week-02]
---

# Lab 2 Solutions (Official Solution)

**Solution notebook**: [Lab 2 - Solutions.ipynb](file://...)

## Topics Covered
- Pandas DataFrame operations
- Handling missing data

## Dataset Used
pokemon_alopez247.csv

## My Notes
-
```

**Run:**
```bash
python3 create_solution_links.py
```

**Adapt for other modules:** Edit `SOLUTIONS` dictionary

---

### 5. `add_summary.sh`
**Purpose:** Quick creation of summary notes from template

**Use when:** You want to create a summary note

**Usage:**
```bash
./add_summary.sh CS814 "Bayes Theorem" w03
```

**Creates:** `CS814/summaries/summary-bayes-theorem.md`

---

## 🌳 Decision Tree: Which Script?

```
I have new materials
    ↓
What type?
    ↓
Lecture .md files?
    → organize_lectures.py
    ↓
Lab instruction .md files?
    → organize_cs982_labs.py (or module-specific version)
    ↓
PDFs / PPTs / Word docs?
    → create_link_notes.py
    ↓
Solution .ipynb notebooks?
    → create_solution_links.py
    ↓
Data files (.csv, .db)?
    → No script needed (keep on Desktop)
    ↓
Practice notebooks?
    → No script needed (keep on Desktop)
    ↓
Want to create summary?
    → add_summary.sh
```

---

## 🔄 Common Workflows

### Weekly Organization (5 min)
**After downloading new materials:**

```bash
cd ~/Documents/UniCourse/_scripts

# Check for new PDFs/documents
python3 create_link_notes.py

# If you got lecture .md files
python3 organize_lectures.py

# If you got lab .md files
python3 organize_cs982_labs.py

# Done!
```

---

### Semester Start Setup (30 min)

1. **Check what materials you have:**
```bash
ls ~/Desktop/Strathclyde\ /Uni\ Course\ Raw/CS*/
```

2. **Organize lectures if .md available:**
```bash
python3 organize_lectures.py
```

3. **Organize labs if .md available:**
```bash
python3 organize_cs982_labs.py
# Repeat for other modules if needed
```

4. **Create link-notes for PDFs:**
```bash
python3 create_link_notes.py
```

5. **Verify in Obsidian:**
- Open Obsidian
- Check each module folder
- Test searching for content
- Click a few links to verify they work

---

### After Getting New Lecture .md Files

**Example: Lecturer posts weeks 6-10 lectures as markdown**

1. **Save to Desktop in lecture folder:**
```
Desktop/Strathclyde /Uni Course Raw/CS814.../Lectures/Lectures md/
```

2. **Edit `organize_lectures.py`:**
Add weeks 6-10 to the mappings dictionary

3. **Run script:**
```bash
python3 organize_lectures.py
```

4. **Verify:**
Check Obsidian lectures folder for new files

---

## 🛠️ Adapting Scripts for New Modules

### Creating `organize_cs814_labs.py`

**Step 1: Copy existing script**
```bash
cp organize_cs982_labs.py organize_cs814_labs.py
```

**Step 2: Edit mappings**
```python
CS814_LABS = {
    "CS814 Lab Week 1.md": {
        "week": "01",
        "title": "Python Intro",
        "date": "2025-09-24"
    },
    # ... add all labs
}
```

**Step 3: Update paths**
```python
cs814_source = DESKTOP_BASE / "CS814 - AI for Autonomous Systems" / "Labs" / "Lab mds"
cs814_dest = OBSIDIAN_BASE / "CS814 - AI for Autonomous Systems" / "labs"
```

**Step 4: Update module code**
```python
process_lab(
    source_file,
    cs814_dest,
    "CS814",  # ← Change this
    info["week"],
    info["title"],
    info["date"]
)
```

**Step 5: Test**
```bash
python3 organize_cs814_labs.py
```

---

## 🐛 Troubleshooting

### "File not found" errors

**Check:**
1. Is the file actually on Desktop?
   ```bash
   ls ~/Desktop/Strathclyde\ /Uni\ Course\ Raw/CS982.../
   ```

2. Is the filename exactly right in the script?
   - Check for extra spaces
   - Check for special characters
   - Filenames are case-sensitive!

3. Are the paths quoted properly?
   ```python
   # Note the space in "Strathclyde "
   "/Desktop/Strathclyde /Uni Course Raw/"
   ```

---

### Script runs but files not appearing in Obsidian

**Check:**
1. Did script report success?
2. Check destination folder:
   ```bash
   ls ~/Documents/UniCourse/CS982*/labs/
   ```

3. Refresh Obsidian (Cmd+R or Ctrl+R)

4. Check frontmatter is valid YAML:
   - No tabs, only spaces
   - Quotes around values with special chars
   - Date format: YYYY-MM-DD

---

### Links not working

**Check:**
1. Click link - does it open file browser to wrong location?
2. File might have been moved/deleted from Desktop
3. Check URL encoding in link-note:
   ```python
   from urllib.parse import quote
   file_url = "file://" + quote(str(file_path.absolute()))
   ```

4. On macOS, spaces in paths must be encoded as `%20`

---

## 🎯 Best Practices

### Before Running Scripts

1. **Back up Obsidian vault** (just in case)
2. **Check file locations** on Desktop
3. **Read script output** to verify what it will do
4. **Run on small test first** (comment out most files in mapping)

### After Running Scripts

1. **Open Obsidian** and refresh
2. **Spot check** a few files
3. **Test search** for content
4. **Click links** to verify they work
5. **Read one full file** to ensure formatting is correct

### Regular Maintenance

- **Weekly:** Run `create_link_notes.py` for new PDFs
- **After lectures:** Check if .md available, run organize script
- **Semester end:** Archive old scripts or update for new semester

---

## 📚 Related Documentation

- **[[organization-protocol]]** - When to use which tier
- **[[file-types-guide]]** - Quick file type decisions
- **[[workflow-guide]]** - Weekly study workflow
- **[[quiz-creation-protocol]]** - Making quizzes from materials

---

## 🚀 Quick Reference

| Task | Script | Command |
|------|--------|---------|
| New lecture .md | `organize_lectures.py` | `python3 organize_lectures.py` |
| New lab .md | `organize_cs982_labs.py` | `python3 organize_cs982_labs.py` |
| New PDFs | `create_link_notes.py` | `python3 create_link_notes.py` |
| Solution notebooks | `create_solution_links.py` | `python3 create_solution_links.py` |
| Create summary | `add_summary.sh` | `./add_summary.sh CS982 "Topic" w02` |

---

*Last updated: 2025-10-23*
*Keep this README updated as you create new scripts!*
