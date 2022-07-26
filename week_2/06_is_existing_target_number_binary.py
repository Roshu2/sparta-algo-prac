finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    target_guess = (current_min + current_max) // 2
    while current_min <= current_max:
        if array[target_guess] == target:
            return True
        elif array[target_guess] < target:
            current_min = target_guess + 1
        else:
            current_max = target_guess - 1
        target_guess = (current_min + current_max) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)