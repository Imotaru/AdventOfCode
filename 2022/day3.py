
f = open("input.txt", "r")

lineNum = 0
sum = 0
sum2 = 0

list = []

for line in f.readlines():
    # line = "MSMSCnjBnBjCscjVDVljTvHmmWnrwTrwFTrvTWTT"
    line = line[:-1]
    half = int(len(line) / 2)
    comp1 = line[:-half]
    comp2 = line[half:]
    print(comp1)
    print(comp2)

    for letter in comp2:
        # print(f"checking if letter {letter} from {comp2} is contained in {comp1}")
        if comp1.__contains__(letter):
            if ord(letter) <= 90:
                print(f"common letter is {letter}, so we add {ord(letter) - 64 + 26}")
                sum += ord(letter) - 64 + 26
            else:
                print(f"common letter is {letter}, so we add {ord(letter) - 96}")
                sum += ord(letter) - 96
            break

    list.append(line)
    if len(list) == 3:
        for item in list[0]:
            if list[1].__contains__(item) and list[2].__contains__(item):
                if ord(item) <= 90:
                    sum2 += ord(item) - 64 + 26
                else:
                    sum2 += ord(item) - 96
                break
        list = []

    lineNum += 1



print(f"result 1: {sum} result 2: {sum2}")