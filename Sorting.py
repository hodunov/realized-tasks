""""
scheduled_items = ['2020-12-10 10:10:00', '2020-20-10 10:10:00', '2020-10-12 10:10:00', '2020-19-11 12:30:00',
'2020-10-11 12:12:00', '2020-10-11 12:30:00','2020-09-02 20:00:00']
Входные данные
[['2020-20-10 10:10:00', 1], ['2020-19-11 12:30:00', 1], ['2020-12-10 10:10:00', 1], ['2020-10-12 10:10:00', 1],
['2020-10-11 12:30:00', '2020-10-11 12:12:00', 2], ['2020-09-02 20:00:00', 1]]
Результат
"""
import collections
import datetime as dt

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


# my_date = '2020-12-10 10:10:00'
#
all_dates = [dt.datetime.strptime(date, "%Y-%d-%m %H:%M:%S") for date in scheduled_items]

# for i in all_dates:
#     print(i.date())
#


#
#
# print('-'*10)
# my_dates = [date.strftime("%Y-%d-%m %H:%M:%S") for date in all_dates]
# print(my_dates)

lst = scheduled_items

# print([[l, lst.count(l)] for l in lst])


#
# result = []
# counter = 1
# for element in lst:
#     elem = element[:10]
#     if element.startswith(elem) in result:
#         counter += 1
#         result.append([element,counter])
#     else:
#         result.append([element, counter])
# print(result)

#
# str = "2020-10-11 "
# length = len(str)

# (sum(element[index:index+len(str)] == str for element in data for index, char in enumerate(element)))
data = lst

result = [[0]]
pos = 0
# for element in lst:
#     str = element[:10]
#     count = (sum(element[index:index+len(str)] == str for element in data for index, char in enumerate(element)))
#     if count == 1:
#         result.append([element, count])
#     else:
#         result[pos].insert(0, element)
#         result[pos][-1] = count
#
# print(result)

# print(result[0])
# dic_res = [[0, 0]]
# step = 0
# index_count = 1

# проход по списку и формирование с.а. для диапазонов
# data = lst
#
# result = []

# for index, element in enumerate(lst):
#     str = element[:10]
#     count = (sum(element[index:index+len(str)] == str for element in data for index, char in enumerate(element)))
#     if count >1:
#
#     result.append([element, count])
# print(result)
#
# count = 1
# for element in lst:
#     str = element[:10]
#     result.append([element])
# print(result)
data = lst

# for element in lst:
#     str = element[:10]
#     count = (sum(element[index:index+len(str)] == str for element in data for index, char in enumerate(element)))
#     result.append([element, count])
# print(result)
index_count = 0
result = [[0]]
res_index = 0
el_index = 0
counter = 0
# for element in data:
#     for index, char in enumerate(element):
#         search = "2020-10-11"
#         if element[index:index+len(search)] == search:
#             result[res_index].insert(0, element)
#             counter += 1
#             result[res_index][-1] = counter
#
# print(result)


# sub = '2020-10-11'
#
# print("\n".join(s for s in lst if sub in s)) # Поиск подстроки в строке


# old_list = lst
# new_list = [x for x in old_list if re.search('2020-10-11', x)]
# counte=len(new_list)
# new_list.append(counte)
# print(new_list)
