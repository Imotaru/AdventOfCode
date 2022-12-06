
f = open("day2input.txt", "r")

score = 0
lineNum = 0
for line in f.readlines():
    lineNum += 1
    if line[2] == "X":
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 1
        elif line[0] == "C":
            score += 2
    elif line[2] == "Y":
        score += 3
        if line[0] == "A":
            score += 1
        elif line[0] == "B":
            score += 2
        elif line[0] == "C":
            score += 3
    elif line[2] == "Z":
        score += 6
        if line[0] == "A":
            score += 2
        elif line[0] == "B":
            score += 3
        elif line[0] == "C":
            score += 1

    # # according to old guide
    # lineNum += 1
    # if line[2] == "X":
    #     score += 1
    #     if line[0] == "A":
    #         score += 3
    #     elif line[0] == "C":
    #         score += 6
    # elif line[2] == "Y":
    #     score += 2
    #     if line[0] == "B":
    #         score += 3
    #     elif line[0] == "A":
    #         score += 6
    # elif line[2] == "Z":
    #     score += 3
    #     if line[0] == "C":
    #         score += 3
    #     elif line[0] == "B":
    #         score += 6

print(f"score according to guide: {score}")