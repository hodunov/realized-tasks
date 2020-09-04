""""
Sort the list according to the template described below

Input data:
scheduled_items = ['2020-12-10 10:10:00', '2020-20-10 10:10:00', '2020-10-12 10:10:00', '2020-19-11 12:30:00',
'2020-10-11 12:12:00', '2020-10-11 12:30:00','2020-09-02 20:00:00']

output:
[['2020-20-10 10:10:00', 1], ['2020-19-11 12:30:00', 1], ['2020-12-10 10:10:00', 1], ['2020-10-12 10:10:00', 1],
['2020-10-11 12:30:00', '2020-10-11 12:12:00', 2], ['2020-09-02 20:00:00', 1]]

"""
import re

scheduled_items = ['2020-12-10 10:10:00', '2020-20-10 10:10:00', '2020-10-12 10:10:00',
                   '2020-19-11 12:30:00', '2020-10-11 12:12:00', '2020-10-11 12:30:00',
                   '2020-09-02 20:00:00']

result = []  # resulting list
for element in scheduled_items:
    substring = element.split()[0]  # substring to be searched
    # using re, we will go through the whole list and select the elements that have a substring
    new_list = [item for item in scheduled_items if re.search(substring, item)]
    counter = len(new_list)  # count the number of items in the new_list
    new_list.append(counter)  # add a counter
    if new_list not in result:  # to avoid repetitions in the resulting list
        result.append(new_list)
print(result)
