# Урок 6. Повторение списков
# Задача 1. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.

# Решение задач:
# [7, 2, 4, 1, 6]–> да
# [7, 2, 4, 2, 6] -> нет

import random


# def task1():
#     numbers = [random.randint(1, 10) for _ in range(5)]
#     print(numbers)
#     n = set(numbers)
#     if len(n) != len(numbers):
#         print(f"элементы не уникальны")
#     else:
#         print(f"элементы уникальны")


# # task1()

# -------------------

# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.


# 72426, 27624 –> да
# 44444, 44441 -> нет
def task2():
    numbers_f = 72426
    numbers_s = 27624

    num_f_dict = dict([i, str(numbers_f).count(i)] for i in set(str(numbers_f)))
    print(num_f_dict)
    num_s_dict = dict([i, str(numbers_s).count(i)] for i in set(str(numbers_s)))
    print(num_s_dict)
    if num_f_dict == num_s_dict:
        print("наборы цифр одинаковы")
    else:
        print("наборы цифр не одинаковы")


# task2()

# ------------------------

# Задача 3. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких действий;
# в) Решите задачу средствами python.
# 2+2 => 41+2*3 => 7


def task3():
    # '2 + 2 - 1'
    # 2 + 2
    # 4 - 1

    expression = input("Введите выражение: ")
    expression = expression.replace("-", "+-")
    expression = expression.replace("/", "* 1/")
    print(expression)
    # 9 / 3 = 9 * 1/3

    if "+" in expression:
        expression = expression.split("+")
        print(int(expression[0]) + int(expression[1]))
    # elif '-' in expression:
    #     expression = expression.split('-')
    #     print(int(expression[0]) - int(expression[1]))
    elif "*" in expression:
        expression = expression.split("*")
        print(int(expression[0]) * float(expression[1]))
    # elif '/' in expression:
    #     expression = expression.split('/')
    #     print(int(expression[0]) / int(expression[1]))


# Не решенная задача.
# task3()

# ------------------------------

# Задача 4. Имеется 1000 рублей.
# Бык стоит –100 рублей, корова –50 рублей, телёнок –5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги,
# если всего надо купить 100 голов скота?


def task4():
    budget = 1000
    bull_price = 100
    cow_price = 50
    calf_price = 5
    bulls_count = budget // bull_price
    cow_count = budget // cow_price
    calf_count = budget // calf_price

    for bulls in range(bulls_count + 1):
        for cows in range(cow_count + 1):
            for calf in range(calf_count + 1):
                if (
                    bulls + cows + calf == 100
                    and bulls * bull_price + cows * cow_price + calf * calf_price
                    <= 1000
                    and bulls * bull_price + cows * cow_price + calf * calf_price >= 500
                ):
                    print(f"Быков: {bulls}; Коров: {cows}; Телят: {calf}")


task4()
