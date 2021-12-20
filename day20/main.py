import numpy as np
with open("input.txt") as f:
    data = f.read()

key, grid = data.split("\n\n")
grid = np.array([[str(int(y == "#")) for y in x] for x in grid.split("\n")])

def pad_grid(grid, fill, padding=2):
    bigger_grid = np.full(
        (grid.shape[0] + 2 * padding, grid.shape[1] + 2 * padding), fill
    )
    bigger_grid[
        padding : grid.shape[0] + padding, padding : grid.shape[1] + padding
    ] = grid
    return bigger_grid

def decode(key, grid, iterations=2):
    for idx in range(iterations):
        fill = "0" if idx == 0 else grid[0, 0]
        grid = pad_grid(grid, str(idx % 2))
        output = np.full((grid.shape[0] - 2, grid.shape[1] - 2), "0")
        for i in range(grid.shape[0] - 2):
            for j in range(grid.shape[1] - 2):
                stuff = grid[i : i + 3, j : j + 3].flatten()
                output[i, j] = str(int(key[int("".join(stuff), 2)] == "#"))
        grid = output
    return grid

output = decode(key, grid)
print("1:", sum(x == "1" for x in output.flatten()))

output = decode(key, grid, iterations=50)
print("2:", sum(x == "1" for x in output.flatten()))
