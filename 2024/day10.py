# f = open("day10testinput.txt", "r")
f = open("day10input.txt", "r")

grid = []

DIRECTIONS = {
	'U': (-1, 0),
	'R': (0, 1),
	'D': (1, 0),
	'L': (0, -1),
}

for line in f.readlines():
	new_line = []
	for c in line:
		if c != '\n':
			new_line.append(int(c))
	grid.append(new_line)

for line in grid:
	print(line)

# get trail heads
trail_heads = []
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == 0:
			trail_heads.append((x, y))


def discovered_trails_contains(discovered_trails: list[list[tuple[int, int]]], move_chain: list[tuple[int, int]]):
	for trail in discovered_trails:
		if len(trail) != len(move_chain):
			continue
		for i in range(len(trail)):
			if trail[i] != move_chain[i]:
				break

def explore_recursive(grid, current_position: tuple[int, int], move_chain: list[tuple[int, int]], explored_positions: list[tuple[int, int]], accumulated_score: int, discovered_trails: list[list[tuple[int, int]]]):
	possible_moves = []

	if grid[current_position[1]][current_position[0]] == 9:
		if not discovered_trails_contains(discovered_trails, move_chain):
			accumulated_score += 1
			discovered_trails.append(move_chain)
		explored_positions.append(current_position)
		return accumulated_score
	
	explored_positions.append(current_position)


	for direction in DIRECTIONS.values():
		next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
		# this was used in part 1
		# if next_position in explored_positions:
		# 	continue
		if next_position[0] < 0 or next_position[0] >= len(grid[0]) or next_position[1] < 0 or next_position[1] >= len(grid):
			continue
		if grid[next_position[1]][next_position[0]] != grid[current_position[1]][current_position[0]] + 1:
			continue
		possible_moves.append(next_position)
	
	if len(possible_moves) == 0:
		move_chain.pop()
		return accumulated_score

	for move in possible_moves:
		new_move_chain = []
		for old_move in move_chain:
			new_move_chain.append(old_move)
		new_move_chain.append(move)
		
		accumulated_score = explore_recursive(grid, move, new_move_chain, explored_positions, accumulated_score, discovered_trails)
	return accumulated_score
		
		
		


def get_trail_head_score(trail_head: tuple[int, int]):
	trail_head_score = 0
	explored_positions = []
	move_chain = []
	original_head = trail_head
	current_position = trail_head
	discovered_trails = []

	return explore_recursive(grid, current_position, move_chain, explored_positions, 0, discovered_trails)


total_score = 0
for trail_head in trail_heads:
	total_score += get_trail_head_score(trail_head)

print(total_score)

