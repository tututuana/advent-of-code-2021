from collections import deque

with open('input.txt') as f:
    data = f
    d = deque([0] * 9)
    for i in map(int, data.read().split(",")):
        d[i] += 1

for part in (80, 256 - 80):
    for _ in range(part):
        d.append(d.popleft())
        d[6] += d[-1]
    print(sum(d))
