---
title: "Lab 5 Prep — Search Algorithms & 8-Puzzle"
module: "CS814"
tags: [module/CS814, type/summaries, lab-prep, week-05]
date: 2025-10-22
---

# Lab 5 Prep: Search Algorithms & 8-Puzzle
*Quick review before lab - 20 min read*

---

## ✅ Lab 5 Task Checklist

**Part I - Theory (No coding):**
- [ ] Q1.1: Draw search graph (2-3 levels) for 8-puzzle
- [ ] Q1.2-1.3: Get GenAI feedback, compare with your work
- [ ] Q1.4: Trace Best-First Search by hand
- [ ] Q1.5: Trace UCS with variable costs (UP=1, RIGHT=2, DOWN=3, LEFT=4)
- [ ] Q1.6: Trace A* algorithm by hand

**Part II - Python Implementation:**
- [ ] Q2: State representation (list of 9 numbers)
- [ ] Q2: Random initial state + goal state
- [ ] Q2: Valid actions (check bounds)
- [ ] Q3: BFS and DFS (reuse Lab 4!)
- [ ] Q4: UCS implementation (with action costs)
- [ ] Q4: Best-First Search (uses h only)
- [ ] Q4: A* (uses g + h)

---

## 🎯 What You'll Do in Lab 5

**Part I - Theory (Paper/GenAI):**
- Draw search graph for 8-puzzle (first 2-3 levels)
- Use GenAI to critique and improve your formalism
- Trace Best-First Search, UCS, and A* by hand
- Work with **variable action costs** (clockwise preference)

**Part II - Python Implementation:**
- Implement BFS and DFS (reuse Lab 4 code!)
- Implement UCS, Best-First Search, and A*
- Handle **agenda with values** (costs/heuristics)

**Specific States You'll Use:**
- **Initial**: `[1,2,3,4,8,0,7,6,5]`
- **Goal**: `[1,2,3,4,5,6,7,8,0]`

---

## 🔑 Essential Concepts

### 1. The 8-Puzzle Problem

**State Representation Options:**
```python
# Option 1: 3x3 array
[[2, 1, 3],
 [4, 7, 6],
 [5, 8, 0]]

# Option 2: List/Vector
[2, 1, 3, 4, 7, 6, 5, 8, 0]
```

**Operators:** Move the blank (0) up, down, left, or right

**Goal:** Transform initial state to goal state (typically `[1,2,3,4,5,6,7,8,0]`)

---

### 2. The Agenda Concept

**Core idea:** Keep track of states still to be explored

```python
Agenda = [initial_state]

while Agenda is not empty:
    current = remove_from_agenda(Agenda)  # How you remove determines search type!

    if is_goal(current):
        return "Found it!"

    next_states = get_next_states(current)
    add_to_agenda(Agenda, next_states)
```

---

### 3. Uninformed Search Algorithms

#### Depth-First Search (DFS)
- **Strategy:** LIFO - treat agenda as a **stack** (remove last added)
- **Pros:** Memory efficient O(d), can find solution quickly
- **Cons:** Not guaranteed shortest path, can get stuck in loops
- **Implementation:** `current = agenda.pop()` (remove last)

#### Breadth-First Search (BFS)
- **Strategy:** FIFO - treat agenda as a **queue** (remove first added)
- **Pros:** Guaranteed shortest solution (by steps), complete
- **Cons:** Memory intensive O(b^d), can be slow
- **Implementation:** `current = agenda.pop(0)` (remove first)

#### Uniform Cost Search (UCS)
- **Strategy:** Expand cheapest node by path cost **g(n)**
- **g(n)** = cumulative cost from start to node n
- **Implementation:** Always pick node with lowest g(n) from agenda
- **Pros:** Finds optimal solution by cost
- **Cons:** Still uninformed - doesn't consider goal

**Lab 5 Twist - Variable Action Costs:**
In this lab, actions have **different costs** (clockwise preference):
- **Slide UP**: cost = 1
- **Slide RIGHT**: cost = 2
- **Slide DOWN**: cost = 3
- **Slide LEFT**: cost = 4

This makes UCS find different paths than BFS! UCS prefers paths with more "up" moves.

---

### 4. Informed Search (Heuristic)

#### Heuristic Function h(n)
**Estimate** of cost from node n to goal (without doing search!)

**8-Puzzle Heuristics:**

**h1: Misplaced Tiles**
- Count tiles in wrong position (excluding blank)
- Example: `h1 = 5` means 5 tiles need to move

**h2: Manhattan Distance** (better!)
- Sum of distances each tile is from goal position
- Distance = |current_row - goal_row| + |current_col - goal_col|

**Admissible Heuristic:** Never **overestimates** true cost
- h(n) ≤ h*(n) where h*(n) is true cost to goal
- Both h1 and h2 are admissible for 8-puzzle
- **Why important:** Guarantees A* finds optimal solution

---

### 5. A* Algorithm ⭐

**The Formula:**
```
f(n) = g(n) + h(n)

where:
  g(n) = actual cost from start to node n
  h(n) = estimated cost from node n to goal
  f(n) = estimated total cost of path through n
```

**Strategy:** Always expand node with **lowest f(n)**

**Why A* is Optimal:**
- If h(n) is admissible, A* **always** finds shortest path
- Combines best of UCS (considers path cost) and Best-First (considers goal distance)

