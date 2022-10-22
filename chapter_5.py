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
Мишка и игра
Мишка — маленький белый медвежонок. А как известно, маленькие медвежата в свободное время любят играть в кости на шоколадки. 
Одним замечательным солнечным утром, гуляя по льдинам, Мишка встретил своего друга Криса, которому и предложил сыграть в эту занимательную игру.
Правила её очень просты: сначала определяется значение n — количество раундов игры. В очередном раунде каждый 
из игроков один раз бросает стандартный игральный кубик, на грани которого нанесены различные числа от 1 до 6. 
Игрок, выбросивший большее значение, становится победителем в раунде. В случае, если выпавшие значения равны, победа не засчитывается никому.
В самой же игре побеждает участник, выигравший в большем количестве раундов. Если же количества побед, заслуженных игроками, равны, то объявляется ничья.
Мишка ещё совсем маленький и плохо умеет вести счёт, а потому попросил Вас понаблюдать за ходом игры и сообщить ему результат.
Входные данные:
В первой строке входных данных содержится число n (1≤n≤100) — количество раундов игры.
Следующие n строк содержат описание раундов. В i-й из них содержится пара целых чисел mi и ci (1≤mi,ci≤6) — результаты 
бросков Мишки и Криса в i-ом раунде соответственно.
Выходные данные:
В случае победы Мишки в единственной строке выведите "Mishka" (без кавычек), а в случае победы Криса выведите "Chris" (без кавычек). 
Если же игра сведётся к ничьей, то выведите "Friendship is magic!^^" (без кавычек).
PS: генерировать случайные числа(пользоваться модулем random) вам не нужно, данные для игры уже готовы. 
Вам нужно только их считать,  и узнать кто же победил
"""
# n = int(input())
# result = 0
# for i in range(n):
#     m, c = map(int, input().split())
#     if m > c:
#         result += 1
#     elif m < c:
#         result -= 1
# if result == 0:
#     print('Friendship is magic!^^')
# elif result > 0:
#     print('Mishka')
# elif result < 0:
#     print('Chris')

"""
Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки.
Формат ввода:
На первой строке вводится натуральное число N — количество строк.
Далее следуют N строк.
Формат вывода:
Для каждой строки, в которой есть сочетание символов «рок», нужно вывести (в порядке появления таких строк) номер этой 
строки (нумерация начинается с единицы) и номер символа, с которого начинается первое вхождение этой подстроки (нумерация символов также с единицы).
"""
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
# for i in range(n):
#     if 'рок' in a[i].lower():
#         print(i + 1, (a[i].lower().find('рок')) + 1)

"""
Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится "соль". Переписывайте без этого слова.
Формат ввода:
На первой строке вводится натуральное число N — количество пунктов рецепта.
Далее следуют N строк — пункты рецепта.
Формат вывода:
Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием слова "соль" (то есть таких, 
в которых нет подстроки "соль" в нижнем регистре).
"""
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
# for i in range(n):
#     if i == n - 1 and 'соль' not in a[i].lower():
#         print(a[i])
#     elif 'соль' not in a[i].lower():
#         print(a[i], end=', ')

"""
Слишком длинные слова
Иногда некоторые слова вроде «civilization» или «internationalization» настолько длинны, что их весьма утомительно писать много раз в каком либо тексте.
Будем считать слово слишком длинным, если его длина строго больше 10 символов. Все слишком длинные слова можно заменить специальной аббревиатурой.
Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова, а между ними — количество букв 
между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).
Таком образом, «civilization» запишется как «c10n», а «internationalization» как «i18n».
Вам предлагается автоматизировать процесс замены слов на аббревиатуры. При этом все слишком длинные слова должны быть 
заменены аббревиатурой, а слова, не являющиеся слишком длинными, должны остаться без изменений.
Входные данные:
В первой строке содержится целое число n (1≤n≤100). В каждой из последующих n строк содержится по одному слову. 
Все слова состоят из малых латинских букв и имеют длину от 1 до 100 символов.
Выходные данные:
Выведите n строк. В i строке должен находиться результат замены i-го слова из входных данных.
"""
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
#     if len(a[i]) > 10:
#         a[i] = a[i][0] + str(len(a[i][1:-1])) + a[i][-1]
# for i in range(n):
#     print(a[i])


"""
----- 5.3 -----
"""

"""
Перед вами список numbers, состоящий из 100 целых чисел
Ваша задачи пройтись в цикле по элементам списка и вывести на экран каждый элемент на отдельной строке
"""
# numbers = [99, 50, -16, 9, 47, -62, 5, -64, -68, 85, 11, -20, 16, 96, -43, 46, -25, 33, 81, -30, 64, 66, -11, 60, 3, -5, -1,
#  -80, 49, -12, -86, -40, -98, -92, -91, -71, 56, -76, -30, -82, 17, -2, -64, 47, 22, -28, 40, 55, 54, -3, -58, -10,
#  -35, -15, -2, -60, 70, 50, -77, 83, -49, 42, 27, -58, -79, -2, -100, -42, -18, 38, 95, 9, 98, -89, -46, 96, 64,
#  -35, 41, 94, 1, -90, 29, 23, 39, -3, 11, -65, -64, 52, -69, 32, -14, -49, -28, -11, 85, -75, -6, 15]
#
# for i in numbers:
#     print(i)

"""
Перед вами список words, состоящий из 100 строк
Ваша задачи пройтись в цикле по элементам списка и вывести на экран только те элементы, длина которых больше 6.
Выводить каждый элемент нужно на отдельной строке в том же порядке, в котором слова расположены в списке words
"""
# words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
#            'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
#            'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
#            'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
#            'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
#            'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
#            'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
#            'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
#            'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']
#
# for i in words:
#     if len(i) > 6:
#         print(i)

"""
Перед вами список numbers, состоящий из 100 целых чисел
Ваша задачи пройтись в цикле по элементам списка и увеличить каждый в 2 раза.
В итоге изначальный список numbers  должен измениться
В качестве ответа распечатайте измененный список numbers
"""
# numbers = [-35, 68, -91, 23, -92, -82, -74, 32, 39, -30, -100, -29, 54, 26, 54, -45, 20, 53, -17, 68, -35, 11, 26, -17,
#            70, 89, -81, -4, 61, -45, 13, 63, -48, -66, -92, -15, -88, -87, -75, 44, -49, -81, 19, -33, -59, 85, -69, -60,
#            9, -98, 28, 11, 15, -35, -80, 5, -20, -52, -45, 26, 47, -16, 40, -14, -12, 15, 73, -16, 29, -98, 93, -77, 1,
#            85, 77, 73, 100, -71, 99, 39, 2, -38, 49, -31, 15, 43, 94, -39, -89, -46, -71, 39, -56, 41, -93, 4, -79, 48,
#            88, -51]
# n = len(numbers)
#
# for i in range(n):
#     numbers[i] *= 2
# print(numbers)

"""
Заполняем список
Ваша задача создать список из n строк. Программа сперва будет принимать натуральное число n, а затем n строк 
в каждой отдельной строке. В качестве ответа выведите получившийся список.
"""
# n = int(input())
# a = []
#
# for i in range(n):
#     a.append(input())
# print(a)

"""
Входные данные:
На первой строке вводится один символ — строчная буква.
На второй строке вводится предложение.
Выходные данные:
Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), 
в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.
"""
# n = input()
# a = input().split(' ')
#
# for i in a:
#     if n.lower() in i.lower():
#         print(i)

"""
Линейный поиск
Линейный поиск, также известный как последовательный поиск, этот метод используется для поиска элемента в списке. 
Линейный поиск является одним из базовых алгоритмов, с которым вы должны познакомиться, изучая программирования. 
Суть алгоритма в следующем: вы должны проверять каждый элемент списка последовательно один за другим, пока не найдете 
интересующий вас элемент или пока не закончится весь список.
Входные данные:
Программа получает на вход в одной строке элементы списка - целые числа, разделенные пробелом. Количество элементов произвольное
И на следующей строке вводится одно число r - значение поиска
Выходные данные:
Ваша задача реализовать линейный алгоритм поиска введенного значения r. В случае успеха - выведите порядковый номер(индекс) 
первого найденного элемента в списке при условии, что индексация начинается с единицы. Если данный элемент отсутствует - необходимо вывести строку ErrorValue 
"""
# a = input().split(' ')
# r = int(input())
# n = len(a)
#
# for i in range(n):
#     if int(a[i]) == r:
#         print(i + 1)
#         break
# else:
#     print('ErrorValue')

"""
На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение. 
В случае, если положительных значений нет, выведите строку "Empty"
"""
# a = input().split()
# n = len(a)
# minimum = 99999
#
# for i in range(n):
#     if int(a[i]) < minimum and int(a[i]) > 0:
#         minimum = int(a[i])
# if minimum != 99999:
#     print(minimum)
# else:
#     print('Empty')

"""
Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.
Формат ввода:
Вводится одна строка.
Формат вывода:
Выводится одно целое число — максимальное количество раз, которое встречается какая-либо буква (без учёта регистра) 
или иной символ во введённой строке.
"""
# s = input()
# result = []
#
# for i in s:
#     count = 0
#     temp = i
#     for j in s:
#         if temp.lower() == j.lower():
#             count += 1
#     result.append(count)
#
# print(max(result))

"""
Делимость на 11
Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах, и суммой цифр, 
стоящих на нечетных местах, делилась на 11.
Требуется написать программу, которая проверит делимость заданного числа на 11.
Входные данные:
Программа получает на вход одно натуральное число N, делимость которого надо проверить (1 ≤ N ≤ 1010000).
Выходные данные:
Выведите “YES”, если число делится на 11, или “NO” иначе.
"""
n = int(input())
sum_even = 0 #Сумма четных
sum_odd = 0 #Сумма нечетных

for i in n:
    if int(i) % 2 == 0:
        sum_even += int(i)
    else:
        sum_odd += int(i)
if (sum_even - sum_odd) % 11 == 0:
    print('YES')
else:
    print('NO')