---
title: "Quiz Creation Protocol"
tags: [guide, protocol, quizzes]
---

# 🎯 Quiz Creation Protocol

**Purpose**: Guidelines for creating effective, aligned quizzes for course materials.

**Created**: 2025-10-21
**Last Updated**: 2025-10-21

---

## Core Principle

**ALWAYS base quizzes on ACTUAL course materials, not assumptions.**

A quiz should test what the student LEARNED, not what we think they should have learned.

---

## Step-by-Step Process

### 1. Gather ALL Source Materials

**Before creating any quiz questions**, collect:

#### ✅ Primary Sources:
- **Lecture slides/notes** (most important - what professor emphasized)
- **Lab notebooks/exercises** (practical skills practiced)
- **Reading list** (supplementary materials assigned)

#### ✅ Secondary Sources:
- Student's own notes (if available)
- Assignment instructions
- Previous exam questions (if available)

### 2. Read and Analyze Materials

**For Lectures:**
- [ ] Identify key concepts defined
- [ ] Note examples used (often appear in quizzes!)
- [ ] Look for emphatic statements ("This is important!", "Remember...")
- [ ] Note any calculations or worked examples
- [ ] Identify common mistakes mentioned

**For Labs/Notebooks:**
- [ ] List all methods/functions demonstrated
- [ ] Note code patterns practiced
- [ ] Identify problem-solving techniques shown
- [ ] Look for common errors or troubleshooting tips
- [ ] Note datasets used (can reference in questions)

**For Readings:**
- [ ] Identify key topics covered
- [ ] Note definitions provided
- [ ] Look for frameworks or categorizations
- [ ] Identify best practices mentioned

### 3. Create Content Map

**Organize findings into categories:**

```markdown
## Week X Content Map

### Theoretical Concepts (from lecture)
- Definition of X
- Types of Y: A, B, C
- Formula for Z
- When to use W vs V

### Practical Skills (from lab)
- How to do X in pandas
- Interpreting output Y
- Debugging issue Z

### Decision-Making (from readings + lecture)
- When to choose approach A vs B
- How to handle scenario C
- Best practices for D
```

### 4. Design Question Distribution

**Aim for balanced coverage:**

| Section | Points | Focus | Source |
|---------|--------|-------|--------|
| Part 1: Concepts | 25-35% | Definitions, theory, understanding | Lecture |
| Part 2: Technical Skills | 35-45% | Code, methods, operations | Lab |
| Part 3: Application | 15-25% | Decision-making, real scenarios | All |
| Part 4: Integration | 5-15% | Combining multiple concepts | All |

### 5. Write Questions Using This Template

#### Question Template:

```markdown
### Question X (Y points)
**[Clear, specific question based on actual material]**

[Answer format: multiple choice, fill-in, code, or written]

<details>
<summary>💡 Show Answer</summary>

**Answer**: [Correct answer]

**Explanation**: [Why this is correct]

**From [source]**: [Specific reference - "This example appeared in Lab 2"]

**Additional context**: [If helpful]

</details>
```

---

## Question Type Guidelines

### Multiple Choice Questions
**Best for:**
- Testing definitions
- Identifying correct method/function
- Recognizing patterns

**Tips:**
- Use actual code from labs as examples
- Base wrong answers on common mistakes
- Keep options similar length

**Example:**
```markdown
**What method reads a CSV file in pandas?**

- [ ] A) pd.load_csv()
- [ ] B) pd.read_csv()  ← Correct (from lab)
- [ ] C) pd.import_csv()
- [ ] D) pd.open_csv()
```

---

### Fill-in-the-Blank / Short Answer
**Best for:**
- Testing recall of key terms
- Testing lists (e.g., "3 types of X")
- Simple definitions

**Tips:**
- Use exact terminology from lecture
- If professor gave a list, test that list
- Be specific about format expected

**Example:**
```markdown
**What are the THREE measures of central tendency?**

1. ____________
2. ____________
3. ____________

[Answer: Mean, Median, Mode - from lecture slide 15]
```

---

### Code Analysis Questions
**Best for:**
- Understanding what code does
- Identifying errors
- Predicting output

**Tips:**
- Use code snippets from actual labs
- Reference specific datasets they used
- Test common operations they practiced

**Example:**
```markdown
**What does this code do?**

```python
df[df['Year'] == 2014]
```

[Based on actual example from Lab 2 with Salaries dataset]
```

---

### Scenario/Application Questions
**Best for:**
- Decision-making skills
- Applying concepts to new situations
- Critical thinking

**Tips:**
- Base scenarios on lecture examples
- Use realistic data problems
- Test trade-offs discussed in class

**Example:**
```markdown
**You have a dataset with 40% missing values in the 'phone' column. What strategy would you use and why?**

[Tests decision-making from lecture on missing data strategies]
```

---

## Point Allocation Guidelines

### Easy Questions (2-3 points):
- Simple recall
- Single-step operations
- Basic definitions

**Example**: "What does `.head()` return?"

### Medium Questions (4-5 points):
- Understanding concepts
- Multi-step reasoning
- Comparing/contrasting

**Example**: "What's the difference between `.info()` and `.describe()`?"

### Hard Questions (6-10 points):
- Application to new scenarios
- Combining multiple concepts
- Writing code
- Explaining reasoning

**Example**: "Given dataset X with problems Y and Z, write code to clean and analyze it"

---

## Quality Checks

Before finalizing quiz:

### Content Alignment ✅
- [ ] Every question based on actual material (not assumptions)
- [ ] Questions distributed across all major topics
- [ ] No questions on content NOT covered
- [ ] Examples reference actual datasets/scenarios from course

