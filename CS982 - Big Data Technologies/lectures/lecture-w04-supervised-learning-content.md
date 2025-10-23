---
title: "Week 04 — Supervised Learning (Lecture Content)"
module: "CS982"
tags: [module/CS982, type/lectures, week-04, content]
date: 2025-10-15
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Supervised Learning
*Week 04 Lecture*

CS989 Big Data Fundamentals  
CS982 Big Data Technologies  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerLecture overview  
➢ Some questions about the coursework  
➢ Choosing and Evaluating Models  
❖ What techniques are appropriate for what kind of problems  
❖ How to evaluate the model produced  
➢ Regression  
➢ Classification  
➢ DemoSelf-Attendance via MyPlace  
➢ Only works if you are already enrolled in the module on PegasusSome questions about the coursework  
➢ Can we use chatGPT or any other GenAI tool?  
❖ As part of your learning process – YES  
❖ Troubleshoot errors in your code – YES  
❖ Proofreading your text – YES  
❖ Generating (part of) content or code for your coursework – STRICTLY NO  
❖ More details can be found in the “Frequently Asked Questions” document available on  
MyPlaceSome questions about the coursework  
➢ Which dataset should I choose?  
❖ Identify the topic that you are interested in before choosing the dataset  
❖ Take your time in choosing the topic and the dataset  
❖ It’s recommended to work with a tabular dataset  
❖ Avoid time series datasets, such as predicting Bitcoin value  
❖ Avoid datasets with unknown / unclear features  
❖ Avoid datasets with very low number of relevant features  
❖ Highly recommended: do some exploratory analysis before decidingSome questions about the coursework  
➢ The dataset is too small or too large, what should I do?  
❖ If too small, look for another dataset on a similar topic to merge with  
❖ If too large, work on part of the dataset  
❖ Whatever you do, you should mention it in the report  
❖ In fact, all decisions should be well mentioned and justified in the reportSome questions about the coursework  
➢ Can we use chatGPT or any other GenAI tool?  
➢ Which dataset should I choose?  
➢ The dataset is too small or too large, what should I do?  
➢ When I should start working on the coursework? Last week ☺  
➢ Don’t forget to select your group for the first part of the coursework\!\!  
➢ Any other question? Post it on MyPlace or bring it to the lab sessionChoosing Methods  
➢ Ultimate goal is to solve some sort of problem  
❖ Increase sales or customer satisfaction  
❖ Identify fraudulent transactions  
❖ Portfolio management  
➢ Descriptive statistics and Graphs can help understand the data  
➢ Lots of statistical modelling methods, with strengths and weaknesses  
❖ Need to be able to choose most appropriate method(s)  
➢ Need a measure of quality of your model to ensure it performs well in productionMapping Problems to Machine Learning  
➢ Supervised  
❖ Data is labelled: and  
❖ Algorithms learn to predict the output from input dataMapping Problems to Machine Learning  
➢ Unsupervised  
❖ Data is unlabelled: ???  
❖ Algorithms learn to inherent structure from input dataMapping Problems to Machine Learning  
➢ Unsupervised  
❖ Data is unlabelled: ???  
❖ Algorithms learn to inherent structure from input dataMapping Problems to Machine Learning  
➢ Semi-supervised  
❖ Some data is labelled, but most is unlabelled  
❖ Mixture of supervised and unsupervised techniques can be usedMapping Problems to Machine Learning  
Source: Practical Data Science with R, by Nina Zumel and John MountMapping Problems to Machine Learning  
Source: Practical Data Science with R, by Nina Zumel and John MountEvaluation and Validation  
➢ Evaluation  
❖ Quantifying performance of the model  
❖ Needs to be appropriate to goal and modelling task e.g. classification vs scoring tasks  
➢ Validation  
❖ Assurance that it works as well in practise as in training  
❖ Common problem is lack of appropriate training data  
❖ Validation techniques attempt to quantify riskEvaluation and Validation  
➢ Need to split data in training set and test setEvaluation and Validation  
➢ Need to split data in training set and test set  
➢ Measures vary according to type of model  
❖ Classification  
❖ Scoring  
❖ Probability Estimation  
❖ Ranking  
❖ ClusteringEvaluation and Validation  
➢ Important to compare measures against a baseline  
❖ Best model of a very simple form that you are trying to outperform  
❖ Typically a constant or a model that is independent of relationships between inputs and  
outputs e.g.  
❖ Represents a lower bound on desired performance  
➢ Also notion of Bayes rate error  
❖ Best possible model  
❖ Upper bound to aspire toEvaluating Classification ModelsEvaluating Classification Models  
➢ Confusion Matrix – Summaries a  
classifiers predictions against  
known categories  
➢ Basically shows what has been  
classified correctly, what has not  
and how  
Predicted  
CM Yes No  
Yes True Positive (TP) False Negative (FN)  
Type II \- Error  
True  
No False Positive (FP)  
Type I \- Error  
True Negative (TN)Evaluating Classification Models  
This Photo by Unknown Author is licensed under CC BY-SAEvaluating Classification Models  
Predicted Values  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
9 8 7  
3 2 1  
6 5 4Evaluating Classification Models  
TP  
Predicted Values  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
9 8 7  
3 2 1  
6 5 4Evaluating Classification Models  
9 8 7  
Predicted Values  
TP FN  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
3 2 1  
6 5 4Evaluating Classification Models  
9 8 7  
Predicted Values  
TP FN  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
3 2 1  
6 5 4  
FPEvaluating Classification Models  
9 8 7  
Predicted Values  
TP FN  
Apple Banana Tomato  
Tomato Banana Apple  
6 5 4  
FP TN  
True Values  
3 2 1Evaluating Classification Models  
TP  
Predicted Values  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
9 8 7  
3 2 1  
6 5 4Evaluating Classification Models  
Predicted Values  
Apple Banana Tomato  
FN  
True Values  
Tomato Banana Apple  
9 8 7  
3 2 1  
6 5 4Evaluating Classification Models  
Predicted Values  
Apple Banana Tomato  
True Values  
Tomato Banana Apple  
9 8 7  
3 2 1  
6 5 4  
FPEvaluating Classification Models  
Predicted Values  
Apple Banana Tomato  
9 8 7  
True Values  
3 2 1  
Tomato Banana Apple  
6 5 4  
FP TNEvaluating Classification Models  
➢ Several measures based on confusion matrix  
❖ Precision – Fraction of items classified identified as being in a class that actually are  
TP / (TP \+ FP)  
❖ Recall – Fraction of items that are in the class that classifier detects  
TP / (TP \+ FN)  
❖ F1 score – Combines precision and recall  
2 \* (precision \* recall) / (precision \+ recall)  
❖ Accuracy – Fraction of items classified correctly  
(TP \+ TN) / (TP \+ FP \+ TN \+ FN)Evaluating Scoring Models  
➢ Here we look at the residuals  
➢ Essentially is the difference between  
the predicted and actual / true  
outcomesEvaluating Scoring Models  
➢ Absolute Error  
(Δx) \= |𝑥𝑖 − 𝑥|  
➢ Mean Absolute ErrorEvaluating Scoring Models  
➢ Root Mean Square Error (RMSE) – Square root of average square of the  
difference between predicted and actual values (i.e. how far off is prediction)  
➢ R-Squared – a statistical measure that represents the proportion of the  
variance for a dependent variable that's explained by an independent  
variable in a regression modelValidating Models  
➢ Having evaluated a model on training data how well will it perform on real  
data?  
➢ Common problems  
❖ Bias – Systematic error in model e.g. always under predictingValidating Models  
➢ Having evaluated a model on training data how well will it perform on real  
data?  
➢ Common problems  
❖ Variance – Undesirable (and non-systematic) distance between predictions and actual  
values (may be due to oversensitivity of model training  
procedure to small variations in data for example)Bias Variance Trade-OffBias Variance Trade-OffValidating Models  
➢ Having evaluated a model on training data how well will it perform on real  
data?  
➢ Common problems  
❖ Overfitting – Features that arise due to unrepresentative training data  
❖ Non-significance – Model that appears to show an important relation which may not hold  
in the general populationOverfittingOverfittingEnsuring Model Quality – Held Out Data  
➢ Models should not be evaluated on  
training data alone  
➢ Split data in test and training set  
➢ It only gives one a single point of  
estimate thoughEnsuring Model Quality – K-Fold Cross  
Validation  
➢ Models should not be evaluated on  
training data alone  
➢ Repeat model construction and  
evaluation on different subsets of  
data  
➢ Unbiased estimateSupervised Learning – Models  
This Photo by Unknown Author is licensed under CC BYLinear and Logistic Regression  
➢ Both methods learn a model that is a continuous function of its inputs  
➢ Useful when you don’t just want to predict an outcome, but you also want to  
know the relationship between the input variables and the outcome  
➢ Main differences  
❖ Linear regression used to predict quantities  
❖ Logistic regression used to predict probabilities or categories  
➢ Good techniques to try before exploring more complex approachesLinear Regression  
➢ Standard approach for trying to predict a numerical quantity (cost, volume,  
quantity etc.)  
❖ If it works well \- great\!  
❖ If it fails \- detailed diagnostics produced give you a good clue as to what methods you  
should try next  
➢ Models the expected value of a numeric quantity (the dependent or  
response variable) in terms of numeric and categorical inputs (the  
independent or explanatory variables)Linear Regression \- Formally  
➢ Suppose that  
❖ y\[i\] is the numeric quantity that we want to predict  
❖ And x\[i,\] is a row of inputs that corresponds to output y\[i\]  
➢ Linear regression finds a fit function f(x) such that  
❖ y\[i\] \~ f(x\[i,\]) \= b\[1\] x\[i,1\] \+ ... b\[n\] x\[i,n\]  
➢ We want numbers b\[1\],...,b\[n\] (called the coefficients or betas) such that  
f(x\[i,\]) is as near as possible to y\[i\] for all (x\[i,\],y\[i\]) pairs in our training dataLinear Regression \- Example  
➢ Try to predict a student's grade for a class from their lecture and lab  
attendance  
❖ For each individual, i, assume that grade is a linear combination of lecture and lab  
attendance. i.e.  
❖ final.grade\[i\] \= b.lectures \* lecture.attendance\[i\] \+ b.labs \* lab.attendance\[i\]  
➢ Goal is to find the values of b.lectures and b.attendance so that the linear  
combination of lecture.attendance\[i\] and lab.attendance\[i\] comes very close  
to final.grade\[i\] for all students i in the training dataLinear Regression – Calculating  
Coefficients  
➢ Works by trying to minimise the  
residuals, the difference between  
predicted and actual outcomesLogistic Regression  
➢ Member of a class of models called generalised linear models  
➢ Logistic regression can directly predict values that are restricted to the (0,1)  
interval, such as probabilities  
➢ Good first choice for binary classification problems  
➢ Logistic regression predicts the probability y that an instance belongs to a  
specific category  
❖ e.g. the probability that a flight will be delayedLogistic Regression  
➢ Similar form to linear regression but  
aims to predict the probability of a set  
of outcomes mapping to a class. i.e.  
➢ P\[y\[i\] in class\] \~ f(x\[i,\]) \= s(a+b\[1\]  
x\[i,1\] \+ ... b\[n\] x\[i,n\])  
➢ Where, s(z) is the sigmoid function,  
defined as s(z) \= 1/(1+exp(z))Regression – Summary  
➢ Looked at two functional techniques: linear regression and logistic  
regression  
❖ Functional models allow you to better explore how changes in inputs affect predictions  
❖ Linear regression is a good first technique for modelling quantities  
❖ Logistic regression is good first technique for modelling probabilities  
❖ Models with simple forms come with very powerful summaries and diagnosticsDecision Trees  
➢ Simple model type, make a prediction that is piecewise constant  
❖ Split the training data into pieces and use a simple memorised constant on each piece  
❖ Like machine-generated business rules  
➢ Works by proposing many possible cuts in the data then choosing best cuts  
in simultaneous competing criteria of  
❖ Predictive power  
❖ Cross-validation strength  
❖ Interaction with other chosen cutsDecision Trees  
➢ Classification trees, where the target  
variable is categorical and the tree is used  
to identify the class within which a target  
variable would likely fall into  
➢ Regression Trees, where the target  
variable is continuous and tree is used to  
predict its value  
➢ Popular algorithms include ID3, C.45  
https://commons.wikimedia.org/wiki/File:CART\_tree\_titanic\_survivors.png  
Creative Commons Attribution-Share Alike 3.0 Unported license.Decision Trees – iris datasetDecision Tree Regression  
Source: https://scikit-learn.org/stable/auto\_examples/tree/plot\_tree\_regression.htmlDecision Trees – Feature importance  
Source: https://medium.com/analytics-vidhya/random-forest-on-titanic-dataset-88327a014b4dDecision Trees  
➢ Can be applied to any type of data  
➢ Final structure of the classifier can be quite simple  
➢ Resulting trees are usually quite understandableNaïve Bayes  
➢ Uses the notion of conditional probability  
➢ Considers how each training variable is related to output  
➢ Makes predictions by multiplying together effects of each variableNaïve Bayes  
➢ Assume we have a problem instance to be classified, represented by a  
vector x=(x1, x2, …. xn ), and there are a number of class outcomes, ck,  
then Naïve Bayes will assign a probability thus: (𝑐  
\_  
𝑘│𝑥\_1,𝑥\_2, …,𝑥  
\_  
𝑛 )  
➢ This conditional probability can be reformulated to be more tractable  
➢ Which can be written informally asNaïve Bayes  
Weather Play  
Sunny No  
Rain Yes  
Snow No  
Sunny Yes  
Sunny Yes  
Rain No  
Snow No  
Snow No  
Rain No  
Sunny Yes  
Weather Sunny Rain Snow All Frequency Table  
Weather No Yes  
Sunny 1 3  
Rain 2 1  
Snow 3  
Grand Total 6 4  
Likelihood Table  
No Yes  
1 3 \= 4/10 2 1 \= 3/10 3 \= 3/10 6 4  
\= 6/10 \= 4/10  
0.4  
0.3  
0.3Naïve Bayes  
➢ Probability of playing when weather is sunnyNaïve Bayes  
➢ Benefits  
❖ Easy and fast to predict a class  
❖ Performs well for categorical variables  
❖ For numerical variables, a normal distribution is assumed  
➢ Drawbacks  
❖ If categorical variable has a category not in training set, the model will assign 0 and not  
be able to make a prediction  
❖ A limitation is the assumption of independent predictionsSummary  
➢ Choosing and Evaluating Models  
❖ Training and test sets  
❖ Measures for quantifying performance of classification and scoring algorithms  
➢ Memorisation-Based Techniques  
❖ Decision Trees \- Model makes prediction by choosing the summary of all training data  
that was placed in the same leaf node of the decision tree as the current example to be  
scored  
❖ Naïve Bayes \- Prediction for a given example is the product of all the collection of  
applicable single variable models  
