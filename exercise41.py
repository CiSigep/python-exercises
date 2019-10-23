# Exercise 41: Define a function that calculates the average of an indefinite number of numbers.
def avg(*args):
    return sum(args) / len(args)
