# -*- coding: utf-8 -*-
"""problem_11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O3MmsO5xchm157zdJV4f6_gmiaXlx-CR
"""

'''
Write a Python program to filter positive numbers from a list.
'''

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
numbers = [-1, 0, 1, 2, -3, 4, 5, -6]
positive_numbers = filter_positive_numbers(numbers)
print(positive_numbers)