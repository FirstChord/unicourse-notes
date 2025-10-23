---
title: "Second Brain Workflow Guide"
tags: [guide, workflow]
---

# 🧠 Second Brain Workflow Guide

**When to use this**: After you've organized all your materials and are ready to start actively learning and building your second brain.

---

## 🎯 The Goal

Transform passive storage (PDFs sitting in folders) into active knowledge (understanding you can retrieve and apply).

---

## 📂 Step 0: File Organization (Do This First!)

**Before you can build your second brain, you need organized materials.**

### When You Get New Course Materials

Follow the **Three-Tier System** (see [[organization-protocol]] for full details):

**Tier 1: Full Content in Obsidian** (AI-readable)
- Lecture .md files → Run `organize_lectures.py`
- Lab instruction .md files → Run `organize_[module]_labs.py`
- Reading lists → Formatted markdown with checkboxes

**Tier 2: Link-Notes in Obsidian** (Accessible but runnable)
- PDFs, PPTs → Run `create_link_notes.py`
- Solution notebooks → Run `create_solution_links.py`

**Tier 3: Desktop Only** (Working files)
- Data files (.csv, .db) → Keep with notebooks
- Practice notebooks → Keep in weekly folders
- Your work-in-progress → Keep on Desktop

### Quick Weekly Check (5 min)

```bash
cd ~/Documents/UniCourse/_scripts

# After downloading new materials from MyPlace:
python3 create_link_notes.py  # For PDFs/docs
python3 organize_lectures.py  # If you got lecture .mds
python3 organize_cs982_labs.py  # If you got lab .mds

# Verify in Obsidian
```

**Golden Rule:** If Claude needs to read it to help you → Full content in Obsidian

See also:
- [[organization-protocol]] - Complete organization guide
- [[file-types-guide]] - Quick reference for each file type
- `_scripts/README.md` - Script documentation

---

## 📚 Weekly Learning Workflow

### Step 1: After Each Lecture (15-20 min)

**What you have**: Full lecture content in Obsidian (e.g., `lecture-w03-algorithms-content.md`)

**What to do**:

1. **Create a personal note** in `notes/`:
   ```bash
   # In Obsidian, create:
   CS814/notes/note-w03-algorithms.md
   ```

2. **Write in your own words**:
   - Main concepts covered
   - Confusing parts (mark with ❓)
   - Connections to previous weeks
   - Examples that clicked for you

3. **Link it**: In your lecture link-note, add:
   ```markdown
   ## My Notes
   - [[note-w03-algorithms]]
   ```

**Example structure**:
```markdown
---
title: "Week 03 — Algorithms (My Notes)"
module: "CS814"
tags: [module/CS814, type/notes]
---

# Main Ideas
- Search algorithms fall into 3 categories...
- Key difference: informed vs uninformed

# What Clicked
- The graph example on slide 15 made BFS clear

# Still Confused ❓
- How does bidirectional search work exactly?

# Links
- [[lecture-w03-algorithms]]
- [[reading-w03-russell-norvig]]
```

---

### Step 2: After Each Lab (20-30 min)

**What you have**:
- Full lab instructions (e.g., `lab-w03-visualization-content.md`)
- Link-note to solutions (e.g., `lab-w03-solutions.md`)
- Your work notebooks on Desktop

**What to do**:

1. **Create lab reflection** in `notes/`:
   ```markdown
   CS814/notes/lab-reflection-w03.md
   ```

2. **Document**:
   - What you implemented
   - Bugs you hit (and how you solved them)
   - Key code snippets with explanations
   - Performance insights

---

### Step 3: End of Week Summary (30-40 min)

**This is where the magic happens!**

#### Using Claude to Generate Summaries

In Claude Code, say:
> "Summarize CS814 Week 3 for me. I covered algorithms and search. Here's my notes: [paste your note-w03-algorithms.md]"

I'll create a summary with:
- Key concepts distilled
- Quiz questions embedded
- Links to your notes

**OR do it manually**:

```bash
cd ~/Documents/UniCourse/_scripts
./add_summary.sh CS814 "Search Algorithms" w03
```

Then fill in the template with:

```markdown
## Summary
- Main 3-5 takeaways from this week
- One-line explanations

## Key Ideas
- Deep dive on the most important concept
- Why it matters

## Quiz Prompts
- [ ] What's the difference between BFS and DFS?
- [ ] When would you use A* search?
- [ ] Explain the admissible heuristic property
- [ ] What's the time complexity of Dijkstra's algorithm?
- [ ] How does bidirectional search improve performance?

## Links
- [[lecture-w03-algorithms]]
- [[lab-w03]]
- [[note-w03-algorithms]]
- [[reading-w03-russell-norvig]]
```

---

### Step 4: Weekly Review (Friday, 30 min)

Create or update: `_general/weekly-review.md`

```markdown
# Week 3 Review (Oct 14-20)

## CS814: AI for Autonomous Systems
- ✅ Lecture 3: Search algorithms
- ✅ Lab 3: Implemented BFS/DFS
- 💡 Key insight: Heuristics make search efficient
- ❓ Still unclear: Bidirectional search details

## CS982: Big Data
- ✅ Lecture 3: MapReduce
- ⚠️ Lab 3: Need to finish Part 2
- 💡 Key insight: Partition strategy matters

## CS801: Quantitative Methods
- ✅ Lecture 3: Probability distributions
- ✅ Lab 3: Monte Carlo simulations
- 💡 Key insight: Central limit theorem in action

## Quiz Yourself
- [ ] Test on CS814 summary-w03 questions
- [ ] Test on CS982 summary-w03 questions
- [ ] Test on CS801 summary-w03 questions

## Next Week Prep
- [ ] Read CS814 Week 4 materials
- [ ] Review CS982 Hadoop docs before lab
```

