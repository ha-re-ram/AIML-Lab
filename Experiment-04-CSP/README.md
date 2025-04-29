# 🎯 Experiment 04 – Constraint Satisfaction Problem: Water Jug and Map Coloring Problems

This experiment involves solving **two classic constraint satisfaction problems**:

1. **Water Jug Problem** using **Breadth-First Search (BFS)**.
2. **Map Coloring Problem** using **Breadth-First Search (BFS)**.

---

## 📁 Folder Structure

Experiment-04-CSP/
    ├── water_jug_problem.py # Solves Water Jug problem using BFS
    ├── map_coloring_problem.py # Solves Map Coloring problem using BFS 
    └── README.md

---

## 🌊 Water Jug Problem (`water_jug_problem.py`)

### ✅ Problem Overview

Given two jugs with different capacities, the goal is to measure a specific amount of water by filling, emptying, and pouring water between the jugs. This problem is solved using **Breadth-First Search (BFS)**.

### 🔧 Algorithm

1. **State Representation**: The state is represented as a tuple `(jug1, jug2)` where `jug1` is the current water amount in Jug 1, and `jug2` is the current water amount in Jug 2.
2. **Valid State**: A state is valid if both jugs have non-negative water amounts, and neither jug exceeds its capacity.
3. **Goal State**: The goal state is when either jug contains the target amount of water.
4. **Successor Function**: The function generates all possible valid states from the current state by filling, emptying, or pouring water between the two jugs.
5. **BFS**: BFS is used to explore all possible states until the goal state is found.

### 📦 Requirements

- Python standard library (`collections.deque`)

### ▶️ How to Run

```bash
python water_jug_problem.py

---

### 🌍 Map Coloring Problem (map_coloring_problem.py)

## ✅ Problem Overview

Given a map with regions and their neighbors, the goal is to color the map such that no two neighboring regions share the same color. This is solved using Breadth-First Search (BFS) and is commonly known as the graph coloring problem.

### 🔧 Algorithm

State Representation: The state is represented by a dictionary of territories with their respective colors.

Valid Coloring: A coloring is valid if no two neighboring territories share the same color.

BFS: BFS explores all territories, attempting to assign a color to each one while checking the validity of the coloring.

### 📦 Requirements

Python standard library (collections.deque)

### ▶️ How to Run

- python map_coloring_problem.py

---

##📝 Learning Outcomes
Learned to represent constraint satisfaction problems and solved them using BFS.

Gained hands-on experience in state space exploration, successor functions, and goal checks.

Understood the importance of validity checks in ensuring feasible solutions in both the Water Jug and Map Coloring problems.

---

##👨‍💻 Author

Hareram Kushwaha
2nd Year CSE Student, KPRIET
"Solving problems one jug and territory at a time." 🌏💧

---

##📜 License

This project is for academic use and personal learning. Feel free to use or modify with attribution.

---