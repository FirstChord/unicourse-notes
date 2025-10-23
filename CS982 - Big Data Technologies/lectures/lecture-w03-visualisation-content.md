---
title: "Week 03 — Visualisation (Lecture Content)"
module: "CS982"
tags: [module/CS982, type/lectures, week-03, content]
date: 2025-10-08
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Visualisation
*Week 03 Lecture*

CS989 Big Data Fundamentals  
CS982 Big Data Technologies  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerLecture overview  
➢ Graphs and Visualisations  
➢ Visualising Distributions \- Single Variable  
➢ Visualising Distributions \- Multiple Variable  
➢ Discussion  
➢ Graphs and Visualisations \- DemoSelf-Attendance via MyPlace  
➢ Only works if you are already enrolled in the module on PegasusDescriptive Statistics \- Limitations  
➢ Does not reveal data distribution details  
❖ Skewness – it doesn’t provide enough information about the shape of the data distribution  
❖ Outliers – it can mask the presence of outliers  
➢ Ignores relationships between features  
❖ Univariate focus – it typically focuses on one variable at a time  
➢ Potential for Misleading Interpretations  
➢ Etc.DataSaurus Dozen  
Source: https://jumpingrivers.github.io/datasauRus/DataSaurus Dozen  
Source: https://juliasilge.com/blog/datasaurus-multiclass/Graphs and Visualisations  
➢ Summary statistics lose information  
➢ Visualisations can tell us a lot about data  
➢ We are going to use a few packages  
❖ Pandas  
❖ Numpy  
❖ Matplotlib  
❖ SeabornVisualising Distributions \- Single Variable  
➢ Interest in attributes of a variable such as:  
❖ Peak value and number of peaks  
❖ Shape of data – does it look normal or lognormal?  
❖ How much does it vary?  
➢ We are going to cover a number of approaches  
❖ Box Plots  
❖ Violin Plot  
❖ Histograms  
❖ Bar Charts  
❖ Density Plots  
❖ Pie ChartsBox Plots  
➢ Method for presenting numerical data through their quartiles  
➢ Whiskers indicate variability outside the upper and lower quartiles  
➢ Outliers may be plotted as individual points  
➢ Spacings between the different parts of the  
box indicate the degree of dispersion (spread)  
and skewness in the data, and show outliers  
➢ Box plots can be drawn either horizontally or verticallyBox Plots  
Source: https://www.simplypsychology.org/boxplots.htmlBox Plots \- Iris DatasetHistograms  
➢ Tell you where your data is concentrated and highlights outliers and  
anomalies  
➢ Bin variables into fixed-width buckets  
and returns the number of data points  
that fall into each bucketHistograms \- Pokemon DatasetDensity Plot  
➢ Continuous histogram where area under the curve equals 1  
➢ Avoid issue of choosing bin sizeDensity Plot  
➢ Sometimes plotting these figures on different scales can help visualise  
interesting things  
➢ For example using log scalesViolin Plot  
➢ Similar to box plots  
➢ They also show the probability density of the data at different values  
➢ Shows the full distribution of dataBox PlotViolin Plot vs. Box PlotViolin Plot with QuartilesViolin Plot & Swarm PlotBar Charts  
➢ Similar to Histogram, but for discrete data  
➢ Shows frequency of every value in a categorical variable  
➢ A categorical variable is a variable that  
can take on one of a limited, and usually  
fixed, number of possible valuesBar Charts \- Pokemon DatasetBar Charts  
➢ Can be better when there are more categories  
➢ Also can have more impact  
when flipped and sortedWhat am I?Pie ChartPie Charts  
➢ A circular statistical graphic divided into slices to illustrate numerical  
proportions  
➢ The arc length, central angle, and area of each  
slice are proportional to the quantity it represents  
➢ Widely used in business and mass media to  
present data visually  
➢ Can be difficult to compare the sizes of slices or to compare data across  
multiple pie chartsPie Charts  
Source: https://matplotlib.org/stable/gallery/lines\_bars\_and\_markers/bar\_stacked.htmlVisualising Distributions \- Multiple Variable  
➢ Show relationship between variables, how one varies with the another  
➢ Can help identify which variables are the best candidates to include in a  
model  
➢ We will look at a number of approaches  
❖ Line plots  
❖ Scatter plots  
❖ Bar charts for two categorical variables  
❖ HeatmapLine Plots  
➢ Works when the relationship between variables is fairly clean  
➢ Also values are close to uniqueLine PlotsLine Plots  
Source: https://fcpython.com/visualisation/visualising-running-totals-line-chartsScatter Plot  
➢ More useful if the data is not so cleanly related  
➢ Also allows you to see if data are  
related in some way (e.g. correlated)Scatter Plot  
Source: https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/Bar Charts for Two Categorical Variables  
➢ Sometimes data is not numerical but categorical belonging to a fixed  
number of states  
➢ There are several ways of visualising this  
➢ Stacked bar charts are one exampleBar Charts for Two Categorical Variables  
Source: https://matplotlib.org/stable/gallery/lines\_bars\_and\_markers/bar\_stacked.htmlBar Charts for Two Categorical Variables  
➢ Can also visualise the same data side by side  
➢ You can also fill the bars to make  
the ratios easier to see  
➢ Can also define multiple y-axes  
➢ Lots to exploreHeatmap  
➢ Data representation where values contained in a matrix are represented as  
colours  
➢ Correlation in our example, refers to how  
close two variables are to having a linear  
relationship with each other  
➢ In example the lighter the colour the  
stronger the correlationLooking for Correlations  
Standard correlation coefficient (aka Pearson's r) calculates strength of linear  
relationship: \+1 for a strong positive correlation, \-1 for a strong negative oneLooking for Correlations  
Standard correlation coefficient (aka Pearson's r) calculates strength of linear  
relationship: \+1 for a strong positive correlation, \-1 for a strong negative oneLooking for Correlations  
Standard correlation coefficient (aka Pearson's r) calculates strength of linear  
relationship: \+1 for a strong positive correlation, \-1 for a strong negative oneLooking for Correlations  
Standard correlation coefficient (aka Pearson's r) calculates strength of linear  
relationship: \+1 for a strong positive correlation, \-1 for a strong negative oneLooking for Correlations  
Standard correlation coefficient (aka Pearson's r) calculates strength of linear  
relationship: \+1 for a strong positive correlation, \-1 for a strong negative oneHeatmap  
➢ Data representation where values contained in a matrix are represented as  
colours  
➢ Correlation in our example, refers to how  
close two variables are to having a linear  
relationship with each other  
➢ In example the lighter the colour the  
stronger the positive correlationSummary  
➢ Take time to examine your data before modelling  
➢ Summary can help identify problems with data range unites, data types,  
missing values, invalid values etc.  
➢ Visualisation can tell you more about the data distribution and relationship  
between variables  
➢ Visualisation is iterative and helps answer questions about the data  
➢ Overall better to spend time here than waste it building modelsDiscussion \- BoxplotDiscussion \- BoxplotDiscussion \- BoxplotDiscussion \- BoxplotDiscussion  
➢ Topic  
❖ How to select the best graph to visualize my data?  
❖ https://answergarden.ch/2765824  
➢ Things to consider:  
❖ No right or wrong answer  
❖ Discuss and agree on what to addDiscussion – 2022/2023Discussion – 2023/2024Discussion – 2024/2025How to Choose a Chart Type  
➢ How to Choose a Chart Type (that describes your data best) \- Sara A. Metwalli  
❖ What’s the story your data is trying to deliver?  
❖ Who will you present your results to?  
❖ How big is your data?  
❖ What is your data type?  
❖ How do the different elements of your data relate to each other?  
https://towardsdatascience.com/data-visualization-101-how-to-choose-a-chart-type-9b8830e558d6Discussion – “unreadable” graphs  
This Photo by Unknown Author is licensed under CC BY-SADiscussion – “unreadable” graphs  
Source: https://www.addtwodigital.com/add-two-blog/2022/5/4/rule-31-line-charts-shouldnt-have-too-many-linesDiscussion – “unreadable” graphs  
Source: https://commadot.com/pie-charts-are-almost-always-bad-ux/Discussion – “unreadable” graphs  
Source: https://stackoverflow.com/questions/53809507/correlation-plot-of-high-dimensional-data-looks-unreadable  
