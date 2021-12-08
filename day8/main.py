from itertools import permutations

input = open('input.txt', 'r').read().split('\n')

def part1():
    iter = 0
    for line in input:
        matters = line.split(' | ')[1].split(' ')
        for thing in matters:
            if len(thing) in [2, 4, 3, 7]:
                iter += 1
                return iter

def part2():
    m = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7, "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}
    m = {"".join(sorted(k)):v for k,v in m.items()}
    ans = 0
    for line in input:
        a,b = line.split(" | ")
        a = a.split(" ")
        b = b.split(" ")
        for perm in permutations("abcdefg"):
            pmap = {a:b for a,b in zip(perm,"abcdefg")}
            anew = ["".join(pmap[c] for c in x) for x in a]
            bnew = ["".join(pmap[c] for c in x) for x in b]
            if all("".join(sorted(an)) in m for an in anew):
                bnew = ["".join(sorted(x)) for x in bnew]
                ans += int("".join(str(m[x]) for x in bnew))
                return ans

print(part1(), part2())
