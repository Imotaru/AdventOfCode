import re

IS_PART_ONE = False

f = open("day14input.txt", "r")
all_lines = f.read().split("\n")

line_count = 0
result1 = 0
result2 = 0

rock_scans = []
for line in all_lines:
    rock_scans.append(re.findall(r"\d+,\d+", line))
    line_count += 1

lowest_x = 1000000
highest_x = -1
lowest_y = 1000000
highest_y = -1

for line in rock_scans:
    for step in line:
        x_str, y_str = step.split(",")
        x = int(x_str)
        y = int(y_str)
        if x < lowest_x:
            lowest_x = x
        if x > highest_x:
            highest_x = x
        if y < lowest_y:
            lowest_y = y
        if y > highest_y:
            highest_y = y

if not IS_PART_ONE:
    lowest_x = 0
    highest_x = highest_x * 2

Grid = []
AIR = "."
WALL = "#"
SAND = "o"
for y in range(highest_y + 1):
    row = []
    for x in range(highest_x - lowest_x + 1):
        row.append(AIR)
    Grid.append(row)

if not IS_PART_ONE:
    space_row = []
    for i in range(len(Grid[0])):
        space_row.append(".")
    ground_row = []
    for i in range(len(Grid[0])):
        ground_row.append("#")

    Grid.append(space_row)
    Grid.append(ground_row)
    highest_y += 2

for line in rock_scans:
    last_x = -1
    last_y = -1
    for value in line:
        x_str, y_str = value.split(",")
        x = int(x_str) - lowest_x
        y = int(y_str)
        Grid[y][x] = WALL
        if last_x == -1:
            last_x = x
            last_y = y
            continue
        if x == last_x:
            for _y in range(last_y, y, 1 if y > last_y else -1):
                Grid[_y][x] = WALL
        elif y == last_y:
            for _x in range(last_x, x, 1 if x > last_x else -1):
                Grid[y][_x] = WALL
        else:
            print(f"Can't move from {last_x}, {last_y} to {x}, {y}")

        last_x = x
        last_y = y

SAND_SOURCE = (500 - lowest_x, 0)

last_sand_pos = SAND_SOURCE
grounded = False
while(True):
    # remove last sand
    if not grounded:
        Grid[last_sand_pos[1]][last_sand_pos[0]] = AIR

    # drop next sand
    if Grid[last_sand_pos[1] + 1][last_sand_pos[0]] == AIR:
        # spot below is air, drop there
        Grid[last_sand_pos[1] + 1][last_sand_pos[0]] = SAND
        last_sand_pos = (last_sand_pos[0], last_sand_pos[1] + 1)
    elif last_sand_pos[0] - 1 < 0:
        # fell into void
        if IS_PART_ONE:
            print(f"Fell into void to the left, {last_sand_pos[0] - 1} is less than 0")
        else:
            print("THERE IS NOT ENOUGH SPACE TO THE LEFT")
        break
    elif Grid[last_sand_pos[1] + 1][last_sand_pos[0] - 1] == AIR:
        # spot below left is air, drop there
        Grid[last_sand_pos[1] + 1][last_sand_pos[0] - 1] = SAND
        last_sand_pos = (last_sand_pos[0] - 1, last_sand_pos[1] + 1)
    elif last_sand_pos[0] + 1 >= len(Grid[0]):
        # fell into void
        if IS_PART_ONE:
            print(f"Fell into void to the right, {last_sand_pos[0] + 1} is greater or equal to {len(Grid[0])}")
        else:
            print("THERE IS NOT ENOUGH SPACE TO THE RIGHT")
        break
    elif Grid[last_sand_pos[1] + 1][last_sand_pos[0] + 1] == AIR:
        # spot below right is air, drop there
        Grid[last_sand_pos[1] + 1][last_sand_pos[0] + 1] = SAND
        last_sand_pos = (last_sand_pos[0] + 1, last_sand_pos[1] + 1)
        pass
    else:
        # grounded
        grounded = True
        result1 += 1
        Grid[last_sand_pos[1]][last_sand_pos[0]] = SAND
        if last_sand_pos == SAND_SOURCE:
            print(f"Grounded sand corn {result1} at the position of sand source, the sand stopped trickling down")
            break
        print(f"Grounded sand corn {result1}")
        last_sand_pos = SAND_SOURCE
        continue
    grounded = False

i = 0
for line in Grid:
    print(str(i) + " - " + "".join(line))
    i += 1


print(f"result: {result1}")