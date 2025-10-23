---
title: "File Types Guide — Quick Reference"
tags: [reference, organization, quick-guide]
date: 2025-10-23
---

# File Types Guide
*Quick reference: "I have X file, what do I do?"*

---

## 📄 Markdown Files (.md)

### Lecture Notes
- **✅ DO:** Import full content to Obsidian
- **✅ DO:** Add frontmatter, rename to `lecture-w##-topic-content.md`
- **❌ DON'T:** Create link-notes (full content is better)
- **🤖 Claude:** Can read, quiz, summarize, reference
- **Script:** `organize_lectures.py`

### Lab Instructions
- **✅ DO:** Import full content to Obsidian
- **✅ DO:** Add frontmatter, rename to `lab-w##-topic-content.md`
- **❌ DON'T:** Create link-notes (full content is better)
- **🤖 Claude:** Can answer lab questions, create prep materials
- **Script:** `organize_[module]_labs.py`

### Your Personal Notes
- **✅ DO:** Keep in Obsidian notes folder
- **✅ DO:** Use proper frontmatter and tags
- **💡 Why:** Searchable, permanent knowledge base
- **🤖 Claude:** Can read and help organize

---

## 💻 Jupyter Notebooks (.ipynb)

### Official Solutions
- **✅ DO:** Create link-note in Obsidian
- **✅ DO:** Leave notebook on Desktop (needs to run with data)
- **✅ DO:** Name link-note as `lab-w##-solutions.md`
- **❌ DON'T:** Import full notebook content (too verbose)
- **🤖 Claude:** Can read notebooks via file path
- **Script:** `create_solution_links.py`

### Starter Code / Templates
- **✅ DO:** Create link-note if it's official course material
- **✅ DO:** Keep on Desktop in lab folder
- **💡 Why:** You'll modify it, needs to run
- **🤖 Claude:** Can read and help debug
- **Script:** `create_link_notes.py`

### Practice / Tutorial Notebooks
- **✅ DO:** Keep on Desktop only, organized by week
- **❌ DON'T:** Create link-notes (would clutter Obsidian)
- **💡 Why:** Working materials, not reference
- **🤖 Claude:** Share specific ones as needed
- **Script:** None

### Your Personal Notebooks
- **✅ DO:** Keep on Desktop while working
- **⚠️ CONSIDER:** Move to Obsidian if it becomes final/reference material
- **💡 Why:** Active work area, changes frequently
- **Example:** `YourName_Lab2_Draft.ipynb` stays on Desktop

---

## 📊 Data Files

### CSV Files (.csv)
- **✅ DO:** Keep on Desktop with notebooks
- **✅ DO:** Organize by week/lab folder
- **❌ DON'T:** Create link-notes in Obsidian
- **💡 Why:** Needed for code execution, not human-readable
- **🤖 Claude:** Can reference from lab instructions, can't "read" raw CSV usefully

### Database Files (.db, .sqlite)
- **✅ DO:** Keep on Desktop with notebooks
- **❌ DON'T:** Put in Obsidian
- **💡 Why:** Binary files, need to be queried by code
- **🤖 Claude:** Can help write queries, can't access file directly

### JSON / XML (.json, .xml)
- **✅ DO:** Keep on Desktop if used by code
- **⚠️ CONSIDER:** Import to Obsidian if it's configuration/reference
- **💡 Example:** API response examples might go in Obsidian as code blocks

### Excel Files (.xlsx, .xls)
- **✅ DO:** Keep on Desktop
- **⚠️ CONSIDER:** Convert to CSV if used in Python
- **❌ DON'T:** Put in Obsidian (binary format)

---

## 📑 PDF Files

### Lecture Slides (when no .md available)
- **✅ DO:** Create link-note in Obsidian
- **⚠️ BETTER:** Try to get .md version from instructor
- **⚠️ BEST:** Convert to .md if critical content
- **🤖 Claude:** **Cannot read PDF content easily** - this is a limitation
- **Script:** `create_link_notes.py`

### Lab Instructions (when no .md available)
- **✅ DO:** Create link-note in Obsidian
- **⚠️ BETTER:** Save as .md if possible (File > Save As > Markdown)
- **🤖 Claude:** **Cannot read PDF content easily**
- **Script:** `create_link_notes.py`

### Academic Papers / Textbook Chapters
- **✅ DO:** Add to reading list with checkbox
- **✅ DO:** Create link-note if it's heavily referenced
- **❌ DON'T:** Try to import 50-page PDFs to Obsidian
- **💡 Tip:** Add summary notes after reading
- **🤖 Claude:** Can't read, but can discuss concepts if you share key points

### Assignment Briefs
- **✅ DO:** Create link-note
- **⚠️ BETTER:** Extract requirements to markdown checklist
- **Example:**
```markdown
## Assignment 2 Requirements
- [ ] Implement A* algorithm
- [ ] Test on 8-puzzle
- [ ] Write report (1500 words)

**Full brief**: [[assignment-2-brief.md]] (link to PDF)
```

---

## 🎥 Media Files

