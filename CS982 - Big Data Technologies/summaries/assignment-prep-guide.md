---
title: "Assignment Preparation Guide"
module: "CS982"
tags: [module/CS982, type/summaries, assignment-prep]
date: 2025-10-23
deadline: 2025-11-03 18:00
---

# CS982 Assignment Preparation Guide
*Complete prep guide with lectures, labs, and resources*

🎯 **Deadline:** Monday, November 3rd, 2025 at 18:00 (11 days!)

---

## 📋 Assignment Overview

### Part I: Create (70% of grade)
**Deliverables:**
- Report: 2500 words (+/- 10%) as PDF
- Code: All analysis code submitted

**Task:** Analyze an open dataset and write a data science report

**Key Sections:**
1. Problem identification (10%)
2. Dataset introduction (10%)
3. Summary statistics with figures (20%)
4. ONE unsupervised learning method (20%)
5. ONE supervised learning method (20%)
6. Reflection on methods (10%)
7. Structure & references (10%)

### Part II: Evaluate (30% of grade)
**Task:** Self-assess Part I and justify your mark
- Give Part I a mark (0-100)
- Write 1000-word justification
- Your mark depends on how close you are to marker's grade

---

## 🎓 Critical Lectures to Master

### ⭐ Week 2: Data Handling (ESSENTIAL - 20% of marks)
**File:** [[lecture-w02-data-handling-content]]

**Why Critical:**
- Summary statistics section is 20% of marks
- Need to understand: mean, median, mode, std dev, IQR
- Data cleaning and handling missing values
- Pandas fundamentals

**Key Topics to Review:**
- Descriptive statistics (measures of central tendency)
- Measures of dispersion/variation
- Data transformations
- Handling missing data strategies
- Using `.describe()`, `.groupby()`, `.agg()`

**Review Time:** 30-45 min

---

### ⭐ Week 3: Visualization (ESSENTIAL - part of 20%)
**File:** [[lecture-w03-visualization-content]]

**Why Critical:**
- "Summary statistics including figures" means you MUST visualize
- Good figures = better marks in that 20% section
- Proper labeling, captions, legends matter for structure marks

**Key Topics to Review:**
- Choosing right chart type (bar, histogram, scatter, box plot)
- When to use each visualization
- matplotlib and seaborn basics
- Figure labeling and captions
- Presenting data clearly

**Review Time:** 30-45 min

---

### ⭐ Week 4: Supervised Learning (ESSENTIAL - 20% of marks)
**File:** [[lecture-w04-supervised-learning-content]]

**Why Critical:**
- Must implement ONE supervised method (20% of marks)
- Need to justify your choice
- Must explain results clearly
- Common choices: Linear regression, Logistic regression, Decision trees

**Key Topics to Review:**
- Difference between classification and regression
- How each algorithm works
- When to use which method
- Model evaluation metrics (accuracy, precision, recall, R², MSE)
- Train/test split
- Overfitting vs underfitting

**Review Time:** 45-60 min

---

### ⭐ Week 5: Unsupervised Learning (ESSENTIAL - 20% of marks)
**File:** [[lecture-w05-unsupervised-learning-content]]

**Why Critical:**
- Must implement ONE unsupervised method (20% of marks)
- Must justify why you chose it
- Common choices: K-means clustering, Hierarchical clustering, PCA

**Key Topics to Review:**
- Clustering algorithms (K-means, hierarchical)
- How to choose K (elbow method)
- Dimensionality reduction (PCA)
- When to use each method
- Evaluating clustering (silhouette score, within-cluster sum of squares)
- Interpreting results

**Review Time:** 45-60 min

---

### 💡 Week 1: Python Intro (Foundation)
**File:** [[lecture-w01-python-intro-content]]

**Why Helpful:**
- Review if Python skills rusty
- NumPy basics
- Data structures

**Review Time:** 20 min (if needed)

---

## 🔬 Critical Labs to Practice

