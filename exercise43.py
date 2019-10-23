# Exercise 43: enter keyword arguments for the function below such that the returned value is 9.
def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=3, b=6, c=0))
