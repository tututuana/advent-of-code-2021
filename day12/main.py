from collections import defaultdict

paths = defaultdict(list)
for line in open('input.txt'):
    a, b = line.strip().split('-')
    paths[a].append(b)
    paths[b].append(a)

def count_paths(paths, start, end, seen=None, used_double=False):
    if seen is None:
        seen = set()

    if start == end:
        return 1

    n_paths = 0
    for a in paths[start]:
        new_used_double = used_double
        if a == a.lower() and a in seen:
            if used_double or a in ['start', 'end']:
                continue
            else:
                new_used_double = True

        n_paths += count_paths(paths, a, end, seen | {start}, new_used_double)

    return n_paths

print(count_paths(paths, 'start', 'end', used_double=True))
print(count_paths(paths, 'start', 'end'))
