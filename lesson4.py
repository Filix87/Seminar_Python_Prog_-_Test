# Урок 4. Словари, множества и профилирование

# СЕМИНАР ПО ПРОГРАММИРОВАНИЮ №4

# Задача 0. Создайте кортеж. Запишите в него 10 случайных чисел.
import random


def task1():
    numbers = tuple(random.randint(1, 10) for _ in range(10))

    print(numbers)


# task1()
# ---------------------
# Задача 1:
# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже
# по заданному индексу другим случайным числом.


def task2():
    numbers = tuple(random.randint(1, 10) for _ in range(10))

    print(numbers)

    i = int(input("введите индекс элемента для замены: "))
    n = random.randint(0, 100)

    list1 = list(numbers)
    list1[i] = n

    numbers = tuple(list1)
    print(numbers)


# task2()


def task2_2():
    def chenge_element(numbers, index):
        return numbers[:index] + (random.randint(1, 100),) + numbers[index + 1 :]

    numbers = tuple(random.randint(1, 100) for _ in range(10))
    index = 2
    print(numbers)
    numbers_new = chenge_element(numbers, index)
    print(numbers_new)


# task2_2()

# --------------------
# Задача 2:
# На вход подаются два числа.
# Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.


def calculate():
    num_f = 9
    num_s = 3

    summ, raznist, umnozhenie, delenie = calculate(num_f, num_s)
    print(summ, raznist, umnozhenie, delenie)  # не получается разобраться.....


# calculate()


# -----------------------

# Задача 3:
# 15 мин
# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов.
# Определите, сколько элементов было удалено.
# [1, 2, 9, 5, 2, 18, 3, 5, 13, 2] -> [1, 2, 9, 5, 18, 3, 13]
# Удалено элементов: 3


def task3():
    numbers = [random.randint(1, 20) for _ in range(10)]
    print(numbers)
    length = len(numbers)
    numbers = list(set(numbers))
    print(numbers)
    print(f"Элементов было удалено: {length - len(numbers)}")


# --------------------------

# task3()

# Задача 4. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные».
# На главную роль нужен актёр обладающий всеми тремя качествами.
# Определите, сколько есть претендентов на главную роль.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


def task3():
    krasivye = {
        "Илья",
        "Федор",
        "Семен",
        "Олег",
        "Лев",
        "Антон",
        "Артем",
        "Боря",
        "Стас",
        "Марк",
        "Ян",
    }
    umnye = {
        "Илья",
        "Георгий",
        "Лев",
        "Демьян",
        "Антон",
        "Владислав",
        "Боря",
        "Стас",
        "Марк",
        "Влад",
    }
    silnye = {
        "Федор",
        "Георгий",
        "Олег",
        "Демьян",
        "Артем",
        "Елисей",
        "Боря",
        "Стас",
        "Влад",
    }

    prytendenty = krasivye & umnye & silnye
    print(f"Aктеры обладающие всеми этими качествами -> {prytendenty}")


# task3()

# # ----------------------------------

# СЕМИНАР ПО ТЕСТИРОВАНИЮ №4

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#
# Для решения данной задачи используйте функцию .split()


def task4():
    st = "abc"
    i = 1
    h = ""
    for j in st:
        h = h + j + "_" + str(i)
        i += 1
    print(h)


# task4()


def task4_2():
    text = input("Введите строку: ").split()
    print(text)

    newText = set(text)
    text_a = text
    for i in newText:
        count = 0
        text_b = []
        for j in text_a:
            if j == i:
                text_b.append(i + "_" + str(count))
                count += 1
            else:
                text_b.append(j)
        text_a = text_b
    print(text_a)


# task4_2()


def task4_3():
    text = input("Введите строку: ").split()
    print(text)
    textDict = {1: "a", 2: "b", 3: "c", 4: "d"}
    text1 = " "
    for i in text:
        if i in textDict:
            text1 = text1 + i + "_" + str(textDict[i]) + " "
            textDict[i] = textDict[i] + 1
        else:
            text1 = text1 + i + " "
            textDict[i] = 1
    print(text1)


# task4_3()

# # -------------------

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


def task5():
    st = "she sells sea shells on the sea shore the shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper().split()
    print(st)
    list = set(st)
    print(list)
    print(len(list))


# task5()

# # -----------------------

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)

# # ------------ Разобрали какие ошибки были сделаны у Вани и Пети
