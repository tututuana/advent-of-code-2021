data = open('input.txt').readlines()

dots = set()
folds = []

for row in data:
    row = row.strip()
    if not row:
        continue
    if row.startswith('fold'):
        i = row.find('=')
        folds.append((row[i-1], int(row[i+1:])))
    else:
        dots.add(tuple(int(a) for a in row.split(',')))

def fold(grid, axis, coord):
    new = set()
    for coordx in grid:
        if axis == 'x':
            if coordx[0] > coord:
                new.add((coord + coord - coordx[0], coordx[1]))
            else:
                new.add( coordx )
        else:
            if coordx[1] > coord:
                new.add((coordx[0], coord + coord - coordx[1]))
            else:
                new.add(coordx)
    return new

def part1(dots):
    grid = fold(dots, * folds[0])
    return len(grid)

def render(dots):
    w = max(k[0] for k in dots) + 1
    h = max(k[1] for k in dots) + 1
    layout = [[' ' for _ in range(w)] for _ in range(h)]
    for coordx in dots:
        layout[coordx[1]][coordx[0]] = '#'
    return '\n'.join(''.join(k) for k in layout)

def part2(grid):
    for f in folds:
        grid = fold(grid, *f)
    return '\n' + render(grid)

print("1:", part1(dots))
print("2:", part2(dots))
