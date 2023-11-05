import collections

# Define the grid
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# Define the start and goal nodes
start = (0, 0)
goal = (len(grid) - 1, len(grid[0]) - 1)

# Define the heuristic function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Define the successor function
def successors(node):
    # Get the row and column of the node
    row, col = node
    # Initialize an empty list of successors
    succ = []
    # Check the four adjacent cells
    if row > 0 and grid[row - 1][col] != 1:
        succ.append((row - 1, col)) # Up
    if row < len(grid) - 1 and grid[row + 1][col] != 1:
        succ.append((row + 1, col)) # Down
    if col > 0 and grid[row][col - 1] != 1:
        succ.append((row, col - 1)) # Left
    if col < len(grid[0]) - 1 and grid[row][col + 1] != 1:
        succ.append((row, col + 1)) # Right
    # Return the list of successors
    return succ

# Import the heapq module
import heapq

# Initialize the open list as a priority queue
open_list = []
# Initialize the closed list as a dictionary
closed_list = {}
# Push the start node to the open list with f = 0
heapq.heappush(open_list, (0, start))
# Set the parent of the start node to None
closed_list[start] = None

# Loop until the open list is empty
while open_list:
    # Pop the node with the lowest f from the open list
    f, node = heapq.heappop(open_list)
    # Check if the node is the goal node
    if node == goal:
        # Found the solution
        break
    # Generate the successors of the node
    for succ in successors(node):
        # Calculate the g value of the successor
        g = f + 1
        # Calculate the f value of the successor
        f = g + heuristic(succ, goal)
        # Check if the successor is already in the closed list
        if succ in closed_list:
            # Skip the successor
            continue
        # Push the successor to the open list with f
        heapq.heappush(open_list, (f, succ))
        # Set the parent of the successor to the node
        closed_list[succ] = node

# Check if the goal node was reached
if node == goal:
    # Initialize an empty list for the path
    path = []
    # Trace back the path from the goal node to the start node
    while node != start:
        # Add the node to the path
        path.append(node)
        # Get the parent of the node
        node = closed_list[node]
    # Add the start node to the path
    path.append(start)
    # Reverse the path
    path.reverse()
    # Print the path
    print("The shortest path is:")
    print(path)
else:
    # No solution was found
    print("No path was found.")
