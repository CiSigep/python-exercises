# Exercise 49: Append the contents of "bear1.txt" to "bear2.txt"
with open("bear1.txt", "r") as file_one, open("bear2.txt", "a") as file_two:
    file_two.write(file_one.read())
