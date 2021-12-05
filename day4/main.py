import numpy as np

def solve(i, a, part):
    m = np.zeros((a.shape[:]))
    won = set()
    for j,n in enumerate(i):
        for k,o in enumerate(a):
            for l in range(len(o)):
              if n in o[l,:]:
                    m[k, l, [h for h,f in enumerate(o[l,:]) if f == n][0]] = 1
              if n in o[:, l]:
                    m[k, [h for h,f in enumerate(o[:,l]) if f == n][0], l] = 1
              if part == 1 and (sum(m[k, l, :]) == len(o) or sum(m[k, :, l]) == len(o)):
                    return n * sum([o[s, g] for s,f in enumerate((m == 0)[k]) for g,h in enumerate(f) if h == True])
              if part == 2 and (sum(m[k, l, :]) == len(o) or sum(m[k, :, l]) == len(o)):
                    won.add(k)
              if part == 2 and len(won) == len(a):
                    return n * sum([o[s, g] for s,f in enumerate((m == 0)[k]) for g,h in enumerate(f) if h == True])

def main():
    b = [l.split(',') if i == 0 else l.split('\n') for i, l in enumerate(open('input.txt','r').read().strip().split('\n\n'))]
    inp = np.array(b.pop(0), dtype='int')
    a = []
    for l in b:
        t = []
        for w in l:
          t.append(w.split())
        a.append(t)
    a = np.array(a, dtype='int')
    print(solve(inp, a, 1), solve(inp, a, 2))

main()
