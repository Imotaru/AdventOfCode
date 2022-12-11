import re

import re2

f = open("day5input.txt", "r")

lineNum = 0

# stacks = [
#     ["Z", "N"],
#     ["M", "C", "D"],
#     ["P"],
# 
# ]
stacks = [
    ["J", "H", "P", "M", "S", "F", "N", "V"],
    ["S", "R", "L", "M", "J", "D", "Q"],
    ["N", "Q", "D", "H", "C", "S", "W", "B"],
    ["R", "S", "C", "L"],
    ["M", "V", "T", "P", "F", "B"],
    ["T", "R", "Q", "N", "C"],
    ["G", "V", "R"],
    ["C", "Z", "S", "P", "D", "L", "R"],
    ["D", "S", "J", "V", "G", "P", "B", "F"],
]

result = ""

all_lines = f.readlines()
pattern = "(\\d+)"
for line in all_lines:
    numbers = re.findall(pattern, line)
    amt = int(numbers[0])
    origin = int(numbers[1]) - 1
    target = int(numbers[2]) - 1

    for x in range(amt):
        stacks[target].append(stacks[origin][len(stacks[origin]) - amt + x])

    for x in range(amt):
        stacks[origin].pop()

for stack in stacks:
    result += stack[len(stack) - 1]

print(f"result 1: {result}")