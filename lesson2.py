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
