---
title: "Lab 5 Prep Quiz — Search Algorithms"
module: "CS814"
tags: [module/CS814, type/quizzes, week-05, lab-prep]
date: 2025-10-22
---

# Lab 5 Prep Quiz: Search Algorithms
*Quick readiness check - 50 points total*

Take this before lab to test your understanding!

---

## Section 1: Core Concepts (20 points)

### Question 1 (4 points)
**Define the following for A* algorithm:**
- g(n): actual cost between nodes 
- h(n): cost 
- f(n):

<details>
<summary>💡 Show Answer</summary>

**Answers:**
- **g(n)**: Actual path cost from start node to node n
- **h(n)**: Estimated (heuristic) cost from node n to goal
- **f(n)**: Estimated total cost = g(n) + h(n)

*f(n) is what A* uses to decide which node to expand next (picks lowest f)*
</details>

---

### Question 2 (4 points)
**What makes a heuristic "admissible"?**

<details>
<summary>💡 Show Answer</summary>

**Answer:**
A heuristic h(n) is admissible if it **never overestimates** the true cost to reach the goal.

Formally: h(n) ≤ h*(n), where h*(n) is the actual minimum cost from n to goal.

**Why it matters:** If h is admissible, A* is guaranteed to find the optimal solution.
</details>

---

### Question 3 (4 points)
**For the 8-puzzle, is h(n) = 2 × (number of misplaced tiles) admissible? Why or why not?**

<details>
<summary>💡 Show Answer</summary>

**Answer: NO, it is NOT admissible.**

**Reasoning:**
- Each misplaced tile requires **at least 1 move** to fix (could be more)
- Multiplying by 2 **overestimates** the cost
- An admissible heuristic must never overestimate

**Example:** If 3 tiles are misplaced, minimum moves = 3, but h(n) = 2×3 = 6 (overestimate!)

*h(n) = 1 × misplaced tiles IS admissible (underestimates, which is safe)*
</details>

---

### Question 4 (4 points)
**Why does BFS guarantee the shortest path but DFS doesn't?**

<details>
<summary>💡 Show Answer</summary>

**Answer:**

**BFS (Breadth-First):**
- Explores all nodes at depth d before depth d+1
- First time it finds goal = shortest path by number of steps
- Systematic layer-by-layer exploration

**DFS (Depth-First):**
- Goes deep down one branch before trying others
- Might find goal on a long path first
- Could miss shorter paths in unexplored branches
- No guarantee to explore shortest path first

*BFS uses queue (FIFO), DFS uses stack (LIFO) - this determines exploration order!*
</details>

---

### Question 5 (4 points)
**What data structure does A* use for the agenda, and what value determines priority?**

<details>
<summary>💡 Show Answer</summary>

**Answer:**
- **Data structure:** Priority queue (min-heap)
- **Priority value:** f(n) = g(n) + h(n)
- **Behavior:** Always expand node with **lowest f(n)**

In Python, typically use `heapq` or manually sort by f-value.
</details>

---

## Section 2: 8-Puzzle Specific (15 points)

### Question 6 (5 points)
**Calculate h1 (misplaced tiles) for this state:**

```
Current:        Goal:
2 8 3          1 2 3
1 6 4          8 0 4
7 0 5          7 6 5
```

<details>
<summary>💡 Show Answer</summary>

**Answer: h1 = 5**

**Calculation:**
- Position (0,0): 2 should be at (0,1) ❌
- Position (0,1): 8 should be at (1,0) ❌
- Position (0,2): 3 is correct ✓
- Position (1,0): 1 should be at (0,0) ❌
- Position (1,1): 6 should be at (2,1) ❌
- Position (1,2): 4 is correct ✓
- Position (2,0): 7 is correct ✓
- Position (2,1): 0 (blank) - not counted
- Position (2,2): 5 is correct ✓

**Total misplaced (excluding 0): 5 tiles**

*Note: blank (0) is never counted in misplaced tiles heuristic*
</details>

---

### Question 7 (5 points)
**What are the valid operators for the 8-puzzle?**

<details>
<summary>💡 Show Answer</summary>

**Answer:**
Four possible operators (move the blank):
1. **Move blank UP** (swap with tile above)
2. **Move blank DOWN** (swap with tile below)
3. **Move blank LEFT** (swap with tile to left)
4. **Move blank RIGHT** (swap with tile to right)

