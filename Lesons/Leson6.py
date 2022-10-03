# a = ['a', 'b', 'v']
# print(a)
#
# empty_list = []  # оголосити список
# empty_list_1 = list()  # оголосити список

# варіанти копіювання
# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# print(a)
# print(b)
# print(c)
# print(d)

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# print(a)
# print(b)
# print(c)
# print(d)
#
# b[0] = 'sasas'
# c[2] = 'bbb'
# print(a)
# print(b)
# print(c)
# print(d)
#
# # визначити індефікатор
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

# рядок в список
# s = 'Helloworld'
# s= s.upper()
# print(s)
# new_s = list(s)
# print(new_s)

# доробити
# d = '-q-w-e-----rt'
#   # прибрати -
# print(d.split('-'))
# a = ['a', 'b', 'c']  #
# result = ','.join(a)  # перевести в строку розділити через ,
# print(result)

# вкладення в кладенні можна до 3
# temp = ['bbb', 'cccc']
# a = ['hello', 'world', temp]
# b = ['test']
# result = [temp, a, b]
# print(result)
# print(result[1][1])

# temp = ['bbb', 'cccc']
# a = ['hello', 'world', temp]
# b = ['test']
# result = [temp, 'new value', b]
# print(result)
# for fist_iter in result:
#     if type(fist_iter) is list:
#         for second_iter in fist_iter:
#             if type(second_iter) is list:
#                 for third_iter in second_iter:
#                     if isinstance(third_iter, list):
#                         print('It`s list')
#                     else:
#                         print(third_iter)
#             else:
#                 print(second_iter)
#     else:
#         print(fist_iter)

# додавання елементів в існуючий список
# a = []
# a.append('Hello')
# a.append('New')
# print(a)

# temp = ['bbb', 'cccc']
# a = ['hello', 'world', temp]
# b = ['test']
# result = [temp, 'new value', b]
# print(result)
# new_list = []
# for fist_iter in result:
#     if type(fist_iter) is list:
#         for second_iter in fist_iter:
#             if type(second_iter) is list:
#                 for third_iter in second_iter:
#                     if isinstance(third_iter, list):
#                         print('It`s list')
#                     else:
#                         new_list.append(third_iter)
#             else:
#                 new_list.append(second_iter)
#     else:
#         new_list.append(fist_iter)
# print(new_list)

# a =[ 'Hello', 'world', 'New', 'Text']
# a.insert(1, 'xxxx')
# print(a)

# m = ['1', '2']
# t = ['3', '4']
# # m.append(t)
# # print(m)
# m.extend(t)
# print
#
from copy import copy, deepcopy

# l = [1, 2, 3, ['a', 'b', 'c']]
# lll = list(l)
# l_slice = l[:]
# l_copy = copy(l)
# l_deep = deepcopy(l)
# print(l_slice, l_deep, l_copy)
# l[0] = 5
# print(l)
# print(l_slice, l_deep, l_copy)
# l[3][0]='New'
# print(l)
# print(l, l_slice, l_copy, l_deep, lll)


# l = [1, 2, 3, ['a', 'b', 'c']]
# del l[3][0]  # видалити по індексу
# l.remove(1)  # видалити за певним значенням "1"
# print(l)

# a = 'r'
# print(a)
# print(type(a))
# b = 'r',
# print(b)
# print(type(b))
#
# a = 'javascript', 'python 3.8', 'c++'
# j, p, c = a
# print(j)
# print(p)
# print(c)
# print(a[0])
# print(a[1])
# print(a[2])
# a = ['javascript', 'python 3.8', 'c++']
# b = tuple(a)
# print(b)

# a = 'javascript', 'python 3.8', 'c++'
# j, *p = a
# print(j)
# print(p)# список
#
# b, *d = a
# print(b)
# print(*d) #туплекс

# a = ('c', 'b', 'a', 'x')
# b = 1, 2, 3
# print(type(a))
# print(type(b))
# d = sorted(a)
# c = sorted(b)  # сортування та переведення в список
# # print(id(a))
# # print(id(d))
# print(d)
# print(c)
# print(d + c)

# a = ["x", "a", "c", 3, 48, 45, 3]
# b = []
# for i in a:
#     b.append(str(i))
# print(sorted(b))

# l = ["a", 'b', 'c', '1', '3', '2', 1, 4, 2]
# nums = []
# strigs = []
# res = []
# for i in l:
#     if isinstance(i, int):
#         nums.append(i)
#     elif isinstance(i, str):
#         strigs.append(i)
# nums.sort()
# strigs.sort()
# res = nums + strigs
# print(res)

# print(set('Hello'))  # прибрати дублі вивід рандомний
#
# a = {1, 2, 6, 8}
# b = {1, 2, 2, 3, 4, 5, 7}
# res = a | b  # або == OR взяти без дублікатів
# print(res)
#
# res1 = a & b  # І == AND взяти тільки дублікати
# print(res1)

# q який останній та кількість
##Variant1
# st = input('Please enter the string: ')
# count = 0
# f_st = []
# for i in range(len(st)):
#     if st[i] == "q":
#         count += 1
#         f_st.append(i)
# print(f_st[-1])
# print(count)
##Variant2

data = input('Please enter the string: ')
f = 'q'
count, count_q = 0, 0
index = -1
for item in data:
    if item == f:
        index = count
        count_q += 1
    count += 1
print(f'count total: {count}, count q: {count_q}, index: {index}')
