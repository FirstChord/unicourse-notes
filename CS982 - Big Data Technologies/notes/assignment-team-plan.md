---
title: "Assignment Team Plan - BBC Great British Class Survey"
module: "CS982"
tags: [module/CS982, type/notes, assignment, team-work]
date: 2025-10-25
deadline: 2025-11-03 18:00
---

# CS982 Assignment Team Plan
*Collaborative work plan for BBC Great British Class Survey analysis*

🎯 **Deadline:** Monday, November 3rd, 2025 at 18:00 (9 days!)

---

## 📋 Team Work Division

Based on team discussion, we're splitting initial coding work into **3 parallel streams**:

### Stream 1: DataViz / EDA (Exploratory Data Analysis)
**Section coverage:**
- Summary statistics (20% of marks)
- Data exploration and visualization
- Problem identification support (10% of marks)

### Stream 2: Supervised Learning
**Section coverage:**
- Supervised learning method implementation (20% of marks)
- Replicating BBC's class assignments

### Stream 3: Unsupervised Learning
**Section coverage:**
- Unsupervised learning method implementation (20% of marks)
- Alternate clustering/categorization

**Timeline:** Each person has a few days to a week to generate code, charts, and statistical review for their section.

---

## 🎯 Project Aims (From Report Skeleton)

1. **Independently replicate data-driven insights** in areas already explored by BBC
2. **Derive new insights** not mentioned in BBC's reporting (with humorous twist)
3. **Apply supervised ML** to replicate class assignments from BBC's engine & self-identified class
4. **Apply unsupervised ML** to propose alternate clustering/categorization

---

## 📊 Dataset Overview

**Name:** BBC Great British Class Survey, 2011-2013
**Source:** UK Data Service (safeguarded dataset)
**Size:** 268MB unzipped, 325,712 rows × 276 columns
**Format:** STATA .dta file (load with `pd.read_stata()`)

