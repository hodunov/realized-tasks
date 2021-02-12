"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

import re


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
    if all(elem in list(available.keys()) for elem in list(recipe.keys())):
        return min([available[key] // recipe[key] for key in recipe])
    else:
        return 0


# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe, available))

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# print(cakes(recipe, available))

"""
The old switcheroo 2

This is a follow up from my kata The old switcheroo</br/>

Write

def encode(str)
that takes in a string str and replaces all the letters with their respective positions in the English alphabet.

encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'
"""


def encode(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for element in string.lower():
        if element in alphabet:
            result += str(alphabet.index(element)+1)
        else:
            result += element
    return result

# encode('abc') # '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') # '315452311819'
# encode('abc-#@5') #  '123-#@5'


"""
FIXME: Replace all dots
The code provided is supposed replace all the dots . in the specified String str with dashes -

But it's not working properly.

Task
Fix the bug so we can all go home early.

Notes
String str will never be null.

"""


def replace_dots(str):
    return re.sub(r"\.", "-", str)

# print(replace_dots("no dots"))
# print(replace_dots("........"))


"""
First non-repeating character

Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. 
For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None 
-- see sample tests.
"""


def first_non_repeating_letter(string):
    result = [letter for letter in string if string.lower().count(
        letter.lower()) == 1]
    return result[0] if result else ""

# print(first_non_repeating_letter('stress'))
# print(first_non_repeating_letter('sTreSS'))
# print(first_non_repeating_letter(''))
# print(first_non_repeating_letter('abba'))


"""
Human readable duration format

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
"""


def format_duration(second):
    result = []
    times = [(60, 'second'),
             (60, 'minute'),
             (24, 'hour'),
             (365, 'day'),
             (second+1, 'year')]
    for duration, title in times:
        second, minute = divmod(second, duration)
        if minute:
            result.append('%d %s%s' % (minute, title, 's' * (minute > 1)))
    return ' and '.join(', '.join(result[::-1]).rsplit(', ', 1)) or 'now'


# print(format_duration(3662))  # 1 hour, 1 minute and 2 seconds
# print(format_duration((86400*365+60)))  # 1 year and 1 minute

"""
Get the mean of an array

It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
"""


def get_average(marks):
    return int(sum(marks) / len(marks))
    

# print(get_average([1, 5, 87, 45, 8, 8])) # 25

"""
Double Sort

Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, or a mix of both. You will not get an empty array, nor a sparse one.

Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings sorted in alphabetic order. The values must maintain their original type.

Note that numbers written as strings are strings and must be sorted with the other strings.

"""


def db_sort(arr): 
   return sorted(arr, key=lambda val: (isinstance(val, str), val))


def db_sort2(arr):
    new_arr = [x for x in arr if type(x)==int]
    new_arr.sort()
    arr = [x for x in arr if x not in new_arr]
    arr.sort()
    return new_arr + arr

# print(db_sort(["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"])) # should be equal [46,78,574,"287", "3","423", "69","Apple","Grape","Peach"]
# assert db_sort(["Apple",46,"287",574,"Peach","3","69",78,"Grape","423"]) == [46,78,574,"287", "3","423", "69","Apple","Grape","Peach"]
# print(db_sort2([5, 6, 6, 7, 10, 15, 110, '2500', '!', 'come', 'on'])) # should equal [5, 6, 6, 7, 10, 15, 110, '!', '2500', 'come', 'on']

"""
Double Trouble

Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.

Example:

x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2. No other pairs = t, so rest of array remains:

[1, 3, 4, 5]

Work through the array from left to right.

Return the resulting array.
"""

def trouble(lst, target):
    for i in range(len(lst) - 1):
        if lst[i] + lst[i + 1] == target:
            del lst[i + 1]
            return trouble(lst, target)
    return lst

# print(trouble([1, 3, 5, 6, 7, 4, 3], 7))  # should equal [1, 3, 5, 6, 7, 4]
# print(trouble([2, 2, 2, 2, 2, 2], 4))  # should equal [2]


"""
Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.

"""

def triple_trouble(one, two, three):
    return ''.join(map(str, [one[i]+two[i]+three[i] for i in range(len(one))]))


print(triple_trouble("Bm", "aa", "tn")) # should equal "Batman"