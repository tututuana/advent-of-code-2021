from functools import lru_cache

_input = [x for x in open("input.txt").read().strip().split('\n')]

vs = 'wxyz'

def simulate(line, state):
	state = list(state)
	cmd = line.split(" ")[0]
	if cmd == 'inp':
		raise Exception("")
	a = line.split(" ")[1]
	b = line.split(" ")[2]
	def parse(x):
		if x in vs:
			return state[vs.index(x)]
		return int(x)
	if cmd == 'add':
		state[vs.index(a)] += parse(b)
	if cmd == 'mul':
		state[vs.index(a)] *= parse(b)
	if cmd == 'div':
		state[vs.index(a)] //= parse(b)
	if cmd == 'mod':
		state[vs.index(a)] %= parse(b)
	if cmd == 'eql':
		state[vs.index(a)] = int(state[vs.index(a)] == parse(b))
	return tuple(state)

@lru_cache(maxsize=None)
def run2(ch, zstart, w):
	state = (w, 0, 0, zstart)
	for i in range(ch*18+1, ch*18+18):
		state = simulate(_input[i], state)
	r = state[3]
	print(run(ch, zstart, w) == r)
	return r

AX, DZ, AY = [], [], []
for lineno, line in enumerate(_input):
	if "add x " in line and "add x z" not in line:
		AX.append(int(line.split()[2]))
	if "div z " in line:
		DZ.append(int(line.split()[2]))
	if "add y " in line and lineno%18 == 15:
		AY.append(int(line.split()[2]))

def run(ch, z, w):
	x = AX[ch] + (z % 26)
	z = z // DZ[ch]
	if x != w:
		z *= 26
		z += w + AY[ch]
	return z

Zbudget = [26**len([x for x in range(len(DZ)) if DZ[x]==26 and x >= i]) for i in range(len(DZ))]
CANDIDATES = list(range(1, 10))
@lru_cache(maxsize=None)
def search(ch, zsofar):
	if ch == 14:
		if zsofar == 0:
			return [""]
		return []
	if zsofar > Zbudget[ch]:
		return []
	xwi_inputbe = AX[ch] + zsofar % 26
	wopts = CANDIDATES
	if xwi_inputbe in range(1, 10):
		wopts = [xwi_inputbe]
	ret = []
	for w in wopts:
		znext = run(ch, zsofar, w)
		nxt = search(ch + 1, znext)
		for x in nxt:
			ret.append(str(w) + x)
	return ret

solns = search(0, 0)
solns = [int(x) for x in solns]
print("1:", max(solns))
print("2:", min(solns))
