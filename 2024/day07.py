import re

# f = open("day07testinput.txt", "r")
f = open("day07input.txt", "r")

equations = []

solution_regex = r"^\d+(?=:)"
parameter_regex = r"(?<=: )(\d+(?: \d+)*)"

for line in f.readlines():
	solution = re.search(solution_regex, line).group(0)
	parameters = re.search(parameter_regex, line).group(0).split()
	equations.append((solution, parameters))


def is_equation_valid(equation, operator_str):
	calculated_solution = int(equation[1][0])
	for i in range(len(operator_str)):
		if operator_str[i] == "0":
			calculated_solution += int(equation[1][i + 1])
		elif operator_str[i] == "1":
			calculated_solution *= int(equation[1][i + 1])
		elif operator_str[i] == "2":
			calculated_solution = int(str(calculated_solution) + equation[1][i + 1])
	return int(equation[0]) == calculated_solution


def base3_representation(digits, number):
	# Convert number to base 3
	base3 = ''
	while number > 0:
		base3 = str(number % 3) + base3
		number //= 3

	# Pad with leading zeros if necessary
	base3 = base3.zfill(digits)

	# If the result is longer than the specified digits, return an error
	if len(base3) > digits:
		raise ValueError("Number too large to fit in the specified number of digits")

	return base3

total_result = 0

for equation in equations:
	current_attempt = 0
	for i in range(3 ** (len(equation[1]) - 1)):
		operator_string = base3_representation(len(equation[1]) - 1, i)

		current_attempt += 1
		if is_equation_valid(equation, operator_string):
			total_result += int(equation[0])
			break

print(total_result)

