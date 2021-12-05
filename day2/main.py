def read_data():
    with open("input.txt", "r") as f:
        data = f.read().split("\n")
    return data

data = read_data()

def part1():
    depth = 0
    horizontal = 0
    for line in data:
        if line.startswith("down"):
            depth += int(line.split(" ")[1])
        elif line.startswith("up"):
            depth -= int(line.split(" ")[1])
        elif line.startswith("forward"):
            horizontal += int(line.split(" ")[1])
    return depth * horizontal

def part2():
    aim = 0
    horiz = 0
    depth = 0
    for line in data:
        if line.startswith("down"):
            aim += int(line.split(" ")[1])
        elif line.startswith("up"):
            aim -= int(line.split(" ")[1])
        elif line.startswith("forward"):
            horiz += int(line.split(" ")[1])
            depth += aim * int(line.split(" ")[1])
    return depth * horiz

print(part1(), part2())
