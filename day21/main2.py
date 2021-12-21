from collections import defaultdict
from collections import Counter

ll = [int(x.split(": ")[1]) for x in open("input.txt").read().strip().split('\n')]

dice = list(Counter(
	i + j + k
	for i in range(1, 4)
	for j in range(1, 4)
	for k in range(1, 4)
).items())

universes = {(0, ll[0], 0, ll[1]): 1}
p1wins = 0
p2wins = 0
while universes:
	nuv = defaultdict(int)
	for state, cnt in list(universes.items()):
		score1, pos1, score2, pos2 = state
		for d, dcount in dice:
			p1 = (pos1 + d - 1) % 10 + 1
			s1 = score1 + p1
			if s1 >= 21:
				p1wins += cnt * dcount
				continue
			for d2, d2count in dice:
				p2 = (pos2 + d2 - 1) % 10 + 1
				s2 = score2 + p2
				if s2 >= 21:
					p2wins += cnt * dcount * d2count
					continue
				nuv[(s1, p1, s2, p2)] += cnt * dcount * d2count
	universes = nuv

print(max([p1wins, p2wins]))
