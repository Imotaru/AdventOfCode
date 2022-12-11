import re

f = open("day11input.txt", "r")

all_lines = f.read().split("\n")

class monkey:
    def __init__(self, items: list[int] = None, operation: str = "", operation_var: int = -1, test_mod: int = -1, true_target: int = -1, false_target: int = -1):
        self.items = items
        self.operation = operation
        self.operation_var = operation_var
        self.test_mod = test_mod
        self.true_target = true_target
        self.false_target = false_target
        self.activity = 0


current_monkey = None
monkeys = []

num_pattern = "(\\d+)"

# init monkeys
for line in all_lines:
    if line.startswith("Monkey"):
        current_monkey = monkey()
    elif line.__contains__("Starting items:"):
        items = re.findall(num_pattern, line)
        current_monkey.items = []
        for item in items:
            current_monkey.items.append(int(item))
    elif line.__contains__("Operation"):
        current_monkey.operation = "*" if line.__contains__("*") else "+"
        if len(re.findall(num_pattern, line)) > 0:
            current_monkey.operation_var = int(re.findall(num_pattern, line)[0])
        else:
            current_monkey.operation = "^"
            current_monkey.operation_var = 2

    elif line.__contains__("Test"):
        current_monkey.test_mod = int(re.findall(num_pattern, line)[0])
    elif line.__contains__("If true"):
        current_monkey.true_target = int(re.findall(num_pattern, line)[0])
    elif line.__contains__("If false"):
        current_monkey.false_target = int(re.findall(num_pattern, line)[0])
        monkeys.append(current_monkey)


def calculate_monkey_activity(monkeys: list[monkey], rounds: int, part_one: bool, log: bool = False) -> int:
    greatest_common_divisor = 1
    for monkey in monkeys:
        greatest_common_divisor *= monkey.test_mod

    for round in range(rounds):
        i = 0
        for monkey in monkeys:
            if log:
                print(f"Monkey {i}:")
            i += 1
            for item in monkey.items:
                if log:
                    print(f"  Monkey inspects an item with a worry level of {item}.")
                worry_level = item
                if monkey.operation == "*":
                    worry_level *= monkey.operation_var
                    if log:
                        print(f"    Worry level is multiplied by {monkey.operation_var} to {worry_level}.")
                elif monkey.operation == "+":
                    worry_level += monkey.operation_var
                    if log:
                        print(f"    Worry level increases by {monkey.operation_var} to {worry_level}.")
                else:
                    if log:
                        print(f"    Worry level is multiplied by {worry_level} to {worry_level}.")
                    worry_level *= worry_level
                if part_one:
                    worry_level = int(worry_level / 3)
                    if log:
                        print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")
                target = monkey.true_target if worry_level % monkey.test_mod == 0 else monkey.false_target
                if worry_level % monkey.test_mod == 0:
                    if log:
                        print(f"    Current worry level is divisible by {monkey.test_mod}.")
                else:
                    if log:
                        print(f"    Current worry level is not divisible by {monkey.test_mod}.")

                if log:
                    print(f"    Item with worry level {worry_level} is thrown to monkey {target}.")
                if not part_one:
                    if worry_level >= greatest_common_divisor:
                        worry_level %= greatest_common_divisor
                        if log:
                            print(f"    Worry level reduced to {worry_level} because it was greater than {greatest_common_divisor}")
                monkeys[target].items.append(worry_level)
                monkey.activity += 1
            monkey.items = []

    highest_monkey_activity = 0
    second_highest_monkey_activity = 0

    for monkey in monkeys:
        i = 0
        print(f"Monkey {i} activity = {monkey.activity}")
        i += 1
        if monkey.activity > highest_monkey_activity:
            second_highest_monkey_activity = highest_monkey_activity
            highest_monkey_activity = monkey.activity
        elif monkey.activity > second_highest_monkey_activity:
            second_highest_monkey_activity = monkey.activity

    return highest_monkey_activity * second_highest_monkey_activity

print(f"result 1: {calculate_monkey_activity(monkeys, 20, part_one=True)}")
print(f"Result 2: {calculate_monkey_activity(monkeys, 10000, part_one=False)}")