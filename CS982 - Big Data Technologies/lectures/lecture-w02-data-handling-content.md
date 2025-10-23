---
title: "Week 02 — Data Handling (Lecture Content)"
module: "CS982"
tags: [module/CS982, type/lectures, week-02, content]
date: 2025-10-01
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Data Handling
*Week 02 Lecture*

CS989 Big Data Fundamentals  
CS982 Big Data Technologies  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerLecture overview  
➢ An introduction to the definition, types, and significance of data  
➢ Techniques for examining and understanding data  
➢ Best practices for organizing, cleaning, and preparing data for analysis  
➢ Discussion: What Makes a Good Dataset?  
➢ Hands-on exploration of a dataset using PythonSelf-Attendance via MyPlace  
➢ Only works if you are already enrolled in the module on PegasusData  
This Photo by Unknown Author is licensed under CC BYFrom Datum to Dataset  
➢ Data is plural for ‘Datum’ – coming from Latin  
➢ Datum is a single factual, a single entity, a single point of matter  
➢ Datums are often referred to as ‘Data Points’  
➢ ‘Data’ represents a collection of data points  
➢ A ‘Dataset’ is also a collection of datapointsData  
➢ Raw, unprocessed Facts and statistics collected for reference or analysis  
➢ Can be numbers, text, symbols, measurements, or observations  
➢ On which operations are performed (by a computer)  
➢ Which may be stored and transmitted in the form of electrical signals and  
recorded on magnetic, optical, or mechanical recording mediaWhat Counts as Data?  
➢ A date  
➢ A name  
➢ A colour  
➢ A grade for an exam  
➢ A vote in an election  
➢ Your favourite movie  
➢ A number of clicks on a website  
➢ Time spent on a picture or a video  
➢ An index of poverty  
➢ A reading from a blood glucose meter  
➢ The step count from your phone for  
the last hour  
➢ The result from a lab test  
➢ Etc.Data, Information and Knowledge  
➢ **Data** is raw, unanalysed, unorganized material that is the result of observing  
events, environments, and ourselves by our senses and modern sensors  
➢ **Information** is the set of data that has already been processed, analysed,  
and structured in a meaningful way to become useful, and usually represents  
patterns that can be recognized from data.  
➢ Experience and intuition leads to **knowledge**, which makes sense of  
information within the context surrounding that information  
https://www.datacamp.com/cheat-sheet/the-data-information-knowledge-wisdom-pyramidKnowledge and Wisdom  
**Wisdom** represents human beliefs, purposes, values and judgement which  
allows us to make decisions based on knowledge  
➢ Knowledge is knowing that a tomato is a fruit  
➢ Wisdom is knowing not to put tomato in a fruit saladQualitative Data  
Spoken or narrative, gathered from:  
➢ Individual interviews  
➢ Focus groups  
➢ Observations  
Example \- “I was not feeling that well on Wednesday after my injection but by  
Thursday I was a lot worse. I rested and then took my meds and I was okay  
again by Friday.”Quantitative Data  
➢ Quantitative data are data about numeric variables (e.g. how many; how  
much; or how often)  
➢ There are two types of quantitative data, which is also referred to as numeric  
data:  
❖ Discrete data is a count that can't be made more precise e.g. 49/100 people contracted  
the disease  
❖ Measurements are continuous e.g. my blood glucose level was 4.91Exploring Data  
➢ It is tempting to start modelling when doing data analysis – avoid this\!\!  
➢ Gain an insight into the data \- this helps decide what data analysis methods  
are appropriate  
➢ Datasets are never (or rarely) perfect  
❖ Missing data  
❖ Corrupt data  
❖ Invalid data  
➢ A combination of summary statistics (and visualisation \- next week)Descriptive Statistics  
➢ Used to describe the basic features of the data in a study  
➢ They provide simple summaries about the sample and the measures  
➢ Brief descriptive coefficients that summarize a given dataset  
➢ Can be either a representation of the entire population or a sample of itDescriptive Statistics  
Areas of Interest for Descriptive Statistics  
Measures of  
Frequency  
Measures of Central  
Tendency  
Measures of  
Dispersion / Variation  
• Count  
• Percent  
• Frequency  
• Mean  
• Median  
• Mode  
• Position  
• Standard Deviation  
• Variance  
• Range  
• Interquartile Range  
(IQR)Measures of Frequency  
➢ Count: the total number of times a particular value occurs  
❖ Example: In a survey of 50 students, 12 students chose “Chocolate” as their favourite ice cream flavour.  
❖ Count (Chocolate) \= 12  
❖ Advantage: Simple and easy to calculate  
❖ Disadvantage: Doesn’t show proportion relative to total; hard to compare across different-sized datasetsMeasures of Frequency  
➢ Count: the total number of times a particular value occurs  
➢ Percent: the proportion of the total expressed as a percentage  
❖ Example: 12 out of 50 students like chocolate  
❖ Percent \= (12 ÷ 50\) × 100 \= 24%  
❖ Advantage: Standardized, easy to compare across groups of different sizes  
❖ Disadvantage: Requires knowing the total number; may hide absolute numbersMeasures of Frequency  
➢ Count: the total number of times a particular value occurs  
➢ Percent: the proportion of the total expressed as a percentage  
➢ Frequency: can refer to either the raw count or the relative occurrence of a value  
❖ Often used interchangeably with count or percent  
❖ Advantage: Gives a complete view of distribution; can be visualized in charts  
❖ Disadvantage: Can be confusing if “frequency” is not clearly defined (raw vs. relative)  
Flavour Count Percent  
Chocolate 12 24%  
Vanilla 20 40%  
Strawberry 18 36%Descriptive Statistics: Central Tendency  
Measures of Central Tendency  
➢ Mean  
➢ Median  
➢ ModeThe Mean  
➢ Mean is the arithmetic average computed by summing all the values in the  
dataset and dividing the sum by the number of data values  
➢ For a given dataset: \[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12\]The Mean  
➢ Mean is the arithmetic average computed by summing all the values in the  
dataset and dividing the sum by the number of data values  
➢ For a given dataset: \[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12\]  
Sum of data points \= (12+14+11+12+12+12+15+17+22+15+12) \= 154  
Number of data points \= (take a total count of observations) \= 11  
Mean \= (Divide sum of data points into total number of data points)  
\= 154 / 11 \= 14The Median  
➢ The middle number in the dataset (n / 2), when arranged in ascending order  
➢ For an odd numbers of observations, median is the (n+1) / 2 ordered value  
➢ For an even numbers of observations, median is average of the two middle  
values  
➢ For a given dataset: \[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12\]  
Ascending Order: \[11, 12, 12, 12, 12, 12, 14, 15, 15, 17, 22\]The Median  
➢ The middle number in the dataset (n / 2), when arranged in ascending order  
➢ For an odd numbers of observations, median is the (n+1) / 2 ordered value  
➢ For an even numbers of observations, median is average of the two middle  
values  
➢ For a given dataset: \[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12\]  
Ascending Order: \[11, 12, 12, 12, 12, **12**, 14, 15, 15, 17, 22\]  
Thus, the middle number in the dataset Median \= 12The Mode  
➢ Mode is the data point having the highest frequency \- maximum occurrences  
➢ For a given dataset: \[12, 14, 11, 12, 12, 12, 15, 17, 22, 15, 12\]The Mode  
➢ Mode is the data point having the highest frequency \- maximum occurrences  
➢ For a given dataset: \[**12**, 14, 11, **12**, **12**, **12**, 15, 17, 22, 15, **12**\]  
Maximum occurring data point or Mode \= 12Mean, Median, Mode: Strengths and  
Limitations  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
❖ Mean: …  
❖ Mode: …  
❖ Median: …Mean, Median, Mode: Strengths and  
Limitations  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
❖ Mean: 15  
❖ Mode: 15  
❖ Median: 15Mean, Median, Mode: Strengths and  
Limitations  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
❖ Mean: 15  
❖ Mode: 15  
❖ Median: 15  
➢ First set: 1, 10, 11, 12, 13, 14, 15, 15, 15, 15, 16, 17, 18, 19, 20, 29  
❖ Mean: …  
❖ Mode: …  
❖ Median: …Mean, Median, Mode: Strengths and  
Limitations  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
❖ Mean: 15  
❖ Mode: 15  
❖ Median: 15  
➢ First set: 1, 10, 11, 12, 13, 14, 15, 15, 15, 15, 16, 17, 18, 19, 20, 29  
❖ Mean: 15  
❖ Mode: 15  
❖ Median: 15Standard Deviation  
➢ Standard Deviation can be interpreted as the average distance of the  
individual observations from the mean  
➢ A higher standard deviation means the data points are more spread out from  
the meanVariance & Range  
➢ Variance is defined as the square of standard deviation  
Since variance involves squaring the differences, it tends to emphasize larger  
deviations from the mean. Standard deviation is more intuitive because it is in  
the same unit as the original data  
➢ Range is defined as the difference between the largest value in a dataset (or  
the maximum) and the smallest value in a dataset (or the minimum)Central Tendency  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
➢ First set: 1, 10, 11, 12, 13, 14, 15, 15, 15, 15, 16, 17, 18, 19, 20, 29Central Tendency vs. Variation  
➢ First set: 10, 10, 10, 11, 11, 11, 15, 15, 15, 15, 19, 19, 19, 20, 20, 20  
➢ First set: 1, 10, 11, 12, 13, 14, 15, 15, 15, 15, 16, 17, 18, 19, 20, 29Data Position and Interquartile Range  
➢ A quartile is any of the three values which divide the sorted dataset into four equal  
parts, so that each part represents one fourth of the sampled population  
➢ First quartile (designated Q1) \= lower quartile \= cuts off lowest 25% of data \= 25th  
percentile  
➢ Second quartile (designated Q2) \= median \= cuts dataset in half \= 50th percentile  
➢ Third quartile (designated Q3) \= upper quartile \= cuts off highest 25% of data, or  
lowest 75% \= 75th percentile  
➢ The difference between the upper and lower quartiles is called the interquartile  
rangeManaging Data  
This Photo by Unknown Author is licensed under CC BY-SAWhy Managing Data is Important?  
Source: https://decision.substack.com/p/what-is-vibe-codingWhy Managing Data is Important?Why Managing Data is Important?Why Managing Data is Important?  
Source: https://twitter.com/DeepLearningAI\_/status/1655579294893060097Why Managing Data is Important?  
Source: https://twitter.com/DeepLearningAI\_/status/1655579294893060097Managing Data  
➢ Data is very rarely clean  
❖ Have to deal with missing data  
❖ Transform data to work with  
➢ When we have missing data we have three basic options  
❖ (Re) Collect the missing parts  
❖ Drop (feature or observation)  
❖ Replace it with a meaningful valueMissing Data in Categorical Variables  
➢ Easy to create a new category missing  
➢ Gets around the problem of data being automatically dropped  
➢ Introduces a new variable which retains original data  
➢ We should have some interest in why data is missingMissing Numerical Data  
➢ If values are missing randomly then we could replace with a meaningful value e.g.  
mean  
❖ This assumes that missing data are distributed similarly and so this will be correct on average  
❖ Could be improved if we know how this is related to other data  
❖ Process is known as data imputation, more details available at this blog  
https://machinelearningmastery.com/handle-missing-data-python/  
➢ If not random then  
❖ Separate into categories (ranges) and treat missing values as for categorical variables  
❖ Replace with zeros (and add another variable to keep track of this)Data Transformations  
➢ Data transformations aim to make data easier to model and understand  
➢ Typical transformations include  
❖ Converting continuous data to discrete categories e.g. income ranges may be more useful  
than distinct values  
❖ Normalising and rescaling values when relative values are more meaningful than absolute  
ones e.g. income is likely to be region dependent. Also required for some modelling  
approaches  
❖ Log transformations for skewed distributions e.g. when data is spread over several orders  
of magnitudeDiscussion  
➢ Topic  
❖ What are the criteria for a “good” Dataset?  
❖ https://answergarden.ch/2749164  
➢ Things to consider:  
❖ No right or wrong answer  
❖ Agree on a group leaderDiscussion – 22/23Discussion – 23/24Discussion – 24/25Example Dataset  
➢ San Francisco City Employee salary data available from Kaggle \-  
https://www.kaggle.com/kaggle/sf-salaries  
➢ We will start exploration with the Pandas package  
➢ Built-in features include the ability to read data from many sources, create large  
dataframes (or matrixes / tables) from these sources and compute aggregate  
analytics based on what questions you’d like to answer  
➢ It has some built-in visualisations tools, we will come back to that next week when  
we look at other packages  
➢ Tutorials and details on Pandas are available online e.g.  
http://pandas.pydata.org/pandas-docs/stable/tutorials.htmlExample Dataset  
➢ Head returns first 5 lines of the dataSummary Statistics  
➢ Describe will tell you about the spread of the data, count, mean, min, max,  
quartiles, etc.Drill Down  
➢ Can use various methods to look at the data in lots of different ways  
