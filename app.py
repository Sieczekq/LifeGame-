import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

from tkinter import simpledialog

GRID_SIZE = 200

def initialize_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.8, 0.2]).reshape(size, size)

# Funkcja do aktualizacji siatki na podstawie reguł gry
def update_grid(grid, survival_rules, birth_rules):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            total = int((grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                         grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                         grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                         grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]))
            if grid[i, j] == 1:
                if total not in survival_rules:
                    new_grid[i, j] = 0
            else:
                if total in birth_rules:
                    new_grid[i, j] = 1
    return new_grid

def update_plot(frameNum, img, grid, survival_rules, birth_rules):
    new_grid = update_grid(grid, survival_rules, birth_rules)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

def get_rules():
    root = tk.Tk()
    root.withdraw()  

    survival_rules = simpledialog.askstring("Reguły przetrwania", "Podaj liczby dla reguł przetrwania:")
    birth_rules = simpledialog.askstring("Reguły narodzin", "Podaj liczby dla reguł narodzin:")

    survival_rules = list(map(int, survival_rules.split(',')))
    birth_rules = list(map(int, birth_rules.split(',')))

    return survival_rules, birth_rules

# Główna funkcja
def main():
    global GRID_SIZE
    grid = initialize_grid(GRID_SIZE)
    
    # Pobranie reguł od użytkownika
    survival_rules, birth_rules = get_rules()

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    
    ani = animation.FuncAnimation(fig, update_plot, fargs=(img, grid, survival_rules, birth_rules), frames=10, interval=50, save_count=50)
    
    plt.show()

if __name__ == '__main__':
    main()
