import os

def count(step):
    levels = [int(x) for x in open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split("\n")]
    sum = 0
    for i in range(len(levels) - step):
        if levels[i] < levels[i + step]:
            sum += 1
    return sum

print(count(1), count(3))