### Video Lectures (links)
- **✅ DO:** Add URL to reading list
- **✅ DO:** Include in weekly materials
- **❌ DON'T:** Download video files (huge)
- **🤖 Claude:** Cannot watch videos
- **Format:**
```markdown
### 📺 Week 2 Videos
- [ ] [A* Algorithm Explained - Computerphile](https://youtube.com/...)
```

### Audio Recordings
- **✅ DO:** Link in reading list if official
- **❌ DON'T:** Add personal lecture recordings to Obsidian
- **💡 Why:** Large files, not searchable
- **🤖 Claude:** Cannot listen to audio

### Images / Diagrams
- **✅ DO:** Add to Obsidian notes if illustrative
- **✅ DO:** Use markdown image syntax
- **💡 Example:** `![8-puzzle goal state](path/to/image.png)`
- **🤖 Claude:** Can see images when you share them

---

## 📦 Code Files

### Python Scripts (.py)
- **✅ DO:** Keep on Desktop if executable
- **⚠️ CONSIDER:** Add to Obsidian as code block if it's reference/example
- **💡 Example:** Utility scripts stay on Desktop, algorithm examples in notes
- **🤖 Claude:** Can read and help debug

### Configuration Files (.json, .yaml, .toml)
- **✅ DO:** Keep on Desktop with project
- **⚠️ CONSIDER:** Document important configs in Obsidian
- **Example:** `requirements.txt` stays on Desktop

---

## 📝 Office Documents

### Word Documents (.docx)
- **⚠️ DO:** Convert to .md if possible (File > Save As > Markdown)
- **✅ DO:** Create link-note if can't convert
- **💡 Why:** Markdown is more future-proof
- **🤖 Claude:** Limited reading ability for .docx

### PowerPoint (.pptx)
- **✅ DO:** Create link-note
- **❌ DON'T:** Try to import (complex format)
- **⚠️ CONSIDER:** Export to PDF first
- **🤖 Claude:** Cannot read presentations

---

## 🗂️ Archive Files

### ZIP / TAR (.zip, .tar.gz)
- **✅ DO:** Extract to Desktop
- **✅ DO:** Organize extracted contents per this guide
- **❌ DON'T:** Keep compressed in Obsidian
- **💡 Tip:** Delete archive after extracting

---

## 🎯 Decision Matrix

| File Type | Tier | Obsidian Action | Desktop Action | Claude Access |
|-----------|------|-----------------|----------------|---------------|
| Lecture .md | 1 | Import full | Keep backup | ✅ Full |
| Lab .md | 1 | Import full | Keep backup | ✅ Full |
| Solution .ipynb | 2 | Link-note | Keep here | ✅ Via link |
| Practice .ipynb | 3 | Nothing | Organize by week | ❌ Share if needed |
| .csv data | 3 | Nothing | With notebooks | ❌ Referenced |
| Lecture .pdf | 2 | Link-note | Keep here | ⚠️ Limited |
| Paper .pdf | 2 | Link from reading list | Keep here | ⚠️ Limited |
| Your notes .md | 1 | Keep here | - | ✅ Full |
| Your work .ipynb | 3 | Nothing (until final) | Keep here | ❌ Share if needed |
| Video URL | 1 | In reading list | - | ❌ Can't watch |
| .py script | 3 | Code block if reference | Keep here | ✅ Can read |

---

## 🚀 Quick Start Checklist

**Got new course materials? Follow these steps:**

1. **Identify file type** (use this guide)
2. **Determine tier** (1, 2, or 3)
3. **Take action:**
   - Tier 1 → Run organize script or import manually
   - Tier 2 → Run link-note script
   - Tier 3 → Organize on Desktop, no Obsidian action
4. **Verify:**
   - Can you find it in Obsidian (if Tier 1 or 2)?
   - Can you run it from Desktop (if Tier 2 or 3)?
   - Can Claude access it (if you need help)?

---

## 💡 Pro Tips

### Converting PDFs to Markdown
**Option 1: Save As (if editable PDF)**
- Open in Preview/Adobe
- File > Export > Text
- Clean up formatting
- Add to Obsidian

**Option 2: Copy/Paste**
- Select all text
- Paste into text editor
- Clean up
- Add frontmatter

**Option 3: Ask for .md version**
- Email instructor: "Is there a markdown version of the lecture slides?"
- Many instructors write in markdown first

### Organizing Your Desktop
```
Desktop/
  Strathclyde /Uni Course Raw/
    CS814 - AI for Autonomous Systems/
      Labs/
        Week 1/
          *.ipynb (starter, practice)
          *.csv (data)
        Week 2/
          ...
    CS982 - Big Data Technologies/
      Labs/
        ...
```

### Testing Claude Access
After organizing, test:
- "Claude, what's in Lab 2 for CS982?"
- "Create a quiz for Week 3 lecture"
- "What dataset is used in Lab 4?"

If I can answer easily, your organization is working! ✅

---

## 📚 Related Guides

- [[organization-protocol]] - Comprehensive decision tree
- [[workflow-guide]] - Daily/weekly workflows
- [[quiz-creation-protocol]] - Making effective quizzes
- `_scripts/scripts-README.md` - Script documentation

---

*Last updated: 2025-10-23*
*Quick reference extracted from organization-protocol.md*
