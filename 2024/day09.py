# f = open("day09testinput.txt", "r")
f = open("day09input.txt", "r")

# read first line
line = f.readline()

# uncompress data
uncompressed_data = []
next_id = 0
is_data = True
for char in line:
	if char == "\n":
		break
	if is_data:
		for i in range(int(char)):
			uncompressed_data.append(next_id)
		next_id += 1
	else:
		for i in range(int(char)):
			uncompressed_data.append('.')
	is_data = not is_data

print(uncompressed_data)

# reorganize data part 1
# left_most_explored = -1
# for i in range(len(uncompressed_data) - 1, 0, -1):
# 	if uncompressed_data[i] == '.':
# 		continue
# 	if i <= left_most_explored:
# 		break
# 	next_free_id = -1
# 	for j in range(left_most_explored + 1, len(uncompressed_data), 1):
# 		left_most_explored = j
# 		if uncompressed_data[j] == '.':
# 			next_free_id = j
# 			break
# 	if next_free_id != -1 and next_free_id < i:
# 		uncompressed_data[next_free_id] = uncompressed_data[i]
# 		uncompressed_data[i] = '.'

# reorganize data part 2

# returns (id, length, start_position (from the end))
def find_data_block(uncompressed_data, start_index) -> (int, int, int):
	id = -1
	length = 0
	start_position = -1

	i = start_index
	while i >= 0:
		if length == 0:
			if uncompressed_data[i] != '.':
				id = uncompressed_data[i]
				length = 1
				start_position = i
			i -= 1
		else:
			if uncompressed_data[i] == id:
				length += 1
			else:
				break
			i -= 1

	return (id, length, start_position)			


i = len(uncompressed_data) - 1

while True:
	# identify data block
	data_block = find_data_block(uncompressed_data, i)
	if data_block[0] == -1:
		break

	# find free space
	next_free_id = -1
	next_free_length = 0
	for j in range(0, len(uncompressed_data), 1):
		if uncompressed_data[j] == '.':
			if next_free_length == 0:
				next_free_id = j
			next_free_length += 1
		else:
			if next_free_length >= data_block[1]:
				break
			else:
				next_free_id = -1
				next_free_length = 0
	
	if next_free_length < data_block[1] or next_free_id > data_block[2]:
		i = data_block[2] - data_block[1]
		continue
	
	# move data
	if next_free_id != -1 and next_free_id < data_block[2]:
		for j in range(next_free_id, next_free_id + data_block[1], 1):
			uncompressed_data[j] = uncompressed_data[data_block[2]]
		for j in range(data_block[2], data_block[2] - data_block[1], -1):
			uncompressed_data[j] = '.'
		i += 1
	i -= 1
	
	# if next_free_id != -1 and next_free_id < i:
	# 	uncompressed_data[next_free_id] = uncompressed_data[i]
	# 	uncompressed_data[i] = '.'

	



# print(uncompressed_data)

# calculate checksum
checksum = 0
for i in range(len(uncompressed_data)):
	if uncompressed_data[i] == '.':
		continue
	checksum += uncompressed_data[i] * (i)

print(checksum)