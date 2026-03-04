import math

# f = open("day11testinput.txt", "r")
f = open("day11input.txt", "r")

str_numbers = f.readline().split(' ')

def add_to_dict(dict, key, value):
	if key in dict.keys():
		dict[key] += value
	else:
		dict[key] = value

numbers = {}
for str_num in str_numbers:
	int_num = int(str_num)
	add_to_dict(numbers, int_num, 1)

step_amount = 75

for i in range(step_amount):
	new_numbers = {}
	for key in numbers.keys():
		digit_amount = 0 if key == 0 else math.floor(math.log10(key)) + 1
		if key == 0:
			add_to_dict(new_numbers, 1, numbers[key])
		elif digit_amount % 2 == 0:
			divisor = 10**(digit_amount / 2)
			add_to_dict(new_numbers, int(key / divisor), numbers[key])
			add_to_dict(new_numbers, int(key % divisor), numbers[key])
		else:
			add_to_dict(new_numbers, key * 2024, numbers[key])
	
	numbers = new_numbers

stone_amount = 0
for key in numbers.keys():
	stone_amount += numbers[key]
print(f"After blinking {step_amount} times you have {stone_amount} stones")