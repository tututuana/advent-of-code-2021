def CountBits(set, bit):
	one = 0
	zero = 0
	for num in set:
		if (num & (1 << bit)) != 0: one += 1
		else: zero += 1
	return (one, zero)

def Day03(input):
	bits = len(input[0])
	bitsets = [[0,0] for i in range(bits)]
	nums = []

	for line in input:
		if line == "": continue
		num = int(line, 2)
		for i in range(bits):
			if ((num & (1 << i)) != 0): bitsets[i][0] += 1
			else: bitsets[i][1] += 1
		nums.append(num)

	gamma = 0
	epsilon = 0
	for i in range(bits):
		gamma |= (bitsets[i][0] >= bitsets[i][1]) and (1 << i) or 0
		epsilon |= (bitsets[i][0] < bitsets[i][1]) and (1 << i) or 0

	print(f"Part 1: {epsilon * gamma}")

	current = nums
	oxygen = 0
	for i in range(bits-1, -1, -1):
		bitCount = CountBits(current, i)
		if bitCount[0] >= bitCount[1]:
			current = [num for num in current if (num & (1 << i)) != 0]
		else:
			current = [num for num in current if (num & (1 << i)) == 0]
		if len(current) == 1:
			oxygen = current[0]
			break

	current = nums
	co2 = 0
	for i in range(bits-1, -1, -1):
		bitCount = CountBits(current, i)
		if bitCount[0] < bitCount[1]:
			current = [num for num in current if (num & (1 << i)) != 0]
		else:
			current = [num for num in current if (num & (1 << i)) == 0]
		if len(current) == 1:
			co2 = current[0]
			break

	print(f"Part 2: {oxygen * co2}")



with open("input.txt", "r") as f:
    input = f.read().splitlines()
Day03(input)
