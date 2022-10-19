"""
----- 5.1 -----
"""

"""
Допишите программу так, чтобы она печатала на экран список, содержащий последовательность чисел 0,1,2,3,4,5,6,7,8,9 ?
"""
# print(list(range(10)))

"""
Теперь необходимо передать в функцию range параметры, чтобы получилась последовательность чисел от 12 до 34 включительно?
"""
# print(list(range(12, 35)))

"""
Теперь давайте добавим шаг. Необходимо сформировать последовательность 25, 33, 41, 49, 57 .... , 169
"""
# print(list(range(25, 170, 8)))

"""
Нам осталось поработать с убывающими последовательностями.
Сформируйте последовательность -11, -12, -13, -14 .... , -35
"""
# print(list(range(-11, -36, -1)))

"""
Еще одну
Сформируйте последовательность 10, 9, 8, 7, ... , 0
"""
# print(list(range(10, -1, -1)))

"""
И последняя последовательность 1000, 950, 900, 850, ... , 500
"""
# print(list(range(1000, 499, -50)))


"""
----- 5.2 -----
"""

"""
Программа принимает на вход натуральное число N. Ваша задача вывести на экран все числа от 1 до N каждое число на отдельной строке. 
"""
# n = int(input())
# for i in range(1, n + 1):
#     print(i)

"""
Напишите программу, которая выведет все элементы арифметической прогрессии от 0 до 500 включительно с шагом 5.
Каждый элемент выводится отдельно на своей строке в таком виде
"""
# for i in range(0, 501, 5):
#     print(i)

"""
Программа принимает на вход натуральное число N. 
Ваша задача вывести на экран все числа от N до 1 в сторону уменьшения каждое число на отдельной строке. 
"""
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

"""
«Надо было брать биткоин в 2012!» именно такую фразу ваша программа должна вывести на экран 13 раз
"""
# for i in range(13):
#     print('Надо было брать биткоин в 2012!')

"""
Повторение - мать учения 
Каждый, кто смотрел Симпсонов, помнит, что в начале любой серии Барт писал забавные фразы на доске.
Давайте и мы напишем подобную программу. На вход ей будет поступать фраза и затем количество раз, которое эту фразу нужно повторить.
"""
# line = input()
# count = int(input())
# for i in range(count):
#     print(line)

"""
Давайте вспомним задачу FizzBuzz
Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a<b), после чего для всех чисел от a до b включительно выводит:
    “Fizz”, если это число делится на 3;
    “Buzz”, если это число делится на 5;
    “FizzBuzz”, если выполнены оба предыдущих условия;
    само это число в остальных случаях.
Формат ввода:
Два числа a и b, каждое на отдельной строке.
Формат вывода:
Для всех чисел от a до b напечатайте по одной строке, соответствующей правилам, описанным в условии.
"""
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 != 0:
#         print('Fizz')
#     elif i % 5 == 0 and i % 3 != 0:
#         print('Buzz')
#     elif i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)

"""
Квадрат и куб
Давайте составим сводную информацию о квадратах и кубах интервала чисел.
На вход программе подается два натуральных числа a и b (гарантируется, что a<b), после чего для каждого целого числа 
на интервале от a до b включительно необходимо вывести фразу следующего вида:
«Число {число}; его квадрат = {квадрат}; его куб = {куб}»
Кавычки выводить не нужно и пользуйтесь f-строкой.
Формат входных данных:
На вход программе подается два натуральных числа a и b, каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
"""
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')

"""
Кратные 3 или 5
Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.
Напишите программу, которая принимает натуральное число n и находит сумму всех чисел ниже переданного числа n, 
которые делятся на 3 или на 5.
"""
# n = int(input())
# s = 0
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
# print(s)

"""
Напишите программу, которая найдет сумму кубов натуральных чисел от 50 до 100 включительно
"""
# s = 0
# for i in range(50, 101):
#     s += i ** 3
# print(s)

"""
Стандартная задача на нахождения факториала. Факториал числа n! обозначается и находится по формуле 
n!=1∗2∗3∗...∗nn!=1∗2∗3∗...∗n
Значит, согласно этой формуле
4!=1∗2∗3∗4=244!=1∗2∗3∗4=24
5!=1∗2∗3∗4∗5=1205!=1∗2∗3∗4∗5=120
Но учитывайте,  что
1!=11!=1
0!=10!=1
"""
# n = int(input())
# mult = 1
# for i in range(n + 1):
#     if i == 0 or i == 1:
#         i = 1
#     mult *= i
# print(mult)

"""

"""
