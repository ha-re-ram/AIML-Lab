from collections import deque

# Define the territories and their neighbors
T = 'tasmania'
WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'

# Define the colors
colors = {'r', 'g', 'b'}

# Define the map of Australia
australia = {
    T: [V],
    WA: [NT, SA],
    NT: [WA, Q, SA],
    SA: [WA, NT, Q, NSW, V],
    Q: [NT, SA, NSW],
    NSW: [Q, SA, V],
    V: [SA, NSW, T]
}

# Function to check if the coloring is valid
def is_valid_coloring(coloring):
    for territory, neighbors in australia.items():
        for neighbor in neighbors:
            if coloring.get(territory) == coloring.get(neighbor):
                return False
    return True

# Function to perform BFS for map coloring
def bfs_map_coloring(territories, colors):
    queue = deque([(territories, {})])
    
    while queue:
        current_territories, coloring = queue.popleft()
        
        # If all territories are colored, check if the coloring is valid
        if len(coloring) == len(territories):
            if is_valid_coloring(coloring):
                return coloring
        
        for territory in current_territories:
            if territory not in coloring:
                for color in colors:
                    new_coloring = dict(coloring)
                    new_coloring[territory] = color
                    queue.append((current_territories, new_coloring))
    
    return None

def main():
    problem = bfs_map_coloring(australia.keys(), colors)
    
    if problem:
        print("Valid Coloring:")
        for territory, color in problem.items():
            print(f"{territory}: {color}")
    else:
        print("No valid coloring found.")

if __name__ == "__main__":
    main()
