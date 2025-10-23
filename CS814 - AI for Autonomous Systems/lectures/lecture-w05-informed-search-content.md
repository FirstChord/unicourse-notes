---
title: "Week 05 — Informed Search (Lecture Content)"
module: "CS814"
tags: [module/CS814, type/lectures, week-05, content]
date: 2025-10-22
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Informed Search
*Week 05 Lecture*

***Informed Search***  
***Joseph El Gemayel, Ph.D., FHEA***  
***Teaching Fellow***  
***Computer & Information Sciences***  
***Email: joseph.el-gemayel@strath.ac.uk***  
***Office: LT1214 \- Livingstone TowerPresentation outline***  
***1\. Searching Using an Agenda***  
***2\. Comparison between BFS and DFS***  
***3\. Uniform Cost Search (UCS)***  
***4\. Heuristic Search***  
***5\. Enforced Hill Climbing vs. Best-First Search***  
***6\. A\* algorithmSearching Using an Agenda***  
***• When we expand a node we get multiple new nodes***  
***to expand, but we can only expand one at a time***  
***\[C:3, M:3, B:1\]***  
***C:2 C:1 C:1, M1***  
***\[C:1, M:3, B:0\] \[C:2, M:3, B:0\] \[C:2, M:2, B:0\]Searching Using an Agenda***  
***• When we expand a node we get multiple new nodes***  
***to expand, but we can only expand one at a time***  
***• We keep track of the nodes still to be expanded using***  
***a data structure called an agenda***  
***\[C:3, M:3, B:1\]***  
***C:1 C:1, M1***  
***\[C:1, M:3, B:0\] \[C:2, M:3, B:0\] \[C:2, M:2, B:0\]***  
***C:2 Agenda: \[\[C:3, M:3, B:1\]\]Searching Using an Agenda***  
***• When we expand a node we get multiple new nodes***  
***to expand, but we can only expand one at a time***  
***• We keep track of the nodes still to be expanded using***  
***a data structure called an agenda***  
***• When it is time to expand a new node, we choose the***  
***first node from the agenda. As new states are***  
***discovered, we add them to the agenda somehow***  
***Step 0: Agenda: \[\[C:3, M:3, B:1\]\]***  
***Step 1: Agenda: \[\[C:1, M:3, B:0\], \[C:2, M:3, B:0\], \[C:2,***  
***M:2, B:0\]\]Searching Using an Agenda***  
***• When we expand a node we get multiple new nodes***  
***to expand, but we can only expand one at a time***  
***• We keep track of the nodes still to be expanded using***  
***a data structure called an agenda***  
***• When it is time to expand a new node, we choose the***  
***first node from the agenda. As new states are***  
***discovered, we add them to the agenda somehow***  
***• We can get different styles of search by altering how***  
***the states get added / removedDepth-First Search***  
***• To get depth-first (a.k.a. LIFO) search, remove the last***  
***item added into the agenda (treat the agenda as a***  
***stack):***  
***Agenda \= \[S0\]***  
***while Agenda ≠ \[\] do***  
***Current \= remove-last(Agenda)***  
***if Goal(Current) then return(“Found it\!”)***  
***Next \= NextStates(Current)***  
***for nx in Next***  
***if nx not in Agenda and nx not explored***  
***Agenda \= Agenda \+ nxProperties of Depth-First Search***  
***• Depth-first can often get to the answer quickly***  
***• The agenda stays short: O(d) for memory, where d is***  
***the depth of the tree***  
***• The time taken to find the solution is O(d) in the best***  
***case and O(bd) in the worst case (where b is the***  
***average branching factor)***  
***• But if there are loops or infinite branches in the search***  
***space, it may not return a solution***  
***• It isn’t guaranteed to give the shortest solutionBreadth-First Search***  
***• To get breadth-first (a.k.a. FIFO) search, remove the***  
***first item added into the agenda (treat the agenda as***  
***a queue):***  
***Agenda \= \[S0\]***  
***while Agenda ≠ \[\] do***  
***Current \= remove-first (Agenda)***  
***if Goal(Current) then return(“Found it\!”)***  
***Next \= NextStates(Current)***  
***for nx in Next***  
***if nx not in Agenda and nx not explored***  
***Agenda \= Agenda \+ nxProperties of Breadth-First Search***  
***• Breadth-first can often take a long time to get to the***  
***answer***  
***• But it isn’t bothered by loops or infinite branches in***  
***the search space***  
***• The agenda can get very big: O(bd) for memory,***  
***giving exponential space consumption***  
***• Also exponential time complexity: O(bd) nodes will be***  
***expanded***  
***• But it always gives the shortest solution, in terms of***  
***the number of steps in the planUniform Cost Search (UCS)***  
***• Main idea: Expand the cheapest node (cost path g(n))***  
***Agenda \= \[S0\]***  
***while Agenda ≠ \[\] do***  
***Current \= CheapestNode(Agenda)***  
***Agenda \= Rest(Agenda)***  
***if Goal(Current) then return(“Found it\!”)***  
***Next \= NextStates(Current)***  
***for nx in Next***  
***if nx not explored***  
***if nx is not in agenda***  
***Agenda \= Agenda \+ nx***  
***elif nx in agenda with a higher cost***  
***replace it with its new costUniform Cost Search (UCS)***  
***S0***  
***S1***  
***S2Uniform Cost Search (UCS)***  
***S0***  
***5 2***  
***S1***  
***S2Uniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***Number on the arrow is the current cost***  
***Number next to the node is the cumulative costUniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***1***  
***7***  
***S5 S6***  
***3 9***  
***Number on the arrow is the current cost***  
***Number next to the node is the cumulative costUniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***1***  
***7***  
***S5 S6***  
***3 9***  
***4 5***  
***S7***  
***7 8***  
***S8***  
***Number on the arrow is the current cost***  
***Number next to the node is the cumulative costUniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***3***  
***4***  
***1***  
***7***  
***S3 S4 S5 S6***  
***8 9 3 9***  
***4 5***  
***S7***  
***7 8***  
***S8***  
***Number on the arrow is the current cost***  
***Number next to the node is the cumulative costUniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***3***  
***4***  
***1***  
***7***  
***S3 S4 S5 S6***  
***8 9 3 9***  
***4 5***  
***S7***  
***7 8***  
***S8***  
***Explored States from S0 to S7***  
***UCS: S0/0, S2/2, S5/3, S1/5, S3/6, S7/7Uniform Cost Search (UCS)***  
***S0***  
***0***  
***5 2***  
***S1***  
***5 2***  
***S2***  
***0***  
***4***  
***1***  
***7***  
***S3 S4 S5 S6***  
***5 9 3 9***  
***0***  
***4 5***  
***S1 5***  
***S7***  
***7 8***  
***S8***  
***Explored States from S0 to S7***  
***UCS: S0/0, S2/2, S5/3, S1/5, S3/5, S1/5, etc.Uninformed Search Algorithms***  
***• Do not consider the future consequences of actions***  
***• Act on how the world is***  
***• Without incorporating knowledge into searching, one***  
***can have no bias (i.e. a preference) on the search***  
***space.***  
***• Without a bias, one is forced to look everywhere to***  
***find the answer. Hence, the complexity of uninformed***  
***search is intractable.***  
***• To do more, Know moreInformed Search Algorithms***  
***• Act on how the world would be***  
***• Must have a model of how the world evolves in***  
***response to actions***  
***• Often there is extra knowledge that can be used to***  
***guide the search: an estimate of the distance/cost***  
***from node n to a goal node.***  
***• This estimate is called a heuristic search.Heuristic Search***  
***• Uninformed Search Algorithms are blind – they search***  
***all possibilities in an order dictated by NextStates(Si)***  
***• When people search, we look in the most promising***  
***places first***  
***• The most promising states are often those which are***  
***closest to the goal state, G***  
***• But how can we know how close we are to the goal***  
***state?Heuristic Search***  
***• We can often estimate the distance from Si to G by***  
***using a heuristic function, h(Si,G)***  
***• The function efficiently compares the two states and***  
***tries to get an estimate of how many moves remain***  
***without doing any searchHeuristic Search***  
***• We can often estimate the distance from Si to G by***  
***using a heuristic function, h(Si,G)***  
***• The function efficiently compares the two states and***  
***tries to get an estimate of how many moves remain***  
***without doing any search***  
***• For example, in the 8-puzzle game, it can be the***  
***number of pieces in the wrong place, as the other***  
***pieces are considered in their right place***  
***h(Si,G) \= 1\*Pbad \+ 0\*PgoodEnforced Hill Climbing***  
***• The easiest way to use a heuristic estimate to search***  
***is to require that every single move we make takes us***  
***closer to the goal***  
***• The form of search doesn’t even require an agenda,***  
***since at each decision point, we take the action that***  
***looks best to us and repeat until we’re doneEnforced Hill Climbing***  
***S0,5***  
***Start***  
***S1,5***  
***S2,3***  
***S3,5***  
***S4,2***  
***S5,2***  
***S6,1 Goal***  
***S7,0Enforced Hill Climbing***  
***S0,5***  
***Start***  
***S1,5***  
***S2,3***  
***S3,5***  
***S5,2***  
***S7,0 GoalEnforced Hill Climbing***  
***• The easiest way to use a heuristic estimate to search***  
***is to require that every single move we make takes us***  
***closer to the goal***  
***• The form of search doesn’t even require an agenda,***  
***since at each decision point, we take the action that***  
***looks best to us and repeat until we’re done***  
***• Problems: dead ends, solution quality (i.e. the number***  
***of steps can be very poor)Enforced Hill Climbing***  
***S0,5***  
***Start***  
***S1,5***  
***S2,6***  
***S3,5***  
***S4,2***  
***S5,2***  
***S6,1 Goal***  
***S7,0Enforced Hill Climbing***  
***S0,5***  
***Start***  
***S1,5***  
***S2,6***  
***S3,5***  
***S4,2***  
***S5,2***  
***Dead End***  
***S6,1 Goal***  
***S7,0Best-First Search***  
***• Enforced hill climbing is great when it works, but for***  
***most problems it’s better to keep track of the nodes***  
***we haven’t yet expanded, using the agenda***  
***• We can then use the heuristic function to determine***  
***which node to expand next***  
***• As new states are discovered, we add them to the***  
***agenda and record the value of the heuristic function***  
***• When we pick the next node to explore, we choose***  
***the one which has the lowest value for the heuristic***  
***function (i.e. the one that looks nearest to the goal)Best-First Search***  
***S0,5***  
***S1,3***  
***S2,4***  
***S4,5***  
***S5,6***  
***S6,2***  
***S7,0***  
***S3,5Best-First Search***  
***S0,5***  
***S1,3***  
***S2,4***  
***S4,5***  
***S5,6***  
***S6,2***  
***Visited States:***  
***S0,5; S1,3; S2,4; S6,2; S7,0***  
***S7,0***  
***S3,5***  
***Unexplored States:***  
***S4, S5, S3Best-First Search***  
***• Pick the best node on the agenda:***  
***Agenda \= \[S0\]***  
***while Agenda ≠ \[\] do***  
***Current \= Best(Agenda)***  
***Agenda \= Rest(Agenda)***  
***if Goal(Current) then return(“Found it\!”)***  
***Next \= NextStates(Current)***  
***for nx in Next***  
***if nx not explored and nx not in agenda***  
***Agenda \= Agenda \+ nxBest-First Search***  
***• Best-first search can speed up the search by a very***  
***large factor, but it isn’t guaranteed to return the***  
***shortest solution***  
***• Best-first search is incomplete without systematic***  
***checking of repeated statesUCS \+ Best-First Search***  
***• When deciding to expand a node, we need to take***  
***account of how long the path is so far, and add that on***  
***to the heuristic value:UCS \+ Best-First Search***  
***• When deciding to expand a node, we need to take***  
***account of how long the path is so far, and add that on***  
***to the heuristic value:***  
***f(Si,G) \= g(S0 ,Si) \+ h(Si,G)Algorithm A: UCS \+ Best-First Search***  
***• When deciding to expand a node, we need to take***  
***account of how long the path is so far, and add that on***  
***to the heuristic value:***  
***f(Si,G) \= g(S0 ,Si) \+ h(Si,G)***  
***• This will give a search which has elements of both***  
***Uniform-cost search and best-first search***  
***• This type of search is called “Algorithm A”Algorithm A\****  
***• If h(Si,G) never over-estimates the distance from Si to***  
***the goal, it is called an admissible heuristic***  
***• If h(Si,G) is admissible, then Algorithm A will always***  
***return the shortest path (like breadth-first search) but***  
***will omit much of the work if the heuristic function is***  
***informativeAdmissible Heuristics***  
***• A heuristic h is admissible (optimistic) if and only if:***  
***h (s) ≤ h\*(s), s is a state***  
***where h\*(s) is the true cost to a nearest goalAdmissible Heuristics***  
***• A heuristic h is admissible (optimistic) if and only if:***  
***h (s) ≤ h\*(s), s is a state***  
***where h\*(s) is the true cost to a nearest goal***  
***• For example, in the 8-puzzle game, is the following***  
***heuristic function admissible?***  
***h(Si,G) \= 2\*Pbad \+ 0\*PgoodAlgorithm A\****  
***• If h(Si,G) never over-estimates the distance from Si to***  
***the goal, it is called an admissible heuristic***  
***• If h(Si,G) is admissible, then Algorithm A will always***  
***return the shortest path (like breadth-first search) but***  
***will omit much of the work if the heuristic function is***  
***informative***  
***• The use of an admissible heuristic turns Algorithm A***  
***into Algorithm A\****  
***• Uses: problem solving, route finding, path planning in***  
***robotics, computer games, etc.Why is A\* Optimal?***  
***• Suppose a suboptimal goal node, Sk, appears in the***  
***agenda – we haven’t selected it yet, so we don’t yet***  
***know that it’s a goal nodeWhy is A\* Optimal?***  
***• Suppose a suboptimal goal node, Sk, appears in the***  
***agenda – we haven’t selected it yet, so we don’t yet***  
***know that it’s a goal node***  
***• Also on the agenda, there must be a node, Si which is***  
***on the optimal path from S0 to the goal stateWhy is A\* Optimal?***  
***• Suppose a suboptimal goal node, Sk, appears in the***  
***agenda – we haven’t selected it yet, so we don’t yet***  
***know that it’s a goal node***  
***• Also on the agenda, there must be a node, Si which is***  
***on the optimal path from S0 to the goal state***  
***• Since the heuristic function, h(Si,G), is admissible,***  
***this means:***  
***f(Sk,G)=g(S0,Sk) \+ h(Sk ,G) \> f(Si,G)=g(S0,Si) \+ h(Si ,G)***  
***so Sk will never be selected over Si for expansionA\* Algorithm***  
***Agenda \= \[S0\]***  
***while Agenda ≠ \[\] do***  
***Cur \= LowestFValue(Agenda)***  
***Agenda \= Rest(Agenda)***  
***if Goal(Cur) then return(“Found it\!”)***  
***Next \= NextStates(Cur)***  
***for each nx in Next***  
***calculate f(nx) \= g(Cur) \+ cost(Cur,nx) \+ h(nx)***  
***if nx not explored***  
***if nx is not in agenda***  
***Agenda \= Agenda \+ nx***  
***elif nx in agenda with a higher f value***  
***replace it with its new f valueHeuristic Functions***  
***• Consider the 8-puzzle:***  
***7 2 4***  
***1 2 3***  
***5 6***  
***4 5 6***  
***8 3 1***  
***7 8***  
***• Can we come up with a good admissible heuristic***  
***function for this problem?Summary***  
***• A\* is optimal and complete except if there is an infinite***  
***number of nodes with f \< f(G).***  
***• Time complexity depends on the quality of heuristic***  
***but is still exponential.***  
***• For space complexity, A\* keeps all nodes in memory.***  
***A\* has worst case space complexity, but an iterative***  
***deepening version is possible (IDA\*).A\* Algorithm***  
