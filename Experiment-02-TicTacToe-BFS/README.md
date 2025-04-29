# 🎮 AIML Experiment 2 – Tic Tac Toe (Human vs AI using BFS)

This project is part of the Artificial Intelligence & Machine Learning (AIML) lab experiments. It features a simple implementation of the **Tic Tac Toe** game, where a **human** competes against an **AI opponent** using the **Breadth-First Search (BFS)** strategy to determine its moves.

---

## 🧠 Objective

To simulate an interactive game between a human and an AI, where the AI uses **BFS** to:
- Explore all possible game states.
- Evaluate the outcomes of each move.
- Choose the best move to maximize its chances of winning.

---

## 📌 Features

- 3x3 Tic Tac Toe grid.
- Human plays as `X`, AI plays as `O`.
- Intelligent AI that uses **Breadth-First Search** to simulate future game moves.
- Clear visual representation of the board in the terminal.
- Win, draw, or loss conditions detected and displayed.

---

## 📁 Project Structure

Experiment-02-TicTacToe-BFS/ 
   ├── tic_tac_toe_bfs.py # Python source code 
   └── README.md 

## Project documentation

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.

2. Clone or download this repository, then open a terminal in the project directory.

3. Run the game:
   ```bash
   python tic_tac_toe_bfs.py

4. Follow the on-screen instructions:
    Input the row and column numbers (0 to 2) when prompted.
    The AI will respond with its move automatically.

---
## 🧠 AI Logic Explained (BFS)

The AI uses Breadth-First Search (BFS) to:
    Generate all possible game states from the current board.
    Check each future move until a terminal state (win/loss/draw) is reached.
    Choose the move that leads to the best outcome:
        +1 for AI win
        -1 for human win
        0 for draw
    This helps the AI avoid losing moves and favor winning or draw states.

---

🛠️ Code Highlights
print_board(board) — Neatly prints the current game board.

check_winner(board, player) — Checks if the specified player has won.

get_valid_moves(board) — Finds all empty cells.

bfs(board, player) — Runs BFS to evaluate future board states.

main() — Controls the game loop and switches turns.

---

💡 Learning Outcome
By completing this experiment, students will:

Understand how search algorithms can be applied to games.

Learn how to simulate turn-based logic using Python.

Build AI decision-making using tree-based evaluation.

---

📦 Requirements
No external libraries required. The game uses only built-in Python modules:

 collections.deque — For BFS queue

---

👨‍💻 Author
Hareram Kushwaha
2nd Year CSE, KPRIET
🌟 "Building intelligence, one game at a time."


---

Let me know if you’d like a **combined README** with both Experiment 1 (Data Analysis) and Experiment 2 (Tic Tac Toe) or a zipped folder structure layout.
