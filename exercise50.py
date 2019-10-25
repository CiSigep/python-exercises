# Exercise 50: Read a file and add its contents into the file 2 more times.
with open("data.txt", "a+") as file:
    file.seek(0)
    contents = file.read()
    file.seek(0)
    file.write(contents)
    file.write(contents)