### ⭐ Lab 2: Exploring Data (ESSENTIAL)
**Files:**
- [[lab-w02-exploring-data-content]] - Instructions
- [[lab-w02-solutions]] - Solutions

**Why Critical:**
- Direct practice for summary statistics section
- Pokemon dataset manipulation
- Handling missing data
- Grouping and aggregation

**What to Practice:**
- Loading datasets with pandas
- Using `.describe()`, `.info()`, `.shape`
- Handling missing values (`.dropna()`, `.fillna()`)
- Creating new columns
- Grouping data (`.groupby()`)
- Calculating statistics by group

**Time:** 60-90 min

---

### ⭐ Lab 3: Visualization (ESSENTIAL)
**Files:**
- [[lab-w03-visualization-content]] - Instructions
- [[lab-w03-solutions]] - Solutions

**Why Critical:**
- Direct practice for figures in report
- Multiple chart types covered
- Proper labeling techniques

**What to Practice:**
- Bar charts, histograms, scatter plots
- Box plots for showing distributions
- Heatmaps for correlations
- Adding titles, labels, legends
- Saving figures with good resolution

**Time:** 60-90 min

---

### ⭐ Lab 4: Supervised Learning (ESSENTIAL)
**Files:**
- [[lab-w04-supervised-learning-content]] - Instructions
- [[lab-w04-solutions]] - Solutions

**Why Critical:**
- Practice implementing supervised methods
- Model evaluation techniques
- Life satisfaction GDP dataset example

**What to Practice:**
- Train/test split
- Fitting models (LinearRegression, LogisticRegression)
- Making predictions
- Evaluating with metrics
- Visualizing model performance

**Time:** 90-120 min

---

### ⭐ Lab 5: Unsupervised Learning (ESSENTIAL)
**Files:**
- [[lab-w05-unsupervised-learning-content]] - Instructions

**Why Critical:**
- Practice clustering algorithms
- Choosing number of clusters
- Interpreting results

**What to Practice:**
- K-means clustering
- Hierarchical clustering
- Elbow method for K selection
- Visualizing clusters
- Silhouette analysis

**Time:** 90-120 min

---

## 📺 External Resources & Videos

### Data Exploration & Statistics

