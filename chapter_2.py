"""
----- 2.1 -----
"""

"""
Напишите программу, которая выводит фразу «Я стану крутым программистом!» три раза на отдельных строках; строки должны быть именно такие, символ в символ!.
Для удобства советую поместить эту фразу в переменную и затем использовать ее при выводе.
"""
# n = "Я стану крутым программистом!"
# print(n)
# print(n)
# print(n)

"""
Напишите программу, которая напечатает строку, состоящую из 777 букв "W"
"""
# n = "W"
# print(n * 777)

"""
Напишите программу, которая выводит «Лев Николаевич Толстой написал "Война и мир"» (без внешних кавычек).
"""
# n = 'Лев Николаевич Толстой написал "Война и мир"'
# print(n)

"""
Напишите программу, которая сначала считывает две фразы по очереди, а потом воспроизводит их в той же последовательности, 
каждую на отдельной строчке.
"""
# n = input()
# m = input()
# print(n)
# print(m)

"""
Напишите программу, которая сначала считывает три фразы по очереди, а потом воспроизводит их в обратной последовательности, 
каждую на отдельной строчке.
"""
# n = input()
# m = input()
# p = input()
# print(p)
# print(m)
# print(n)

"""
Напишите программу, которая считывает с клавиатуры слово (или фразу, неважно), после чего выводит это же слово четыре 
раза на одной строке, разделяя их пробелами.
"""
# n = input()
# print(n, n, n, n, sep = ' ')

"""
Напишите программу, которая считывает с клавиатуры фразу и выводит на экран количество символов, которое содержалось в ней, 
учитывая все знаки препинания и пунктуации.
"""
# n = input()
# print(len(n))

"""
Напишите программу, которая считывает с клавиатуры два слова (или фразы, неважно), после чего вы должны 
при помощи операции конкатенации сцепить вторую фразу с первой и вывести результат на экран.
"""
# n = input()
# m = input()
# print(m + n)

"""
Напишите программу, которая считывает с клавиатуры слово (или фразу, неважно), после чего вывести данную строку, 
увеличенную по длине  в 3 раза.
"""
# n = input()
# print(n * 3)

"""
Программа принимает на вход три символа через пробел в одну строку. Необходимо вывести код каждого символа 
при помощи функции ord в определенном формате.
"""
# n, m, p = map(str, input().split())
# print('Simvol code ' + str(n) + ' is ' + str(ord(n)) + '.')
# print('Simvol code ' + str(m) + ' is ' + str(ord(m)) + '.')
# print('Simvol code ' + str(p) + ' is ' + str(ord(p)) + '.')


"""
----- 2.2 -----
"""

"""
Программа получает на вход строку и ваша задача вывести первый элемент данной строки
"""
# n = input()
# print(n[0])

"""
Программа получает на вход строку и ваша задача вывести последний символ этой строки
"""
# n = input()
# print(n[-1])

"""
Программа получает на вход строку и ваша задача вывести первые 4 символа этой строки
Гарантируется, что вводится будет строка длиной не менее 4 символов
"""
# n = input()
# print(n[0:4])

"""
Программа получает на вход строку и ваша задача вывести последние 4 символа этой строки
Гарантируется, что вводится будет строка длиной не менее 4 символов
"""
# n = input()
# print(n[len(n) - 4:])

"""
Программа получает на вход строку. Ваша задача вывести все символы этой строки, которые имеют четные индексы
"""
# n = input()
# print(n[::2])

"""
Программа получает на вход строку. Ваша задача вывести все символы этой строки, которые имеют нечетные индексы
"""
# n = input()
# print(n[1::2])

"""
Программа получает на вход строку. Ваша задача развернуть строку и вывести ее на экран.
"""
# n = input()
# print(n[::-1])

"""
Программа получает на вход строку.
Выведите каждый третий символ строки в обратном порядке, начиная с последнего.
"""
# n = input()
# m = n[::-1]
# print(m[::3])

"""
Программа получает на вход одно слово. Ваша задача перенести последнюю букву в начало, тем самым сдвинуть 
все остальные буквы вправо на один разряд. В качестве ответа нужно вывести полученное слово
"""
# n = input()
# print(n[-1] + n[:len(n) - 1])


"""
----- 2.3 -----
"""

