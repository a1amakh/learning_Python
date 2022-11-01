"""
----- 6.1 -----
"""

"""
Создайте две переменные empty и empty_too, сохраните в них значение None
При помощи оператора is выведите на первой строке результат их сравнения на равенство и затем на второй строке результат 
их сравнения на неравенсто
"""
# #Блок решения
# empty = None
# empty_too = None
#
# #Блок вывода
# print(empty is empty_too)
# print(empty is not empty_too)

"""
Создайте список i_love_none из 50 элементов None и распечатайте его
"""
# #Блок решения
# i_love_none = [None for i in range(50)]
#
# #Блок вывода
# print(i_love_none)


"""
----- 6.2 -----
"""

"""
Сохраните в переменной my_tuple кортеж состоящий из 4 любых элементов.
Распечатывать ничего не нужно, просто создайте кортеж
"""
# my_tuple = (1, 2, 3, 4)

"""
Сохраните в переменной lonely кортеж из одного элемента: 777
Распечатайте на экран lonely
"""
# #Блок решения
# lonely = (777,)
#
# #Блок вывода
# print(lonely)

"""
Допишите программу ниже, чтобы она вывела через пробел в одной строке значения самого маленького и самого большого 
элементов кортежа my_tuple.
"""
# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
#             759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
#             631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
#             -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
#             867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
#             -986, -964, -73, 29)
#
# #Блок решения
# #Блок вывода
# print(min(my_tuple), max(my_tuple))

"""
Допишите программу ниже, чтобы она вывела среднего арифметического всех элементов кортежа my_tuple.
"""
# my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781,
#             759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791,
#             631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933,
#             -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278,
#             867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472,
#             -986, -964, -73, 29)
#
# #Блок решения
# #Блок вывода
# print(sum(my_tuple) / len(my_tuple))

"""
При помощи операций сцепления и дублирования сохраните в переменной result следующий кортеж 
Он состоит из:
    трех единиц
    пяти букв R
    восьми букв A
    пяти цифр 2
Для удобства можете пользоваться переменными a b c d
В качестве ответа выведите содержимое переменной result
"""
# a = (1,)
# b = ('R',)
# c = ('A',)
# d = (2,)
# result = ()
#
# #Блок решений
# result = a * 3 + b * 5 + c * 8 + d * 5
#
# #Блок вывода
# print(result)

"""
Сформировать кортеж, содержащий натуральные числа в интервале [a; b] и вывести его на экран.
Формат ввода:
Вводится два натуральных числа a и b в отдельных строках. Гарантируется, что a<b.
Формат вывода:
Вывести кортеж, содержащий натуральные числа в интервале [a; b]
"""
# result = ()
#
# #Блок ввода
# a = int(input())
# b = int(input())
#
# #Блок решения
# result = tuple(range(a, b + 1))
#
# #Блок вывода
# print(result)

"""
Сформировать кортеж, содержащий нечетные натуральные числа в интервале [n; n^2] и вывести его на экран.
Формат ввода:
Вводится натуральное число n. 
Формат вывода:
Вывести кортеж, содержащий нечетные натуральные числа в интервале  [n; n^2]
"""
# result = []
#
# #Блок ввода
# n = int(input())
#
# #Блок решения
# for i in range(n, n ** 2 + 1):
#     if i % 2 != 0:
#         result.append(i)
#
# result = tuple(result)
#
# #Блок вывода
# print(result)


"""
----- 6.3 -----
"""

"""

"""
