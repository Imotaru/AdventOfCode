# f = open("day08testinput.txt", "r")
f = open("day08input.txt", "r")

grid = []

for line in f.readlines():
	new_line = []
	for c in line:
		if c != '\n':
			new_line.append(c)
	grid.append(new_line)

nodes = {}

# create nodes dictionary
for y in range(len(grid)):
	for x in range(len(grid[y])):
		c = grid[y][x]
		if c != '.':
			if c not in nodes.keys():
				nodes[c] = []
			nodes[c].append((x, y))

anti_nodes = {}
unique_anti_node_count = 0

for node_type in nodes.keys():
	for i in range(len(nodes[node_type])):
		for j in range(len(nodes[node_type])):
			if i == j:
				continue

			step_count = 0
			while True:
				x = nodes[node_type][i][0] + (nodes[node_type][i][0] - nodes[node_type][j][0]) * step_count
				y = nodes[node_type][i][1] + (nodes[node_type][i][1] - nodes[node_type][j][1]) * step_count

				if len(grid[0]) > x >= 0 and len(grid) > y >= 0:
					step_count += 1
					if node_type not in anti_nodes.keys():
						anti_nodes[node_type] = []
					anti_nodes[node_type].append((x, y))
					if grid[y][x] != '#':
						grid[y][x] = '#'
						unique_anti_node_count += 1
				else:
					# out of bounds, can stop searching
					break

for line in grid:
	squished = ""
	for c in line:
		squished += c
	print(squished)
print(unique_anti_node_count)