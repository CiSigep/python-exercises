# Exercise 38: Define a function that replaces non integer values in a list with zeroes.
def replace_with_zero(lst):
    return [ele if isinstance(ele, int) else 0 for ele in lst]