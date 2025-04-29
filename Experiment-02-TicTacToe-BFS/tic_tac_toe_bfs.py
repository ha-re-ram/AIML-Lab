from collections import deque

# Function to print the board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to get list of valid (empty) moves
def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']

# Function to apply a move
def make_move(board, move, player):
    board[move[0]][move[1]] = player

# BFS evaluation function
def bfs(board, current_player):
    queue = deque([(board, current_player)])
    
    while queue:
        current_board, player = queue.popleft()
        
        if check_winner(current_board, 'X'):
            return -1  # Human wins
        elif check_winner(current_board, 'O'):
            return 1   # AI wins
        elif not get_valid_moves(current_board):
            return 0   # Draw
        
        for move in get_valid_moves(current_board):
            next_board = [row[:] for row in current_board]
            make_move(next_board, move, 'O' if player == 'X' else 'X')
            queue.append((next_board, 'O' if player == 'X' else 'X'))

# Main game loop
def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("You are Player X. AI is Player O.")
    print("Enter your move as row and column (0, 1, or 2).")
    print_board(board)

    while True:
        if current_player == 'X':
            # Human move
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if (row not in range(3) or col not in range(3)) or board[row][col] != '-':
                print("Invalid move! Try again.")
                continue

            make_move(board, (row, col), 'X')
        else:
            # AI move
            print("AI is thinking...")
            best_score = -float('inf')
            best_move = None

            for move in get_valid_moves(board):
                temp_board = [row[:] for row in board]
                make_move(temp_board, move, 'O')
                score = bfs(temp_board, 'X')  # Evaluate after AI's move
                if score > best_score:
                    best_score = score
                    best_move = move

            make_move(board, best_move, 'O')
            print(f"AI plays at position {best_move}")

        print_board(board)

        # Check for win or draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif not get_valid_moves(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    main()