"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита. 
Ваша задача преобразовать строку так, чтобы все символы были только заглавными.
"""
# n = input()
# print(n.upper())

"""
На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита. 
Ваша задача преобразовать строку так, чтобы все символы были только строчными
"""
# n = input()
# print(n.lower())

"""
На вход программе поступает строка, ваша задача подсчитать сколько раз в ней встречается латинская буква "e". 
При этом стоит учитывать как маленькие, так и заглавные буквы
"""
# n = input()
# s = n.count('e')
# s += n.count('E')
# print(s)

"""
На вход программе поступает строка, ваша задача удалить из нее все символы "w" и "z".
Учитываем только маленькие буквы
"""
# n = input()
# temp = n.replace('w', '')
# temp = temp.replace('z', '')
# print(temp)

"""
На вход программе поступает строка, ваша задача вывести на экран индекс первой найденной латинской буквы "a"
Если такого символа в введенной строке нет, выведите -1
"""
# n = input()
# print(n.find('a'))

"""
На вход программе поступает строка, ваша задача вывести на экран индекс последней найденной латинской буквы "a"
Если такого символа в введенной строке нет, выведите -1
"""
# n = input()
# print(n.rfind('a'))

"""
Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза. 
Для удобства будем считать словом любую последовательность символов.
"""
# n = input()
# print(len(n.split()))

"""
Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
Ваша задача заменить все пробелы запятыми и вывести полученную строку.
"""
# n = input()
# print(n.replace(' ', ','))

"""
На вход подается строка. Ваша задача отформатировать строку так, чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.
Примечание:
Количество букв может быть различным, но гарантируется что их количество не меньше 6
"""
# n = input()
# print(n[:3].upper() + n[3:len(n) - 3].lower() + n[len(n) - 3:].upper())

"""
Упражнение на строки
Петя записался в кружок по программированию. На первом занятии Пете задали написать простую программу. 
Программа должна делать следующее: в заданной строке, которая состоит из прописных и строчных латинских букв, она:
    удаляет все гласные буквы,
    перед каждой согласной буквой ставит символ ".",
    все прописные согласные буквы заменяет на строчные.
Гласными буквами считаются буквы "A", "O", "Y", "E", "U", "I", а согласными — все остальные. 
На вход программе подается ровно одна строка, она должна вернуть результат в виде одной строки, получившейся после обработки.
"""
# n = input()
# temp = n.lower()
# temp = temp.replace('a', '')
# temp = temp.replace('o', '')
# temp = temp.replace('y', '')
# temp = temp.replace('e', '')
# temp = temp.replace('u', '')
# temp = temp.replace('i', '')
# temp = '.'.join(temp)
# print('.' + temp)


"""
----- 2.5 -----
"""

"""
Создайте этот прекрасный рисунок
/\_/\ 
>^,^< 
 / \  
(|_|)_/
Старайтесь для переноса строк использовать экранированный символ "\n"
"""
# n = '/\\_/\\\n>^,^<\n / \\ \n(|_|)_/'
# print(n)

"""
Смог нарисовать котика, сможешь и песика!)))
  /~~~\
 //^ ^\\
