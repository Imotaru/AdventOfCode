import re

# f = open("day01testinput.txt", "r")
f = open("day01input.txt", "r")

left_arr = []
right_arr = []

for line in f.readlines():
	numbers = re.findall(r'\d+', line)
	left_arr.append(int(numbers[0]))
	right_arr.append(int(numbers[1]))

left_arr.sort()
right_arr.sort()

diff = 0

for i in range(len(left_arr)):
	diff += abs(left_arr[i] - right_arr[i])

# part 1 solution
print(diff)

similarity = 0

for l in left_arr:
	for r in right_arr:
		if r == l:
			similarity += l
		elif r > l:
			# since the lists are sorted we can break once r > l
			break

print(similarity)