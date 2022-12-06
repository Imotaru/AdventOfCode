
f = open("day1input.txt", "r")

highest_calories = -1
second_highest_calories = -1
third_highest_calories = -1

current_calories = 0
lineNum = 0
for line in f.readlines():
    lineNum += 1
    if line == "\n" or line == "":
        if current_calories > highest_calories:
            third_highest_calories = second_highest_calories
            second_highest_calories = highest_calories
            highest_calories = current_calories
        elif current_calories > second_highest_calories:
            third_highest_calories = second_highest_calories
            second_highest_calories = current_calories
        elif current_calories > third_highest_calories:
            third_highest_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

print(f"The three highest calorie elves have {highest_calories}, {second_highest_calories}, {third_highest_calories} so in total {highest_calories + second_highest_calories + third_highest_calories}")