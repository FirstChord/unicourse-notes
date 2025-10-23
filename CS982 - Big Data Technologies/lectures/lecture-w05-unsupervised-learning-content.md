---
title: "Week 05 — Unsupervised Learning (Lecture Content)"
module: "CS982"
tags: [module/CS982, type/lectures, week-05, content]
date: 2025-10-22
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Unsupervised Learning
*Week 05 Lecture*

CS989 Big Data Fundamentals  
CS982 Big Data Technologies  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerLecture overview  
➢ What is clustering?  
➢ Distance measures  
➢ Hierarchical clustering  
➢ K-Means clustering  
➢ Evaluation of clustering  
➢ What is Good Clustering?Self-Attendance via MyPlace  
➢ Only works if you are already enrolled in the module on PegasusMapping Problems to Machine Learning  
➢ Supervised  
❖ Data is labelled: and  
❖ Algorithms learn to predict the output from input dataMapping Problems to Machine Learning  
➢ Unsupervised  
❖ Data is unlabelled: ???  
❖ Algorithms learn to inherent structure from input dataMapping Problems to Machine Learning  
➢ Unsupervised  
❖ Data is unlabelled: ???  
❖ Algorithms learn to inherent structure from input dataUnsupervised Methods  
➢ Unsupervised methods involve no training  
❖ Used to discover patterns / relationships in data and in understanding the data  
❖ The data given to unsupervised algorithm are not labelled, which means only the “input”  
features are given  
❖ Algorithms are left to themselves to discover interesting structures in the data  
❖ For example: groups of customers with similar purchase patterns or correlations between  
population movement and socioeconomic factors  
➢ The main approach that we will look at is clusteringCluster Analysis  
➢ Goal is to group observations in data into cluster so that the items in the  
same cluster are more similar to each other than items in other clustersCluster Analysis  
➢ Goal is to group observations in data into cluster so that the items in the  
same cluster are more similar to each other than items in other clusters  
➢ For example company that offers holidays might want to cluster clients  
behaviour and tastes by:  
❖ Which sites / countries they like to visit or kind of activities they participate in  
❖ Whether they prefer adventure, luxury, beach or educational holidaysCluster Analysis  
➢ Goal is to group observations in data into cluster so that the items in the  
same cluster are more similar to each other than items in other clusters  
➢ For example company that offers holidays might want to cluster clients  
behaviour and tastes by:  
❖ Which sites / countries they like to visit or kind of activities they participate in  
❖ Whether they prefer adventure, luxury, beach or educational holidays  
➢ This might help the company design attractive packages and target  
appropriate segments of their client baseCluster Analysis  
➢ We want to find the regions  
of the space where the data  
is densest  
➢ If those regions are distinct  
or nearly distinct then we  
have clustersDistance  
➢ In order to cluster we need notions of similarity and dissimilarity  
➢ In terms of distance, points in the same cluster are / should be closer to  
each other than to points in other clusters  
➢ Common distance measures:  
❖ Euclidean  
❖ Manhattan  
❖ Cosine  
❖ HammingDistance  
➢ Different distance metrics will give different clusters, as will different  
clustering algorithms  
❖ Application domain may determine what is chosen  
❖ Or trial and errorEuclidean Distance  
➢ Common and simple measure  
This image is licensed under the Creative Commons Attribution 4.0 International license.  
https://commons.wikimedia.org/wiki/File:Euclidean\_distance\_2d.svgEuclidean Distance  
➢ Common and simple measure  
➢ The Euclidean distance between two  
vectors x and y is:  
➢ Makes sense when all data is real-  
valued (quantitative)  
This image is licensed under the Creative Commons Attribution 4.0 International license.  
https://commons.wikimedia.org/wiki/File:Euclidean\_distance\_2d.svgManhattan Distance  
Source: https://www.offset.com/photos/top-down-view-of-manhattan-city-blocks-262626Manhattan Distance  
➢ Manhattan Distance measure is the  
number of horizontal and vertical moves  
it takes to get from one point to another  
➢ No diagonal moves  
Source: https://www.offset.com/photos/top-down-view-of-manhattan-city-blocks-262626Manhattan Distance  
➢ Manhattan Distance measure is the  
number of horizontal and vertical moves  
it takes to get from one point to another  
➢ No diagonal movesManhattan Distance  
➢ Manhattan Distance measure is the  
number of horizontal and vertical moves  
it takes to get from one point to another  
➢ No diagonal moves  
➢ The Manhattan Distance between two  
vectors x and y is:Key Conceptual Difference  
Aspect Euclidean Distance (L2) Geometry Measures direct, straight-line distance Sensitivity Sensitive to large differences (outliers) due  
to squaring Shape of clusters Prefers spherical clusters Mathematical properties Smooth, differentiable Correlation with features Assumes features are continuous and  
comparable  
Manhattan Distance (L1)  
Measures axis-aligned path distance  
More robust to outliers  
Prefers diamond-shaped clusters (aligned  
with axes)  
Less smooth but more robust  
Works better when features are not  
smoothly related or sparseGuideline – Not Hard Rules  
Situation Recommended Distance  
Continuous, well-scaled features Euclidean  
Sparse or high-dimensional features Manhattan  
Presence of outliers Manhattan  
Spherical clusters expected Euclidean  
Axis-aligned or rectangular clusters ManhattanCosine Distance  
➢ Cosine distance is a method commonly  
used in text analysis e.g. search systems  
➢ Measures the angle between two vectors  
➢ Two perpendicular vectors are furthest  
apart (Cosine(90) \= 0\)  
➢ Two parallel are the most similar  
(Cosine(0) \= 1\)  
Source: https://www.tyrrell4innovation.ca/miword-of-the-day-iscosine-distance/When Cosine Distance Makes Sense  
Use Cosine Distance when:  
✓ Proportional patterns between features rather than absolute values  
✓ The features are non-negative and on a comparable scale  
✓ The data is normalized (ideally L2-normalized) so each row has unit length  
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.htmlWhen Cosine Distance is Not a Good Fit  
Avoid Cosine Distance if:  
✘ Features have different physical meanings or scales (e.g., “age” and  
“income”)  
✘ Magnitude does matter (e.g., total purchase amount, energy use)  
✘ There are many zero or negative values (since cosine similarity assumes  
positive magnitudes and directionality)Hamming Distance  
➢ For categorical variables (small/medium/large), you can define the distance  
as 0 if two points are in the same category and 1 otherwise  
➢ Can extend to non-binary categoriesHamming Distance  
➢ For categorical variables (small/medium/large), you can define the distance  
as 0 if two points are in the same category and 1 otherwise  
➢ Can extend to non-binary categories  
➢ In this example, Hamming distance is 3  
Fruit Sphere Sweet Sour Crunchy  
Apple Y Y Y Y  
Banana N Y N N  
Calculation  
Is  
different  
Y N Y Y  
Value 1 0 1 1  
This example and more details from:  
http://people.revoledu.com/kardi/tutorial/Similarity/HammingDistance.htmlHamming Distance  
Use it when your features are categorical or binary, meaning:  
✓ You’re working with one-hot encoded variables  
✓ You care about exact matches/mismatches, not magnitudes or angles  
Avoid Hamming distance if:  
✘ Your features are continuous or ordinal  
✘ You have mixed data types  
✘ You expect gradual similarity (e.g., 1 vs. 2 should be closer than 1 vs. 10\)Summary Table  
Situation Recommended Distance  
Continuous, scaled features Euclidean  
Sparse, high-dimensional data Manhattan  
Direction or proportion matters Cosine  
Binary or categorical features Hamming  
Remember: these are guidelines, not strict rules. In practice, try more than one  
and evaluate results using cluster validation metrics or visualizations.Preparing the Data – Scaling  
➢ Units (or disparity in units) impact what clusters an algorithm will discover  
➢ Ideally you want a unit of change in each coordinate to represent the same  
degree of differencePreparing the Data – Scaling  
➢ Units (or disparity in units) impact what clusters an algorithm will discover  
➢ Ideally you want a unit of change in each coordinate to represent the same  
degree of difference  
➢ One approach is to transform all features to have a mean value of 0 and a  
standard deviation of 1 – StandardScaler  
https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.StandardScaler.html  
➢ Make the standard deviation the unit of measurement in each coordinate  
https://www.w3schools.com/python/python\_ml\_scale.aspClustering  
This Photo by Unknown Author is licensed under CC BY-SAHierarchical Clustering  
➢ Hierarchical clustering is a method of cluster analysis which seeks to build a  
hierarchy of clusters  
➢ There are 2 types  
❖ Agglomerative, "bottom up" approach – Supported by Python  
❖ Divisive, "top down" approach – Not Supported by Python  
➢ In general, the merges and splits are determined in a greedy manner  
➢ The results of hierarchical clustering are usually presented in a dendrogramHierarchical Clustering  
Source: https://dashee87.github.io/data%20science/general/Clustering-with-Scikit-with-GIFs/Linkage  
➢ Determines how objects should be joined or divided  
❖ Single uses the minimum distances between all observations of the two sets  
❖ Average uses the average of the distances of each observation of the two sets  
❖ Complete uses the maximum distances between all observations of the two sets  
https://medium.com/@kirtitambe17/important-notes-on-cluster-analysis-ac0abc65a337  
Source: https://www.drive5.com/usearch/manual/linkage.htmlLinkage  
Source: https://scikit-learn.org/stable/auto\_examples/cluster/plot\_linkage\_comparison.htmlK-Means Clustering  
➢ Alternative to hierarchical clustering  
➢ Need to specify number of clusters  
This image is released to the public domain  
https://commons.wikimedia.org/wiki/File:Iris\_Flowers\_Clustering\_kMeans.svgK-Means Clustering  
➢ K-Means clustering aims to partition all instances into K clusters in which  
each instance belongs to just one cluster  
➢ Tries to make the within-cluster instances as similar as possible while also  
keeping the clusters as different (far apart) as possible  
Cluster’s centroidK-Means Clustering  
Source: https://dashee87.github.io/data%20science/general/Clustering-with-Scikit-with-GIFs/K-Means – Algorithm  
1\) Specify number of clusters  
2\) Randomly allocate centroids  
3\) Repeat until clusters stabilise  
a) Calculate distance between instances  
and all centroids  
b) Assign instance to nearest centroid  
c) Compute centroids for clustersClustering Using K-Means  
➢ Algorithm is not guaranteed to have a unique stopping point  
➢ Final clusters depend on initial cluster centres  
➢ Can run K-means several times with different random starts and then select  
the best resultsNumber of Clusters  
➢ Sometimes there is no problem specifying the number of clusters in  
advance e.g. segmenting a client database into X clusters for X salesman  
➢ Sometimes the cut off is implicit in stopping at a certain point e.g. placing  
cell phone towers  
➢ However in most exploratory applications, the number of clusters is not  
known in advance  
➢ So how do we decide how many clusters there should be?Number of Clusters  
➢ Silhouette Score  
❖ Measure of how similar an object is to its own cluster (cohesion) compared to other  
clusters (separation)  
❖ Value ranges from −1 to \+1  
❑ where a high value close to 1 indicates that the object is well matched to its own cluster,  
❑ where a value close to 0 indicates that the object is close to a cluster boundary,  
❑ where a low value close to \-1 indicates that the object may have been assigned to the wrong cluster  
❖ High values indicate appropriate clusteringNumber of ClustersNumber of Clusters  
➢ Silhouette Score  
➢ Calinski-Harabasz Index  
❖ known as the Variance Ratio Criterion  
❖ Ratio of the sum of between-clusters dispersion and of inter-cluster dispersion for all  
clusters  
❖ There is no "acceptable" cut-off value. You simply compare CH values by eye. A higher  
index value suggests better clustering.Evaluation of clustering  
➢ Silhouette Score  
➢ Calinski-Harabasz Index  
➢ Homogeneity  
❖ A clustering result satisfies homogeneity if all of its clusters contain only data points  
which are members of a single class  
➢ Completeness  
❖ A clustering result satisfies completeness if all the data points that are members of a  
given class are elements of the same clusterEvaluation of clustering  
Mainly Used  
➢ Silhouette Score  
➢ Calinski-Harabasz Index  
➢ Homogeneity  
❖ A clustering result satisfies homogeneity if all of its clusters contain only data points  
which are members of a single class  
➢ Completeness  
❖ A clustering result satisfies completeness if all the data points that are members of a  
given class are elements of the same clusterEvaluation of clustering  
Mainly Used  
➢ Silhouette Score  
➢ Calinski-Harabasz Index  
➢ Homogeneity  
❖ A clustering result satisfies homogeneity if all of its clusters contain only data points  
which are members of a single class  
➢ Completeness  
❖ A clustering result satisfies completeness if all the data points that are members of a  
given class are elements of the same cluster  
1\. True labels must be available  
2\. Nb of unique true labels \= Nb of clustersAccuracy vs Completeness/Homogeneity  
Instances True Target Cluster  
1 A A  
2 A A  
3 A A  
Accuracy: 100%  
Completeness: 100%  
Homogeneity: 100%  
4 A A  
5 A A  
6 B B  
7 B B  
8 B B  
9 B B  
10 B BAccuracy vs Completeness/Homogeneity  
Instances True Target Cluster  
Instances True Target Cluster  
1 A A  
1 A B  
2 A A  
3 A A  
Accuracy: 100%  
Completeness: 100%  
Homogeneity: 100%  
2 A B  
3 A B  
4 A A  
4 A B  
5 A A  
5 A B  
6 B B  
6 B A  
7 B B  
8 B B  
Accuracy: 0%  
Completeness: 100%  
Homogeneity: 100%  
7 B A  
8 B A  
9 B B  
9 B A  
10 B B  
10 B AAccuracy vs Completeness/Homogeneity  
Instances True Target Cluster  
Instances True Target Cluster  
1 A 1  
1 A 2  
2 A 1  
3 A 1  
Accuracy: 100%  
Completeness: 100%  
Homogeneity: 100%  
2 A 2  
3 A 2  
4 A 1  
4 A 2  
5 A 1  
5 A 2  
6 B 2  
6 B 1  
7 B 2  
8 B 2  
Accuracy: 0%  
Completeness: 100%  
Homogeneity: 100%  
7 B 1  
8 B 1  
9 B 2  
9 B 1  
10 B 2  
10 B 1Perfect for Clustering  
Source: https://developers.google.com/machine-learning/clustering/interpretHopeless for Clustering  
Source: https://developers.google.com/machine-learning/clustering/interpretClusters vs True Targets  
This image is released to the public domain  
https://commons.wikimedia.org/wiki/File:Iris\_Flowers\_Clustering\_kMeans.svgClusters vs True Targets  
This image is released to the public domain  
https://commons.wikimedia.org/wiki/File:Iris\_Flowers\_Clustering\_kMeans.svgWhat is Good Clustering?Summary  
➢ Goal of clustering is to discover or draw out similarities among subsets of  
your data  
➢ Points in the same cluster should be more similar to each other than they  
are to points in other clusters  
➢ Scaling data is / may be necessary  
➢ Clustering is an iterative process and often used for data exploration or as a  
precursor to supervised learning methods  
