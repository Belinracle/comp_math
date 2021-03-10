import numpy as np


def section_checker(function, left, right):
    for i in np.arange(left + 0.1, right, 0.1):
        if function(i) * function(i - 0.5) <= 0:
            return True
    return False


def choose_from_list(any_list):
    for i in range(len(any_list)):
        print(str(i) + ": " + any_list[i])
    result = read_int(0, len(any_list) - 1, "Выберите пункт")
    return result


def choose_from_map(any_map):
    strings = []
    for elem in any_map:
        strings.append(elem[0])
    num = choose_from_list(strings)
    return num


def read_int(minimum, maximum, message):
    while True:
        print(message)
        try:
            n = int(input().strip())
        except ValueError:
            print("Вводимое значение не является целым числом")
            continue
        if n < minimum:
            print("Вводимое значение не может быть меньше " + str(minimum))
        elif n > maximum:
            print("Вводимое значение не может быть больше " + str(maximum))
        else:
            return n


def read_float(minimum, maximum, message):
    while True:
        print(message)
        try:
            n = float(input().strip())
        except ValueError:
            print("Вводимое значение не является числом")
            continue
        if n < minimum:
            print("Вводимое значение не может быть меньше " + str(minimum))
        elif n > maximum:
            print("Вводимое значение не может быть больше " + str(maximum))
        else:
            return n
