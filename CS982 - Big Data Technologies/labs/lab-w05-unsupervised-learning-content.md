---
title: "Week 05 — Unsupervised Learning (Lab Content)"
module: "CS982"
tags: [module/CS982, type/labs, week-05, content]
date: 2025-10-22
---

# Unsupervised Learning
*Week 05 Lab*

CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Lab 5 \- Unsupervised Methods  
Before you start this lab, you need to get familiar with some instructions. We know that  
programming can be daunting, so we have some extra materials to help you. Make sure to download  
the notebooks available on MyPlace in week 5\. There are 2 notebooks, each Notebook is showing a  
different model for clustering. You can either download all as a folder or download each and every  
file by itself. But remember to put the Jupyter Notebook in the same folder as the dataset(s),  
whenever needed, so it can work properly.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part I – Hierarchical Clustering  
Question 1  
Import the necessary libraries (numpy, pandas, scikit-learn packages metrics and clustering). You can  
also import other libraries either now or later in the notebook whenever a library is needed.  
Question 2  
We are going to work with the Balance scale dataset available on archive.ics.uci.edu. For this reason,  
you need first to download the dataset by following this link:  
http://archive.ics.uci.edu/ml/datasets/balance+scale (this will download a zip folder that includes  
the file balance-scal, which is the actual dataset)  
Once downloaded, make sure to put the dataset in the same folder as the notebook, then read the  
dataset using the method .read\_csv(…)  
Question 3  
Try to explore the dataset (EDA).  
According to https://archive.ics.uci.edu/dataset/12/balance+scale, “this dataset was generated to  
model psychological experimental results. Each example is classified as having the balance scale tip  
to the right, tip to the left, or be balanced. The attributes are the left weight, the left distance, the  
right weight, and the right distance. If (left-distance \* left-weight) is less than (right-distance \* right-  
weight) then the scale will tip to the right. If (left-distance \* left-weight) is greater than (right-  
distance \* right-weight) then the scale will tip to the left. If they are equal, it is balanced”  
.  
Question 4  
In this dataset, the target feature is the first column, which obviously we don’t need when doing  
unsupervised learning, unless we need to calculate completeness and homogeneity. Therefore,  
create a new variable to hold the true target (first column) and another variable to hold the  
remaining data (attributes) so we can use the attributes for clustering.  
Question 5  
Scale the data that we are going to use for clustering.  
Question 6  
We know that there are 3 possible categories for the data. Create 3 data clusters using  
Agglomerative Hierarchical Clustering. Calculate the silhouette score, homogeneity and  
completeness for these clusters? (Helping hand, if you need to convert labels from strings to  
something else look at sklearn.preprocessing.LabelEncoder())  
Question 7  
What are the impact of different distance and affinity measures on the silhouette score,  
homogeneity and completeness for these clusters (options available at http://scikit-  
learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)? What is the  
best combination?CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part II – K-Means Clustering  
For this part, you should create another notebook. Also, note that questions 1 to 5 are the same as  
part I, so you might simply need to copy the solution or maybe write them again for more practice.  
Question 1  
Import the necessary libraries (numpy, pandas, scikit-learn packages metrics and clustering). You can  
also import other libraries either now or later in the notebook whenever a library is needed.  
Question 2  
We are going to work with the Balance scale dataset available on archive.ics.uci.edu. For this reason,  
you need first to download the dataset by following this link:  
http://archive.ics.uci.edu/ml/datasets/balance+scale (this will download a zip folder that includes  
the file balance-scal, which is the actual dataset)  
Once downloaded, make sure to put the dataset in the same folder as the notebook, then read the  
dataset using the method .read\_csv(…)  
Question 3  
Try to explore the dataset (EDA).  
This dataset was generated to model psychological experimental results. Each example is classified  
as having the balance scale tip to the right, tip to the left, or be balanced. The attributes are the left  
weight, the left distance, the right weight, and the right distance. If (left-distance \* left-weight) is  
less than (right-distance \* right-weight) then the scale will tip to the right. If (left-distance \* left-  
weight) is greater than (right-distance \* right-weight) then the scale will tip to the left. If they are  
equal, it is balanced.  
Question 4  
In this dataset, the target feature is the first column, which obviously we don’t need when doing  
unsupervised learning, unless we need to calculate completeness and homogeneity. Therefore,  
create a new variable to hold the true target (first column) and another variable to hold the  
remaining data (attributes) so we can use the attributes for clustering.  
Question 5  
Scale the data that we are going to use for clustering.  
Question 6  
We know that there are 3 possible categories for the data. Create 3 data clusters using K-Means  
Clustering. Calculate the silhouette score, homogeneity and completeness for these clusters?  
(Helping hand, if you need to convert labels from strings to something else look at  
sklearn.preprocessing.LabelEncoder())  
Question 7  
What are the silhouette score, homogeneity and completeness for different numbers of clusters  
created using K-Means?CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Question 8  
Additional exercise. Read about Principle Component Analysis and look at this example \-  
http://scikit-learn.org/stable/auto\_examples/decomposition/plot\_pca\_iris.html. Consider how it  
could be applied to clustering in our examples.  
Question 9  
PCA can be used to reduce the number of features. However, do you think we can reduce the  
number of features for this dataset without using PCA?  
