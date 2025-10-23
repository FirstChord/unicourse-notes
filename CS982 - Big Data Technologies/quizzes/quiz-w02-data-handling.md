---
title: "Week 02 Quiz — Data Handling & Pandas (UPDATED)"
module: "CS982"
tags: [module/CS982, type/quizzes, week-02]
---

# 🎯 Week 02 Interactive Quiz
**Topic**: Data Handling & Pandas
**Based on**: Lecture 2, Lab 2 Notebooks, and Reading Materials

**Instructions**:
1. Answer each question without looking at materials first
2. Check answers using the expandable sections
3. Keep track of your score
4. Aim for 80%+ mastery!

---

## Part 1: Concepts from Lecture (30 points)

### Question 1 (3 points)
**According to the lecture, what is the difference between Data, Information, and Knowledge?**

Write your answer:
- Data is plural of datum and is use to descibe unalysed un organisef information, groups of data points are called datasets
- information is data that has been anaylsed and can be used to explore useful patternes
- Knowledge is like human wisdom..so for example we know bananas are sweet, things like this can be used like heuristics to guide data anaylsis


<details>
<summary>💡 Show Answer</summary>

**Answer**:
- **Data**: Raw, unanalyzed, unorganized material from observations and sensors
- **Information**: Data that has been processed, analyzed, and structured in a meaningful way; represents patterns recognized from data
- **Knowledge**: Understanding that comes from experience and intuition; makes sense of information within context

**The hierarchy**: Data → Information → Knowledge → Wisdom

**Example from lecture**:
- Knowledge: Knowing a tomato is a fruit
- Wisdom: Knowing not to put tomato in a fruit salad 🍅

</details>

---

### Question 2 (3 points)
**What are the TWO types of quantitative data mentioned in the lecture?**

- [x] A) Discrete and Continuous
- [ ] B) Qualitative and Quantitative
- [ ] C) Structured and Unstructured
- [ ] D) Primary and Secondary

<details>
<summary>💡 Show Answer</summary>

**Answer: A) Discrete and Continuous**

