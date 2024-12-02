import re
import time

start_time = time.time()

# f = open("day02testinput.txt", "r")
f = open("day02input.txt", "r")

def is_report_safe(report, is_part_two: bool, is_skipped_level: bool):
	is_all_increasing = True
	is_all_decreasing = True
	min_gap = 2_140_000_000
	max_gap = -1
	fail_index = -1

	for i in range(len(report) - 1):
		gap = abs(report[i] - report[i + 1])
		if gap > max_gap:
			max_gap = gap
		if gap < min_gap:
			min_gap = gap
		if report[i] < report[i + 1]:
			is_all_decreasing = False
		elif report[i] > report[i + 1]:
			is_all_increasing = False
		if not (is_all_increasing or is_all_decreasing) or min_gap < 1 or max_gap > 3:
			if not is_part_two:
				return False
			else:
				fail_index = i
				break

	if not is_part_two or fail_index == -1:
		return True

	if is_part_two and not is_skipped_level:
		for i in range(max(fail_index - 1, 0), fail_index + 2):
			skipped_level_report = []
			for j in range(len(report)):
				if j != i:
					skipped_level_report.append(report[j])
			if is_report_safe(skipped_level_report, is_part_two, True):
				return True

	return False


reports = []

for line in f.readlines():
	numbers = re.findall(r'\d+', line)
	report = []
	for number in numbers:
		report.append(int(number))
	reports.append(report)

safe_reports = 0

for report in reports:
	if is_report_safe(report, False, False):
		safe_reports += 1

print(f"Part 1: {safe_reports}")

safe_reports = 0

for report in reports:
	if is_report_safe(report, True, False):
		safe_reports += 1

print(f"Part 2: {safe_reports}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")