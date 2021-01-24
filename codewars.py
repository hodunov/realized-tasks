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

"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""


def to_camel_case(text):
    text = text.replace("_", "-")
    return "".join([text.split("-")[0]] + [i.capitalize() for i in text.split("-")[1:]])


# print(to_camel_case("the-stealth_warrior"))
# print(to_camel_case("A_B-C"))


"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            if count != 0:
                count -= 1
            else:
                return False
    return count == 0

# print(valid_parentheses("hi(hi)("))
# print(valid_parentheses("hi(hi)()"))

"""
Pete, the baker
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

def cakes(recipe, available):
    if all(elem in list(available.keys())  for elem in list(recipe.keys())):
        return min([available[key] // recipe[key] for key in recipe ])
    else:
        return 0


# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe, available))

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# print(cakes(recipe, available))
