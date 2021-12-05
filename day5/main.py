lines = [line.rstrip('\n') for line in open('input.txt')]

def part1():
    hashmap = {}
    for l in lines:
        pts = l.split(" -> ")
        x1, y1 = pts[0].split(",")
        x2, y2 = pts[1].split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2 or y1 == y2:
            cix = 1 if x2 > x1 else -1
            ciy = 1 if y2 > y1 else -1
            for x in range(x1, x2 + cix, cix):
                for y in range(y1, y2 + ciy, ciy):
                    key = f"{x},{y}"
                    value = (hashmap.get(key) or 0) + 1
                    hashmap[key] = value
    print(len([v for v in hashmap.values() if v >= 2]))

def part2():
    import re
    import collections
    points = collections.defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups())

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                points[(x, y1)] += 1
        else:
            x_mod = -1 if x1 > x2 else 1
            y_mod = -1 if y1 > y2 else 1
            for x, y in zip(range(x1, x2+x_mod, x_mod), range(y1, y2+y_mod, y_mod)):
                points[(x, y)] += 1
    print(len([x for x in points.values() if x >= 2]))

if __name__ == "__main__":
    part1()
    part2()
