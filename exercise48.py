# Exercise 48: Open "bear.txt" and write the first 90 characters to a new file called "first.txt"
with open("bear.txt", "r") as bear_file, open("first.txt", "w") as first_file:
    first_file.write(bear_file.read()[:90])
