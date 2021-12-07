import math

def part1(inp):
    inp = [int(x) for x in inp.split(",")]
    minx = min(inp)
    maxx = max(inp)

    best = math.inf

    for i in range(minx, maxx + 1):
        cost = sum(abs(i - j) for j in inp)
        if cost < best:
            best = cost

    print(best)

def part2(inp):
    inp = [int(x) for x in inp.split(",")]
    minx = min(inp)
    maxx = max(inp)

    best = math.inf

    def f(n):
        return (n * (n + 1)) // 2

    for i in range(minx, maxx + 1):
        cost = sum(f(abs(i - j)) for j in inp)
        if cost < best:
            best = cost

    print(best)

with open("input.txt") as f:
    inp = f.read()

part1(inp)
part2(inp)
