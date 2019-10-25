# Exercise 45: Open a file and read the first 90 characters.
my_file = open("bear.txt")
print(my_file.read()[:90])
my_file.close()
