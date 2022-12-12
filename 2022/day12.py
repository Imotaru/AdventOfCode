import collections

f = open("day12input.txt", "r")
all_lines = f.read().split("\n")

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

target = 37
target_reached = False


def build_grid():
    line_count = 0
    grid = []
    start_pos = (0, 0)
    for line in all_lines:
        row = []
        i = 0
        for c in line:
            height = ord(c)
            if height == 83:
                height = 10
                start_pos = (i, line_count)
            elif height == 69:
                height = target
            else:
                height -= 86
            row.append(height)
            i += 1
        grid.append(row)
        line_count += 1
    return (grid, start_pos)


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        try:
            if grid[y][x] == target:
                return path
        except:
            print(f"Pos {x}, {y} was out of range")
        if grid[y][x] == target:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] - grid[y][x] <= 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


Grid, Start_pos = build_grid()
for line in Grid:
    print(line)
print(Start_pos)

Path = bfs(Grid, Start_pos)
print(Path)
print(f"Part1: {len(Path) - 1}")

lowest_elevation = []

for y in range(len(Grid)):
    for x in range(len(Grid[0])):
        if Grid[y][x] == 11:
            lowest_elevation.append((x, y))

shortest_result = len(Grid) * len(Grid[0])
for start_pos in lowest_elevation:
    path = bfs(Grid, start_pos)
    if path is None:
        continue
    result = len(path) - 1
    if result < shortest_result:
        shortest_result = result
print(f"Part2: {shortest_result}")