# Exercise 33: Same as 30, but only print integers that are grater than 50.
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)