- **Discrete data**: A count that can't be made more precise
  - Example: 49/100 people contracted the disease (you can't have 49.5 people)

- **Continuous data** (Measurements): Can be measured to any precision
  - Example: Blood glucose level was 4.91 (could be 4.912, 4.9123, etc.)

</details>

---

### Question 3 (4 points)
**Calculate the Mean, Median, and Mode for this dataset:**
`[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12]`

Write your answers:
- Mean: 14______
- Median: 12______
- Mode: 12______

<details>
<summary>💡 Show Answer</summary>

**Answers**:
- **Mean**: 14
  - Sum = 12+14+11+12+12+12+15+17+22+15+12 = 154
  - Count = 11
  - Mean = 154 ÷ 11 = 14

- **Median**: 12
  - Sorted: [11, 12, 12, 12, 12, **12**, 14, 15, 15, 17, 22]
  - Middle value (position 6 of 11) = 12

- **Mode**: 12
  - 12 appears 5 times (most frequent)

*This example is from the lecture slides!*

</details>

---

### Question 4 (3 points)
**What are the THREE measures of central tendency?**

1. range
2. median
3. mean

<details>
<summary>💡 Show Answer</summary>

**Answer**:
1. **Mean** - arithmetic average
2. **Median** - middle value when sorted
3. **Mode** - most frequent value

**When to use each**:
- Mean: Good for normally distributed data without outliers
- Median: Better when you have outliers or skewed data
- Mode: Useful for categorical data or finding most common value

</details>

---

### Question 5 (4 points)
**The lecture showed two datasets with the same Mean (15), Median (15), and Mode (15):**

Dataset 1: `10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20`
Dataset 2: `1, 10, 11, 12, 13, 14, 15, 15, 15, 15, 16, 17, 18, 19, 20, 29`

**Why do these datasets feel different even though they have identical central tendency measures? What additional measure would reveal the difference?**

Write your answer:
-they have different a wider variance, so would find out the standard deviation 

<details>
<summary>💡 Show Answer</summary>

**Answer**: The datasets have different **spread/dispersion/variation**.

**The measure that reveals this**: **Standard Deviation** (or Variance, or Range)

- Dataset 1: More tightly clustered around 15 (lower standard deviation)
- Dataset 2: More spread out with outliers (1 and 29) giving higher standard deviation

**Key lesson**: Central tendency alone doesn't tell the whole story - you need measures of dispersion too!

**Measures of Dispersion** (from lecture):
- Standard Deviation
- Variance
- Range
- Interquartile Range (IQR)

</details>

---

### Question 6 (3 points)
**According to the lecture, what are the THREE basic options for handling missing data?**

1.  Missing it out
2. using the mean for the missing data 
3. _using a different number 

<details>
<summary>💡 Show Answer</summary>

**Answer** (from lecture slide):
1. **(Re)collect** the missing parts
2. **Drop** (feature or observation)
3. **Replace** it with a meaningful value

**Additional context from lecture**:
- For **categorical** variables: Create a new "missing" category
- For **numerical** variables (if random): Replace with mean (data imputation)
- For **numerical** variables (if not random): Separate into categories or replace with zeros

</details>

---

### Question 7 (3 points)
**What does IQR stand for and what does it measure?**

Write your answer:
- interquartile range 

<details>
<summary>💡 Show Answer</summary>

**Answer**: **Interquartile Range**

**What it measures**: The difference between the upper quartile (Q3) and lower quartile (Q1)

**Formula**: IQR = Q3 - Q1

**What it tells us**: The range containing the middle 50% of the data (cuts off the top 25% and bottom 25%)

**From the lecture**:
- Q1 (First quartile) = 25th percentile
- Q2 (Second quartile) = Median = 50th percentile
- Q3 (Third quartile) = 75th percentile

</details>

---

### Question 8 (4 points)
**The lecture emphasized "It is tempting to start modelling when doing data analysis – avoid this!!"**

**Why is exploring data important before modeling? List at least 3 reasons from the lecture.**

Write your answers:
1. the data might be missing important information
2. there might be high variance and edge cases that need to be standardised or normalised 
3. it might have one category that is too dominant and skews the results

<details>
<summary>💡 Show Answer</summary>

**Answer** (from lecture):

1. **Gain insight into the data** - helps decide what analysis methods are appropriate
2. **Identify missing data** - datasets are rarely perfect
3. **Identify corrupt data** - data quality issues
4. **Identify invalid data** - outliers, errors, inconsistencies

**Tools for exploration** (from lecture):
- Summary statistics (describe, mean, median, etc.)
- Visualization (covered in Week 3)

**Key point**: Understand your data BEFORE you try to model it!

</details>

---

### Question 9 (3 points)
**Match the measure to its definition:**

1. Count: this is simply observing and counting all the bits of data
2. Percent: observe how many times something happens in comparison to something else
3. Frequency: observing how often something happens

Options:
- A) Proportion of total expressed as a percentage
- B) Total number of times a value occurs
- C) Can refer to either raw count or relative occurrence

<details>
<summary>💡 Show Answer</summary>

**Answers**:
1. Count: **B)** Total number of times a value occurs
2. Percent: **A)** Proportion of total expressed as a percentage
3. Frequency: **C)** Can refer to either raw count or relative occurrence

**Example from lecture** (ice cream flavors):
- Chocolate: Count = 12, Percent = 24%
- Vanilla: Count = 20, Percent = 40%
- Strawberry: Count = 18, Percent = 36%

</details>

---

## Part 2: Pandas Operations from Lab (40 points)

### Question 10 (3 points)
**What does this code do?**

```python
salaries = pd.read_csv("Salaries.csv", low_memory=False)
```

- [ ] A) Writes data to a CSV file
- [x] B) Reads a CSV file into a pandas DataFrame
- [ ] C) Converts a DataFrame to CSV format
- [ ] D) Loads data with high memory usage

<details>
<summary>💡 Show Answer</summary>

**Answer: B) Reads a CSV file into a pandas DataFrame**

**Key points from lab**:
- `pd.read_csv()` is the method to read CSV files
- Files must be in the same folder as the notebook (or provide full path)
- `low_memory=False` helps with large datasets
- Result is stored in a DataFrame called `salaries`

</details>

---

### Question 11 (4 points)
**What is the difference between these two commands?**

```python
# Option A
salaries.head(5)

# Option B
salaries.tail(3)
```

