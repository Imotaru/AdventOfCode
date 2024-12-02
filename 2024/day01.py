import re
import time

start_time = time.time()

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
last_r = 0

for l in left_arr:
	for i in range(last_r, len(right_arr)):
		r = right_arr[i]
		if r == l:
			similarity += l
		elif r > l:
			break
		last_r += 1

# part 2 solution
print(similarity)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")