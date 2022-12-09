f = open("day9input.txt", "r")

all_lines = f.readlines()

line_count = 0
result1 = 0
result2 = 0

last_head_pos = [0, 0]
length = 10
points = []
for x in range(length):
    points.append([0, 0])

visited_pos = [
    [0, 0]
]

display_on = False

display = [
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".","H",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".", ".", ".", ".", ".", ".", ".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
]


def set_display(x, y, c, only_if_empty=False):
    if display_on:
        if only_if_empty and display[-y + 15][x + 11] != ".":
            return
        display[-y + 15][x + 11] = c

# build file system
for line in all_lines:
    line = line[:-1]
    direction, steps = line.split(" ")
    if direction == "U":
        dir = [0, 1]
    elif direction == "D":
        dir = [0, -1]
    elif direction == "L":
        dir = [-1, 0]
    else:
        dir = [1, 0]

    for i in range(int(steps)):
        set_display(points[0][0], points[0][1], ".")
        points[0][0] = points[0][0] + dir[0]
        points[0][1] = points[0][1] + dir[1]
        set_display(points[0][0], points[0][1], "H")
        print(f"Move {direction} {i + 1} / {steps}")

        for j in range(length):
            if j == 0:
                continue
            if abs(points[j][0] - points[j - 1][0]) > 1 and abs(points[j][1] - points[j - 1][1]) > 1 or abs(points[j][0] - points[j - 1][0]) == 1 and abs(points[j][1] - points[j - 1][1]) > 1 or abs(points[j][0] - points[j - 1][0]) > 1 and abs(points[j][1] - points[j - 1][1]) == 1:
                set_display(points[j][0], points[j][1], ".")
                old_pos = [points[j][0], points[j][1]]
                if points[j - 1][1] > points[j][1]:
                    points[j][1] = points[j][1] + 1
                else:
                    points[j][1] = points[j][1] - 1

                if points[j - 1][0] > points[j][0]:
                    points[j][0] = points[j][0] + 1
                else:
                    points[j][0] = points[j][0] - 1

                set_display(points[j][0], points[j][1], str(j))
                if j == length - 1:
                    print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Jump from {old_pos} to {points[j]}, head was at {points[j - 1]}")
            elif points[j][0] == points[j - 1][0]:
                if abs(points[j - 1][1] - points[j][1]) > 1:
                    set_display(points[j][0], points[j][1], ".")
                    if points[j - 1][1] > points[j][1]:
                        points[j][1] = points[j][1] + 1
                    else:
                        points[j][1] = points[j][1] - 1
                    set_display(points[j][0], points[j][1], str(j))

                    if j == length - 1:
                        print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Follow Vertical")
                else:
                    set_display(points[j][0], points[j][1], str(j), only_if_empty=True)
                    if j == length - 1:
                        print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Sleep")
            elif points[j][1] == points[j - 1][1]:
                if abs(points[j - 1][0] - points[j][0]) > 1:
                    set_display(points[j][0], points[j][1], ".")
                    if points[j - 1][0] > points[j][0]:
                        points[j][0] = points[j][0] + 1
                    else:
                        points[j][0] = points[j][0] - 1
                    set_display(points[j][0], points[j][1], str(j))
                    if j == length - 1:
                        print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Follow Horizontal")
                else:
                    set_display(points[j][0], points[j][1], str(j), only_if_empty=True)
                    if j == length - 1:
                        print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Sleep")
            else:
                set_display(points[j][0], points[j][1], str(j), only_if_empty=True)
                if j == length - 1:
                    print(f"Head: {points[j - 1]}, Tail: {points[j]}. Last Action: Skip")
                continue

        if display_on:
            for row in display:
                print(row)


        tail_pos_is_new = True
        for pos in visited_pos:
            if pos[0] == points[length - 1][0] and pos[1] == points[length - 1][1]:
                tail_pos_is_new = False
                break
        if tail_pos_is_new:
            visited_pos.append([points[length - 1][0], points[length - 1][1]])
    line_count += 1

print(f"result: {len(visited_pos)}")
