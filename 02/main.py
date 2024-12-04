def is_safe_report(report):
    levels = list(map(int, report.split()))

    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    if not (increasing or decreasing):
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))

    if is_safe_report(report):
        return True

    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_safe_report(" ".join(map(str, modified_report))):
            return True

    return False

def count_safe_reports(data):
    reports = data.strip().split("\n")
    safe_count = sum(1 for report in reports if is_safe_with_dampener(report))
    return safe_count

def process_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return count_safe_reports(data)

filename = "data.txt"
print("Number of safe reports:", process_file(filename))
