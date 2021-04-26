import numpy as np


def print_with_indent(message, symbol):
    print(symbol * 10 + "  " + message + "  " + symbol * 10)


def print_error(message):
    print_with_indent(message, "!")


def read_section(message, symbol):
    print(message)
    values = []
    while not values:
        try:
            values = input().split(symbol)
            values = [float(i.strip()) for i in values]
            if len(values) != 2:
                print_error("Количество введенных значение некорректно, должно быть 2")
                values = []
            elif values[0] == values[1]:
                print_error("Левая граница не может равняться правой")
                values = []
        except ValueError:
            print_error("Введенные значения не числа")
            values = []
    if values[1] < values[0]:
        values.reverse()
    return values


def section_checker(function, left, right):
    for i in np.arange(left + 0.1, right, 0.1):
        if function(i) * function(i - 0.5) <= 0:
            return True
    return False


def choose_from_list(any_list):
    for i in range(len(any_list)):
        print(str(i) + ": \n" + any_list[i])
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
            print_error("Вводимое значение не является целым числом")
            continue
        if n < minimum:
            print_error("Вводимое значение не может быть меньше " + str(minimum))
        elif n > maximum:
            print_error("Вводимое значение не может быть больше " + str(maximum))
        else:
            return n


def read_float(minimum, maximum, message):
    while True:
        print(message)
        try:
            n = float(input().strip())
        except ValueError:
            print_error("Вводимое значение не является числом")
            continue
        if n < minimum:
            print_error("Вводимое значение не может быть меньше " + str(minimum))
        elif n > maximum:
            print_error("Вводимое значение не может быть больше " + str(maximum))
        else:
            return n