(/(_*_)\)
_/''*''\_
(/_)^(_\)
"""
# n = '  /~~~\\\n //^ ^\\\\\n(/(_*_)\\)\n_/\'\'*\'\'\\_\n(/_)^(_\\)'
# print(n)


"""
----- 2.6 ------
"""

"""
Напишите программу, которая считывает слово, затем выводит:
«Что Вы сказали? [это слово] ? Какое интересное слово».
"""
# n = input()
# print('Что Вы сказали? {0}? Какое интересное слово'.format(n))

"""
Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем 
формате "Здравствуйте, <фамилия> <имя>!"
"""
# name = input()
# surname = input()
# print('Здравствуйте, {0} {1}!'.format(surname, name))

"""
Напишите программу, которая считывает целое число, и затем сообщает какие числа будут следующим и предыдущим 
в определенном формате. Пробелы, знаки препинания, заглавные и строчные буквы важны!
"""
# n = input()
# print('Для числа {n} предыдущим будет число {n1}.'.format(n = n, n1 = int(n) - 1))
# print('Для числа {n} следующим будет число {n2}.'.format(n = n, n2 = int(n) + 1))


"""
----- 2.7 -----
"""

"""
На вход программе поступает строка - имя пользователя. Вам необходимо при помощи f-строки вывести сообщение:
"Мое имя <name>!"
"""
# n = input()
# print(f'Мое имя {n}!')

"""
Теперь ваша программа спрашивает у пользователя не только имя, но и его возраст. После этого программа должна вывести сообщение:
"Hello <name>. You are <age> years old."
Обратите внимание, что буквы в имени все должны быть заглавные. И не забывайте пользоваться f-строкой
"""
# name = input()
# age = input()
# print(f'Hello {name.upper()}. You are {age} years old.')

"""
77 лет
Напишите программу, которая запрашивает имя пользователя и его год рождения. Программа должна вывести 
на экран сообщение "<Имя пользователя>, вам исполнится 77 лет в <год>"
"""
# name = input()
# year = int(input())
# print(f'{name}, вам исполнится 77 лет в {year + 77}')

"""
Напишите программу для перевода натурального значения секунд в значение минут определенного формата.
"""
# n = int(input())
# print(f"{n} сек - это {n // 60} мин. {n % 60} сек.")

"""
Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. 
В результате на экране разрешение экрана и общее количество пикселей в определенном формате. 
Все знаки препинания, пробелы, регистр букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»
"""
# n, m = map(int, input().split())
# print(f'Разрешение экрана: {n} x {m}.\nОбщее количество пикселей = {n * m}.')

"""
Виды деления
Давайте при помощи F-строк выведем информацию о трех видах деления, которые мы с вами изучили ранее: обычное деление, целочисленное и деление по остатку. 
Входные данные:
На вход программе поступают два целых числа, при этом гарантируется, что второе число не равно 0.
Выходные данные: 
Необходимо вывести результат трех видов деления первого числа на второе в определенном формате (см. примеры ниже)
"""
# n = int(input())
# m = int(input())
# print(f'{n} / {m} = {n / m}\n{n} // {m} = {n // m}\n{n} % {m} = {n % m}')

"""
Нашей программе поступает на вход x, y, z - три целых числа, обозначающие координаты вектора А. 
Затем необходимо найти координаты вектора B, путем увеличения на 5 каждой из координаты вектора А.
Оба вектора необходимо распечатать в определенном формате
"""
# x = int(input())
# y = int(input())
# z = int(input())
# print(f'Vector A({x}, {y}, {z})\nVector B({x + 5}, {y + 5}, {z + 5})')

"""
Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число), 
которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:
"Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
You must pay <стоимость>"
"""
# course = float(input())
# count = int(input())
# print(f'Current dollar rate is {course}. You want buy {count} dollars\nYou must pay {count * course}')


"""
----- 2.8 -----
"""

"""
На вход вашей программе поступают координаты точки x и y - два целых числа, каждое вводится на отдельной строчке. 
Ваша задача обязательно сохранить поступающие на вход значения в переменные x и y соответственно, и затем вывести строку
вида Точка(x = {значение}, y = {значение})
"""
# x = int(input())
# y = int(input())
# print(f'Точка({x = }, {y = })')

"""
Допишите программу, чтобы выводилось только шесть знаков после запятой у переменной number_pi
"""
# number_pi = 3.141592653589793
# print(f'{number_pi:.6f}')

"""
У курсов валют на биржах обычно указываются 4 знака после запятой, как показано на картинке ниже
Но при купле/продаже обычно оставляют только два знака после запятой. 
В этом и будет заключаться, ваша задача - принять вещественное число, и вывести его в формате двух знаков после запятой
"""
# n = float(input())
# print(f'{n:.2f}')

"""
Вводится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов под отображение числа. 
Если в числе не хватает разрядов, необходимо выводить незначащие нули
"""
# n = int(input())
# print(f'{n:010d}')

"""
Вводится целое число, необходимо выполнить выравнивание его по центру, отведя 15 символов под отображение числа. 
Символом заполнителем должен являться знак пробела
"""
# n = int(input())
# print(f'{n:^15d}')

"""
Вам необходимо подправить код ниже так, чтобы он выравнивал
    первый print по центру
    второй print по правому краю
    третий print по левому краю
