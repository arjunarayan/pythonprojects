def twoLoop(num_list, target):
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            if i == j:
                continue
            else:
                if num_list[i] + num_list[j] == target:
                    return [i, j]
    return [-1,-1]


def dictionary(numbers, target):
    num_dict = {}
    for i in range(0, len(numbers)):
        number = numbers[i]
        expected_number = target - number
        if expected_number in num_dict and num_dict[expected_number] != i:
            return [num_dict[expected_number], i]
        num_dict[number] = i
    return [-1,-1]


print(dictionary([2, 7, 11, 15], 26))