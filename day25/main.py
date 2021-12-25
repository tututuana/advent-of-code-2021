f = open("input.txt").read().strip().split("\n")

vsx = []
rights = []

maxx = len(f[0])
_max = len(f)

for i, line in enumerate(f):
    for j, char in enumerate(line):
        if line[j] == "v":
            vsx.append((i, j))
        if line[j] == ">":
            rights.append((i, j))

turn = 0
while True:
    rset = set(rights)
    vset = set(vsx)
    move = 0
    newRights = []
    newVs = []
    for r in rights:
        i, j = r
        nextLoc = (i, (j + 1) % maxx)
        if nextLoc in rset or nextLoc in vset:
            newRights.append(r)
        else:
            newRights.append(nextLoc)
            move += 1
    rset = set(newRights)
    for v in vsx:
        i, j = v
        nextLoc = ((i + 1) % _max, j)
        if nextLoc in vset or nextLoc in rset:
            newVs.append(v)
        else:
            newVs.append(nextLoc)
            move += 1
    rights = newRights
    vsx = newVs
    turn += 1
    if move == 0:
        break

print("1:", turn)