Количество знаков для выравнивания 20 символов, знак разделителя - &
"""
# n = input()
# print(f'|{n:&^20}|')
# print(f'|{n:&>20}|')
# print(f'|{n:&<20}|')


"""
----- 2.9 -----
"""

"""
Допишите программу ниже, чтобы она вывела через пробел в одной строке значения самого маленького и самого большого элементов списка my_list.
"""
# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# print(min(my_list), max(my_list))

"""
Программа получает на вход список из целых чисел. Ваша задача вывести True в случае, если в данном списке встречается значение 777. 
В противном случае вывести False
Примечание:
Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной my_list вам необходимо написать строчку
my_list = list(map(int, input().split()))
"""
# n = list(map(int, input().split()))
# print(777 in n)

"""
Программа получает на вход список из целых чисел. Ваша задача найти сумму списка
Примечание:
Чтобы прочитать из ввода целые числа и сохранить их в виде списка в переменной list_numbers вам необходимо написать строчку
list_numbers = list(map(int, input().split()))
"""
# n = list(map(int, input().split()))
# print(sum(n))

"""
Арбузы
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно
выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Входные данные
Программа получает список целых чисел записанных через пробел. Каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
Выходные данные
Вам нужно вывести два числа через пробел: массу арбуза, который Иван Васильевич купит теще и массу арбуза, который он купит себе.
"""
# n = list(map(int, input().split()))
# print(min(n), max(n))

"""
Программа получает на вход список из целых чисел. Ваша задача найти среднее арифметическое введенного списка чисел
"""
# n = list(map(int, input().split()))
# print(sum(n) / len(n))


"""
----- 2.10 -----
"""

"""
Программа получает на вход список целых чисел и ваша задача вывести второй элемент этого списка.
Гарантируется, что список будет состоять не менее чем из трех элементов
"""
# n = list(map(int, input().split()))
# print(n[1])

"""
Программа получает на вход список целых чисел и ваша задача вывести срез списка с третьего элемента по пятый включительно.
Гарантируется, что список будет состоять не менее чем из пяти элементов.
"""
# n = list(map(int, input().split()))
# print(n[2:5])

"""
Программа получает на вход список целых чисел и ваша задача вывести последние три элемента этого списка через срез
Гарантируется, что список будет состоять не менее чем из пяти элементов.
"""
# n = list(map(int, input().split()))
# print(n[-3:])

"""
Программа получает на вход список целых чисел и ваша задача вывести каждый третий элемент этого списка, начиная со второго по счету значения.
Гарантируется, что список будет состоять не менее чем из семи элементов.
"""
# n = list(map(int, input().split()))
# print(n[1::3])

"""
Программа получает на вход список целых чисел и ваша задача вывести этот список  в обратном порядке при помощи срезов
Гарантируется, что список будет состоять не менее чем из  трех элементов.
"""
# n = list(map(int, input().split()))
# print(n[::-1])

"""
Перед вами список топовых сериалов по версии кинопоиска. Ваша задача заменить в нем сериал "Бригада" на "Сверхъестественное" и "Друзья" на "Настоящий детектив"
В качестве ответа распечатайте на экран обновленный список.
"""
# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1] = 'Сверхъестественное'
# top[2] = 'Настоящий детектив'
# print(top)

"""
Перед вами находится список months, хранящий сокращенное название месяцев в году
Ваша программа получает на вход порядковый номер месяца в году - целое число от 1 до 12.
Ваша задача распечатать кратное название месяца, которое соответствует порядковому номеру месяца
"""
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# n = int(input())
# print(months[n - 1])


"""
----- 2.11 -----
"""

"""
На вход программе поступает список значений. Ваша задача преобразовать его таким образом, чтобы элементы расположились в обратном порядке. 
"""
# mas = input().split()
# mas.reverse()
# print(*mas)

"""
Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999.
"""
# n = list(map(int, input().split()))
# temp = n.count(999)
# print(temp)

"""
Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999
"""
# n = list(map(int, input().split()))
# temp = n.count(999)
# print(temp)

"""
Дефиснутая фраза
Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом, чтобы все буквы стали 
заглавными и между буквами в каждом слове появились дефисы
"""
# n, m = map(str, input().split())
# print('-'.join(n.upper()), '-'.join(m.upper()))

"""
Напишите программу, которая выводит слова введённой строки (части, разделённые символами пустого пространства) в столбик. 
Нужно обойтись только методом split у списков и методом join у строк, в программе должен быть всего один вызов print.
"""
# n = input()
# a = list(n.split())
# print('\n'.join(a))

"""
Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
Вам необходимо вывести фамилию и инициалы, как в примерах ниже
"""
# n = list(input().split())
# print(n[2] + ' ' + n[0][0] + '.' + n[1][0] + '.')