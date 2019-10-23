# Exercise 36: Define a function that given a list, returns a list of only the integers in the list.
def only_numbers(lst):
    return [ele for ele in lst if isinstance(ele, int)]
