import ast
import math

def parse_input(i):
	out = []
	for line in i:
		out.append(ast.literal_eval(line.strip()))
	return out

def length(num):
	if isinstance(num, list):
		return sum([length(n) for n in num])
	else:
		return 1

def snailnum_ref(num, n):
	if isinstance(num, list):
		if n < length(num[0]):
			return snailnum_ref(num[0], n)
		else:
			return snailnum_ref(num[1], n - length(num[0]))
	else:
		if n > 0:
			print("Fail")
		return num

def snailnum_modify(num, n, new_val):
	if isinstance(num, list):
		if n < length(num[0]):
			return [snailnum_modify(num[0], n, new_val), num[1]]
		else:
			return [num[0], snailnum_modify(num[1], n - length(num[0]), new_val)]
	else:
		if n > 0:
			print("Fail")
		return new_val

def snailnum_replace(num, path, new_val):
	if len(path) > 0:
		if path[0] == 0:
			return [snailnum_replace(num[0], path[1:], new_val), num[1]]
		elif path[0] == 1:
			return [num[0], snailnum_replace(num[1], path[1:], new_val)]
	else:
		return new_val

def earliest_explode(num, acc):
	if isinstance(num, int):
		return None
	first_ref = 0
	secnd_ref = length(num[0])
	if isinstance(num[0], int) and isinstance(num[1], int) and acc >= 4:
		return [0, 1, []]
	else:
		first_explode = earliest_explode(num[0], acc + 1)
		if first_explode is None:
			pass
		else:
			new_path = [0]
			new_path.extend(first_explode[2])
			return [first_explode[0], first_explode[1], new_path]
		secnd_explode = earliest_explode(num[1], acc + 1)
		if secnd_explode is None:
			pass
		else:
			new_path = [1]
			new_path.extend(secnd_explode[2])
			return [secnd_ref + secnd_explode[0], secnd_ref + secnd_explode[1], new_path]

def splitting_path(num):
	if isinstance(num, int):
		if num >= 10:
			return True
		else:
			return None
	else:
		left_path = splitting_path(num[0])
		if left_path is True:
			return [0]
		elif isinstance(left_path, list):
			out = [0]
			out.extend(left_path)
			return out
		right_path = splitting_path(num[1])
		if right_path is True:
			return [1]
		elif isinstance(right_path, list):
			out = [1]
			out.extend(right_path)
			return out
	return None

def split(num, path):
	if len(path) > 0:
		nxt = path.pop(0)
		if nxt == 0:
			return [split(num[0], path), num[1]]
		elif nxt == 1:
			return [num[0], split(num[1], path)]
	else:
		to_split = num
		return [to_split // 2, math.ceil(to_split / 2)]

def reduce(num):
	mod = False
	while True:
		exploding_pair = earliest_explode(num, 0)
		if exploding_pair is not None:
			if exploding_pair[0] > 0:
				num = snailnum_modify(num, exploding_pair[0] - 1, snailnum_ref(num, exploding_pair[0] - 1) + snailnum_ref(num, exploding_pair[0]))
			if exploding_pair[1] < length(num) - 1:
				num = snailnum_modify(num, exploding_pair[1] + 1, snailnum_ref(num, exploding_pair[1] + 1) + snailnum_ref(num, exploding_pair[1]))
			num = snailnum_replace(num, exploding_pair[2], 0)
			mod = True
			continue
		split_path = splitting_path(num)
		if split_path is not None:
			num = split(num, split_path)
			continue
		break
	return num

def magnitude(num):
	if isinstance(num, int):
		return num
	else:
		return (3 * magnitude(num[0])) + (2 * magnitude(num[1]))

def add_snailnums(fst, snd):
	unreduced = [fst, snd]
	reduced = reduce(unreduced)
	return reduced

def part1(i):
	final_num = i.pop(0)
	while len(i) > 0:
		nxt = i.pop(0)
		final_num = add_snailnums(final_num, nxt)
	return magnitude(final_num)

def part2(i):
	curr_best = 0
	for x in range(len(i)):
		for y in range(len(i)):
			if x != y:
				curr_best = max(magnitude(add_snailnums(i[x], i[y])), magnitude(add_snailnums(i[y], i[x])), curr_best)
	return curr_best

def main():
	with open("input.txt", "r") as f:
		i = parse_input(f.readlines())
	print(part1(i))
	with open("input.txt", "r") as f:
		i = parse_input(f.readlines())
	print(part2(i))

if __name__ == '__main__':
	main()
