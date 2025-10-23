
For the assignment a literature reiew is not necessary however reaseach and referencing is expected to justify + support desicions present in your report 

Supervised -labelled -trained on predicting the output

Unsupervised - data is unlabelled so the algorithms learn inherent stucture. It's group together (cluster) data points that seem similar

An example might be left to itself to find interesting structures in data...like customers with similar purchase patterns...corrolations between population 

**Cluster Analysis** 

Trying to find regions where data is densest. If those regios are distinct you'll be able to see the clusters

Look up and understand *Euclidean Distance* (Straight line distance). This is some times and sometimes not. For example in a city a straight line distance doesnt really work as they are build on grids.

*The Manthattan distance:* No diagonal moves (look it up). Based on the distance on axis. Mainly on categorical features

*Cosine Distance* - measuring angle between two vectores..good for comparative 

Look up one-hot encoded variable

Hamming Distance

Summary: 
Continuous, scaled features = Euclidean

Sparse, high-dimensional data =  Manhattan

Direction or proportion matters =  Cosine

Binary or categorical features = Hamming


Scaling..two ways,,, Standardisation (we'll be using this more, use StandardScaler) or Normalisation.
 

Assignment tips: 
- make sure you scale your data before you try any clustering
- make sure you prepare your data well for scaling