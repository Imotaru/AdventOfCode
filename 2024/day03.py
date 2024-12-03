import re
import time

start_time = time.time()

# f = open("day03testinput.txt", "r")
f = open("day03input.txt", "r")

part1CommandList = []

part2CommandList = []
do_list = []
dont_list = []

for line in f.readlines():
	part1CommandList.append(re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line))

	part2CommandList.append(re.finditer(r'(mul\((\d{1,3}),(\d{1,3})\))', line))
	do_list.append(re.finditer(r'do\(\)', line))
	dont_list.append(re.finditer(r'don\'t\(\)', line))

# part 1
sum = 0
for commands in part1CommandList:
	for command in commands:
		sum += int(command[0]) * int(command[1])
print(f"Part 1: {sum}")


# part 2
sum = 0
currently_doing = True

for i in range(len(part2CommandList)):
	do_indexes = []
	dont_indexes = []
	command_indexes = []

	for do_command in do_list[i]:
		do_indexes.append(do_command.start())
	for dont_command in dont_list[i]:
		dont_indexes.append(dont_command.start())
	for command in part2CommandList[i]:
		command_indexes.append(command.start())

	commands_popped = 0
	for j in range(len(do_indexes) + len(dont_indexes) + len(command_indexes)):
		smallest_index_source = ''
		smallest_index = 2_140_000_000

		if len(do_indexes) >= 1 and do_indexes[0] < smallest_index:
			smallest_index = do_indexes[0]
			smallest_index_source = 'do'

		if len(dont_indexes) >= 1 and dont_indexes[0] < smallest_index:
			smallest_index = dont_indexes[0]
			smallest_index_source = 'dont'

		if len(command_indexes) >= 1 and command_indexes[0] < smallest_index:
			smallest_index = command_indexes[0]
			smallest_index_source = 'command'

		if smallest_index_source == 'do':
			currently_doing = True
			do_indexes = do_indexes[1:]
		elif smallest_index_source == 'dont':
			currently_doing = False
			dont_indexes = dont_indexes[1:]
		elif smallest_index_source == 'command':
			if currently_doing:
				sum += int(part1CommandList[i][commands_popped][0]) * int(part1CommandList[i][commands_popped][1])
			command_indexes = command_indexes[1:]
			commands_popped += 1

print(f"Part 2: {sum}")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")