'''
Write a Python function (user defined/not built-in) to find the maximum and minimum numbers from a sequence of numbers.
'''

numbers = [3, 5, 1, 9, 2, 7]
def find_max_min(numbers):
    if not numbers:
        return None, None

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

max_num, min_num = find_max_min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