### Difficulty Balance ✅
- [ ] Mix of easy (30%), medium (50%), hard (20%) questions
- [ ] Early questions build confidence
- [ ] Harder questions test deeper understanding
- [ ] No "trick questions" - test understanding, not memory

### Answer Quality ✅
- [ ] All answers include explanations
- [ ] Explanations reference source material
- [ ] Common misconceptions addressed
- [ ] Examples provided where helpful

### Technical Accuracy ✅
- [ ] All code examples are valid and tested
- [ ] Terminology matches course materials
- [ ] Formulas are correct
- [ ] No ambiguous questions

---

## Common Mistakes to Avoid

### ❌ DON'T:
1. **Create questions based on what "should" be covered**
   - Quiz what WAS taught, not what you think should be taught

2. **Use generic examples**
   - Use the ACTUAL datasets/examples from labs (Salaries.csv, Pokemon.csv, etc.)

3. **Test obscure details**
   - Focus on concepts emphasized in lecture, not footnotes

4. **Write trick questions**
   - Goal is assessment, not confusion

5. **Ignore the lab notebooks**
   - Labs show what students actually practiced - test those skills!

6. **Make assumptions about depth**
   - If lecture only briefly mentioned something, don't make it a major quiz section

### ✅ DO:
1. **Reference specific examples from materials**
   - "From the Salaries dataset in Lab 2..."
   - "As shown in Lecture slide 15..."

2. **Test what they practiced**
   - If they did it in lab, test it in the quiz

3. **Include real-world decision-making**
   - "When would you use X vs Y?" (if covered in lecture)

4. **Provide learning in the answers**
   - Answers should teach, not just validate

5. **Track back to learning objectives**
   - If lecture said "By the end of this week you'll be able to X", test X

---

## Special Considerations

### For Technical/Coding Courses:
- Include actual code from labs
- Test both understanding (what does code do?) and application (write code to do X)
- Reference specific libraries/methods taught
- Test troubleshooting skills if emphasized

### For Theoretical Courses:
- Test frameworks and categorizations
- Include definition questions
- Test application of theory to scenarios
- Compare/contrast concepts

### For Mixed Courses (theory + practice):
- Balance conceptual and practical questions
- Show connections (e.g., "How does the lecture concept of 'mean' relate to pandas `.mean()` method?")
- Test both knowledge and skills

---

## Example: Bad vs Good Question

### ❌ Bad (Generic, Not Aligned):
```markdown
**What is a DataFrame?**

- [ ] A) A 2D data structure
- [ ] B) A 1D array
- [ ] C) A dictionary
- [ ] D) A list
```
**Problem**: Generic, could be from any pandas course, doesn't reference their specific materials

### ✅ Good (Specific, Aligned):
```markdown
**In Lab 2, what was the difference between these two types?**

```python
type(salaries.TotalPay)  # What type?
type(salaries)            # What type?
```

**Problem**: Based on ACTUAL code from their lab, uses THEIR dataset, tests what they specifically learned
```

---

## File Naming Convention

```
quiz-w##-topic-name.md
```

**Examples:**
- `quiz-w02-data-handling.md`
- `quiz-w05-unsupervised-learning.md`
- `quiz-midterm-review.md`

---

## Template for New Quiz

```markdown
---
title: "Week ## Quiz — Topic Name"
module: "CS###"
tags: [module/CS###, type/quizzes, week-##]
---

# 🎯 Week ## Interactive Quiz
**Topic**: [Topic Name]
**Based on**: Lecture ##, Lab ##, Reading Materials

**Instructions**:
1. Answer without looking at materials first
2. Check answers using expandable sections
3. Track your score
4. Aim for 80%+ mastery

---

## Part 1: [Category Name] (X points)

### Question 1 (Y points)
**[Question based on actual material]**

<details>
<summary>💡 Show Answer</summary>

**Answer**: [Answer]

**From [source]**: [Reference]

</details>

---

[Continue with more questions...]

---

## 📊 Scoring Guide

**Total Points**: [Total]

- **90-100%**: Mastered
- **80-89%**: Strong understanding
- **70-79%**: Good foundation, review weak areas
- **Below 70%**: Need more study

---

## 🎯 Your Score

**Date**: ___________
**Score**: _____ / [Total] (_____%)

**Topics to Review**:
-

---

## 📚 Related Resources

- [[lecture-w##-topic]]
- [[lab-w##]]
- [[reading-list-w##]]

---

*Quiz created: [Date]*
*Based on: [Specific materials used]*
```

---

## For Future Agents

When asked to create a quiz:

1. **First, ASK**: "Do you have the lecture slides/notes, lab files, and reading list?"
2. **Then, READ**: Don't guess - read the actual materials
3. **Then, MAP**: Create a content map of what was covered
4. **Then, CREATE**: Write questions based on the map
5. **Finally, CHECK**: Verify every question traces back to actual material

**Remember**: A quiz is only as good as its alignment with what was actually taught!

---

## Success Metrics

A well-created quiz should:
- ✅ Make the student say "Yes, we covered that!"
- ✅ Reference specific examples they saw
- ✅ Test skills they practiced
- ✅ Feel fair (not trick questions)
- ✅ Teach through the answer explanations
- ✅ Build confidence (start easier, get harder)

---

## Additional Resources

### For Interactive Elements:
- Use HTML `<details>` tags for collapsible answers
- Use checkboxes `- [ ]` for multiple choice
- Use code blocks with syntax highlighting
- Include emojis for visual organization (✅ ❌ 💡 🎯)

### For Obsidian:
- Tag quizzes properly: `tags: [module/CS###, type/quizzes, week-##]`
- Link to related materials: `[[lecture-w##]]`
- Use relative links for portability

---

*This protocol was developed through creating CS982 Week 2 quiz*
*Key insight: Reading actual materials vs guessing made HUGE difference in quality!*