**Important checks:**
- Must check boundaries (can't move blank outside 3×3 grid)
- In code: check row/col indices before applying move

**Alternative formulation:** Move a tile into the blank space (equivalent)
</details>

---

### Question 8 (5 points)
**Calculate Manhattan distance for tile "8" in this configuration:**

```
Current position of 8: row 0, col 1
Goal position of 8: row 1, col 0
```

<details>
<summary>💡 Show Answer</summary>

**Answer: Manhattan distance = 2**

**Formula:**
```
Manhattan = |current_row - goal_row| + |current_col - goal_col|
          = |0 - 1| + |1 - 0|
          = 1 + 1
          = 2
```

*This means tile 8 needs minimum 2 moves to reach its goal position*

**Full h2 heuristic** = sum of Manhattan distances for ALL tiles (except blank)
</details>

---

## Section 3: Algorithm Implementation (15 points)

### Question 9 (7 points)
**Fill in the pseudocode for A*:**

```python
def a_star(initial_state, goal_state):
    agenda = [(initial_state, ?, ?)]  # What values?
    explored = set()

    while agenda:
        current, g, f = get_node_with_lowest_?(agenda)  # Lowest what?

        if current == goal_state:
            return "Found!"

        explored.add(current)

        for next_state in get_neighbors(current):
            if next_state in explored:
                continue

            new_g = g + ?  # Cost so far
            new_h = heuristic(next_state, goal_state)
            new_f = ?  # Total estimated cost

            add_to_agenda(agenda, next_state, new_g, new_f)

    return "No solution"
```

<details>
<summary>💡 Show Answer</summary>

**Completed code:**

```python
def a_star(initial_state, goal_state):
    agenda = [(initial_state, 0, heuristic(initial_state, goal_state))]
    # Values: (state, g=0, f=0+h)
    explored = set()

    while agenda:
        current, g, f = get_node_with_lowest_f(agenda)
        # Lowest f-value (total estimated cost)

        if current == goal_state:
            return "Found!"

        explored.add(current)

        for next_state in get_neighbors(current):
            if next_state in explored:
                continue

            new_g = g + 1  # or cost of action
            new_h = heuristic(next_state, goal_state)
            new_f = new_g + new_h

            add_to_agenda(agenda, next_state, new_g, new_f)

    return "No solution"
```

**Key points:**
- Initial g = 0 (no cost yet)
- Initial f = 0 + h(initial)
- Always pick lowest **f** value
- new_g increments by step cost (usually 1)
- new_f = new_g + new_h
</details>

---

### Question 10 (8 points)
**Why is tracking explored states important? What problem does it prevent?**

Give an example with the 8-puzzle.

<details>
<summary>💡 Show Answer</summary>

**Answer:**

**Why important:** Prevents infinite loops and repeated work

**Problem prevented:** Revisiting same states (cycles in state space)

**8-Puzzle Example:**
```
State A:          State B:
1 2 3            1 2 3
4 0 5      ⟷     4 5 0
6 7 8            6 7 8
```

- From A, move blank right → B
- From B, move blank left → A (back where we started!)
- Without tracking: infinite loop A→B→A→B...
- With explored set: "Already seen state A, skip it"

**Implementation:**
```python
explored = set()

if current_state in explored:
    continue  # Skip this state

explored.add(current_state)
```

**Performance benefit:** Also avoids redundant computation - don't re-explore states you've already processed
</details>

---

## 🎯 Scoring Guide

- **45-50 points:** Excellent! You're ready for lab
- **35-44 points:** Good! Review weak areas quickly
- **25-34 points:** Read the summary again, focus on A*
- **< 25 points:** Spend 20 min with summary + YouTube videos

---

## 📝 Key Takeaways

If you remember nothing else, remember these:

1. **A* = g(n) + h(n)** - combines actual cost + estimated cost
2. **Admissible heuristic** = never overestimates (guarantees optimal)
3. **Track explored states** = prevents infinite loops
4. **BFS uses queue (FIFO), DFS uses stack (LIFO)**
5. **8-puzzle heuristics**: misplaced tiles (ok), Manhattan distance (better)

---

*Go to lab-5-prep-search-algorithms.md for detailed explanations!*
