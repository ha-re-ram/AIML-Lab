# 🎯 Experiment 04 – Constraint Satisfaction Problem: Water Jug & Map Coloring

This experiment involves solving **two classic constraint satisfaction problems** using **Breadth-First Search (BFS)**:

1. 🌊 **Water Jug Problem**  
2. 🌍 **Map Coloring Problem**

---

## 📁 Folder Structure

```
Experiment-04-CSP/
├── water_jug_problem.py       # Solves Water Jug Problem using BFS
├── map_coloring_problem.py    # Solves Map Coloring Problem using BFS
└── README.md
```

---

## 🌊 Water Jug Problem (`water_jug_problem.py`)

### ✅ Problem Overview

Given two jugs with different capacities, the goal is to measure a specific amount of water by filling, emptying, and pouring between the jugs. Solved using **Breadth-First Search (BFS)**.

### 🔧 Algorithm

- **State Representation**: Tuple `(jug1, jug2)` for current water levels.
- **Valid State**: Neither jug has a negative value or exceeds capacity.
- **Goal State**: One of the jugs contains the target amount.
- **Successor Function**: Generates all valid states by pouring, filling, or emptying.
- **Search**: BFS explores all possible transitions to reach the goal.

### 📦 Requirements

- Python Standard Library: `collections.deque`

### ▶️ How to Run

```bash
python water_jug_problem.py
```

---

## 🌍 Map Coloring Problem (`map_coloring_problem.py`)

### ✅ Problem Overview

Given a map of territories and their neighbors, the objective is to assign colors such that **no neighboring regions have the same color**. Implemented using **BFS** for coloring and validation.

### 🔧 Algorithm

- **State Representation**: Dictionary mapping regions to assigned colors.
- **Valid Coloring**: Ensures neighboring regions don't share a color.
- **Search**: BFS assigns colors to each region while checking constraints.

### 📦 Requirements

- Python Standard Library: `collections.deque`

### ▶️ How to Run

```bash
python map_coloring_problem.py
```

---

## 📝 Learning Outcomes

- Represented real-world problems as **constraint satisfaction problems**.
- Explored **state-space search** using BFS.
- Designed **successor functions** and implemented **goal checks**.
- Understood the role of **validity checks** in CSPs for ensuring feasible solutions.

---

## 👨‍💻 Author

**Hareram Kushwaha**  
2nd Year CSE Student, KPRIET  
_"Solving problems one jug and territory at a time."_ 🌍💧

---

## 📜 License

This project is intended for academic use and personal learning.  
Feel free to use or modify with attribution.

---
