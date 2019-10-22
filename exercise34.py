# Exercise 34: Print out the key-value pairs of the dictionary below in the format of "{key}: {value}"
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))
    # print(f"{key}: {value}") # works in Python 3.6+
