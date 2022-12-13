f = open("day13input.txt", "r")
all_lines = f.read().split("\n")

result1 = 0
result2 = 0

index = 1
left = ""
right = ""


def are_in_right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, list) and isinstance(right, int):
        return are_in_right_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return are_in_right_order([left], right)

    for i in range(min(len(left), len(right))):
        is_right_order = are_in_right_order(left[i], right[i])
        if is_right_order is None:
            continue
        return is_right_order

    if len(left) != len(right):
        return len(left) < len(right)
    else:
        return None

# part 1
for line in all_lines:
    if len(line) == 0:
        continue
    elif len(left) == 0:
        left = line
    elif len(right) == 0:
        right = line
        left_value = eval(left)
        right_value = eval(right)
        is_right_order = are_in_right_order(left_value, right_value)
        if is_right_order is None or is_right_order:
            result1 += index

        left = ""
        right = ""
        index += 1

# part 2
l = []
for line in all_lines:
    if len(line) == 0:
        continue
    l.append(eval(line))

l.append([[2]])
l.append([[6]])

def bubble_sort(list_arg):
    n = len(list_arg)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if are_in_right_order(list_arg[j + 1], list_arg[j]):
                tmp = list_arg[j]
                list_arg[j] = list_arg[j + 1]
                list_arg[j + 1] = tmp
                flag = 1

        if flag == 0:
            break
    return list_arg

sorted_list = bubble_sort(l)

pos = []
for i in range(len(sorted_list)):
    if sorted_list[i] == [[2]] or sorted_list[i] == [[6]]:
        pos.append(i + 1)

print(f"result 1: {result1}, result 2: {pos[0] * pos[1]}")
