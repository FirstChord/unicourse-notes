---
title: "Week 04 — Problems and Search (Lecture Content)"
module: "CS814"
tags: [module/CS814, type/lectures, week-04, content]
date: 2025-10-15
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Problems and Search
*Week 04 Lecture*

***Problems and Search***  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerPresentation outline  
1\. Why Search?  
2\. Classic AI Search Problems  
3\. Problem Formulation  
4\. Problem Formulation – Examples  
5\. Search Methods  
6\. The river problem as an exampleWhy Search?  
All AI is search\!  
1\. Not totally true (obviously) but more true than you  
might think.  
2\. Finding a good/best solution to a problem amongst  
many possible solutionsClassic AI Search ProblemsClassic AI Search ProblemsClassic AI Search ProblemsClassic AI Search ProblemsClassic AI Search ProblemsClassic AI Search ProblemsProblem Formulation  
A Problem Space consists of:  
• The current state of the world (**initial state**),  
• A description of the desired state of the world (**goal**  
**state**); this could be implicit or explicit,  
• A description of the **actions** we can take to transform  
one state of the world into another (**operators**).  
Take your time with the problem formulation\!\!Solutions  
• Solutions are **sequences of moves** which transform  
the **initial** state into the **goal** state  
• The quality of the solution required will affect the  
amount of work we need to do  
– any solution will do  
– fixed amount of time, return good solution  
– near optimal solution needed  
– optimal solution neededState Space Representation  
• A good formulation saves work  
– less search for the answer  
• Three requirements for a search algorithm:  
– formal structures to describe the states  
– rules for manipulating them  
– identifying what constitutes a solution  
• This gives us a **state space representation**State Space Representation  
• A state space comprises  
– states: snapshots of the problem  
– operators: how to move from one state to another  
Example problem:  
Missionaries and Cannibals  
Moving 1 or 2 from one side  
to another  
Never leave missionaries  
outnumbered by cannibalsState Space Search  
Problem solving using state space search consists of  
the following four steps:  
1\. Design a representation for states (including the  
initial state and the goal state)  
2\. Characterise the operators  
3\. Build a goal state recogniser  
4\. Search through the state space somehow by  
considering (in some or other order) the states  
reachable from the initial and goal states8-Puzzle Game8-Puzzle Game  
Representing the states:  
1\. 3 by 3 array  
2 1 3  
4 7 6  
5 8 0  
2\. A vector of length 9  
2, 1, 3, 4, 7, 6, 5, 8, 0  
3\. A list of facts  
Upper\_left \= 2  
Upper\_middle \= 1  
etc.8-Puzzle Game  
Specifying operators:  
1\. Each piece:  
Move 1 left  
Move 1 right  
Move 1 up  
Move 1 down  
Etc.  
2\. Only for the blank:  
Slide blank / 0 left  
Slide blank / 0 right  
Slide blank / 0 up  
Slide blank / 0 down8-Puzzle GameThe missionaries and cannibals problemThe missionaries and cannibals problem  
Representing the states:  
\[C, M, B\]  
Initial state: \[3, 3, 1\]  
Final state: \[0, 0, 0\]The missionaries and cannibals problem  
Representing the states:  
\[C, M, B\]  
Initial state: \[3, 3, 1\]  
Final state: \[0, 0, 0\]  
Operators:  
Travel Across Travel Back  
\- \[1, 0, 1\] \[1, 0, 1\]  
\- \[2, 0, 1\] \[2, 0, 1\]  
\- \[0, 1, 1\] \[0, 1, 1\]  
\- \[0, 2, 1\] \[0, 2, 1\]  
\- \[1, 1, 1\] \[1, 1, 1\]The missionaries and cannibals problem  
Representing the states:  
\[C, M, B\]  
Initial state: \[3, 3, 1\]  
Final state: \[0, 0, 0\]  
Operators:  
Travel Across Travel Back  
\- \[1, 0, 1\] \[1, 0, 1\]  
\- \[2, 0, 1\] \[2, 0, 1\]  
\- \[0, 1, 1\] \[0, 1, 1\]  
\- \[0, 2, 1\] \[0, 2, 1\]  
\- \[1, 1, 1\] \[1, 1, 1\]  
Path Cost: Number of crossingsSummary  
• Search: process of constructing sequences of actions  
that achieve a goal given a problem.  
• It is assumed that the environment is observable,  
single-agent, deterministic, static, sequential, and  
discrete.  
• Goal formulation is the first step in solving problems  
by searching. It facilitates problem formulation.  
• Formulating a problem requires specifying three  
components: State representation (including Initial  
state and Goal state), Operators (Actions and  
Validations), and Path cost functionSearch Spaces  
• The search space of a problem is implicit in its  
formulation  
– You search the space of your representations  
• We generate the space dynamically during search  
(including loops, dead ends, branches)  
• Operators are move generators  
• We can represent the search space with trees  
• Each node in the tree is a state  
• When we call NextStates(*S0*) → \[*S1*,*S2*,*S3*\], then we  
say we have expanded *S0*Basic Search Algorithms  
• **Uninformed (Blind) search**: breadth-first, depth-first,  
depth limited, iterative deepening, bidirectional  
search, and Uniform cost searchBasic Search Algorithms  
• **Uninformed (Blind) search**: breadth-first, depth-first,  
depth limited, iterative deepening, bidirectional  
search, and Uniform cost search  
• **Informed (Heuristic) search**: search is guided by an  
evaluation function: Greedy best-first, A\*, IDA\*, etc.Basic Search Algorithms  
• **Uninformed (Blind) search**: breadth-first, depth-first,  
depth limited, iterative deepening, bidirectional  
search, and Uniform cost search  
• **Informed (Heuristic) search**: search is guided by an  
evaluation function: Greedy best-first, A\*, IDA\*, etc.  
• **Game playing**, an adversarial search: minimax  
algorithm, alpha-beta pruningBasic Search Algorithms \- Comparison  
• **Completeness**: Is the technique guaranteed to find  
an answer (if there is one)  
• **Optimality**: does it always find a least-cost solution?  
An optimal algorithm will find a solution with minimum  
cost  
• **Time Complexity**: How long does it take to find a  
solution  
• **Space Complexity**: How much memory does it take  
to find a solutionBasic Search Algorithms \- Comparison  
• The average number of new nodes we create when  
expanding a new node is the effective branching  
factor **b**  
• The maximum branching factor **max(b)** is defined as  
the maximum nodes created when a new node is  
expanded  
• The length of a path to a goal is the depth **d**  
• The maximum length of any path in the state space **m**Basic Search Algorithms \- Comparison  
• The eight puzzle has a effective  
branching factor of 2.67, so a search  
tree at depth 20 has about 127 million  
nodes  
• Rubik’s cube has a effective branching  
factor of 13.34. There are 901,083,404,  
981,813,616 different states. The  
average depth of a solution is about 18  
• Chess has a branching factor of about  
35, there are about 10120 states.Expanding Nodes in the Search SpaceDepth-First Search  
*S0*  
*S1*  
*S6*  
*S10*Depth-First Search  
*S1*  
*S2*  
*S4*  
*S0*  
*S6*  
*S10*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S3*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S3*  
*S5*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S7*  
*S3*  
*S5*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S7*  
*S3 S9S5*  
*S8*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S7*  
*S3 S9S5*  
*S8*Depth-First Search  
*S0*  
*S1*  
*S6*  
*S10*  
*S2*  
*S4*  
*S7*  
*S3 S9S5*  
*S8*Depth-First Search  
• To get depth-first (a.k.a. LIFO) search, remove the last  
item added into the agenda (treat the agenda as a  
stack):  
Agenda \= \[*S0*\]  
while Agenda ≠ \[\] do  
Current \= remove-last(Agenda)  
if Goal(Current) then return(“Found it\!”)  
Next \= NextStates(Current)  
for nx in Next  
if nx not in Agenda  
Agenda \= Agenda \+ nxBreadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S4*  
*S5*  
*S3*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S4*  
*S5*  
*S6*  
*S3*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*  
*S5*  
*S4 S8S6*  
*S7*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*  
*S5*  
*S4 S8*  
*S6*  
*S7*  
*S9*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*  
*S5*  
*S4 S8*  
*S6*  
*S7*  
*S9*  
*S10*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*  
*S5*  
*S4 S8*  
*S6*  
*S7*  
*S9 S12 S13 S14S10*  
*S11*Breadth-First Search  
*S0*  
*S1*  
*S2*  
*S3*  
*S5*  
*S4 S8*  
*S6*  
*S7*  
*S9 S12 S13 S14S10*  
*S11*Breadth-First Search  
• To get breadth-first (a.k.a. FIFO) search, remove the  
first item added into the agenda (treat the agenda as  
a queue):  
Agenda \= \[*S0*\]  
while Agenda ≠ \[\] do  
Current \= remove-first (Agenda)  
if Goal(Current) then return(“Found it\!”)  
Next \= NextStates(Current)  
for nx in Next  
if nx not in Agenda  
Agenda \= Agenda \+ nxDepth-Limited Search  
*S0*  
*S1*  
*S4*  
*S6*  
*S2*  
*S3*  
*S5*  
Limit \= 2Iterative Deepening Depth-first Search  
*S0*  
*S1*  
*S2*  
*S3*  
Limit1 \= 1  
Limit2 \= 2Summary  
• A solution is a path from the initial state to a goal  
state.  
• Search algorithms are judged on the basis of  
completeness, optimality, time complexity and space  
complexity.  
• Several search strategies: BFS, DFS, DLS, and IDS.  
• All uninformed search algorithms have an exponential  
time complexity – hopeless as a viable problem  
solving mechanism (unless you have a quantum  
computer\!)The River problem as an exampleThe River problem as an example  
Fundamental steps:  
✓ Define how to represent the state  
✓ Define the initial state and the final state  
✓ Define the list of each and every possible action and  
the conditions or criteria of a valid state  
✓ The algorithm  
✓ *The output*Possible State Representations  
1\. Farmer Duck / Wolf Corn  
2\. Farmer– Duck –  
3\. 4\. Etc.  
\[1, 0, 1, 0, 1\]Initial vs. Final State  
1\. Farmer Wolf Duck Corn /  
/ Farmer Wolf Duck Corn  
2\. Farmer Wolf Duck Corn  
\- \- \- \-  
3\. \[1, 1, 1, 1, 1\]  
\[0, 0, 0, 0, 0\]  
4\. Etc.Actions & Valid States  
From any state:  
1\. Farmer goes alone,  
2\. 3\. 4\. 6\. 7\. 8\. Farmer goes with the Wolf,  
Farmer goes with the Duck,  
Farmer goes with the Corn,  
5\. Farmer comes back alone,  
Farmer comes back with the Wolf,  
Farmer comes back with the Duck,  
Farmer comes back with the Corn.Actions & Valid States  
\[?, ?, ?, ?, ?\]  
1\. 2\. 3\. 4\. 5\. 6\. 7\. 8\. Farmer goes alone: \[-1, 0, 0, 0, \-1\]  
Farmer goes with the Wolf: \[-1, \-1, 0, 0, \-1\]  
Farmer goes with the Duck: \[-1, 0, \-1, 0, \-1\]  
Farmer goes with the Corn: \[-1, 0, 0, \-1, \-1\]  
Farmer comes back alone: \[1, 0, 0, 0, 1\]  
Farmer comes back with the Wolf: \[1, 1, 0, 0, 1\]  
Farmer comes back with the Duck: \[1, 0, 1, 0, 1\]  
Farmer comes back with the Corn: \[1, 0, 0, 1, 1\]Actions – Initial state  
\[1, 1, 1, 1, 1\]  
1\. 2\. 3\. 4\. 5\. 6\. 7\. 8\. Farmer goes alone: \[-1, 0, 0, 0, \-1\]  
Farmer goes with the Wolf: \[-1, \-1, 0, 0, \-1\]  
Farmer goes with the Duck: \[-1, 0, \-1, 0, \-1\]  
Farmer goes with the Corn: \[-1, 0, 0, \-1, \-1\]  
Farmer comes back alone: \[1, 0, 0, 0, 1\]  
Farmer comes back with the Wolf: \[1, 1, 0, 0, 1\]  
Farmer comes back with the Duck: \[1, 0, 1, 0, 1\]  
Farmer comes back with the Corn: \[1, 0, 0, 1, 1\]Actions & Valid States – Initial state  
\[1, 1, 1, 1, 1\]  
1\. 2\. 3\. 4\. 5\. 6\. 7\. 8\. Farmer goes alone: \[-1, 0, 0, 0, \-1\]  
Farmer goes with the Wolf: \[-1, \-1, 0, 0, \-1\]  
Farmer goes with the Duck: \[-1, 0, \-1, 0, \-1\]  
Farmer goes with the Corn: \[-1, 0, 0, \-1, \-1\]  
Farmer comes back alone: \[1, 0, 0, 0, 1\]  
Farmer comes back with the Wolf: \[1, 1, 0, 0, 1\]  
Farmer comes back with the Duck: \[1, 0, 1, 0, 1\]  
Farmer comes back with the Corn: \[1, 0, 0, 1, 1\]The River problem \- Formulation  
State representation: location of farmer and items in  
both sides of river \[items in South side / items in North  
side\] : (FWDC/-, FD/WC, C/FWD, …)  
Initial State: farmer, wolf, duck and corn in the south  
shore FWDC/-  
Goal State: farmer, duck and corn in the north shore  
\-/FWDCThe River problem \- Formulation  
Operators: the farmer takes in the boat at most one item  
from one side to the other side  
(F-Takes-W, F-Takes-D, F-Takes-C, F-Takes-Self)  
Path cost: the number of crossingsActions & Valid StatesAlgorithm  
\[1, 1, 1, 1, 1\]  
??  
?? ??  
✓ States to be explored  
✓ States already explored  
✓ How to add states to the Agenda?Output of the AlgorithmThe River problem \- Solution  
F-Takes-D, F-Takes-Self, F-Takes-W, F-Takes-D, F-Takes-C,  
F-Takes-Self, F-Takes-D.DFS vs BFS – Let’s practice  
