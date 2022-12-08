f = open("day8.txt", "r")

all_lines = f.readlines()

line_count = 0
hidden_trees = []
scenic_score = 0

grid = []
width = 0
height = len(all_lines)

for line in all_lines:
    line = line[:-1]
    if width == 0:
        width = len(line)
    line_count += 1
    line_arr = []
    for c in line:
        line_arr.append(c)

    grid.append(line_arr)

# Part 1
for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            continue
        current_tree = grid[x][y]
        # print(f"Current Tree: ({x}, {y}) = {current_tree}")

        is_visible_left = True
        for _x in range(x):
            if grid[_x][y] >= current_tree:
                # print(f"Checking left: ({_x}, {y}) is {grid[_x][y]} greater or equal to {current_tree}, so it became hidden in this direction")
                is_visible_left = False
                break
            else:
                # print(f"Checking left: ({_x}, {y}) is {grid[_x][y]}, so shorter than {current_tree}, still visible")
                pass

        is_visible_top = True
        for _y in range(y):
            if grid[x][_y] >= current_tree:
                # print(f"Checking top: ({x}, {_y}) is {grid[x][_y]} greater or equal to {current_tree}, so it became hidden in this direction")
                is_visible_top = False
                break
            else:
                # print(f"Checking top: ({x}, {_y}) is {grid[x][_y]}, so shorter than {current_tree}, still visible")
                pass

        is_visible_right = True
        for _x in range(width - 1 - x):
            x_pos = x + _x + 1
            if grid[x_pos][y] >= current_tree:
                # print(f"Checking right: ({x_pos}, {y}) is {grid[x_pos][y]} greater or equal to {current_tree}, so it became hidden in this direction")
                is_visible_right = False
                break
            else:
                # print(f"Checking right: ({x_pos}, {y}) is {grid[x_pos][y]}, so shorter than {current_tree}, still visible")
                pass

        is_visible_down = True
        for _y in range(height - 1 - y):
            y_pos = y + _y + 1
            if grid[x][y_pos] >= current_tree:
                # print(f"Checking down: ({x}, {y_pos}) is {grid[x][y_pos]} greater or equal to {current_tree}, so it became hidden in this direction")
                is_visible_down = False
                break
            else:
                # print(f"Checking down: ({x}, {y_pos}) is {grid[x][y_pos]}, so shorter than {current_tree}, still visible")
                pass

        # print(f"Tree ({x}, {y}) is visible left {is_visible_left}, top {is_visible_top}, right {is_visible_right}, down {is_visible_down}")
        if not is_visible_left and not is_visible_top and not is_visible_right and not is_visible_down:
            hidden_trees.append((x, y))


# Part 2
for x in range(width):
    for y in range(height):
        if x == 0 or y == 0 or x == width - 1 or y == height - 1:
            continue

        current_tree = grid[x][y]
        scenic_up = 0
        scenic_down = 0
        scenic_left = 0
        scenic_right = 0

        for _x in range(x):
            _x = x - 1 - _x
            scenic_left += 1
            if grid[_x][y] >= current_tree:
                # print(f"Checking left: ({_x}, {y}) is {grid[_x][y]} greater or equal to {current_tree}, scenic view ends at {scenic_left}")
                break
            else:
                # print(f"Checking left: ({_x}, {y}) is {grid[_x][y]}, scenic view incremented by 1 to {scenic_left}")
                pass

        for _y in range(y):
            _y = y - 1 - _y
            scenic_up += 1
            if grid[x][_y] >= current_tree:
                # print(f"Checking top: ({x}, {_y}) is {grid[x][_y]}  greater or equal to {current_tree}, scenic view ends at {scenic_up}")
                break
            else:
                # print(f"Checking top: ({x}, {_y}) is {grid[x][_y]}, scenic view incremented by 1 to {scenic_up}")
                pass

        for _x in range(width - 1 - x):
            x_pos = x + _x + 1
            scenic_right += 1
            if grid[x_pos][y] >= current_tree:
                # print(f"Checking right: ({x_pos}, {y}) is {grid[x_pos][y]}  greater or equal to {current_tree}, scenic view ends at {scenic_right}")
                break
            else:
                # print(f"Checking right: ({x_pos}, {y}) is {grid[x_pos][y]}, scenic view incremented by 1 to {scenic_right}")
                pass

        for _y in range(height - 1 - y):
            y_pos = y + _y + 1
            scenic_down += 1
            if grid[x][y_pos] >= current_tree:
                # print(f"Checking down: ({x}, {y_pos}) is {grid[x][y_pos]}  greater or equal to {current_tree}, scenic view ends at {scenic_down}")
                break
            else:
                # print(f"Checking down: ({x}, {y_pos}) is {grid[x][y_pos]}, scenic view incremented by 1 to {scenic_down}")
                pass

        scenic = scenic_left * scenic_down * scenic_right * scenic_up
        # print(f"Tree ({x}, {y}) {grid[x][y]} score is {scenic}: up {scenic_up}, down {scenic_down}, left {scenic_left}, right {scenic_right}")
        if scenic > scenic_score:
            scenic_score = scenic

print(f"result 1: {height * width - len(hidden_trees)}, result 2: {scenic_score}")