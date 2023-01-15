import re

IS_TEST = False
RELEVANT_ROW = 10 if IS_TEST else 2000000
MAX_DISTRESS_POS = 20 if IS_TEST else 4000000

f = open("day15testinput.txt" if IS_TEST else "day15input.txt", "r")
all_lines = f.read().split("\n")

line_count = 0
result2 = 0

no_beacon_indexes = set()
beacons_in_row = set()

sensors = []


def get_manhatten_dist(sx, sy, bx, by) -> int:
    return abs(sx - bx) + abs(sy - by)


for line in all_lines:
    sx_str, sy_str, bx_str, by_str = re.findall(r"\d+", line)
    sx = int(sx_str)
    sy = int(sy_str)
    bx = int(bx_str)
    by = int(by_str)

    if by == RELEVANT_ROW:
        beacons_in_row.add(bx)

    mh = get_manhatten_dist(sx, sy, bx, by)

    sensors.append([sx, sy, mh])
    sensors.append([bx, by, mh])

    affected_indexes = mh - abs(RELEVANT_ROW - sy)
    if affected_indexes <= 0:
        continue
    # print(f"({sx}, {sy}), ({bx}, {by}) => {mh}; {mh} - abs({RELEVANT_ROW} - {sy}) = {affected_indexes}")
    no_beacon_indexes.add(sx)
    for i in range(affected_indexes):
        no_beacon_indexes.add(sx + i + 1)
        no_beacon_indexes.add(sx - i - 1)

    line_count += 1

for beacon in beacons_in_row:
    no_beacon_indexes.remove(beacon)

# part 2
# todo for each sensor, check only the ones in the circle with manhatten distance + 1
# for y in range(MAX_DISTRESS_POS + 1):
#     for x in range(MAX_DISTRESS_POS + 1):
#         is_unseen = True
#         largest_diff = 0
#         for s in sensors:
#             mh = get_manhatten_dist(x, y, s[0], s[1])
#             diff = s[2] - mh
#             if diff >= 0:
#                 is_unseen = False
#                 break
#             elif diff < largest_diff:  # is negative, so checking if abs is larger basically, but performance matters
#                 largest_diff = diff
#         if is_unseen:
#             # for s in sensors:
#             #     mh = get_manhatten_dist(x, y, s[0], s[1])
#             #     diff = s[2] - mh
#             #     if diff >= 0:
#             #         is_unseen = False
#             #         break
#                 # print(f"{mh} <= {s[2]} ? diff is {mh - s[2]}")
#             print(f"({x}, {y}) is unseen, result 2 is {x * 4000000 + y}")
#         else:
#             if largest_diff < 0:
#                 x += abs(largest_diff) - 1

positions_to_check = []

i = 0
for s in sensors:
    i += 1
    for n in range(s[2] + 1):
        x = s[0] + s[2] + 1 - n
        y = s[1] + n
        x2 = s[0] - s[2] - 1 + n
        y2 = s[1] - n
        if 0 <= x <= MAX_DISTRESS_POS and 0 <= y <= MAX_DISTRESS_POS:
            positions_to_check.append([x, y])
        if 0 <= x2 <= MAX_DISTRESS_POS and 0 <= y <= MAX_DISTRESS_POS:
            positions_to_check.append([x2, y])
        if 0 <= x <= MAX_DISTRESS_POS and 0 <= y2 <= MAX_DISTRESS_POS:
            positions_to_check.append([x, y2])
        if 0 <= x2 <= MAX_DISTRESS_POS and 0 <= y2 <= MAX_DISTRESS_POS:
            positions_to_check.append([x2, y2])

    print(f"Sensor {i} / {len(sensors)} done")

print(len(positions_to_check))

for pos in positions_to_check:
    is_unseen = True
    for s in sensors:
        mh = get_manhatten_dist(pos[0], pos[1], s[0], s[1])
        diff = s[2] - mh
        if diff >= 0:
            is_unseen = False
            break
    if is_unseen:
        # for s in sensors:
        #     mh = get_manhatten_dist(x, y, s[0], s[1])
        #     diff = s[2] - mh
        #     if diff >= 0:
        #         is_unseen = False
        #         break
            # print(f"{mh} <= {s[2]} ? diff is {mh - s[2]}")
        print(f"({pos}) is unseen, result 2 is {pos[0] * 4000000 + pos[1]}")

print(f"result 1: {len(no_beacon_indexes)}, result 2: {result2}")

# 7499204000000 is too low