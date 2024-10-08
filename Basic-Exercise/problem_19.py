'''
Write a Python program to sort (ascending and descending) a dictionary by value or by key.
'''

d = {'a': 5, 'b': 2, 'c': 7, 'd': 1, 'e': 3}
def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), reverse=reverse))

def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

print("Original dictionary:", d)

print("Sorted by key (ascending):", sort_dict_by_key(d))
print("Sorted by key (descending):", sort_dict_by_key(d, reverse=True))

print("Sorted by value (ascending):", sort_dict_by_value(d))
print("Sorted by value (descending):", sort_dict_by_value(d, reverse=True))
