---
title: "Organization Protocol — Universal File Management"
tags: [protocol, organization, reference]
date: 2025-10-23
---

# Organization Protocol
*Master guide for organizing ANY course material*

---

## 🎯 The Golden Rule

**If Claude needs to read it to help you → Full content in Obsidian**
**If you need to run it → Link-note or Desktop only**
**If it's a working file → Desktop only**

---

## 📊 The Three-Tier System

### Tier 1: Full Content in Obsidian ⭐
**Purpose:** Permanent reference, AI-readable, searchable

**What goes here:**
- Lecture notes (.md files)
- Lab instructions (.md files)
- Reading lists (formatted with checkboxes)
- Important summaries you write
- Quizzes and study materials

**Format:**
- Full markdown content
- Proper YAML frontmatter
- Descriptive filenames: `lecture-w02-topic-name-content.md`
- Organized by module and type

**Why:**
- Claude can read and reference
- Searchable across entire vault
- Single source of truth
- Survives beyond the semester

---

### Tier 2: Link-Notes in Obsidian 🔗
**Purpose:** Access runnable files, maintain references

**What goes here:**
- Solution notebooks (.ipynb)
- Starter code
- PDFs you can't convert to .md
- Important documents that must stay in original format

**Format:**
- Link-note with `file://` URL
- Frontmatter for organization
- Space for your notes
- Links to related materials

**Why:**
- Accessible from Obsidian
- Files stay runnable on Desktop (with data)
- Can add your own observations
- Organized but not duplicated

---

### Tier 3: Desktop Only 💻
**Purpose:** Working area, active development

**What goes here:**
- Data files (.csv, .db, .json, .xlsx)
- Practice/tutorial notebooks
- Your personal work-in-progress
- Temporary materials
- Files that change frequently

**Format:**
- Organized in Desktop module folders
- No Obsidian presence

**Why:**
- Notebooks need data files nearby
- Reduces Obsidian clutter
- Faster to work with
- Desktop is your "active workspace"

---

## 🌳 Decision Tree

```
New material arrives
    ↓
Is it a lecture/lab INSTRUCTION?
    YES → Do you have .md version?
        YES → Tier 1 (import full content)
        NO  → Can you convert to .md?
            YES → Convert, then Tier 1
            NO  → Tier 2 (link-note)
    ↓
Is it a SOLUTION/STARTER notebook?
    YES → Tier 2 (link-note, stays runnable)
    ↓
Is it DATA or PRACTICE material?
    YES → Tier 3 (Desktop only)
    ↓
Is it a READING (paper/chapter)?
    YES → Add to reading list in Tier 1
          Create link-note if PDF available
    ↓
Is it YOUR WORK in progress?
    YES → Tier 3 (Desktop)
          Move to Tier 1 when complete/final
```

---

## 📂 File Organization by Type

### Lecture Materials

| Format | Tier | Action | Script |
|--------|------|--------|--------|
| .md file | 1 | Import full content | `organize_lectures.py` |
| .pdf slides | 2 | Create link-note | `create_link_notes.py` |
| Video link | 1 | Add to reading list | Manual |

### Lab Materials

| Format | Tier | Action | Script |
|--------|------|--------|--------|
| .md instructions | 1 | Import full content | `organize_[module]_labs.py` |
| .pdf instructions | 2 | Create link-note | `create_link_notes.py` |
| Solution .ipynb | 2 | Create link-note | `create_solution_links.py` |
| Starter .ipynb | 2 | Create link-note | `create_link_notes.py` |
| Practice .ipynb | 3 | Desktop only | None |
| Data files | 3 | Desktop only | None |

### Readings

| Format | Tier | Action | Script |
|--------|------|--------|--------|
| Reading list | 1 | Formatted .md with checkboxes | Manual |
| PDF paper | 2 | Link from reading list | Manual |
| Web article | 1 | URL in reading list | Manual |
| Textbook chapter | 2 | Link-note if needed | Manual |

### Your Work

| Format | Tier | Action | Notes |
|--------|------|--------|--------|
| Draft notes | 3 | Desktop | Move to Tier 1 when final |
| Lab notebook | 3 | Desktop | Until complete |
| Assignment | 3 | Desktop | Until submitted |
| Final report | 1 | Import to Obsidian | After completion |

---

## 🏗️ Naming Conventions

### Tier 1 (Full Content)
**Lectures:**
```
lecture-w[##]-[topic-name]-content.md
Example: lecture-w02-data-handling-content.md
```

**Labs:**
```
lab-w[##]-[topic-name]-content.md
Example: lab-w02-exploring-data-content.md
```

