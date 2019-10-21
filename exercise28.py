# Exercise 28: Create a function that takes in a name and returns "Hi <name>"
def say_hi(name):
    # return f"Hi {name}" # Works on Python 3.6 or later, class servers use Python 3.5 though.
    return "Hi %s" % name

