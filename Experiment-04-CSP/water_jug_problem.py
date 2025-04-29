from collections import deque

# Function to check if a state is valid
def is_valid_state(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    return jug1 >= 0 and jug2 >= 0 and jug1 <= jug1_capacity and jug2 <= jug2_capacity

# Function to check if a state is the goal state
def is_goal_state(state, target):
    return state[0] == target or state[1] == target

# Function to get all possible successor states
def get_successors(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    successors = []
    
    # Fill jug1
    successors.append((jug1_capacity, jug2))
    
    # Fill jug2
    successors.append((jug1, jug2_capacity))
    
    # Empty jug1
    successors.append((0, jug2))
    
    # Empty jug2
    successors.append((jug1, 0))
    
    # Pour from jug1 to jug2
    pour_amount = min(jug1, jug2_capacity - jug2)
    successors.append((jug1 - pour_amount, jug2 + pour_amount))
    
    # Pour from jug2 to jug1
    pour_amount = min(jug2, jug1_capacity - jug1)
    successors.append((jug1 + pour_amount, jug2 - pour_amount))
    
    return [succ for succ in successors if is_valid_state(succ, jug1_capacity, jug2_capacity)]

# Function to perform breadth-first search
def bfs(initial_state, jug1_capacity, jug2_capacity, target):
    queue = deque([(initial_state, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        
        # Check if the goal state is reached
        if is_goal_state(state, target):
            return path + [state]
        
        visited.add(state)
        
        # Get successors
        successors = get_successors(state, jug1_capacity, jug2_capacity)
        
        for successor in successors:
            if successor not in visited:
                queue.append((successor, path + [state]))
    
    return None

def main():
    # Inputs
    jug1_capacity = int(input("Enter the capacity of jug 1: "))
    jug2_capacity = int(input("Enter the capacity of jug 2: "))
    target = int(input("Enter the target amount of water: "))
    
    initial_state = (0, 0)  # Initial state of jugs
    
    # Perform BFS
    path = bfs(initial_state, jug1_capacity, jug2_capacity, target)
    
    # Print solution path
    if path:
        print("Solution Found:")
        for state in path:
            print(f"Jug 1: {state[0]}, Jug 2: {state[1]}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
