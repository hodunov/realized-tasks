"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

def high_and_low(numbers):
    numbers = [int(each) for each in numbers.split()]
    return f"{max(numbers)} {min(numbers)}"

print(high_and_low("4 5 29 54 4 0 -214 544 -64 1 -3 6 -6"))
print(high_and_low("1 2 3 4 5"))
