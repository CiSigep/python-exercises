# Exercise 27: Create a function that given a temperature, returns "Hot" if it is greater than 25, "Warm" if it is
# between 25 and 15 inclusive, and "Cold" if it is less than 15.
def hot_warm_or_cold(temp):
    if temp > 25:
        return "Hot"
    elif 25 >= temp >= 15:
        return "Warm"
    else:
        return "Cold"