**Reading Lists:**
```
reading-list-w[##].md
Example: reading-list-w02.md
```

**Summaries:**
```
summary-[topic-name].md
Example: summary-bayes-theorem.md
```

**Quizzes:**
```
quiz-w[##]-[topic-name].md
Example: quiz-w02-data-handling.md
```

### Tier 2 (Link-Notes)
**Solutions:**
```
lab-w[##]-solutions.md
Example: lab-w02-solutions.md
```

**Lectures (PDF only):**
```
lecture-w[##]-[topic-name].md
Example: lecture-w02-introduction.md
```

### Why Kebab-Case?
- ✅ Readable in file browsers
- ✅ Works across all operating systems
- ✅ No special characters
- ✅ Obsidian link-friendly

### Why "-content" Suffix?
- Distinguishes full content from link-notes
- Makes it clear this is AI-readable material
- Consistent with lecture naming

---

## 🤖 What Claude Can Read

### Tier 1: Full Access ✅
- Can read entire content
- Can search and reference
- Can generate quizzes
- Can answer detailed questions
- **Best for helping you learn**

### Tier 2: Partial Access ⚠️
- Can read .ipynb notebooks (via file path)
- **Cannot** read PDFs easily
- Can see link-note metadata
- **Best for code solutions**

### Tier 3: No Direct Access ❌
- Can't see Desktop files
- You can share specific files as needed
- **Best for active work**

---

## 📅 When to Organize

### Weekly (5 min)
- Run `create_link_notes.py` for new PDFs
- Add new readings to lists
- Quick check: anything new to import?

### After Lecture (10 min)
- If .md available: run `organize_lectures.py`
- If not: ensure PDF link-note exists
- Update related reading lists

### Before Lab (5 min)
- Ensure lab instructions are in Obsidian
- Check solution link-notes exist
- Verify data files on Desktop

### Semester Start (30 min)
- Set up module folders
- Import all available .md lectures
- Create reading lists structure
- Run link-note scripts

### Semester End (15 min)
- Move final work to Tier 1
- Archive Desktop working files
- Create summary notes

---

## 🔄 Module-Specific Scripts

### Template Structure
Each module can have its own organization script following this pattern:

```python
# organize_[MODULE]_labs.py or organize_[MODULE]_lectures.py

MAPPINGS = {
    "source_filename.md": {
        "week": "01",
        "title": "Descriptive Title",
        "date": "2025-09-24"
    }
}

def create_frontmatter(module, week, title, date):
    # Standard frontmatter template

def process_file(source, dest, info):
    # Read, format, write
```

### Adapting Scripts
To adapt for a new module:
1. Copy existing script (e.g., `organize_cs982_labs.py`)
2. Update `MODULE` variable
3. Update `MAPPINGS` dictionary with new filenames
4. Update file paths
5. Run and verify

---

## ✅ Quality Checks

After organizing, verify:

### Tier 1
- [ ] Files have proper frontmatter
- [ ] Names follow convention
- [ ] Content is readable (not garbled)
- [ ] Tags are correct
- [ ] Searchable in Obsidian

### Tier 2
- [ ] Links work (click opens file)
- [ ] File paths are correct
- [ ] Link-notes have descriptive content
- [ ] Related files linked

### Tier 3
- [ ] Data files in correct folders
- [ ] Notebooks can find data
- [ ] Personal work organized by week/topic

### Overall
- [ ] No duplicate content
- [ ] Old/inferior versions removed
- [ ] Clean folder structure
- [ ] Claude can find what's needed

---

## 🚨 Common Mistakes

### ❌ DON'T:
- Import practice notebooks to Obsidian (clutter)
- Create link-notes for data files (pointless)
- Keep old PDF link-notes when .md exists (inferior)
- Put working files in Obsidian (changes too often)
- Use spaces in filenames (use kebab-case)

### ✅ DO:
- Import core reference as full content
- Keep runnable files on Desktop
- Use consistent naming
- Run organization scripts
- Clean up after importing

---

## 📚 Related Protocols

- See [[file-types-guide]] for specific file type decisions
- See [[workflow-guide]] for daily/weekly workflow
- See [[quiz-creation-protocol]] for making quizzes
- See `_scripts/scripts-README.md` for script documentation

---

## 🎓 Philosophy

**Obsidian = Your Second Brain**
- Permanent knowledge
- Searchable reference
- AI-accessible help

**Desktop = Your Workbench**
- Active projects
- Running code
- Temporary files

**Keep them separate, keep them clean.**

---

*Last updated: 2025-10-23*
*Based on CS982 lab organization success*