**StatQuest: Descriptive Statistics**
- [Mean, Median and Mode](https://www.youtube.com/watch?v=h8EYEJ32oQ8) (5 min)
- Clear explanation of central tendency measures

**StatQuest: Variance and Standard Deviation**
- [Variance and Standard Deviation Explained](https://www.youtube.com/watch?v=E4HAYd0QnRc) (8 min)
- Visual explanation of dispersion

**Pandas Documentation**
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- Quick reference guide

---

### Data Visualization

**Matplotlib Tutorial**
- [Matplotlib Tutorial for Beginners](https://www.youtube.com/watch?v=UO98lJQ3QGI) (32 min)
- Comprehensive matplotlib basics
- Chart types covered

**Seaborn for Data Science**
- [Seaborn Tutorial](https://www.youtube.com/watch?v=6GUZXDef2U0) (30 min)
- Better-looking plots than matplotlib
- Statistical visualizations

**Choosing the Right Chart**
- [Data Viz Catalog](https://datavizcatalogue.com/)
- When to use which chart type
- Interactive examples

---

### Supervised Learning

**StatQuest: Machine Learning Fundamentals**
- [Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo) (27 min)
- Clear mathematical explanation
- Great for understanding the method

**StatQuest: Logistic Regression**
- [Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8) (9 min)
- When and why to use it
- Interpretation of results

**StatQuest: Decision Trees**
- [Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk) (17 min)
- How they work visually
- Advantages and disadvantages

**Scikit-learn Documentation**
- [Supervised Learning Guide](https://scikit-learn.org/stable/supervised_learning.html)
- Code examples for all methods
- Parameter explanations

---

### Unsupervised Learning

**StatQuest: K-means Clustering**
- [K-means Clustering](https://www.youtube.com/watch?v=4b5d3muPQmA) (9 min)
- Visual explanation
- How to choose K

**StatQuest: Hierarchical Clustering**
- [Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo) (12 min)
- Dendrograms explained
- Comparison with K-means

**StatQuest: Principal Component Analysis (PCA)**
- [PCA Main Ideas](https://www.youtube.com/watch?v=HMOI_lkzW08) (20 min)
- Dimensionality reduction
- When to use it

**Scikit-learn Clustering**
- [Clustering Documentation](https://scikit-learn.org/stable/modules/clustering.html)
- All clustering algorithms
- Evaluation metrics

---

### Academic Writing for Data Science

**How to Write a Data Science Report**
- [Writing Data Science Reports](https://www.youtube.com/watch?v=VqKq78PVO9g) (15 min)
- Structure and flow
- Common mistakes

**Citing Data Sources**
- [How to Cite Datasets](https://guides.lib.berkeley.edu/c.php?g=652630&p=4575532)
- Proper citation format
- Dataset DOIs

---

## 📊 Recommended Study Plan

### Week 1 (Oct 23-27) - Foundation Review

**Day 1-2: Data Handling & Visualization**
- [ ] Review Lecture W02 (data handling) - 45 min
- [ ] Review Lecture W03 (visualization) - 45 min
- [ ] Watch StatQuest videos on statistics - 30 min
- [ ] Redo Lab 2 exercises - 90 min

**Day 3-4: Visualization Practice**
- [ ] Watch Seaborn tutorial - 30 min
- [ ] Redo Lab 3 exercises - 90 min
- [ ] Practice creating different chart types - 60 min
- [ ] Find interesting datasets on Kaggle - 30 min

**Day 5: Choose Dataset**
- [ ] Browse UCI ML Repository and Kaggle - 60 min
- [ ] Verify dataset ISN'T on banned list
- [ ] Download and explore dataset - 60 min
- [ ] Identify 2-3 interesting questions - 30 min

---

### Week 2 (Oct 28-Nov 1) - Machine Learning

**Day 6-7: Supervised Learning**
- [ ] Review Lecture W04 (supervised) - 60 min
- [ ] Watch StatQuest supervised videos - 45 min
- [ ] Redo Lab 4 exercises - 120 min
- [ ] Try 2-3 methods on your dataset - 90 min
- [ ] Choose best method for your report - 30 min

**Day 8-9: Unsupervised Learning**
- [ ] Review Lecture W05 (unsupervised) - 60 min
- [ ] Watch StatQuest clustering videos - 30 min
- [ ] Redo Lab 5 exercises - 120 min
- [ ] Try clustering on your dataset - 90 min
- [ ] Analyze and interpret results - 60 min

**Day 10: Write Report**
- [ ] Problem identification section - 60 min
- [ ] Dataset introduction section - 60 min
- [ ] Summary statistics section - 120 min
- [ ] Unsupervised method section - 120 min

**Day 11: Finish & Polish**
- [ ] Supervised method section - 120 min
- [ ] Reflection section - 60 min
- [ ] Add references and format - 60 min
- [ ] Proofread and check word count - 30 min
- [ ] Prepare code submission - 30 min
- [ ] Part II self-evaluation - 60 min
- [ ] **SUBMIT by 18:00!**

---

## ✅ Pre-Submission Checklist

### Part I: Report

**Content:**
- [ ] Problem/challenge clearly identified and explained
- [ ] Dataset introduced with references
- [ ] Summary statistics calculated and explained
- [ ] At least 3-5 figures/tables with proper labels
- [ ] ONE unsupervised method implemented and explained
- [ ] ONE supervised method implemented and explained
- [ ] Results interpreted in context
- [ ] Reflection on methods (strengths, weaknesses, improvements)
- [ ] Proper citations throughout

**Format:**
- [ ] 2250-2750 words (2500 +/- 10%)
- [ ] PDF format
- [ ] Front cover, table of contents
- [ ] List of figures/tables
- [ ] All figures have captions and labels
- [ ] References section at end
- [ ] Page numbers

**Code:**
- [ ] All code files included
- [ ] Code is commented
- [ ] Code runs without errors
- [ ] Dataset path is relative or documented
- [ ] Requirements.txt or environment info included

---

### Part II: Self-Evaluation

- [ ] Registration number in Cell A3
- [ ] Mark (0-100) in Cell A7
- [ ] Justification (max 1000 words) in Cell A11
- [ ] Justification references marking scheme
- [ ] Justification is detailed and specific
- [ ] Used templateEvaluation.xlsx (don't change format)
- [ ] File saved as .xlsx

---

## 🚨 Common Mistakes to Avoid

### Dataset Selection
❌ Using banned datasets (Iris, Titanic, Wine, etc.)
❌ Using datasets from course labs/lectures
✅ Find unique dataset on Kaggle or UCI ML Repository

### Analysis Depth
❌ Just showing code output without explanation
❌ Tables/figures in appendix instead of main text
❌ No rationale for method chosen
✅ Clear explanation of WHY you chose each method
✅ Interpret results in context of your question
✅ Justify metrics used

### Writing Style
❌ Too technical with no plain English explanation
❌ Too casual/informal
❌ No references
✅ Balance technical accuracy with clarity
✅ Academic tone but readable
✅ Cite data sources and methods

### Reflection Section
❌ "Everything worked great, no issues"
❌ Too brief (2-3 sentences)
✅ Honest evaluation of limitations
✅ Specific suggestions for improvements
✅ Show critical thinking

---

## 🎯 Quick Reference: Point Distribution

| Section | Points | What It Tests |
|---------|--------|---------------|
| Problem identification | 10% | Can you identify interesting question? |
| Dataset introduction | 10% | Do you understand your data? |
| Summary statistics | 20% | Can you explore data properly? |
| Unsupervised method | 20% | Can you apply clustering/PCA? |
| Supervised method | 20% | Can you build predictive model? |
| Reflection | 10% | Critical thinking ability |
| Structure & refs | 10% | Professional presentation |

**Total Part I:** 70% of coursework
**Part II (Self-eval):** 30% of coursework

---

## 💬 Questions? Ask Claude!

**During prep:**
- "Explain K-means clustering for my assignment"
- "What's the difference between classification and regression?"
- "Help me choose between method A and method B for my dataset"

**During writing:**
- "Review my problem statement"
- "Is my reflection section critical enough?"
- "Check if I'm explaining my visualizations clearly"

**Before submission:**
- "Check my report against the marking scheme"
- "Help me estimate a mark for Part II"
- "Review my Part II justification"

---

## 📚 Related Files

- [[assignment-brief]] - Full assignment requirements
- [[assignment-marking]] - Detailed marking rubric
- [[assignment-faq]] - Common questions answered
- [[assignment-guidelines]] - Report formatting rules
- [[assignment-sample-distinction]] - Example distinction work
- [[assignment-sample-merit]] - Example merit work
- [[assignment-sample-pass]] - Example pass work

---

## 🎓 Final Tips for Success

1. **Start with a good dataset** - Interesting question > Complex dataset
2. **Understand before implementing** - Watch videos, read lectures
3. **Explain everything** - Code + explanation = marks
4. **Justify choices** - WHY this method? WHY these metrics?
5. **Visualize well** - Clear, labeled figures make huge difference
6. **Be honest in reflection** - Show critical thinking
7. **Proofread** - Structure and references are 10% of marks!
8. **Don't panic** - You have all the knowledge from labs

---

**Total Estimated Prep Time:** 20-25 hours (spread over 11 days = 2-3 hrs/day)

**You've got this!** 🚀

*Created: 2025-10-23*
*Based on assignment brief, marking scheme, and course content*
