
f = open("day4input.txt", "r")

lineNum = 0
count = 0
count2 = 0

lists = []

all_lines = f.readlines()
for line in all_lines:
    # line = "MSMSCnjBnBjCscjVDVljTvHmmWnrwTrwFTrvTWTT"
    # line = line[:-1]
    min1 = -1
    max1 = -1
    min2 = -1
    max2 = -1
    current_number = ""
    for character in line:
        if character.isdigit():
            current_number += character
        else:
            if min1 == -1:
                min1 = int(current_number)
            elif max1 == -1:
                max1 = int(current_number)
            elif min2 == -1:
                min2 = int(current_number)
            elif max2 == -1:
                max2 = int(current_number)
            current_number = ""

    if (min1 >= min2 and max1 <= max2) or (min1 <= min2 and max1 >= max2):
        count += 1

    list_1 = []
    list_2 = []
    for x in (range(min1, max1 + 1)):
        list_1.append(x)
    for x in (range(min2, max2 + 1)):
        list_2.append(x)

    for x in list_1:
        if list_2.__contains__(x):
            count2 += 1
            break

# 
# index = 0
# for line in all_lines:
#     min1 = -1
#     max1 = -1
#     min2 = -1
#     max2 = -1
#     current_number = ""
#     for character in line:
#         if character.isdigit():
#             current_number += character
#         else:
#             if min1 == -1:
#                 min1 = int(current_number)
#             elif max1 == -1:
#                 max1 = int(current_number)
#             elif min2 == -1:
#                 min2 = int(current_number)
#             elif max2 == -1:
#                 max2 = int(current_number)
#             current_number = ""
# 
#     list = []
#     for x in (range(min1, max1 + 1)):
#         list.append(x)
#     for x in (range(min2, max2 + 1)):
#         list.append(x)
# 
#     count2before = count2
#     listindex = 0
#     for _list in lists:
#         listindex += 1
#         if index == listindex - 1:
#             continue
#         fully_contained_1 = True
#         fully_contained_2 = True
#         for x in list:
#             if not _list.__contains__(x):
#                 fully_contained_1 = False
#                 break
#         for x in _list:
#             if not list.__contains__(x):
#                 fully_contained_2 = False
#                 break
# 
#         if fully_contained_1 or fully_contained_2:
#             print(f"{line} is fully contained in {listindex}: {_list}")
#             count2 += 1
#             break
#     if (count2 == count2before):
#         print(f"{line} is not fully contained")
# 
#     # not 991, 992
#     lineNum += 1
#     index += 1



print(f"result 1: {count}, result2: {count2}")