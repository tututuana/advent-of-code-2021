def part1(data):
    brackets = {
      "(": ")",
      "[": "]",
      "{": "}",
      "<": ">",
    }

    scores = {
      ")": 3,
      "]": 57,
      "}": 1197,
      ">": 25137,
    }

    score = 0
    for line in data.split("\n"):
      stack = []
      for char in line:
        if char in brackets:
          stack.append(char)
        else:
          if not stack or char != brackets[stack.pop()]:
            score += scores[char]
            break
    return score

def part2(data):
	left, right = ["(", "[", "{", "<"], [")", "]", "}", ">"]

	score = {
		")": 3,
		"]": 57,
		"}": 1197,
		">": 25137
	}

	scores = []

	for line in data.split("\n"):
		ok = True
		stack = []

		for token in line:
			if token in left:
				stack.append(token)
			else:
				last = stack.pop()
				if right.index(token) != left.index(last):
					ok = False
					break

		if ok:
			score = 0
			while stack:
				score *= 5
				posScore = left.index(stack.pop())
				score += posScore + 1
			scores.append(score)

	scores.sort()
	return scores[len(scores) // 2]


with open("input.txt", "r") as f:
    data = f.read()
    print(part1(data), part2(data))
