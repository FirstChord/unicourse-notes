---
title: "Week 02 — Data Handling (My Notes)"
module: "CS982"
tags: [module/CS982, type/notes, week-02]
date: 2025-10-23
---

# Week 02 — Data Handling
*My personal notes from lecture*

---

## Understanding Data and Information

The word *data* comes from the Latin *datum*, meaning "something given." Individual pieces are called *data points*, and a collection of them forms a *dataset*.
 Data can take many forms — numbers, text, symbols, measurements, or observations — and can be gathered by humans or sensors.

By itself, data is raw and unorganised. When it is processed, analysed, and structured in a meaningful way, it becomes **information** — something that provides insight, reveals patterns, and supports decision-making.

It's tempting to start modelling data immediately, but this should be avoided. Before analysis, data should be cleaned and explored to ensure accuracy and reliability.

---

## Descriptive Statistics

Descriptive statistics summarise and describe the main features of a dataset. A dataset may represent an entire population or a sample of it.

Key areas include:

### 1. Frequency and Count Measures

* **Count**: Number of times a particular value occurs.
* **Frequency/Percentage**: Expresses how common a value is relative to the total number of observations.

### 2. Measures of Central Tendency

* **Mean**: The average — sum of all values divided by the number of values.
* **Median**: The middle value when the dataset is ordered.
* **Mode**: The most frequently occurring value.

### 3. Measures of Dispersion (Variation)

* **Range**: Difference between the maximum and minimum values.
* **Variance**: The average of the squared differences from the mean — it quantifies how spread out the data is.
* **Standard Deviation**: The square root of variance; it shows the average distance of data points from the mean.
* **Interquartile Range (IQR)**: The range of the middle 50% of the data (between Q1 and Q3).

### 4. Quartiles

Quartiles divide ordered data into four equal parts.

* Q1 (25th percentile), Q2 (median / 50th percentile), Q3 (75th percentile).
* Each quartile represents one quarter of the dataset.

---

## Data Cleaning and Handling Missing Values

Before analysing data, it's important to identify and handle inconsistencies or missing values. Strategies include:

* **Recollecting** missing data if possible.
* **Dropping** incomplete records (only if few and not crucial).
* **Replacing (imputing)** missing values with meaningful estimates:
  * If missing values occur **randomly**, replace them with the **mean, median, or mode**.
  * If not random, treat them as a **separate category** or replace them with a default value (e.g., 0) if appropriate.

---

## Data Transformation

Data transformations make data easier to analyse and model. Common transformations include:

* **Discretisation**: Converting continuous data into categories (e.g., income brackets).
* **Normalisation and Rescaling**: Adjusting the scale of numeric data to make variables comparable.

---

## Normalisation vs Rescaling (Summary)

| Technique | Purpose | Typical Range | Use Case |
|-----------|---------|---------------|----------|
| **Normalisation (Min–Max Scaling)** | Scales data to a fixed range so all values are between 0 and 1. | 0 to 1 | When features need to be on the same scale (e.g., machine learning models). |
| **Standardisation (Rescaling using Z-score)** | Centers data around the mean with unit variance. | Mean = 0, SD = 1 | When the data follows a normal distribution or for models assuming Gaussian data (e.g., regression, PCA). |

**In short:**
* **Normalisation** compresses values into a *bounded range (0–1)*.
* **Standardisation (Rescaling)** centres them around *zero* and adjusts spread to *one* standard deviation.

---

## Links to Related Materials

- [[lecture-w02-data-handling-content]] - Official lecture content
- [[lab-w02-exploring-data-content]] - Week 2 lab
- [[lab-w02-solutions]] - Lab solutions

---

## My Questions ❓

*Add questions here as they come up*

-

---

## Key Takeaways 💡

- Always clean and explore data before modeling
- Understand your measures: mean (affected by outliers) vs median (robust)
- IQR is better than range for understanding spread
- Choose imputation method based on whether data is missing randomly
- Normalisation (0-1) vs Standardisation (mean=0, sd=1) serve different purposes

---

*Created from lecture 2 notes*
*Use this alongside the full lecture content for studying*
