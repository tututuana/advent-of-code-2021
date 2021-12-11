from itertools import product, count

grid = [line.strip() for line in open('input.txt', 'r') if line.strip()]

width, height = len(grid[0]), len(grid)

def neighbors(p):
    for prod in product(range(-1, 2), repeat=2):
        if prod == (0, 0):
            continue
        x = p[0] + prod[0]
        y = p[1] + prod[1]
        if (0 <= x < width) and (0 <= y < height):
            yield (x, y)

grid = [[int(x) for x in row] for row in grid]

cells = width * height
total_flashes = 0
for step in count(1):
    flashes = 0
    grid = [[x + 1 for x in row] for row in grid]
    stack = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x > 9]
    while stack:
        (i, j) = stack.pop()
        flashes += 1
        for (i1, j1) in neighbors((i, j)):
            grid[i1][j1] += 1
            if grid[i1][j1] == 10:
                stack.append((i1, j1))
    total_flashes += flashes
    if step == 100:
        print(f"1: {total_flashes}")
    if flashes == cells:
        print(f"2: {step}")
        break
    grid = [[0 if x > 9 else x for x in row] for row in grid]