**Algorithm:**
```python
Agenda = [(start_node, f_value)]

while Agenda:
    current = node_with_lowest_f_value(Agenda)

    if is_goal(current):
        return "Found it!"

    for next_state in get_next_states(current):
        g = cost_so_far(next_state)
        h = heuristic(next_state, goal)
        f = g + h

        add_or_update_agenda(Agenda, next_state, f)
```

---

### 6. Key Comparisons

| Algorithm | Complete? | Optimal? | Time | Space | Uses |
|-----------|-----------|----------|------|-------|------|
| **DFS** | No* | No | O(b^d) | O(d) | Stack (LIFO) |
| **BFS** | Yes | Yes** | O(b^d) | O(b^d) | Queue (FIFO) |
| **UCS** | Yes | Yes | O(b^d) | O(b^d) | Priority queue (min g) |
| **A*** | Yes | Yes† | Depends on h | O(b^d) | Priority queue (min f) |

\* = unless graph is finite
\** = optimal by steps, not cost
† = if h(n) is admissible

**Key Variables:**
- **b** = branching factor (avg. new states per expansion)
- **d** = depth of solution

---

## 🧠 What to Remember for Lab

### For Part I (Theory):
1. **Draw search graph:** Show state transitions, label edges with actions
2. **GenAI critique:** Be ready to compare your work with AI suggestions
3. **Show traces:** For each algorithm, list visited nodes in order
4. **Variable costs matter:** UCS will take different path than BFS

### For Part II (Python):
1. **Reuse Lab 4 code:** BFS/DFS structure carries over
2. **State Representation:** List of 9 numbers (easier than 2D array)
3. **Valid Moves:** Check bounds before moving blank (0)
4. **Avoid Cycles:** Track explored states with `set()`
5. **Agenda with values:**
   - **BFS/DFS:** agenda = `[state1, state2, ...]`
   - **UCS:** agenda = `[(state1, g1), (state2, g2), ...]`
   - **A*:** agenda = `[(state1, g1, f1), (state2, g2, f2), ...]`
6. **Heuristic Choice:** Manhattan distance > misplaced tiles

---

## 📺 Helpful Resources

**Understanding A* (Visual):**
- [A* Pathfinding Visualization - Computerphile](https://www.youtube.com/watch?v=ySN5Wnu88nE) (10 min)
- Clear explanation of how A* works with animation

**8-Puzzle Specific:**
- [8-Puzzle Problem Solving with A*](https://www.youtube.com/watch?v=6TsL96NAZCo) (15 min)
- Shows exact problem you'll solve in lab

**Python Implementation Help:**
- [A* in Python - Tech With Tim](https://www.youtube.com/watch?v=JtiK0DOeI4A) (20 min)
- Practical coding walkthrough

---

## 💻 Lab-Specific Implementation Tips

### Initial State Setup
```python
# Your lab's starting position
initial_state = [1, 2, 3, 4, 8, 0, 7, 6, 5]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Visualize it:
# 1 2 3
# 4 8 0   ← only 3 tiles out of place!
# 7 6 5
```

### Action Cost Function (for UCS & A*)
```python
def get_action_cost(action):
    costs = {
        'UP': 1,
        'RIGHT': 2,
        'DOWN': 3,
        'LEFT': 4
    }
    return costs[action]
```

### Using GenAI Effectively (Part I)
When asking ChatGPT/Copilot to critique your work:
- **Good prompt:** "I represented 8-puzzle states as [list]. Is this efficient? What are pros/cons?"
- **Bad prompt:** "Do my homework"
- **Document differences:** Note what GenAI suggests vs. your approach
- **Critical thinking:** You can disagree with AI if your reasoning is sound

---

## ⚡ Quick Test Before Lab

Before you go, make sure you can answer:

1. What's the difference between g(n), h(n), and f(n)?
2. Why does BFS guarantee shortest path but DFS doesn't?
3. What makes a heuristic "admissible"?
4. For the 8-puzzle, is "2 × misplaced tiles" admissible?
5. How do you avoid infinite loops in state space search?
6. **NEW:** Which action costs least in this lab's UCS? (UP/DOWN/LEFT/RIGHT)

**If you're unsure, take the quiz next!**

---

## 🎓 Pro Tips for Lab

### Part I (Theory):
✅ **Draw neatly** - you'll submit this, make it clear
✅ **Label everything** - state contents, action names, costs
✅ **Show your work** - for traces, list order of exploration
✅ **GenAI comparison** - copy your original answer before asking AI

### Part II (Implementation):
✅ **Start with BFS** - copy from Lab 4, modify for 8-puzzle
✅ **Convert states to tuples** - lists can't go in sets, tuples can
✅ **Test small first** - use states 1-2 moves from goal
✅ **Print the agenda** - debug by watching what's queued
✅ **Track path** - store parent pointers to reconstruct solution

**Critical: State tracking with tuples**
```python
# Convert list to tuple for hashing
explored = set()
agenda = [tuple(initial_state)]  # tuple, not list!

while agenda:
    current = agenda.pop(0)  # BFS

    if current in explored:
        continue

    explored.add(current)  # works because current is tuple

    # When generating neighbors, convert back to list
    state_list = list(current)
    # ... make moves, then convert back: tuple(new_state)
```

**For UCS/A* - agenda with priorities:**
```python
# Each item: (priority, state, g_cost)
import heapq
agenda = [(0, tuple(initial_state), 0)]  # (f, state, g)

while agenda:
    f, current, g = heapq.heappop(agenda)  # gets lowest f
    # ...
```

---

Good luck! You've got this 🚀

*Based on Lectures W04 (Problems & Search) and W05 (Informed Search)*
