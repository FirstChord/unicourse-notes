---
title: "Week 02 — Exploring Data (Lab Content)"
module: "CS982"
tags: [module/CS982, type/labs, week-02, content]
date: 2025-10-01
---

# Exploring Data
*Week 02 Lab*

CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Lab 2 \- Exploring and Managing a Dataset with Python  
This lab will help you practice working with datasets using NumPy and pandas. You will learn how to  
import libraries, load data, explore datasets, handle missing values, and perform basic data analysis  
and manipulation.  
However, before you start this lab, you need to get familiar with some instructions. We know that  
programming can be daunting, so we have some extra materials to help you. Make sure to download  
the Notebooks available on MyPlace in week 2\. There are three different Notebooks but working on  
the same dataset. You can either download all as a folder or download each and every file by itself.  
But remember to put the Jupyter Notebook in the same folder as the dataset so it can work  
properly.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part I – Getting Started with Pandas and NumPy  
Question 1  
Import the necessary libraries: NumPy and Pandas.  
• Use the import statement in Python.  
• You may use the as keyword to give shorter aliases to make your code easier to read.  
Question 2  
In this lab, we will use the Pokémon dataset available on Kaggle.  
• Link: https://www.kaggle.com/alopez247/pokemon  
• Download the dataset and place the CSV file in the same folder as your Jupyter Notebook.  
• Use the function pd.read\_csv ( … ) to load the dataset into a pandas DataFrame.  
• Hint: Assign it to a variable (e.g., PokemonDF) so you can use it later.  
Question 3  
Display the first 10 rows of the dataset to get a quick overview.  
• Hint: Use the .head(10) method  
Question 4  
Find out how many rows (observations) and columns (features) are in the dataset.  
• Hint: Use the .shape attribute.  
Question 5  
Print the names of all the columns (features) in the dataset.  
• Hint: Use the .columns attribute.  
Question 6  
Display the last 10 rows of the dataset.  
Question 7  
Use .describe() to generate summary statistics for all numerical columns.  
Question 8  
type?  
Check the data type of the column "isLegendary". Why do you think this column is stored as that  
Question 9  
Which columns in the dataset are categorical and which are numerical? How can you tell?CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part II – Data Handling and Manipulation  
For this part, you should create a new Jupyter Notebook.  
Question 1  
Import the necessary libraries (NumPy and Pandas).  
Question 2  
Load the Pokémon dataset again using pd.read\_csv( … ).  
Question 3  
Sort the Pokémon by their Attack power, from highest to lowest.  
• Hint: Use the .sort\_values( … ) method.  
Question 4  
The dataset has two type-related columns: Type\_1 and Type\_2. Analyse how the Defence stat varies  
by type:  
• Group by Type\_1 and calculate the average Defence.  
• Group by Type\_2 and calculate the average Defence.  
• Consider both Type\_1 and Type\_2 together to compare defence across Pokémon types.  
• Hint: Use .groupby( ) along with aggregation functions like .mean( )  
Question 5  
For each Pokémon type, calculate the following statistics for the Total column:  
• Mean  
• Median  
• Maximum  
• Minimum  
• Hint: Use .groupby( ) combined with .agg( ).  
Question 6  
Determine the most common Pokémon type in the dataset.  
• Hint: Use .value\_counts( ) on the Type\_1 column  
Question 7  
Create a new column called "Attack-to-Defense Ratio" (Attack / Defense) and sort the dataset by this  
value. Which Pokémon is most "attack-heavy"?  
Question 8  
Create a new column called "HP Category":  
• "Low" if HP \< 50  
• "Medium" if 50 ≤ HP \< 100  
• "High" if HP ≥ 100  
Then count how many Pokémon fall into each category.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part III – Dealing with Missing Data  
For this part, create another new Jupyter Notebook.  
Question 1  
Import the necessary libraries (NumPy and Pandas).  
Question 2  
Load the Pokémon dataset again using pd.read\_csv( … ).  
Question 3  
Check for missing values in the dataset.  
• Are there any missing values?  
• If yes, how many missing values does each column have?  
• How many missing values are there in total across the dataset?  
• Hint: Use .isnull( ).sum( )  
Question 4  
Remove the columns Type\_2 and Egg\_Group\_2 from the dataset.  
• Hint: Use .drop(columns=\[...\])  
Question 5  
Remove all rows that contain any missing values.  
• Hint: Use .dropna( )  
Question 6  
Instead of dropping rows with missing values, sometimes it is better to fill them in.  
• Explore different strategies for filling missing values:  
o Replace with a constant (e.g., "Unknown")  
o Replace with the mean, median, or mode (depending on the column type)  
o Use forward fill or backward fill (.ffill(inplace=True))  
• Choose and apply a filling strategy that makes sense for this dataset.  
Question to think about: Why might one strategy be better than another depending on the column?  
