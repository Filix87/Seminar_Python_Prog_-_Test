# семинар по ПРОГРАММИРОВАНИЮ 3

import random
import string

# length = 7
# numbers = [0] * length
# for index in range(length):
#     numbers[index] = random.randint(0, 10)
# print(numbers)


# # ---------
def task1():
    length = 7
    numbers = [random.randint(0, 10) for el in range(length)]
    print(numbers)
    sum = 0
    for index in range(length):
        sum += numbers[index]
    print(f"Сумма всех элементов равни {sum}")
    if sum % 2 == 0:
        print("Сумма чётная")
    else:
        print("сумма нечетная")


# task1()
# ------
# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня.
# Определите в какой период выпало больше осадков:в первой или второй половине июня.
# Примечание: список заполняетсяслучайными числами от 0 до 25.
# def task2():
#     len = 30
#     numbers = [random.randint(0, 10) for i in range(len)]
#     print(numbers)
#     sum, sum2 = 0, 0
#     for index in range(15):
#         sum += numbers[index]
#     for index in range(15, len):
#         sum2 += numbers[index]
#     if sum2 < sum:
#         print(f"Осадков больше выпало во второй половине: {sum} - {sum2}")
#     else:
#         print(f"Осадков больше выпало в первой половине: {sum} - {sum2}")


# # task2()


def ili_drugoe_task2():
    days = 30
    numbers = [random.randint(0, 25) for _ in range(days)]
    f_part = numbers[:15]
    s_part = numbers[15:]
    print(numbers)
    print(f_part)
    print(s_part)
    f_sum = 0
    s_sum = 0
    for i in range(len(f_part)):
        f_sum += f_part[i]
        s_sum += s_part[i]
    print(f_sum)
    print(s_sum)
    if f_sum > s_sum:
        print("В первой половине больше осадков")
    elif s_sum > f_sum:
        print("Во второй половине больше осадков")
    else:
        print("одинаково осадков выпало")


# ili_drugoe_task2()

# Задача 2. Напишите программу, которая позволит пользователю заполнить анкету,
# последовательно вводя в программу:-имя;-возраст;-хобби;-любимое животное.
# После окончания ввода, выводится заполненная анкета.


def task3():
    dictionary = {}
    dictionary["name"] = input("Введите свое имя: ")
    dictionary["age"] = input("Введите свой возраст: ")
    dictionary["hobby"] = input("Введите свое хобби: ")
    dictionary["favorite_animal"] = input("Введите свое любимое животное: ")

    for k, v in dictionary.items():
        print(k + ":", v)


# task3()

# #-------------------
# # Задача 3. Напишите скрипт генератора паролей заданной длины,
# # состоящих из латинских букв и чисел.


def task4():
    def generate_pas(length):
        title = string.ascii_letters + string.digits
        password = " ".join(random.choice(title) for i in range(length))
        return password

    password = generate_pas(int(input("Введите количество символов для пароля: ")))
    print(password)


# task4()


# # ---------------------
# # Задача 4. Ручка стоит –5 рублей, карандаш –3 рубля, ластик –4 рубля.
# # Кассир последовательно вводит в программупозиции из чека «ручка»,«карандаш»,
# # «ластик».Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.


def task5():
    dict = {
        "ручка": 5,
        "карандаш": 3,
        "ластик": 4,
        "Ручка": 5,
        "Карандаш": 3,
        "Ластик": 4,
        "РУЧКА": 5,
        "КАРАНДАШ": 3,
        "ЛАСТИК": 4,
    }
    sum = 0
    flag = True
    while flag:
        code = input("Введите наименование товара: ")
        if code in dict:
            sum += dict[code]
        elif code == "стоп":
            flag = False
    print(sum)


# task5()

# # ---------------------------


# Семинар по ТЕСТИРОВАНИЮ 3
# разбор ДЗ (число: 3804578902)
def DZ1():
    n = int(input("Введите число: "))
    list_1 = [1, n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            list_1.append({i, n // i})
    print(list_1)


# DZ1()

# # ---------------------
# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


def task6():
    list_a = [1, 1, 2, 0, -1, 3, 4, 4]
    print(list_a)
    list_b = []
    for i in list_a:
        if i in list_b:
            pass
        else:
            list_b.append(i)
    print(list_b)


# task6()


def task6_2():
    list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
    print(f"Input: {list_1}")
    print(f"Output: {len(list(set(list_1)))} -> {list(set(list_1))}")


# task6_2()

# # ---------------
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


def task7():
    # -----------моё решение
    length = int(input("введите длину списка: "))
    k = int(input("введите число для сдвига: "))
    n = 0
    str = [random.randint(1, 10) for el in range(length)]
    n = str
    str = str[-k:] + str[:-k]
    print(f"{n} -> {str}")

    # task7()

    # --------------
    # Задача №21. Решение в группах
    # Напишите программу для печати всех уникальных
    # значений в словаре.
    # Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    # {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
    # {" VIII ":" S007 "}]
    # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


def task8():
    my_dict = {
        "V": "S001",
        "W": "S002",
        "VI": "S001",
        "X": "S005",
        "VII": "S005",
        "Y": "S009",
        "VIII": "S007",
    }
    col = []
    for i in my_dict:
        print(my_dict[i])
        col = col + [my_dict[i]]
    print(col)
    print(list(set(col)))


# task8()

# -----------------------------
# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


def task9():
    str = [0, -1, 5, 2, 3]
    count = 0
    for i in range(len(list(str))):
        if str[i] > str[i - 1]:
            count += 1
    print(count)


task9()
