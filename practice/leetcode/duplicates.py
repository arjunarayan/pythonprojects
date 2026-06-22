
numbers = [99, 99, 99, 99, 99, 99]

def checkDuplicate(nums):
    num_dict ={}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    output =[]
    for seen in num_dict:
        if num_dict[seen] > 1:
            output.append(seen)
    return output


print(checkDuplicate(numbers))