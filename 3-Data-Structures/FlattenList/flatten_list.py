
def flatten_list(lst):
    if not lst:
        return []
    if type(lst[0])== list:
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    return [lst[0]] + flatten_list(lst[1:])

print(flatten_list([1, 2, [3], [4, 5]]))  # Output: [1, 2, 3, 4, 5]

print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))
