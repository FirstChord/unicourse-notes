---
title: "Week 03 — Problems and Algorithms (Lecture Content)"
module: "CS814"
tags: [module/CS814, type/lectures, week-03, content]
date: 2025-10-08
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Problems and Algorithms
*Week 03 Lecture*

***Problems and Algorithms***  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerLearning outcomes  
By the end of this lecture, you will be able to:  
1\. 2\. 3\. 4\. 5\. Define a problem within the context of CS  
Identify examples of common problems in CS  
Understand what an algorithm is and its role in  
problem-solving  
Describe the simplest AI environment  
Differentiate between explicit and implicit graphsWhat is Computer Science?  
• Computer Science is the study of *algorithms*, the  
machines that make their automation possible and the  
uses to which those automated algorithms can be put  
• The agent program, which we discussed in the  
previous lecture, is one such application. It is the key  
component that enables the automation of an  
Intelligent AgentWhat is Computer Science?  
• Computer Science is the study of *algorithms*, the  
machines that make their automation possible and the  
uses to which those automated algorithms can be put  
• First algorithm: Euclid (300 BC) \- efficient method for  
computing the greatest common divisor (GCD) of two  
integers  
https://en.wikipedia.org/wiki/Euclidean\_algorithm  
• first real electronic computer with a stored program:  
Manchester Mark 1 (1949)What is Computer Science?  
• Computer Science is the study of *algorithms*, the  
machines that make their automation possible and the  
uses to which those automated algorithms can be put  
• First algorithm: Euclid (300 BC); first real electronic  
computer with a stored program: Manchester Mark 1  
(1949)  
• A Computer Scientist is someone who studies a  
*problem*, develops an *algorithm* to solve it, and then  
turns that algorithm into a working, efficient *computer*  
*program* that serves as the solution to the problemWhat is a Problem?  
• Usual meaning of ‘problem’ is something specific to  
be solved: e.g. ‘I can not find my keys.’What is a Problem?  
• Usual meaning of ‘problem’ is something specific to  
be solved: e.g. ‘I can not find my keys.’  
• In Computer Science a *problem* is a name used for  
*all* specific problems of a certain typeWhat is a Problem?  
• Usual meaning of ‘problem’ is something specific to  
be solved: e.g. ‘I can not find my keys.’  
• In Computer Science a *problem* is a name used for  
*all* specific problems of a certain type  
• The specific problems to be solved by the computer  
are called *instances* of the problemExample Problems  
• Given an unsorted list of numbers, find the largest  
number in the list  
\[11, \-5, 13\]: the largest number is 13Example Problems  
• Given an unsorted list of numbers, find the largest  
number in the list  
\[11, \-5, 13\]: the largest number is 13  
\[5,3,1,7,5,3,11,1\]: the largest number is 11Example Problems  
• Given an unsorted list of numbers, find the largest  
number in the list  
• Given an unsorted list of numbers, sort them into  
ascending order  
\[13,-5,11\] \=\> \[-5,11,13\]Example Problems  
• Given an unsorted list of numbers, find the largest  
number in the list  
• Given an unsorted list of numbers, sort them into  
ascending order  
\[13,-5,11\] \=\> \[-5,11,13\]  
\[5,3,1,7,5,3,11,1\] \=\> \[1,1,3,3,5,5,7,11\]Example Problems  
• Given an unsorted list of numbers, find the largest  
number in the list  
• Given an unsorted list of numbers, sort them into  
ascending order  
• Given a set of cities with roads between them, find the  
fastest route between two named cities  
• Given a set of cities with roads between them, find the  
shortest route that visits every city on the mapWhat is an Algorithm?  
• An algorithm is a finite set of instructions for solving  
a problem, which, given a well-defined initial state,  
will result in a corresponding well-defined end-stateWhat is an Algorithm?  
• An algorithm is a finite set of instructions for solving  
a problem, which, given a well-defined initial state,  
will result in a corresponding well-defined end-state  
• Think of it as the precise instructions for solving a  
problem  
list of numbers: \[1,5,3\]  
find the maximum number?What is an Algorithm?  
• An algorithm is a finite set of instructions for solving  
a problem, which, given a well-defined initial state,  
will result in a corresponding well-defined end-state  
• Think of it as the precise instructions for solving a  
problem  
list of numbers: \[1,5,3\]  
Step 1: max \= \-infinity  
Step 2: compare 1 with max, max \= 1  
Step 3: compare 5 with max, max \= 5  
Step 4: compare 3 with max, max \= 5What is an Algorithm?  
• An algorithm is a finite set of instructions for solving  
a problem, which, given a well-defined initial state,  
will result in a corresponding well-defined end-state  
• Think of it as the precise instructions for solving a  
problem  
• A well-specified algorithm will solve *all* specific  
instances of the problem  
• An algorithm will *always* terminate in a finite number  
of stepsThe Google Maps ProblemFormalising the ProblemFormalising the ProblemA Possible Algorithm?  
1\. Let S be the start city and G be the goal cityA Possible Algorithm?  
1\. Let S be the start city and G be the goal city  
2\. Create a path \[S\] and add it to the set of paths, PA Possible Algorithm?  
1\. 2\. 3\. Let S be the start city and G be the goal city  
Create a path \[S\] and add it to the set of paths, P  
Remove the shortest path from P and call it SPA Possible Algorithm?  
1\. 2\. 3\. 4\. Let S be the start city and G be the goal city  
Create a path \[S\] and add it to the set of paths, P  
Remove the shortest path from P and call it SP  
If SP ends in G, return SP and haltA Possible Algorithm?  
1\. 2\. 3\. 4\. 5\. Let S be the start city and G be the goal city  
Create a path \[S\] and add it to the set of paths, P  
Remove the shortest path from P and call it SP  
If SP ends in G, return SP and halt  
For every city you can reach from the end of SP in a  
single step where it doesn’t loop back on itself, make  
a new path and add it to PA Possible Algorithm?  
1\. 2\. 3\. 4\. 5\. Let S be the start city and G be the goal city  
Create a path \[S\] and add it to the set of paths, P  
Remove the shortest path from P and call it SP  
If SP ends in G, return SP and halt  
For every city you can reach from the end of SP in a  
single step where it doesn’t loop back on itself, make  
a new path and add it to P  
6\. Go to Step 3Being a Computer Scientist  
1\. 2\. 3\. 4\. 5\. 6\. Find a problem you’d like to automate  
Formalise the problem, i.e. make it mathematically  
precise  
Design an algorithm that will solve the problem  
Test the algorithm to make sure it works correctly  
Turn the algorithm into a computer program  
Test the program to make sure it works correctlyThe Simplest AI Environments  
What are the simplest environments for our AI agents?The Simplest AI Environments  
What are the simplest environments for our AI agents?  
• Fully observable (rather than partially observable)  
• Single agent (rather than multi-agent)  
• Deterministic (rather than stochastic)  
• Static (rather than dynamic)  
• Discrete (rather than continuous)  
• Sequential (rather than Episodic)  
• Time unlimited (rather than time limited)The Simplest AI Environments  
What are the simplest environments for our AI agents?  
• Fully observable (rather than partially observable)  
• Single agent (rather than multi-agent)  
• Deterministic (rather than stochastic)  
• Static (rather than dynamic)  
• Discrete (rather than continuous)  
• Sequential (rather than Episodic)  
• Time unlimited (rather than time limited)  
For problems like this, search is often the right solutionExplicit Graphs  
Explicit graphs are ones where you can hold the whole  
of the graph in memory  
start  
goalExplicit Graphs  
Explicit graphs are ones where you can hold the whole  
of the graph in memory  
start  
goalImplicit Graphs  
Implicit graphs are ones where the graph is too large to  
hold in memory (it may even be infinite):  
goal  
startImplicit Graphs – Example  
The travelling salesman problem:  
• Suppose we have n cities:  
• For 1st city, n choices  
• For 2nd city, n-1 choices  
• Etc.  
• n \* (n-1) \* (n-2) \* … \* 1 \= n\!  
• Hence, have n\! sequences  
• But reversing the sequence is considered the same  
tour  
• Hence, n\! / 2 possible toursImplicit Graphs – Example  
Combinatorial Explosion:  
• 10 cities TSP \=\> 1,814,400 possible solutions  
• 20 cities TSP \=\> 1,216,451,004,088,320,000 possible  
solutions \= 1.2 \* 1018  
• 50 cities TSP \=\> 15,207,046,600,856,689,021,806,  
304,083,032,384,422,188,820,784,480,256,000,000,0  
00,000 possible solutions \= 1.52 \* 1064Implicit Graphs – Example  
Combinatorial Explosion:  
• 50 cities TSP \=\> 1.52 \* 1064 possible solutions  
• Age of the universe is 15 billion (1.5 \* 1010) years  
• 30 million seconds in a year  
• Age of the universe: 45 \* 1016 secondsImplicit Graphs – Example  
Combinatorial Explosion:  
• 50 cities TSP \=\> 1.52 \* 1064 possible solutions  
• Age of the universe is 15 billion (1.5 \* 1010) years  
• 30 million seconds in a year  
• Age of the universe: 45 \* 1016 seconds  
• 10GHz computer can evaluate 109 paths per second  
• Running since start of the universe: 1026 paths  
• Not even close to evaluating all pathsHow To Search Huge Graphs  
• Don’t try to hold the whole graph in memory\!  
• Instead, we have the start state (*s0*), the goal state (*g*)  
and a function called *next-states(s)*  
• *next-states(s)* computes those states which we can  
get to from state *s* in a single action  
• To do the search, apply *next-states* to *s0* to give a list  
of states, then apply *next-states* to those states  
• Keep doing this until state *g* appears in the listProblem Solving using Search  
Many problems in AI involve *deliberative reasoning*,  
leading to search in very big implicitly-defined graphs:  
• Path finding in robotics  
• Blocks World planning  
• Rubik’s cube  
• Logistics planning  
• Task scheduling  
• Data mining  
• Machine learningDiscussion  
This Photo by Unknown Author is licensed under CC BY-NC-NDDiscussion  
**Turning a Classroom Door into an Autonomous Agent**  
• Distinguish between: **Environment** vs. **Physical Agent**  
vs. **Intellectual (part of the) Agent**,  
• Identify the properties of the agent **(PEAS)**,  
• Identify the properties of the **Environment**: Fully or  
Partially Observable / Single or Multi-Agent /  
Deterministic or Stochastic / Episodic or Sequential /  
Static or Dynamic / Discrete or ContinuousGroup Activity  
**Turning a Classroom Door into an Autonomous Agent**  
• 4 Groups Total:  
❖ 2 groups → focus on **PEAS (Agent)**  
❖ 2 groups → focus on **Environment Properties**  
• 15 Minutes discussions: brainstorm and agree on your  
group’s conclusions  
• Select a Group Leader: Present your findings (2–3  
minutes per group)Agent Overview  
**Turning a Classroom Door into an Autonomous Agent**  
• Opens, closes, and locks automatically,  
• Responds to people, schedules, and environment,  
• Ensures comfort, safety, and energy efficiencyPEAS Framework  
**Possible solution**  
• Performance measure: Opens/closes at correct times, ensures  
safety & security, maintains comfort (& energy efficiency),  
responds smoothly and safely.  
• Environment: Classroom & hallway, students, teachers, visitors,  
class schedules, (alarms, lighting, temperature).  
• Actuators: Door motor, locking mechanism, display or indicator  
lights, audio alerts or voice assistant, etc.  
• Sensors: Motion/proximity sensors, ID / Facial recognition,  
camera & microphone, (temperature or CO₂ sensors), etc.The system  
**How the system works?**  
• Detects people approaching→ decides to open or stay locked  
• Uses schedule to manage access automatically  
• Unlocks for emergencies (e.g., fire alarm)  
• (Learns usage patterns over time)Environment Characteristics  
**Possible solution**  
• Single-Agent? Yes (humans parts of the environment),  
• Fully observable? Partially observable,  
• Deterministic? Mostly, but humans add uncertainty,  
• Discrete? Continuous (Time and motion are continuous),  
• Static? Dynamic (Environment changes constantly)  
• Sequential? Yes– past actions affect future states,  
