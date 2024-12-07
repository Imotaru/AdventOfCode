import re
import time

start_time = time.time()

# f = open("day05testinput.txt", "r")
f = open("day05input.txt", "r")

f_text = f.read()
order_rules_str = re.findall(r'(\d+)\|(\d+)', f_text)
order_rules = []

for ors in order_rules_str:
	order_rules.append((int(ors[0]), int(ors[1])))

order_rules_dict = {}

for rule in order_rules:
	if rule[0] not in order_rules_dict.keys():
		order_rules_dict[rule[0]] = []
	order_rules_dict[rule[0]].append(rule[1])

cases = re.findall(r'(\d+(?:,\d+)+)', f_text)

token_set = set()

for rule in order_rules:
	token_set.add(rule[0])
	token_set.add(rule[1])

def build_small_order_rules_dict(tokens):
	small_order_rules_dict = {}
	for key in order_rules_dict.keys():
		if key not in tokens:
			continue
		small_order_rules_dict[key] = []
		for value in order_rules_dict[key]:
			if value in tokens:
				small_order_rules_dict[key].append(value)

	return infer_new_rules(small_order_rules_dict)

def infer_new_rules(order_rules_dict):
	new_rule_count = 1
	while new_rule_count != 0:
		new_rule_count = 0
		for token in order_rules_dict.keys():
			for big_token in order_rules_dict[token]:
				if big_token not in order_rules_dict.keys():
					continue
				for even_bigger_token in order_rules_dict[big_token]:
					if even_bigger_token not in order_rules_dict[token] and token != even_bigger_token:
						order_rules_dict[token].append(even_bigger_token)
						new_rule_count += 1
	return order_rules_dict

def find_error(case, rule_dict):
	for i in range(len(case) - 1):
		for j in range(i + 1, len(case)):
			if case[i] not in rule_dict.keys() or case[j] not in rule_dict[case[i]]:
				return (i, j)
	return (-1, -1)

part_1_solution = 0
part_2_solution = 0
for c in cases:
	cases_str = c.split(',')
	case = []
	for c_str in cases_str:
		case.append(int(c_str))

	test_valid = True

	custom_dict = build_small_order_rules_dict(case)
	error = find_error(case, custom_dict)

	if error[0] == -1:
		part_1_solution += case[int(len(case) / 2)]
	else:
		while error[0] != -1:
			temp = case[error[1]]
			case[error[1]] = case[error[0]]
			case[error[0]] = temp
			error = find_error(case, custom_dict)

		part_2_solution += case[int(len(case) / 2)]


print(f"Part 1: {part_1_solution}")
print(f"Part 2: {part_2_solution}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
