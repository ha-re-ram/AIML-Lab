import random

def generate_board():
    return [random.randint(0, 7) for _ in range(8)]

def calculate_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1
    return cost

def get_next_board(board):
    next_boards = []
    current_cost = calculate_cost(board)
    for i in range(8):
        for j in range(8):
            if j != board[i]:
                next_board = list(board)
                next_board[i] = j
                next_boards.append(next_board)
    next_boards.sort(key=lambda x: calculate_cost(x))
    return next_boards[0], calculate_cost(next_boards[0])

def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def hill_climbing():
    current_board = generate_board()
    current_cost = calculate_cost(current_board)
    while True:
        print("Current Board:")
        print_board(current_board)
        print("Cost:", current_cost)
        if current_cost == 0:
            print("Solution Found!")
            break
        next_board, next_cost = get_next_board(current_board)
        if next_cost >= current_cost:
            print("Local maximum reached. Restarting...")
            current_board = generate_board()
            current_cost = calculate_cost(current_board)
        else:
            current_board = next_board
            current_cost = next_cost

def main():
    print("Solving 8 Queens Problem using Hill Climbing Algorithm:")
    hill_climbing()

if __name__ == "__main__":
    main()