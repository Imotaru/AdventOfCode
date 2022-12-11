f = open("day6input.txt", "r")

all_lines = f.readlines()

length = 14  # 4

for line in all_lines:
    for i in range(len(line)):
        pot_marker = line[i:i+length]
        if len(pot_marker) < length:
            print("Couldn't find result")
            exit()
        valid = True
        for j in range(length):
            if j == 0:
                if pot_marker[1:].__contains__(pot_marker[j]):
                    print(f"{j}: {pot_marker[1:]} contained {pot_marker[j]} from {pot_marker}")
                    valid = False
                    break
            elif j == length - 1:
                if pot_marker[:length - 1].__contains__(pot_marker[j]):
                    print(f"{j}: {pot_marker[:length - 1]} contained {pot_marker[j]} from {pot_marker}")
                    valid = False
                    break
            elif pot_marker[j+1:length].__contains__(pot_marker[j]):
                print(f"{j}-A: {pot_marker[j+1:length]} contained {pot_marker[j]} from {pot_marker}")
                valid = False
                break
            elif pot_marker[0:j].__contains__(pot_marker[j]):
                print(f"{j}-B: {pot_marker[0:j]} contained {pot_marker[j]} from {pot_marker}")
                valid = False
                break

        if valid:
            print(f"solution is {i + length}")
            exit()
