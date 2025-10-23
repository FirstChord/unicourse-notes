---
title: "Week 04 — Supervised Learning (Lab Content)"
module: "CS982"
tags: [module/CS982, type/labs, week-04, content]
date: 2025-10-15
---

# Supervised Learning
*Week 04 Lab*

CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Lab 4 \- Supervised Methods  
Before you start this lab, you need to get familiar with some instructions. We know that  
programming can be daunting, so we have some extra materials to help you. Make sure to download  
the notebooks available on MyPlace in week 4\. There are 2 notebooks, each notebook is working on  
a different dataset and aiming to solve a particular problem. You can either download all as a folder  
or download each and every file by itself. But remember to put the Jupyter notebook in the same  
folder as the dataset(s), whenever needed, so it can work properly.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part I – Wine dataset  
Question 1  
Import the necessary libraries (numpy, pandas, sklearn and metrics). You can also import other  
libraries either now or later in the notebook whenever a library is needed.  
Question 2  
We are going to work with the Wine dataset available on archive.ics.uci.edu. For this reason, you  
need first to download the dataset by following this link:  
https://archive.ics.uci.edu/ml/datasets/Wine (this will download a zip folder that includes the file  
wine.data – the actual dataset)  
Once downloaded, make sure to put the dataset in the same folder as the notebook, then read the  
dataset using the method .read\_csv(…)  
Question 3  
Perform an exploratory data analysis (EDA) on the dataset to better understand its underlying  
structure and key features. Typical steps in EDA include examining the data’s shape and structure,  
checking for missing values, visualizing distributions, and identifying relationships between variables  
through basic statistical summaries and visualizations like histograms, box plots, and scatter plots.  
Question 4  
In this dataset, the target feature is the first column, which represents the class of wine. Segment  
the dataset by separating the target class (first column) from the remaining data (rest of the  
columns), which contains the attributes. This will allow us to use the remaining attributes as input  
features for the classifiers while the target class will serve as the output for prediction.  
Question 5  
Remember, we need to split the dataset into two subsets: a training set and a test set. The training  
set will be used to train the machine learning model, while the test set will be used to validate the  
model's performance. Therefore, split the dataset into a 70/30 split, where 70% of the data will be  
used for training and the remaining 30% for testing.  
Question 6  
Create the following classifiers to predict the class of wine based on the attributes:  
• Logistic regression1  
• K nearest neighbours2  
• Decision tree3  
• Naïve Bayes4  
For each classifier, evaluate its performance by displaying the confusion matrix, as well as other key  
performance metrics such as precision, recall, F1-score, and accuracy. After obtaining these metrics  
1 https://scikit-learn.org/stable/modules/generated/sklearn.linear\_model.LogisticRegression.html  
2 https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html  
3 https://scikit-learn.org/stable/modules/tree.html  
4 https://scikit-learn.org/stable/modules/naive\_bayes.htmlCS989: Big Data Fundamentals  
CS982: Big Data Technologies  
for each model, compare their performance to determine which classifier performs the best in  
predicting the class of wine.  
Question 7  
Each classifier (model) has several parameters that can be tuned to enhance performance. For more  
information about the parameters available for each model, please refer to the links provided  
earlier.  
For this exercise, experiment with different values for each of the parameters of the classifiers to  
determine which configurations may lead to better results and improved model performance.  
Be sure to evaluate the performance of each model after tuning by analyzing metrics such as  
accuracy, precision, recall, F1-score, and the confusion matrix. This will help you identify the optimal  
parameter settings for each classifier.  
Part II – Titanic Dataset  
For this part of the lab, you should create a new notebook to ensure that you do not mix it with the  
previous one. This will help maintain clarity and organization in your work.  
Question 1  
Attempt the same approach as you did in the first part, but this time focus on the Titanic dataset,  
which can be found at: https://www.kaggle.com/c/titanic/data  
