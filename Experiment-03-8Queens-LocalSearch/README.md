# 🎯 Experiment 03 – Solving 8 Queens Problem using Local Search Algorithms

This experiment implements two popular **local search algorithms** — **Genetic Algorithm** and **Hill Climbing** — to solve the classic **8 Queens Problem**, where the goal is to place 8 queens on a chessboard such that no two queens attack each other.

---

## 📁 Folder Structure

```
Experiment-03-8Queens-LocalSearch/
├── genetic.py     # Solves using Genetic Algorithm
├── hill.py        # Solves using Hill Climbing
└── README.md
```

---

## 🧠 Problem Statement

> Place 8 queens on a standard 8×8 chessboard so that no two queens threaten each other.  
> This means that no two queens share the same row, column, or diagonal.

---

## 🚀 Approach 1: Genetic Algorithm (`genetic.py`)

### ✅ Features

- Random population generation
- Fitness function based on non-attacking queen pairs
- Parent selection via roulette wheel
- Crossover and mutation
- Early stopping if perfect solution found

### 📦 Requirements

- Python standard library (`random`)

### ▶️ How to Run

```bash
python genetic.py
```

---

## 🧪 Sample Output

```text
Enter the initial positions of queens (0-7) for each row:
Row 0: 0
Row 1: 4
...

Solution Found:
. . . . . . . Q 
Q . . . . . . . 
. . . . Q . . . 
...

Solution found in generation: 153
```

---

## 🔁 Approach 2: Hill Climbing (`hill.py`)

### ✅ Features

- Starts from a random board
- Moves to best neighbor (greedy)
- Restarts on local maximum
- Stops when cost = 0 (perfect solution)

### 📦 Requirements

- Python standard library (`random`)

### ▶️ How to Run

```bash
python hill.py
```

---

## 🧪 Sample Output

```text
Solving 8 Queens Problem using Hill Climbing Algorithm:
Current Board:
Q . . . . . . . 
. . Q . . . . . 
...
Cost: 3
...

Solution Found!
```

---

## 📊 Comparison of Algorithms

| Feature              | Genetic Algorithm     | Hill Climbing       |
|----------------------|------------------------|----------------------|
| Search Style         | Population-based       | Single-state based   |
| Stuck in Local Max   | Rare (due to mutation) | Frequent (uses restart) |
| Speed                | Medium                 | Fast                 |
| Complexity           | Higher                 | Lower                |

---

## 💡 Learning Outcomes

- Applied local search techniques to a classic AI problem  
- Understood how mutation, crossover, and fitness guide genetic evolution  
- Observed how greedy algorithms can get stuck in local maxima  
- Learned trade-offs between exploration vs exploitation  

---

## 👨‍💻 Author

**Hareram Kushwaha**  
2nd Year CSE Student, KPRIET  
_"Learning AI one queen at a time."_ 👑

---

## 📜 License

This project is for academic use and personal learning.  
Feel free to use or modify with attribution.
