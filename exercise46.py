# Exercise 46: Define a function that takes in a character and a filepath and returns the count of the occurences of the
# character in the file.

def count_characters(character, filepath):
    file = open(filepath)
    count = file.read().count(character)
    file.close()
    return count
