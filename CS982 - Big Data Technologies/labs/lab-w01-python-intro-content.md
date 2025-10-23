---
title: "Week 01 — Python Intro (Lab Content)"
module: "CS982"
tags: [module/CS982, type/labs, week-01, content]
date: 2025-09-24
---

# Python Intro
*Week 01 Lab*

CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Before you start  
For all labs related to this module, you can use any Python editor/compiler that you are familiar  
with. However, it’s highly recommended to use the Jupyter Notebook provided by Anaconda.  
If you are using University computers, the software is already installed on all University computers.  
If you would like to install Anaconda on your own Personal Computer, please use the following link:  
https://www.anaconda.com/download  
Lab 1  
To start, launch the Anaconda Navigator application.  
Then launch the Jupyter Notebook within Anaconda:  
Once started, click on Desktop (or OneDrive to save your files on your OneDrive), locate a specific  
folder where you want to save all your lab materials or create a new folder if needed. Then click on  
New → Python 3 to create a new Python file to write Python code.  
Now you are ready to write Python\!\! So, let’s start.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part I – Let’s get started  
Question 1  
The following code will print out the text “Hello World\!\!” as it can be seen from the output below:  
Write (change) the code to display your name.  
Question 2  
Write (change) the code to display your name followed by your registration number but separated  
with the character “-“, for example as below:  
Question 3  
Write a Python program to print the following text:  
Question 4  
The following code will ask the user (the user is anyone using the application) for two numbers and  
they display the sum of the two numbers:  
Write (change) the code to display the multiplication of two numbers entered by the user.  
Question 5  
Change the code from the previous solution to display whether the multiplication is positive or  
negative. There are two solutions for this question, can you try to guess both of them.  
Question 6  
Change the code from the previous solution to display whether the multiplication is zero, positive or  
negative. There are two solutions for this question, can you try to guess both of them.  
Question 7  
Write a Python program that prints all the numbers from 0 to 50 except 37 and 16\. For this question,  
you need to use a loop either for or while.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Question 8  
Write a Python program to count the number of even and odd numbers from a series of numbers.  
For this reason, you need first to create a list of numbers and then count and display how many even  
and odd numbers there are in the list.  
Question 9  
Modify the solution of the previous question so the list can be generated randomly.  
Question 10  
In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two  
preceding ones. The sequence commonly starts from 0 and 1\. Starting from 0 and 1, the first few  
values in the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc.  
Write a Python program to calculate the first 30 values of the Fibonacci series.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Part II – Let’s explore some libraries and functions  
Question 11  
The code below will show the Python version installed on the computer. To do so, we need first to  
import the library sys, which provides access to some variables used or maintained by the  
interpreter and to functions that interact strongly with the interpreter. Once imported, we can use  
the attribute .version to display the Python version.  
Try this on your machine. If it shows a different version installed, it is still fine; this is just the version  
installed on your computer. More information about the library can be found using the following  
link: https://docs.python.org/3/library/sys.html  
Question 12  
Change the code from the previous question to display the platform (operating system) that you are  
using? Hint: Check the previously provided link.  
While the library sys might not be very important, there are other useful libraries that we will  
explore later.  
Question 13  
The code below will generate 30 random values between 0 and 100 and will store these numbers in  
a list called numbers. This will be done by (1) importing the library random. Then (2) we use the  
function .random(), which will return a random value between 0 and 1, and multiply the returned  
value by 100 to increase the range. Then (3) the value is converted into integer. (4) All of this will be  
done 30 times to generate 30 values that (5) will be stored in a list called numbers.  
To find the maximum in this list, we will have to go over all the numbers and check for the highest  
value, as shown in the below code.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
However, there is another simpler way to find the maximum in a list by using the built-in method /  
function called max, which will take a list as a parameter and will return the element from the list  
with the maximum value. Functions (or methods) are branches of coding that accomplish a specific  
task. We can of course create our own functions, if needed, but we can also use some functions  
written by others instead of writing our own functions.  
Use the same concept to find the minimum value in a list.  
Question 14  
Change the code from the previous solution to calculate and find the average or the arithmetic mean  
of the previously created list.  
Question 15  
Change the code from the previous solution (Question 13\) to generate 100 numbers with a range  
between \-500 and \+500. Then write Python code to do the following:  
1\. 2\. Split the list into two different lists: the first one for positive values only and the second list  
for negative values only.  
Calculate the count, maximum, minimum, and average for each of the two lists.CS989: Big Data Fundamentals  
CS982: Big Data Technologies  
Helpful materials  
If you are stuck, here are some bits of Python that you might find useful…  
Printing out strings and values:  
print("The value of n is", n)  
Simple conditionals:  
if n \< 100:  
print("n is less than 100")  
Conditionals using else:  
if a \> b:  
return(a)  
else:  
return(b)  
Conditionals using elif:  
if temp \< 20:  
print("too cold")  
elif temp \> 20:  
print("too hot”)  
else:  
print("just right")  
Using Blocks of indented code:  
if k \== 3:  
print("k is 3")  
k \= square(k)  
else:  
print("k is not 3")  
k \= k \+ 100  
return(k)  
Using while loops:  
while n \<= 10:  
print(n)  
n \= n \+ 1  
Testing for exact division:  
if n % 3 \== 0:  
print("n divides exactly by 3")  