Write your answer:
- The head will return the top 5 rows of the dataset. The tail witll show the bottom 3 


<details>
<summary>💡 Show Answer</summary>

**Answer**:
- **`.head(5)`**: Returns the **first 5 rows** of the dataset
- **`.tail(3)`**: Returns the **last 3 rows** of the dataset

**From the lab**: These are useful for quickly inspecting data at the beginning and end.

**Bonus**: `.head()` without a number defaults to 5 rows!

</details>

---

### Question 12 (4 points)
**What information does `salaries.shape` return? Give an example.**

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**: Returns a tuple of **(rows, columns)**

**Example from lab**:
```python
salaries.shape
# Output: (148654, 13)
```

Means: 148,654 rows (instances) and 13 columns (features)

**Usage**:
- `df.shape[0]` - get number of rows
- `df.shape[1]` - get number of columns

</details>

---

### Question 13 (5 points)
**What's the difference between `.info()` and `.describe()`?**

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**:

**`.info()`**:
- Shows **data types** of each column
- Shows **non-null counts** (identifies missing data)
- Shows **memory usage**
- Good for understanding **structure** and **data quality**

**`.describe()`**:
- Shows **descriptive statistics** (count, mean, std, min, 25%, 50%, 75%, max)
- Only works on **numeric columns**
- Good for understanding **distribution** and **spread** of data

**From lab**: Both were demonstrated on the Salaries dataset!

</details>

---

### Question 14 (4 points)
**What is the difference between a Series and a DataFrame?**

```python
type(salaries.TotalPay)        # What type?
type(salaries)                  # What type?
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**:

```python
type(salaries.TotalPay)   # pandas.core.series.Series
type(salaries)            # pandas.core.frame.DataFrame
```

**Difference**:
- **Series**: 1-dimensional labeled array (like a single column)
- **DataFrame**: 2-dimensional labeled table (like a spreadsheet with multiple columns)

**From the lab**: When you select ONE column, you get a Series. When you select multiple columns (or the whole dataset), you get a DataFrame.

</details>

---

### Question 15 (5 points)
**Explain what this code does:**

```python
Salaries_2014 = salaries[salaries.Year == 2014]
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**: Creates a **filtered subdataset** containing only rows where Year equals 2014.

**Breakdown**:
1. `salaries.Year == 2014` - Creates a Boolean Series (True/False for each row)
2. `salaries[...]` - Filters the DataFrame using that Boolean mask
3. Result: New DataFrame with only 2014 records

**From the lab**: This is called **Boolean indexing** or **filtering**.

**Usage in lab**:
```python
Salaries_2014 = salaries[salaries.Year == 2014]
print(Salaries_2014.TotalPay.mean())  # Mean salary for 2014
```

</details>

---

### Question 16 (4 points)
**What does `.loc[:, "JobTitle":"TotalPayBenefits"]` do?**

- [ ] A) Selects all rows and specific columns from JobTitle to TotalPayBenefits
- [ ] B) Selects specific rows and all columns
- [ ] C) Selects only the JobTitle and TotalPayBenefits columns
- [ ] D) Filters rows based on JobTitle

<details>
<summary>💡 Show Answer</summary>

**Answer: A) Selects all rows and specific columns from JobTitle to TotalPayBenefits**

**Syntax breakdown**:
- `.loc[rows, columns]`
- `:` means "all rows"
- `"JobTitle":"TotalPayBenefits"` means columns from JobTitle through TotalPayBenefits (inclusive)

**From lab**:
```python
subDataset = salaries.loc[:, "JobTitle":"TotalPayBenefits"]
```
This created a subdataset with selected columns for further analysis.

</details>

---

### Question 17 (5 points)
**What does this code do?**

```python
role = salaries.groupby("JobTitle")
role.mean()
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**: **Groups data by JobTitle** and calculates the **mean of each group**.

**Step-by-step**:
1. `.groupby("JobTitle")` - Groups all rows with the same job title together
2. `.mean()` - Calculates the average for each numeric column within each group

**Result**: Shows average salary (and other numeric fields) for each job title.

**From the lab**: GroupBy is powerful for aggregating data by categories!

**Additional operations from lab**:
```python
role.TotalPay.describe()  # Describe just TotalPay by group
role.TotalPay.agg(["mean", "min", "max", "median"])  # Multiple aggregations
```

</details>

---

### Question 18 (3 points)
**What does `.sort_values()` do?**

```python
Salaries_2014.TotalPay.sort_values()
Salaries_2014.TotalPay.sort_values(ascending=False)
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer**: Sorts values in a Series or DataFrame.

