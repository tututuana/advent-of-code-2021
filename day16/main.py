def parsex(allbits):
    v = allbits[:3]
    allbits = allbits[3:]
    v = int(v, base=2)
    t = allbits[:3]
    allbits = allbits[3:]
    t = int(t, base=2)
    if t == 4:
        parts = ''
        while True:
            p = allbits[:5]
            allbits = allbits[5:]
            parts += p[1:]
            if p[0] == '0':
                break
        n = int(parts, base=2)
        packet = (v, t, n)
        return packet, allbits
    i = allbits[0]
    allbits = allbits[1:]
    if i == '0':
        l = allbits[:15]
        allbits = allbits[15:]
        sub_len = int(l, 2)
        sub = []
        sub_bits = allbits[:sub_len]
        allbits = allbits[sub_len:]
        while sub_bits:
            s, sub_bits = parsex(sub_bits)
            sub.append(s)
    else:
        l = allbits[:11]
        allbits = allbits[11:]
        sub = []
        for _ in range(int(l, base=2)):
            s, allbits = parsex(allbits)
            sub.append(s)

    packet = (v, t, i, l, sub)
    return packet, allbits

def parse(s):
    allbits = []
    for n in [int(n, base=16) for n in s]:
        b = bin(n)[2:]
        while len(b) < 4:
            b = '0' + b
        allbits.extend(list(b))
    allbits = ''.join(allbits)
    return parsex(allbits)[0]

def part1(s):
    packet = parse(s)
    to_handle = [packet]
    answer = 0

    while to_handle:
        p = to_handle.pop(0)
        answer += p[0]
        if p[1] == 4:
            continue
        to_handle.extend(p[4])

    print(f'1: {answer}')

def eval_packet(p):
    t = p[1]
    if t == 4:
        return p[2]

    sub = p[4]
    vals = list(map(eval_packet, sub))
    if t == 0:
        return sum(vals)
    if t == 1:
        out = 1
        for p in sub:
            out *= eval_packet(p)
        return out
    if t == 2:
        return min(vals)
    if t == 3:
        return max(vals)
    if t == 5:
        return 1 if vals[0] > vals[1] else 0
    if t == 6:
        return 1 if vals[0] < vals[1] else 0
    if t == 7:
        return 1 if vals[0] == vals[1] else 0

def part2(s):
    answer = eval_packet(parse(s))

    print(f'2: {answer}')

input = open('input.txt', "r").read()
part1(input)
part2(input)
