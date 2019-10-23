# Exercise 42: Define a function that takes a list of strings, converts to uppercase and sorts them, and
# returns the list.


def uppercase_sort_list(*args):
    return sorted([ele.upper() for ele in args])

