# 🎓 MSc AI Course Dashboard

Welcome to your Obsidian vault for MSc AI at Strathclyde!

## 📚 Modules

| Code | Module | Quick Access |
|------|--------|--------------|
| CS814 | [[CS814 - AI for Autonomous Systems/README\|AI for Autonomous Systems]] | [[CS814 - AI for Autonomous Systems/summaries/\|Summaries]] |
| CS982 | [[CS982 - Big Data Technologies/README\|Big Data Technologies]] | [[CS982 - Big Data Technologies/summaries/\|Summaries]] |
| CS801 | [[CS801 - Quantitative Methods for AI/README\|Quantitative Methods for AI]] | [[CS801 - Quantitative Methods for AI/summaries/\|Summaries]] |
| CS978 | [[CS978 - Legal, Ethical and Professional Issues/README\|Legal, Ethical & Professional Issues]] | [[CS978 - Legal, Ethical and Professional Issues/summaries/\|Summaries]] |

## 🔍 Search Tips

### Tag Queries
Use these searches in Obsidian to filter your notes:

- **All lectures**: `tag:#type/lectures`
- **All labs**: `tag:#type/labs`
- **All summaries**: `tag:#type/summaries`
- **Specific module**: `tag:#module/CS814`
- **CS814 lectures**: `tag:#module/CS814 tag:#type/lectures`
- **All notes**: `tag:#type/notes`

### Dataview Queries
If you have the Dataview plugin installed, try these:

```dataview
TABLE module as Module, tags as Tags
FROM #type/summaries
SORT file.name ASC
```

```dataview
LIST
FROM #module/CS814
WHERE contains(tags, "#type/lectures")
```

## ➕ Add New Summary

### Method 1: Use the Script
```bash
cd ~/Documents/UniCourse/_scripts
./add_summary.sh CS814 "Topic Name" w03
```

### Method 2: Manual
1. Copy the template: [[_templates/summary-template]]
2. Save to the appropriate module's `summaries/` folder
3. Name it: `summary-w##-topic-name.md`
4. Fill in the frontmatter and content

### Method 3: Ask Claude
When working with Claude Code, say:
> "Summarise this for CS814 Week 03"

Claude will create the summary file in the correct location with proper formatting.

## ✅ Next Actions

- [ ] Review this week's lectures (all modules)
- [ ] Complete outstanding lab exercises
- [ ] Create summary notes for recent topics
- [ ] Update quiz prompts in each module
- [ ] Review and consolidate notes before exams

## 📂 Folder Structure

```
UniCourse/
├── 00_INDEX.md (this file)
├── CS814 - AI for Autonomous Systems/
│   ├── README.md
│   ├── lectures/
│   ├── labs/
│   ├── notes/
│   ├── assignments/
│   ├── summaries/
│   └── quizzes/
├── CS982 - Big Data Technologies/
│   └── ... (same structure)
├── CS801 - Quantitative Methods for AI/
│   └── ... (same structure)
├── CS978 - Legal, Ethical and Professional Issues/
│   └── ... (same structure)
├── _general/ (cross-module notes)
├── _templates/ (note templates)
└── _scripts/ (automation scripts)
```

## 🎯 Study Workflow

1. **After Each Lecture**: Create link-note if not already exists
2. **During Study**: Add your notes to `notes/` folder
3. **Before Exam**: Create summary using template
4. **Revision**: Use tag queries to review all summaries
5. **Practice**: Work through quizzes and assignments

## 🔗 General Resources

- [[_general/start-here|👋 Start Here]] — New to this vault?
- [[_general/workflow-guide|🧠 Workflow Guide]] — How to build your second brain
- [[_general/|Cross-Module Notes]]
- [[_templates/summary-template|Summary Template]]
- [[_templates/lecture-note-template|Lecture Note Template]]
- [[_templates/lab-note-template|Lab Note Template]]

---
*Last updated: 2025-10-21*
