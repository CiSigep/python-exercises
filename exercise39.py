# Exercise 39: Define a function that will take in a list of floats as strings, convert them, and return the sum.
def convert_and_sum(lst):
    return sum([float(ele) for ele in lst])
