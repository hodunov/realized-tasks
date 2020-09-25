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

# print(high_and_low("4 5 29 54 4 0 -214 544 -64 1 -3 6 -6"))

"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.
"""

# Best practice: 
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# Another var
def find_uniq(arr):
    a = sorted(arr)
    print(a)
    return a[0] if a[0] != a[1] else a[-1]