**From the lab**:
- `sort_values()` - Sorts in **ascending order** (default, lowest to highest)
- `sort_values(ascending=False)` - Sorts in **descending order** (highest to lowest)

**Example**: Sort salaries to find highest/lowest paid employees.

</details>

---

## Part 3: Missing Data (20 points)

### Question 19 (5 points)
**What's the difference between these three missing data checks?**

```python
# Option A
Salaries_2014.isnull()

# Option B
Salaries_2014.isnull().any()

# Option C
Salaries_2014.isnull().any().any()
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer** (from lab):

**A) `.isnull()`**:
- Returns a Boolean DataFrame (True/False for EACH value)
- Shows exactly which cells have missing data
- Very detailed but can be overwhelming for large datasets

**B) `.isnull().any()`**:
- Returns a Boolean Series (one True/False for EACH COLUMN)
- Tells you which columns have at least one missing value
- **Most commonly used** for quick column-level check

**C) `.isnull().any().any()`**:
- Returns a single Boolean (True/False for ENTIRE dataset)
- Tells you if there are ANY missing values anywhere
- Quick yes/no check

**Better alternative for counting**:
```python
Salaries_2014.isnull().sum()  # Count missing values per column
```

</details>

---

### Question 20 (5 points)
**What's the difference between `.drop()` and `.dropna()`?**

```python
# Option A
Salaries_2014 = Salaries_2014.drop("Notes", axis=1)

# Option B
Salaries_2014 = Salaries_2014.dropna()
```

Write your answer:
-

<details>
<summary>💡 Show Answer</summary>

**Answer** (from lab):

**`.drop("Notes", axis=1)`**:
- **Drops a specific column** by name
- `axis=1` means "drop column" (axis=0 would drop rows)
- Use when a feature is not useful or contains only null values

**`.dropna()`**:
- **Drops all rows** that contain ANY missing values
- Default behavior: drop rows with any NaN
- Can specify `how='all'` to only drop if ALL values are NaN
- Can specify `axis=1` to drop columns instead

**From the lab**: The "Notes" column was dropped because it had only null values!

</details>

---

### Question 21 (5 points)
**In the lab, the "Notes" column had 0 non-null values (all missing). The "Status" column had 38,119 non-null out of 148,654 total (74% missing).**

**What strategy would you use for each? Explain your reasoning.**

Write your answer:
- Notes column:
- Status column:

<details>
<summary>💡 Show Answer</summary>

**Sample Answer**:

**Notes column (100% missing)**:
- **Strategy**: Drop the entire column
- **Reasoning**: No data at all = no value. Keeping it wastes memory and might cause errors in analysis.
- **From lab**: `df.drop("Notes", axis=1)`

**Status column (74% missing)**:
- **Strategy**: Keep the column but don't drop rows. Consider:
  1. Create "Unknown" category for missing values
  2. Create a boolean feature `has_status = df['Status'].notnull()`
  3. Investigate WHY 74% is missing (part-time vs full-time employees?)

- **Reasoning**: 74% missing is too much to drop rows (you'd lose most of your data!). The presence/absence of status might itself be meaningful information.

**Key principle**: Never blindly drop missing data - understand the context first!

</details>

---

### Question 22 (5 points)
**According to the lecture, when should you use MEAN imputation for missing numerical data? When should you NOT?**

Write your answer:
- When to use:
- When NOT to use:

<details>
<summary>💡 Show Answer</summary>

**Answer** (from lecture):

**When to use mean imputation**:
- When values are **missing randomly** (MCAR - Missing Completely At Random)
- Assumes missing data are distributed similarly to observed data
- Will be "correct on average"

**When NOT to use**:
- When data is **not missing randomly** (systematic pattern)
- When you have outliers (mean will be skewed)
- When the data is skewed (median might be better)

**Alternatives if not random** (from lecture):
1. Separate into categories (ranges) and treat as categorical variable
2. Replace with zeros and add a tracking variable
3. Use more sophisticated imputation (e.g., based on related features)

**From lecture**: "Could be improved if we know how this is related to other data"

</details>

---

## Part 4: Applied Thinking (10 points)

### Question 23 (10 points)
**Real Scenario from Lab:**

The Salaries dataset has 148,654 employees across 4 years (2011-2014). You want to analyze 2014 salaries.

**Your tasks**:
1. Filter for 2014 only
2. Remove rows with missing salary data
3. Find the top 5 highest-paid job titles (by average TotalPay)
4. Compare police vs fire department salaries

**Write the pandas code to accomplish this (at least steps 1-3):**

```python
# Your code here



