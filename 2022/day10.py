f = open("day10input.txt", "r")

all_lines = f.read().split("\n")

cycle_count = 0
relevant_cycles = [20, 60, 100, 140, 180, 220]
signal_strength_sum = 0
x = 1
crt_output = []


def process_cycle():
    row = int((cycle_count - 1) / 40)
    column = (cycle_count - 1) % 40
    if column == 0:
        crt_output.append("")

    if abs(x - (column)) <= 1:
        crt_output[row] += "#"
    else:
        crt_output[row] += "."

    if cycle_count in relevant_cycles:
        global signal_strength_sum
        signal_strength_sum += x * cycle_count


for line in all_lines:
    cycle_count += 1
    process_cycle()

    if line == "noop":
        continue

    cycle_count += 1
    command, number = line.split(" ")
    process_cycle()
    x += int(number)

for line in crt_output:
    print(line)


print(f"result 1: {signal_strength_sum}")