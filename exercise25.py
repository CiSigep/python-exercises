# Exercise 25: Create a function that takes in a string and returns true if the string is 8 characters or longer
def password_validate(password):
    if len(password) >= 8:
        return True
    else:
        return False
    # return len(password) >= 8 also works, but the context of this exercise is conditionals.
