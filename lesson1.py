# Семинар по ТЕСТИРОВАНИЮ 1
# Задача 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = int(input())
# m = int(input())
# day = (m+n-1)//n
# print(day)
# print(m % n)

# ------
# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input())
# b = int(input())
# c = int(input())
# print((a//2+a % 2)+(b//2+b % 2)+(c//2+c % 2))

# ------
# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input())
# j = int(input())
# if i == j:
#     print('нехватает данных')
# else:
#     print(j+i-1)

# # ------
# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# i = int(input())
# if i % 4 == 0 and i % 100 != 0:
#     print('YES')
# elif i % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# # ------
# Это вариант классической задачи Иосифа Флавия. В кругу стоят n человек,
# пронумерованных числами от 1 до n. Начинается расчет, при котором каждый k-й по
# счету человек выбывает из круга, после чего счет продолжается со следующего за ним
# человека. Напишите программу, определяющую номер человека, который остаетсяв
# кругу последним.
# Пример ввода: 9 3
# пример вывода (Номер последнего оставшегося человека): 1

# n = int(input('количество: '))
# k = int(input('рассчет: '))
# last = 0
# for i in range(1, n+1):
#     last = (last+k) % i
# print(last+1)

# # ------
# Семинар по ПРОГРАММИРОВАНИЮ 1

# # Напишите программу, которая на вход принимает число и выдаёт его квадрат (число умноженное на само себя).
# # Например:
# # 4 -> 16
# # -3 -> 9
# # -7 -> 49

# a = int(input('введите число: '))
# a = int(a)
# print(f'Результат {a*a}')

# ------
# Напишите программу, которая на вход принимает два числа и проверяет, является ли второе число квадратом первого.
# a = 5; b = 25 -> да
# a = 9; b = -3 -> нет
# a = -3 b = 0 -> нет

# a = int(input('введите число a: '))
# b = int(input('введите число b: '))

# if a**2 == b:
#     print(f'a = {a}; b = {b} -> {b} является квадратом {a}')
# else:
#     print(f'a = {a}; b = {b} -> {b} неявляется квадратом {a}')

# -----
# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

# a = int(input('введите число: '))
# count = 0
# while a != 0:
#     if a % 3 == 0:
#         count += 1
#         print(a)
#     a = int(input('введите число: '))
# print('цикл закончен')
# print(f'чисел кратных трем было {count}')

# #я не сразу понял условия задачи и решил немного иначе... но было тоже интересно)
# a = int(input('введите число: '))
# count = 0
# while a != 0:
#     if a % 3 == 0:
#         count += 1
#         print(a)
#     a -= 1
# print('цикл закончен')
# print(f'чисел кратных трем было {count}')

# -----
# Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
# Например: 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# n = abs(int(input("Введите число: ")))
# i = -n
# print(f"{n} ->  ", end="")
# while i < n + 1:
#     print(f"{i}\t", end="")
#     i += 1

# -----
# Пример целочисленного деления
# number = 1743
# while number > 0:
#     digit = number % 10
#     print(f"{digit}\t", end="")
#     number //= 10

# -----
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# number = 123.3567
# print(int(number*10//1) % 10)

# -----
# # Напишите программу, которая находит наибольшее и наименьшее число из списка значений
# numbers = [1, 6, 9, 10. - 3, -4, 5]
# print(numbers)
# print(numbers[3])
# print(f'мфксимум {max(numbers)}')
# print(f'мфксимум{min(numbers)}')

# min_value = numbers[0]
# max_value = numbers[0]

# for el in numbers:
#     print(el)
#     if el < min_value:
#         min_value=el
#     if el >max_value:
#         max_value=el

# print(f'максимум {max_value}')
# print(f'минимум {min_value}')

# -----
# семинар по ПРОГРАММИРОВАНИЮ 2
# Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

# number = int(input('Введите число: '))

# 9
# 1 2 3 4 5 6 7 8 9

# counter = 1
# while counter = 1
# print(counter)
# counter += 1


# for i in range(1, number+1, 2):
#     print(i, end=' ')

# def zadacha1():
#     number = int(input('Введите число'))

#     print('Цикл for:')
#     for i in range(1, number+1):
#         if number % i == 0:
#             if i % 2 == 0:
#                 print(f'{i} четное')
#             else:
#                 print(f'{i} нечетное')


# ???????? ниже не работает. Почему?
# def check(num):
#     if num % 2 == 0:
#         return 'четное'
#     else:
#         return 'нечетное'


# def zadacha1():
#     number = int(input('Введите число: '))

#     for i in range(1, number+1):
#         if number % i == 0:
#             print(f'{i} {check(i)}')
# # -----
# # Задача 1. Выведите таблицу истинности для выражения ¬X ∨Y.


# def zadacha2():
#     for x in range(0, 2):
#         for y in range(0, 2):
#             print(f'{x} {y} | {int(not(x) or y)}')
# # -----
# # Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа -определять количество вхождений одной строки в другую.
# # «qwe»«qwertyqwe»-> 2