**Key Feature Groups:**
- Demographics (categorical, integers)
- Statistical summaries (floats)
- Probability model outputs (BBC's class calculations)
- Encoded survey questions (one-hot, binary, freetext)
- Survey metadata (timestamps, etc.)

**Known Issues:**
- Wave 1 Batch 2 has demographic differences → may need to drop
- Inconsistent encoding (e.g., "2. Yes" vs "Yes") → needs cleaning
- Not a representative UK sample → restrict conclusions to respondents only

---

## 🔬 Stream 1: DataViz / EDA

### Your Objectives

1. **Data Loading & Initial Inspection**
   - Load dataset with pandas
   - Check shape, info, data types
   - Identify feature groups (raw vs derived)

2. **Data Cleaning**
   - Handle inconsistent encoding (re-encode as binary 1/0)
   - Check for NaN/nulls
   - Identify and document outliers
   - Fix categorical typos

3. **Basic Demographics Visualization**
   - Gender distribution
   - Age distribution
   - Most common professions (SOC2010 codes)
   - Education levels
   - Self-identified class vs BBC calculated class

4. **Data Quality Checks**
   - Missing data heatmap
   - Feature correlation heatmap (subset of key features)
   - Distribution plots for numerical features

5. **Summary Statistics Tables**
   - Descriptive stats (mean, median, std, quartiles) for key numeric features
   - Frequency tables for key categorical features
   - Group-by analysis (e.g., stats by class, by age group, by gender)

### Key Course Materials

📚 **Lectures:**
- [[lecture-w02-data-handling-content]] - Descriptive statistics, handling missing data
- [[lecture-w03-visualisation-content]] - Chart types, when to use what

🔬 **Labs:**
- [[lab-w02-exploring-data-content]] - Pokemon dataset exploration (similar workflow)
- [[lab-w02-solutions]] - Solutions for reference
- [[lab-w03-visualization-content]] - Creating effective visualizations
- [[lab-w03-solutions]] - Chart examples

📖 **Your Notes:**
- [[note-w02-data-handling]] - Your personal notes on data handling

### Recommended Visualizations

| Analysis | Chart Type | Purpose |
|----------|-----------|---------|
| Gender/Age distribution | Stacked bar (100% scale) | Show demographic makeup |
| Wave breakdown | Histogram | Show when survey completed |
| Profession frequencies | Horizontal bar chart | Top 10-15 professions |
| Missing data | Heatmap | Identify patterns in NaNs |
| Feature correlations | Correlation heatmap | Find related variables |
| Numeric distributions | Histograms/box plots | Check for outliers |
| Class comparison | Grouped bar chart | Self-ID vs BBC calculated |

### Deliverables for Team

**Code:**
```python
# 1. Data loading and cleaning script
# 2. EDA visualization script
# 3. Summary statistics generation
```

**Charts:**
- All visualizations saved as high-res PNG
- Each with proper titles, labels, legends
- Captions prepared for report

**Statistical Review:**
- Markdown file or notebook section documenting:
  - Key findings from descriptive stats
  - Data quality issues discovered
  - Recommendations for ML pipeline
  - Interesting patterns for "new insights" section

### Python Packages Needed
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Timeline Suggestion
- **Day 1-2:** Data loading, cleaning, initial exploration
- **Day 3-4:** Create all visualizations
- **Day 5-6:** Summary statistics and documentation
- **Day 7:** Review and polish

---

## 🎓 Stream 2: Supervised Learning

### Your Objectives

1. **Understand the Target Variable**
   - BBC's calculated class (`NEWcluwt`? - check dataset docs)
   - Self-identified class
   - Decide which to use as ground truth

2. **Feature Selection**
   - Exclude BBC's derived features (avoid circular logic)
   - Focus on raw survey responses + demographics
   - Handle categorical encoding (one-hot encoding)

3. **Data Preparation**
   - Train/test split (80/20 or 70/30)
   - Handle missing values in features
   - Scale/normalize if needed

4. **Model Selection & Training**
   - Try multiple algorithms:
     - **Logistic Regression** (multi-class)
     - **Decision Tree Classifier**
     - **Random Forest Classifier**
     - **K-Nearest Neighbors**
   - Compare performance

5. **Evaluation**
   - Accuracy, precision, recall, F1-score
   - Confusion matrix
   - Feature importance (which survey questions matter most?)

6. **Justify Choice**
   - Why did you choose the final model?
   - How does it perform vs BBC's original?
   - What does this tell us about class predictability?

### Key Course Materials

📚 **Lectures:**
- [[lecture-w04-supervised-learning-content]] - Classification algorithms, evaluation metrics

🔬 **Labs:**
- [[lab-w04-supervised-learning-content]] - Life satisfaction GDP example
- [[lab-w04-solutions]] - Implementation patterns

📊 **External Resources:**
- StatQuest: [Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8) (9 min)
- StatQuest: [Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk) (17 min)
- [Scikit-learn Classification Guide](https://scikit-learn.org/stable/supervised_learning.html)

### Recommended Approach

**Step 1: Binary Classification First (Easier)**
- Predict just 2 classes (e.g., "Working Class" vs "Middle Class")
- Get pipeline working, understand performance

**Step 2: Multi-class Classification**
- Extend to all 7-8 BBC classes
- More complex but more interesting

### Deliverables for Team

**Code:**
```python
# 1. Feature engineering script
# 2. Multiple model training scripts
# 3. Evaluation and comparison script
```

**Charts:**
- Confusion matrix heatmap
- Feature importance plot (if using tree-based methods)
- ROC curve (if applicable)
- Model comparison bar chart (accuracy across models)

**Statistical Review:**
- Which model performed best and why?
- Which features were most predictive?
- How does our model compare to BBC's original?
- Can we replicate self-identified class? (harder)

### Python Packages Needed
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

### Timeline Suggestion
- **Day 1-2:** Feature selection, data prep, train/test split
- **Day 3-4:** Train multiple models
- **Day 5-6:** Evaluation and comparison
- **Day 7:** Documentation and justification

---

## 🔍 Stream 3: Unsupervised Learning

### Your Objectives

1. **Feature Selection**
   - Exclude BBC's class variables (we want to discover patterns, not replicate)
   - Focus on raw survey responses that might reveal hidden groupings
   - Consider dimensionality reduction first (PCA)

2. **Determine Number of Clusters**
   - **Elbow method** (within-cluster sum of squares)
   - **Silhouette analysis**
   - Try different K values (3-10 clusters?)

3. **Apply Clustering Methods**
   - **K-means clustering** (most common)
   - **Hierarchical clustering** (dendrogram visualization)
   - Compare results

4. **Interpret Clusters**
   - What characterizes each cluster?
   - Profile each cluster (demographics, preferences, behaviors)
   - Do clusters align with BBC's class model? Or different?

5. **Visualization**
   - PCA 2D plot with cluster colors
   - Cluster characteristics (parallel coordinates or radar charts)
   - Comparison to BBC classes

### Key Course Materials

📚 **Lectures:**
- [[lecture-w05-unsupervised-learning-content]] - Clustering, PCA, evaluation

🔬 **Labs:**
- [[lab-w05-unsupervised-learning-content]] - Clustering examples

📊 **External Resources:**
- StatQuest: [K-means Clustering](https://www.youtube.com/watch?v=4b5d3muPQmA) (9 min)
- StatQuest: [Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo) (12 min)
- StatQuest: [PCA](https://www.youtube.com/watch?v=HMOI_lkzW08) (20 min)

### Recommended Approach

**Step 1: Dimensionality Reduction**
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # For visualization
# or keep more components for clustering
pca = PCA(n_components=0.95)  # Keep 95% variance
```

**Step 2: Determine K**
```python
from sklearn.cluster import KMeans
# Try K from 2 to 10, plot elbow curve
# Calculate silhouette scores
```

**Step 3: Cluster and Interpret**
```python
# Fit final model
# Assign cluster labels
# Profile each cluster (mean values per cluster)
```

### Deliverables for Team

**Code:**
```python
# 1. PCA/dimensionality reduction script
# 2. Elbow method and silhouette analysis
# 3. Clustering implementation
# 4. Cluster profiling and interpretation
```

**Charts:**
- Elbow curve (WCSS vs K)
- Silhouette score plot
- PCA scatter plot with cluster colors
- Cluster profiles (radar chart or heatmap)
- Dendrogram (if using hierarchical)

**Statistical Review:**
- How many clusters did you choose and why?
- What characterizes each cluster?
- How do clusters compare to BBC's 7-8 classes?
- Any surprising groupings?
- Potential names for clusters (if not class-based)

### Python Packages Needed
```python
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, silhouette_samples
from scipy.cluster.hierarchy import dendrogram, linkage
```

### Timeline Suggestion
- **Day 1-2:** Feature selection, PCA exploration
- **Day 3-4:** Determine optimal K, run clustering
- **Day 5-6:** Cluster interpretation and profiling
- **Day 7:** Documentation and comparison to supervised results

---

## 📝 Integration Phase (All Streams)

Once each stream has completed their analysis:

### Integration Meeting (Day 7-8)
1. **Share findings** - Each stream presents code, charts, insights
2. **Identify connections** - How do supervised/unsupervised results compare?
3. **Select best charts** - Which visualizations make it into the report?
4. **Draft insights** - What are our "new insights with humorous twist"?

### Report Writing (Day 8-10)
Divide writing responsibilities:
- **Background & Context** (already drafted in skeleton)
- **Dataset Introduction** (Stream 1 lead, 10%)
- **EDA & Summary Stats** (Stream 1 lead, 20%)
- **Supervised Learning** (Stream 2 lead, 20%)
- **Unsupervised Learning** (Stream 3 lead, 20%)
- **Reflection** (All contribute, 10%)
- **Structure & References** (All review, 10%)

### Word Count Target
- **Total:** 2500 words ± 10% (2250-2750)
- **Per section estimate:**
  - Background: 200 words ✓ (already drafted)
  - Dataset intro: 300 words
  - EDA/Stats: 600 words (most important, 20%)
  - Supervised: 500 words
  - Unsupervised: 500 words
  - Reflection: 300 words
  - Conclusions: 100 words

---

## 🎓 Marking Scheme Reminder

| Section | Points | What Matters |
|---------|--------|--------------|
| Problem identification | 10% | Clear rationale for why this is interesting |
| Dataset introduction | 10% | Evidence of understanding data + references |
| Summary statistics | 20% | **Clear labeled figures + written explanation** |
| Unsupervised method | 20% | Implementation + understanding + **justification** |
| Supervised method | 20% | Implementation + understanding + **justification** |
| Reflection | 10% | **Critical thinking** - strengths, weaknesses, improvements |
| Structure & refs | 10% | Professional presentation, proper citations |

**Key to high marks:**
✅ Don't just show code output - **explain what it means**
✅ **Justify method choices** - why K-means? why logistic regression?
✅ **Interpret in context** - what does this tell us about social class?
✅ Figures **in main text** with captions, not in appendix
✅ Be **critical in reflection** - what would you do differently?

---

## 📚 All Relevant Course Materials

### Lectures
- [[lecture-w01-introduction-to-python-content]] - Python/pandas basics
- [[lecture-w02-data-handling-content]] - **Essential for Stream 1**
- [[lecture-w03-visualisation-content]] - **Essential for Stream 1**
- [[lecture-w04-supervised-learning-content]] - **Essential for Stream 2**
- [[lecture-w05-unsupervised-learning-content]] - **Essential for Stream 3**

### Labs
- [[lab-w02-exploring-data-content]] & [[lab-w02-solutions]] - EDA patterns
- [[lab-w03-visualization-content]] & [[lab-w03-solutions]] - Viz examples
- [[lab-w04-supervised-learning-content]] & [[lab-w04-solutions]] - Supervised ML
- [[lab-w05-unsupervised-learning-content]] - Clustering examples

### Assignment Materials
- [[assignment-brief]] - Full requirements
- [[assignment-marking]] - Detailed rubric
- [[assignment-prep-guide]] - Full prep guide with resources
- [[assignment-faq]] - Common questions
- [[assignment-sample-distinction]] - Example A work

---

## 🚨 Common Pitfalls to Avoid

**EDA Stream:**
❌ Just dumping `.describe()` output without explanation
❌ Figures without proper labels, titles, captions
❌ Not checking data quality issues (missing values, outliers)
✅ Tell the story - what do the visualizations reveal?

**Supervised Stream:**
❌ Using BBC's derived features to predict BBC's classes (circular)
❌ No justification for method choice
❌ Only reporting accuracy (need precision, recall, confusion matrix)
✅ Explain feature importance and what it means

**Unsupervised Stream:**
❌ Choosing K randomly without justification
❌ Not interpreting what the clusters actually mean
❌ Using BBC class labels to cluster (defeats the purpose)
✅ Profile clusters and compare to supervised/BBC results

---

## 📋 Team Coordination Checklist

### Week 1 (Oct 25-27)
- [ ] All team members access dataset from UK Data Service
- [ ] Set up shared code repository (GitHub?)
- [ ] Each stream: Read relevant lectures and labs
- [ ] Stream 1: Start data loading and cleaning
- [ ] Stream 2 & 3: Wait for clean data from Stream 1

### Week 2 (Oct 28-30)
- [ ] Stream 1: Complete EDA and visualizations
- [ ] Stream 2: Train and evaluate supervised models
- [ ] Stream 3: Perform clustering and interpretation
- [ ] Daily standups: Share progress and blockers

### Final Days (Oct 31 - Nov 3)
- [ ] Nov 1: Integration meeting - share all findings
- [ ] Nov 2 AM: Draft all report sections
- [ ] Nov 2 PM: Review, combine, check word count
- [ ] Nov 3 AM: Final proofread, check figures, references
- [ ] Nov 3 2PM: Submit by 18:00 deadline

---

## 💡 Quick Tips for Success

**For Stream 1 (EDA):**
- Use seaborn for prettier plots than matplotlib
- Save figures at 300 DPI for report quality
- Create reusable plotting functions
- Document data cleaning decisions

**For Stream 2 (Supervised):**
- Start simple (binary classification) then expand
- Use cross-validation for robust evaluation
- Feature engineering might be key (age groups, income brackets)
- Compare to baseline (what if we just predicted most common class?)

**For Stream 3 (Unsupervised):**
- PCA for visualization AND for reducing features before clustering
- Try different distance metrics in K-means
- Hierarchical clustering gives you the dendrogram (great viz!)
- Name your clusters based on characteristics

**For Everyone:**
- Comment your code thoroughly
- Use descriptive variable names
- Create functions for repeated tasks
- Version control everything
- Share code frequently

---

## 🔗 Dataset Links

**Dataset Access:** https://datacatalogue.ukdataservice.ac.uk/studies/study/7616
**BBC Article:** https://www.bbc.co.uk/news/magazine-34766169
**University of Strathclyde** is a corporate subscriber - access via institutional login

**Supporting Documentation Included:**
- `7616_methodology_and_technical_notes.pdf`
- `7616_questionnaire.pdf`
- Data dictionary explaining all 276 features

---

## 📞 Team Communication

**Questions during your stream?**
- Post in team chat
- Tag relevant person if blocking
- Don't wait until last minute!

**Stuck on technical implementation?**
- Check relevant lab solutions
- Review lecture code examples
- Ask Claude for specific help
- StatQuest videos are excellent

**Can't meet your timeline?**
- Communicate early!
- Team can help or redistribute work
- Better to ask for help than deliver incomplete work

---

**Remember:** We're aiming for distinction level work. That means:
- **Technical excellence** - Code works, methods appropriate
- **Clear communication** - Explain everything in plain English
- **Critical thinking** - Reflect honestly on limitations
- **Professional presentation** - Looks like a real data science report

**You've got this!** 🚀

---

*Created: 2025-10-25*
*Based on: Assignment brief, marking scheme, team discussion, and report skeleton*
