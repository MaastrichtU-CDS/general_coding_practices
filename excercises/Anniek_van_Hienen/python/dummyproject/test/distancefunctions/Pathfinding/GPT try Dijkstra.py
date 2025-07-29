
# Create a grid
def create_grid(rows, cols):
    """Create a grid with given rows and columns, initialized to 'O'."""
    return [['O' for i in range(cols)] for i in range(rows)]

def print_grid(grid):
    """Print the grid in a readable format."""
    for row in grid:
        print(' '.join(row))

def set_barrier(grid, row, col):
    """Set a barrier at the specified position (row, col)."""
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = 'X'
    else:
        print(f"Position ({row}, {col}) is out of bounds.")

# Example usage:
print("Creating a grid...")

rows, cols = 5, 5  # Size of the grid
grid = create_grid(rows, cols)

# Set barriers
set_barrier(grid, 1, 1)
set_barrier(grid, 2, 3)
set_barrier(grid, 4, 0)

# Print the grid
print("Grid with barriers:")
print_grid(grid)