---

## 🎲 Quiz & Retrieval Practice

### Daily Practice (5-10 min)

**Option 1: In Obsidian**

1. Open any `summary-w##.md`
2. Read the "Quiz Prompts" section
3. Try to answer WITHOUT looking at notes
4. Check your answers against the "Key Ideas" section
5. Mark your performance:
   - ✅ Solid
   - ⚠️ Shaky, need review
   - ❌ Don't know, must study

**Option 2: Use Claude**

Ask me:
> "Quiz me on CS814 Week 3"

I'll ask the questions from your summary and give immediate feedback.

---

### Weekly Quiz Bank

Periodically, consolidate all quiz questions:

```markdown
# CS814/quizzes/quiz-bank.md

## Week 1: Python & Intro
- What are the 4 properties of intelligent agents?
- ...

## Week 2: Agents
- Define rational agent
- ...

## Week 3: Search Algorithms
- What's the difference between BFS and DFS?
- ...
```

Use this for exam prep!

---

## 🔗 Linking Strategy

**Make your notes talk to each other:**

In `summary-w03-search.md`:
```markdown
## Links
- Builds on: [[summary-w02-agents]]
- Related reading: [[reading-w03-russell-norvig]]
- Applied in: [[lab-w03]]
- My thoughts: [[note-w03-algorithms]]
```

This creates a **knowledge graph** in Obsidian!

---

## 🚀 Power Moves

### 1. **Before Exams: Map of Content (MOC)**

Create `CS814/exam-prep.md`:
```markdown
# CS814 Exam Prep — Map of Content

## Core Topics
- [[summary-w01-intro]]
- [[summary-w02-agents]]
- [[summary-w03-search]]
- ...

## Weak Areas (Review First)
- [[summary-w05-logic]] ⚠️
- [[summary-w07-learning]] ❌

## Practice Problems
- All quiz banks: [[quizzes/quiz-bank]]
- Past papers: [[assignments/past-exam-2024]]
```

### 2. **Ask Claude for Connections**

> "What are the connections between CS814 Week 3 (search) and CS801 Week 2 (optimization)?"

I'll help you see cross-module patterns!

### 3. **Spaced Repetition Export**

If you use Anki, export quiz questions:
```markdown
Q: What's the difference between BFS and DFS?
A: BFS explores level-by-level (queue), DFS explores depth-first (stack). BFS finds shortest path, DFS uses less memory.
```

Save as `anki-export.txt` and import to Anki.

---

## 📅 Suggested Schedule

| Day | Activity | Time |
|-----|----------|------|
| Mon/Wed/Fri | After lecture: Create note-w##.md | 15 min |
| Tue/Thu | After lab: Create lab-reflection.md | 20 min |
| Friday | Create summary-w##.md for each module | 40 min |
| Friday | Update weekly-review.md | 30 min |
| Saturday | Quiz yourself on this week's summaries | 20 min |
| Sunday | Quiz yourself on random past weeks | 20 min |

**Total time**: ~3-4 hours/week (beyond lectures/labs)

---

## 🎯 Success Metrics

You'll know this is working when:

1. **You can explain concepts** without looking at slides
2. **You see connections** between modules
3. **Quiz questions feel easy** after 1-2 reviews
4. **Exam prep is fast** because everything is already processed
5. **You remember more** long-term (not just for exams)

---

## 🆘 When You Get Stuck

**"I don't understand the lecture material"**
→ Create the note anyway with ❓ marks, then ask Claude:
> "Help me understand [concept] from CS814 Week 3"

**"I'm behind and overwhelmed"**
→ Focus on summaries only. Skip detailed notes. Better to have all summaries than perfect notes for half the weeks.

**"I don't know what to put in the summary"**
→ Ask Claude:
> "Summarize CS814 Week 4 for me. Here's the lecture: [description or upload PDF]"

**"Quiz questions feel pointless"**
→ They're not! Research shows retrieval practice is THE most effective study method. Trust the process.

---

## 💬 Using Claude Code for Learning

### Quick Commands

**Generate a summary**:
> "Summarize CS814 Week 5 on machine learning. Create the file in summaries/ with quiz questions"

**Quiz me**:
> "Quiz me on CS982 Week 3 (MapReduce)"

**Explain a concept**:
> "Explain A* search algorithm like I'm 5, then give me the technical version"

**Connect concepts**:
> "What's the relationship between CS814 search algorithms and CS801 optimization methods?"

**Exam prep**:
> "Create a study guide for CS814 covering Weeks 1-5. Focus on key concepts and common exam questions"

**Review my notes**:
> "Here are my notes from Week 3 [paste]. What am I missing? What should I clarify?"

---

## 🎓 Remember

**This system works when you work it.**

- It's okay to miss days
- It's okay to be messy at first
- It's okay to adjust the workflow to fit you
- The goal is **understanding**, not perfect notes

Start small:
1. This week: Just create one summary
2. Next week: Add quiz questions
3. Week after: Try the weekly review

Build the habit gradually!

---

*Created: 2025-10-21*
*Updated: 2025-10-23 - Added organization section*
*Your second brain is ready. Now feed it! 🧠*