```

<details>
<summary>💡 Show Answer</summary>

**Sample Answer** (based on lab techniques):

```python
import pandas as pd

# 1. Filter for 2014
salaries_2014 = salaries[salaries.Year == 2014]

# 2. Remove rows with missing salary data
salaries_2014 = salaries_2014.dropna(subset=['TotalPay'])

# 3. Find top 5 highest-paid job titles (by average)
top_jobs = salaries_2014.groupby('JobTitle').TotalPay.mean()
top_jobs = top_jobs.sort_values(ascending=False)
print(top_jobs.head(5))

# 4. Compare departments (bonus - more advanced)
# Filter for police jobs
police = salaries_2014[salaries_2014.JobTitle.str.contains('POLICE', na=False)]
fire = salaries_2014[salaries_2014.JobTitle.str.contains('FIRE', na=False)]

print(f"Police average: {police.TotalPay.mean()}")
print(f"Fire average: {fire.TotalPay.mean()}")
```

**Key techniques used**:
- Boolean indexing (filtering)
- .dropna() for missing data
- .groupby() for aggregation
- .sort_values() for ranking
- .mean() for averages
- .head() for top N

</details>

---

## 📊 Scoring Guide

**Total Points: 100**

### Breakdown:
- Part 1 (Lecture Concepts): 30 points
- Part 2 (Pandas Operations): 40 points
- Part 3 (Missing Data): 20 points
- Part 4 (Applied): 10 points

### Grading:
- **90-100 points (90%+)**: 🌟 **Excellent!** You've mastered Week 2!
- **80-89 points (80-89%)**: ✅ **Strong** understanding. Review missed topics.
- **70-79 points (70-79%)**: ⚠️ **Good foundation**. Need more practice on weak areas.
- **Below 70 points (<70%)**: 📚 **Needs work**. Review lecture, lab, and readings carefully.

---

## 🎯 Your Score

**Date**: ___________

**Scores by Section**:
- Part 1 (Lecture): _____ / 30
- Part 2 (Pandas): _____ / 40
- Part 3 (Missing Data): _____ / 20
- Part 4 (Applied): _____ / 10

**Total**: _____ / 100 (_____%)

**Topics to Review**:
-
-
-

**Confidence Level** (1-5): _____

---

## 📚 Study Resources

### From Your Course:
- [[lecture-w02-data-handling]] - Link to lecture PDF
- [[lab-w02]] - Link to lab materials
- [[reading-list-w02]] - Pandas guides and readings

### External Resources:
- [Pandas 10-minute tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Handling Missing Data](https://machinelearningmastery.com/handle-missing-data-python/)

---

## 🔄 Next Steps

### If you scored 80%+:
✅ You're ready for Week 3!
- Move on to visualization
- Keep practicing pandas
- Try the bonus lab exercises

### If you scored below 80%:
📚 Strengthen your foundation:
1. Re-watch lecture on descriptive statistics
2. Re-do the lab notebooks from scratch (don't just read, TYPE the code!)
3. Read Python for Data Analysis Chapter 5
4. Retake this quiz in 2-3 days

### Pro Tips:
1. **Don't just read code - WRITE it!** Open Jupyter and try every example
2. **Use the Salaries dataset** - it's in your lab folder, practice on real data
3. **Ask "why?"** - Don't memorize, understand the reasoning
4. **Connect concepts** - How do lecture concepts (mean, median) connect to pandas (.mean(), .median())?

---

*Quiz updated: 2025-10-21*
*Based on: CS982 Lecture 2, Lab 2 Notebooks, Reading List Week 2*
*Perfectly aligned with YOUR actual course materials!* ✨
