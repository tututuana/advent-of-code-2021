from collections import Counter

S, rules = open("input.txt").read().split('\n\n')

react = {}
for line in rules.strip().split('\n'):
    start,end = line.strip().split(' -> ')
    react[start] = end

characters = Counter()
for i in range(len(S)-1):
    characters[S[i] + S[i + 1]] += 1

for x in range(41):
    if x in [10,40]:
        count = Counter()
        for k in characters:
            count[k[0]] += characters[k]
        count[S[-1]] += 1
        print(max(count.values())-min(count.values()))

    characters2 = Counter()
    for k in characters:
        characters2[k[0]+react[k]] += characters[k]
        characters2[react[k]+k[1]] += characters[k]
    characters = characters2
