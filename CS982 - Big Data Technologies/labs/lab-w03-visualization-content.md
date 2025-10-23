---
title: "Week 03 — Visualization (Lab Content)"
module: "CS982"
tags: [module/CS982, type/labs, week-03, content]
date: 2025-10-08
---

# Visualization
*Week 03 Lab*

CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Lab 3 \- Visualising Data in Python  
In this lab, you will explore how to create a variety of data visualisations using Python and its main  
data and plotting libraries. Visualising data is one of the most important steps in data analysis, as it  
allows you to discover patterns, detect outliers, and communicate findings clearly.  
Before you start this lab, you need to get familiar with some instructions. We know that  
programming can be daunting, so we have some extra materials to help you. Make sure to download  
the notebooks available on MyPlace in week 3\. There are 10 different notebooks, each notebook will  
focus on one specific type of graphs. You can either download all as a folder or download each and  
every file by itself. But remember to put the Jupyter notebook in the same folder as the dataset(s) so  
it can work properly.  
In addition, related to the previous lab, filling null (missing) values in a dataset can be challenging  
and it requires a deep understanding of the dataset itself. Below is a link to a Notebook on Kaggle  
that you can explore on your own time. The Notebook includes an implementation of filling missing  
values for a specific dataset, Spaceship Titanic, using Python Language, based on some observations:  
(1) https://www.kaggle.com/code/josephelgemayel/spaceship-titanic-fillna  
The ideas implemented in the Notebook are based on a discussion about some rules to fill NaNs by  
Vincent Debout:  
(2) https://www.kaggle.com/competitions/spaceship-titanic/discussion/315987  
For a better understanding, it’s is recommended to explore first the discussion (2) and then explore  
the implementation (1) of the ideas.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part I – Visualisations with a single variable  
In this section, you will focus on understanding and visualising one variable at a time. This kind of  
analysis helps you get a sense of how each attribute in the dataset behaves individually.  
Question 1  
and visualisation:  
Before you can visualise anything, you need to import the key Python libraries used for data analysis  
• NumPy: for numerical operations,  
• Pandas: for handling and exploring structured data (DataFrames),  
• Matplotlib and Seaborn: for creating visualisations.  
Question 2  
In this lab, we are going to work with the Titanic dataset available on Kaggle. For this reason, you  
need to download the dataset from Kaggle using the following link:  
https://www.kaggle.com/c/titanic/data (it is train.csv that you want)  
Once downloaded, make sure to put the dataset in the same folder as the Notebook, then read the  
dataset using the method .read\_csv(…).  
Question 3  
Box plots help identify outliers, medians, and data spread quickly. They are particularly useful for  
spotting anomalies in numeric data.  
Use box plots to visualise the distribution and spread of numeric variables (such as Age, Fare, etc.).  
Question 4  
title and axis labels.  
Create a bar chart that shows how many passengers survived versus did not survive. Include a clear  
This gives you a quick overview of class imbalance in the dataset, which is an important concept  
when preparing data for predictive models later. A simple bar chart can communicate survival  
proportions effectively.  
Question 5  
Plot a horizontal bar chart showing how many passengers were in each class (1st, 2nd, 3rd). Order  
the bars from smallest (top) to largest (bottom).  
Visualising class distributions helps you understand dataset composition. Ordering the bars improves  
readability and helps spot which class dominates the data.  
Question 6  
Create a density plot for the SibSp column.  
Density plots show how data values are distributed across a continuous range. In this case, it helps  
us see whether most passengers were travelling alone or with family.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Question 7  
Professional visualisations are not only informative but also clear. Learning to customise plots  
prepares you to create visualisations suitable for presentations and reports. Experiment with  
colours, styles, titles, grid lines, or themes.  
Question 8  
Be creative – explore other variables or try new types of plots such as:  
• Histograms for Age or Fare,  
• Pie charts for gender proportions,  
• Violin plots to show Age distribution by survival status.  
Data exploration is not just about following steps. Trying different visualisations encourages critical  
thinking about which plots best reveal insights from the data.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part II – Visualisations with more than one variable  
In this section, you’ll learn to visualise relationships between variables. This is key to uncovering  
patterns and dependencies that single-variable charts cannot show.  
Tip: Create a new Jupyter Notebook for this part to keep your work organised.  
Question 1  
Each notebook runs independently, so you’ll need to import the required tools again. Re-import  
NumPy, Pandas, Matplotlib, and Seaborn.  
Question 2  
We will build upon the earlier univariate exploration to now compare variables and find patterns  
across them. Load the same train.csv file as before.  
Question 3  
Create a stacked bar chart showing how many passengers of each gender (male/female) were in  
each passenger class (1st, 2nd, 3rd).  
This helps you explore categorical relationships, such as whether certain classes had more men or  
women, revealing social and demographic patterns.  
Question 4  
Correlation matrices show how strongly two variables move together. For example, Fare might  
correlate with Pclass. This is a powerful tool to detect relationships and guide feature selection in  
future machine learning tasks.  
Create a heatmap of the correlation matrix between all numeric variables. What features show a  
strong correlation?  
Question 5  
Scatter plots are useful for visualising relationships and possible trends. Combining multiple  
variables helps you see whether patterns emerge across different comparisons.  
Produce a single scatter plot that shows:  
• Age vs Passenger Class,  
• Age vs Number of Siblings (SibSp)  
Use different symbols or colours to distinguish the two comparisons.  
Question 6  
Experiment with other visualisations. Try exploring:  
• Pair plots (sns.pairplot) to visualise multiple relationships at once,  
• Violin or swarm plots for categorical vs numeric comparisons,  
• Facet grids to visualise subgroups (e.g., survival by gender and class)  
Data visualisation is as much an art as it is a science. The more you experiment, the better you’ll  
understand which visuals best convey different kinds of data stories.  
