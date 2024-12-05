import re
import time

start_time = time.time()

# f = open("day04testinput.txt", "r")
f = open("day04input.txt", "r")

letter_grid = []

for line in f.readlines():
	letter_grid.append(line[:-1])

DIMENSION_X = len(letter_grid[0])
DIMENSION_Y = len(letter_grid)

vertical = []
diagonal_top_left = []
diagonal_top_right = []

# build vertical array
for y in range(DIMENSION_Y):
	column = ""
	for x in range(DIMENSION_X):
		column += letter_grid[x][y]
	vertical.append(column)

# build diagonal top left
for y in range(DIMENSION_Y):
	row = ""
	for x in range(DIMENSION_X):
		if y + x >= DIMENSION_Y:
			break
		row += letter_grid[x][y + x]
	diagonal_top_left.append(row)

for x in range(1, DIMENSION_X):
	row = ""
	for y in range(DIMENSION_Y):
		if y + x >= DIMENSION_Y:
			break
		row += letter_grid[x + y][y]
	diagonal_top_left.append(row)

# build diagonal top right
for y in range(DIMENSION_Y):
	row = ""
	for x in range(DIMENSION_X):
		x = DIMENSION_X - x - 1
		if y - x < 0:
			continue
		row += letter_grid[x][y - x]
	diagonal_top_right.append(row)

for x in range(DIMENSION_X - 1):
	row = ""
	x = DIMENSION_X - x - 1
	for y in range(DIMENSION_X - x):
		y = DIMENSION_Y - y - 1
		row += letter_grid[x - y + DIMENSION_Y - 1][y]
	diagonal_top_right.append(row)

count = 0

XMAS = "XMAS"
XMAS_REVERSE = XMAS[::-1]

for row in letter_grid:
	count += row.count(XMAS)
	count += row.count(XMAS_REVERSE)
for row in vertical:
	count += row.count(XMAS)
	count += row.count(XMAS_REVERSE)
for row in diagonal_top_right:
	count += row.count(XMAS)
	count += row.count(XMAS_REVERSE)
for row in diagonal_top_left:
	count += row.count(XMAS)
	count += row.count(XMAS_REVERSE)

print(f"Part 1: {count}")

# Part 2

CROSS_MAS_COUNT = 0
for x in range(1, DIMENSION_X - 1):
	for y in range(1, DIMENSION_Y - 1):
		if letter_grid[x][y] == 'A' and \
			letter_grid[x + 1][y + 1] in ['M', 'S'] and letter_grid[x - 1][y - 1] in ['M', 'S'] \
			and letter_grid[x + 1][y + 1] != letter_grid[x - 1][y - 1] \
			and letter_grid[x + 1][y - 1] in ['M', 'S'] and letter_grid[x - 1][y + 1] in ['M', 'S'] \
			and letter_grid[x + 1][y - 1] != letter_grid[x - 1][y + 1]:

			CROSS_MAS_COUNT += 1

print(f"Part 2: {CROSS_MAS_COUNT}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
