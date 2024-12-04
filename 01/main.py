def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    return total_distance

def read_lists_from_file(filename):
    left_list = []
    right_list = []
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def find_duplicate_in_lists(list_1, list_2):
    total_similiarity = 0
    for item in list_1:
        indices = [i for i, x in enumerate(list_2) if x == item]
        temp = item * len(indices)
        total_similiarity += temp
    return total_similiarity


# Read lists from file
left_list, right_list = read_lists_from_file('data.txt')

# Calculate and print the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(f"The total distance between the lists is: {total_distance}")
print(f"The total similarity between the lists is: {find_duplicate_in_lists(left_list, right_list)}")