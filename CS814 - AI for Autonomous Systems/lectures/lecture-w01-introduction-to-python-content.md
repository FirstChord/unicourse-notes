---
title: "Week 01 — Introduction to Python (Lecture Content)"
module: "CS814"
tags: [module/CS814, type/lectures, week-01, content]
date: 2025-09-24
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Introduction to Python
*Week 01 Lecture*

Introduction to PythonWhy Python?  
➢ Provides good support for the kind of problems we will be looking at,  
➢ Very popular language and used widely in industry for AI,  
➢ Easy to learn and implement,  
➢ Allows access and use of other technologiesPython Syntax  
➢ Python is divided into logical lines, where every line is ended by a NEWLINE token  
➢ Comments begin with the \# character and end at the NEWLINE token  
➢ If you want to write a longer line you can use the \\ character  
➢ You can write two separate statements into a single line using a ;  
➢ Python uses whitespace (spaces and tabs) to define program blocks  
➢ There are reserved words in the language that must be used for specific purposes, we  
will come across these as we progress  
➢ https://www.w3schools.com/python/What is an Algorithm?  
➢ An algorithm is a list of instruction, once executed correctly, will lead to the  
desired result,  
➢ It should contain only instructions that can be understood by the one who/that  
will execute it,  
➢ The methodical step-by-step checking of your algorithm represents more  
than half of the work to be done \!\!DNA vs. Computers  
➢ DNA, which is in a way the genetic program, the algorithm  
at the basis of the construction of human being, is a chain  
constructed from four invariable elements: adenine (A),  
guanine (G), cytosine (C), and thymine (T)DNA vs. Computers  
➢ DNA, which is in a way the genetic program, the algorithm  
at the basis of the construction of human being, is a chain  
constructed from four invariable elements: adenine (A),  
guanine (G), cytosine (C), and thymine (T)  
➢ Computers, whatever they are, are basically capable of  
understanding only four categories of instructions:  
❖ The Input / Output instructions  
❖ Assignment instructions  
❖ Arithmetic and Logical instructions  
❖ Conditional and unconditional instructions  
The Input / Output  
instructions  
Assignment  
instructions  
Algorithms  
Arithmetic and  
Logical instructions  
Conditional and  
unconditional  
instructionsAlgorithms DNA  
The Input / Output  
instructions  
Assignment  
instructions  
Algorithms  
Arithmetic and  
Logical instructions  
Conditional and  
unconditional  
instructionsThe Input / Output instructions  
Input  
OutputThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Output  
print (“Hello World\!”)  
Hello World\!  
Python ScreenThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Output  
❖ print(object(s), sep=separator, end=end, file=file, flush=flush)The Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Output  
❖ print(object(s), sep=separator, end=end, file=file, flush=flush)  
print("Hello", "Joseph", sep=" ", end=“\!\!")  
Hello Joseph\!\!  
Python ScreenThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Output  
❖ print(object(s), sep=separator, end=end, file=file, flush=flush)  
❖ https://www.w3schools.com/python/ref\_func\_print.aspThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Input  
input (“Please enter your name: “)  
Please enter your name: \_  
Python ScreenPython Variables  
➢ A variable is a memory location where a value can be stored  
➢ This value can be a string, a number, etc., e.g. “Joseph", 180, 99.999  
➢ Variables are created when first assigned  
➢ Once created, the value stored can be accessed or updated later  
➢ Python determines the variable type (string, int, float etc.)  
➢ Memory is allocated based on the data type of a variable  
➢ There are rules for naming variables:  
https://www.w3schools.com/python/python\_variables.aspThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Input  
name \= input (“Please enter your name: “)  
print("Hello", name, sep=" ", end=“\!\!")  
Please enter your name: \_  
Python ScreenThe Input / Output instructions  
➢ Input/Output is the communication between an information processing  
system, such as a computer, and the outside world, possibly a human or  
another information processing system  
➢ Input  
name \= input (“Please enter your name: “)  
print("Hello", name, sep=" ", end=“\!\!")  
Please enter your name: Joseph  
Hello Joseph\!\!  
Python ScreenAlgorithms DNA  
The Input / Output  
instructions  
Assignment  
instructions  
Algorithms  
Arithmetic and  
Logical instructions  
Conditional and  
unconditional  
instructionsAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
https://en.wikipedia.org/wiki/Assignment\_(computer\_science)Assignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
➢ \= sign is used to assign variables  
➢ You can assign a value to more than one variable simultaneously, singly or  
multiple  
➢ You can reassign variables, including type  
➢ You can swap values in a single line  
➢ Variables can be global or localAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x \= 5  
y \= "John"  
print(x)  
print(y)  
5  
John  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x \= 5  
print(x)  
x \= "John"  
print(x)  
5  
John  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x, y \= 5, "John"  
print(x)  
print(y)  
5  
John  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x, y \= 5, "John"  
print("x \= ", x)  
print("y \= ", y)  
x, y \= y, x  
print("x \= ", x)  
print("y \= ", y)  
x \= 5  
y \= John  
x \= John  
y \= 5  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x \= 5  
print(x)  
print(y)  
y \= "John"  
ERROR\!\!\!  
NameError: name 'y' is not defined  
Python ScreenPython Data Types  
➢ Numbers: Integers, Floating point numbers, Complex numbers  
➢ Boolean (bool)  
➢ Strings  
❖ Strings have special characters  
❑ \\n Newline  
❑ \\t Horizontal Tab  
❑ \\\\ Backslash  
❑ \\' Single Quote  
❑ \\" Double QuotePython Data Types  
➢ Tuples: Container which holds a series of comma-separated values between  
parentheses  
➢ List: Container which holds comma-separated values (items or elements)  
between square brackets  
➢ Set: An unordered collection of unique elements  
➢ Dictionary: Container of the unordered set of objects like lists. Objects are  
surrounded by curly braces { }. The items are a comma-separated list of  
key:value pairs where keys and values are Python data types  
➢ Etc.  
https://www.w3schools.com/python/python\_datatypes.aspAlgorithms DNA  
The Input / Output  
instructions  
Assignment  
instructions  
Algorithms  
Arithmetic and  
Logical instructions  
Conditional and  
unconditional  
instructionsArithmetic and Logical instructions  
➢ The arithmetic (and logical) instructions define the set of operations  
performed by the processor Arithmetic Logic Unit (ALU)  
https://www.sciencedirect.com/topics/computer-science/arithmetic-instructionArithmetic and Logical instructions  
➢ The arithmetic (and logical) instructions define the set of operations  
performed by the processor Arithmetic Logic Unit (ALU)  
https://www.sciencedirect.com/topics/computer-science/arithmetic-instruction  
➢ Arithmetic Operators  
➢ Comparison Operators  
➢ Logical Operators  
➢ Assignment Operators  
➢ Bitwise Operator  
➢ Conditional OperatorsAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x, y \= 3, 5  
z \= x \+ y  
print(“The sum is ", z)  
The sum is 8  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
firstNb, secondNb \= 3, 5  
sumNbs \= firstNb \+ secondNb  
print(“The sum is ", sumNbs)  
The sum is 8  
Python ScreenAssignment instructions  
➢ An assignment statement sets and/or re-sets the value stored in the storage  
location(s) denoted by a variable name; in other words, it copies a value into  
the variable  
x, y \= 3, 5  
z \= x \+ y  
print(“The sum is ", z)  
The sum is 8  
Python Screen  
Reading: https://www.techtarget.com/whatis/definition/operatorAlgorithms DNA  
The Input / Output  
instructions  
Assignment  
instructions  
Algorithms  
Arithmetic and  
Logical instructions  
Conditional and  
unconditional  
instructionsConditional and unconditional instructions  
➢ A branch is an instruction in a computer program that can cause a computer  
to begin executing a different instruction sequence and thus deviate from its  
default behaviour of executing instructions in order.  
➢ A branch instruction can be either an unconditional branch, which always  
results in branching, or a conditional branch, which may or may not cause  
branching depending on some condition  
➢ https://en.wikipedia.org/wiki/Branch\_(computer\_science)Python – if elif else  
➢ if expression :  
❖ statement\_1  
❖ statement\_2  
➢ elif expression2 :  
❖ statement\_3  
❖ statement\_4  
❖ Etc.  
➢ else:  
❖ statement\_5  
❖ statement\_6  
❖ Etc.  
➢ You can use Boolean logic and operators in your expressionsPython – if elif else  
Python Screen  
x, y \= 3, 5  
if (x \>= y):  
print(“First number is bigger.")  
else:  
print(“Second number is bigger.")  
Second number is bigger.  
Reading: https://www.w3schools.com/python/python\_conditions.aspPython – if elif else  
Python Screen  
x, y \= 3, 5  
if (x \>= y):  
print(“First number is bigger.")  
else:  
print(“Second number is bigger.")  
Second number is bigger.  
x, y \= 9, 5  
if (x \>= y):  
print(“First number is bigger.")  
else:  
print(“Second number is bigger.")  
First number is bigger.  
Reading: https://www.w3schools.com/python/python\_conditions.aspPython – loop (for)  
➢ for variable\_name in sequence :  
❖ statement\_1  
❖ statement\_2  
❖....  
➢ Can be used with the range function or to iterate over a data type  
❖ range(a)  
❖ range(a,b)  
❖ range(a,b,c)  
➢ https://www.w3schools.com/python/python\_for\_loops.aspPython – loop (while)  
➢ while (expression) :  
❖ statement\_1  
❖ statement\_2  
❖ Etc.  
➢ else :  
❖ statement\_3  
❖ statement\_4  
❖ Etc.  
➢ https://www.w3schools.com/python/python\_while\_loops.aspPython – continue / break  
➢ while (expression1) :  
❖ statement\_1  
❖ Etc.  
❖ if expression2 :  
❑ break  
➢ for variable\_name in sequence :  
❖ if expression3 :  
❑ continue  
❖ statement\_1  
❖ Etc.  
➢ https://www.w3schools.com/python/python\_while\_loops.aspPython – Sample Code  
Python Screen  
\#for loop, a very hacky one  
for x in range(10):  
\#check if x is 5  
if x==5:  
break  
if x==3:  
continue  
print(x)  
print("Finished loop\!")  
0  
1  
2  
4  
Finished loop\!Python – Sample Code  
Python Screen  
\#while loop  
x=0  
while x \< 5:  
if x==3:  
x \= x \+ 1  
continue  
print(x)  
x \+= 1  
print("Finished loop\!")  
0  
1  
2  
4  
Finished loop\!Python – Sample Code  
Python Screen  
\#while loop  
x=0  
while x \< 5:  
if x==3:  
x \= x \+ 1  
continue  
print(x)  
x \+= 1  
print("Finished loop\!")  
0  
1  
2  
4  
Finished loop\!  
Reading: https://www.w3schools.com/python/python\_conditions.aspWhere to write Python?  
➢ Online editors and compilers  
❖ https://www.online-python.com/  
❖ https://www.programiz.com/python-programming/online-compiler/  
❖ https://colab.research.google.com/  
➢ Local editors and compilers  
❖ https://www.anaconda.com/products/distribution  
❖ https://code.visualstudio.com/Where to write Python?  
➢ Online editors and compilers  
❖ https://www.online-python.com/  
❖ https://www.programiz.com/python-programming/online-compiler/  
❖ https://colab.research.google.com/  
➢ Local editors and compilers  
❖ https://www.anaconda.com/products/distribution  
❖ https://code.visualstudio.com/Where to write Python?  
➢ Visualize code in Python (online)  
❖ https://pythontutor.com/visualize.html\#mode=edit  
➢ Online help:  
❖ Introduction to Python Module:  
https://classes.myplace.strath.ac.uk/course/view.php?id=25576  
❖ W3schools:  
https://www.w3schools.com/python/  
❖ ChatGPT\!\! YES:  
https://chatgpt.com/  
