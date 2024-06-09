import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the dimensions of the grid
GRID_SIZE = 100

# Initialize the grid with random states
def initialize_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.8, 0.2]).reshape(size, size)

# Update the grid based on the Game of Life rules
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            total = int((grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                         grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                         grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                         grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]))
            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

# Function to update the plot
def update_plot(frameNum, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Main function
def main():
    grid = initialize_grid(GRID_SIZE)
    
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    
    ani = animation.FuncAnimation(fig, update_plot, fargs=(img, grid), frames=10, interval=50, save_count=50)
    
    plt.show()

if __name__ == '__main__':
    main()
