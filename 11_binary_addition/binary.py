import random


def sum_of_binary_numbers(n, arr_a, arr_b):
    # ! красивый и короткий способ
    arr_c = int(arr_a, 2) + int(arr_b, 2)
    return bin(arr_c)

    # ! топорный способ "в лоб"
    # arr_c = [0]*(n + 1)
    # carry = 0
    # for i in range(n - 1, -1, -1):
    #         arr_c[i] = (int(arr_a[i]) + int(arr_b[i]) + carry) % 2
    #         carry = (int(arr_a[i]) + int(arr_b[i]) + carry) // 2
    # arr_c[n] = carry
    # return arr_c


# ! возвращает два рандомных двоичных числа длины n
def random_binary_num(n):

    arr_a = [0]*n
    arr_b = [0]*n
    for i in range(n - 1):
        arr_a[i] = random.randint(0, 1)
        arr_b[i] = random.randint(0, 1)

    return ''.join(str(i) for i in arr_a), ''.join(str(i) for i in arr_b)

# ! открываем файлик и записываем рандомные двоичные числа нужной длины n
n = 8
a, b = random_binary_num(n)
file_numbers = open("input.txt", 'w')
file_numbers.write(str(a) + '\n' + str(b))
file_numbers.close()


# ! считываем из файла два заданных числа и считаем их сумму
def reading_from_file(file_name):
    with open(file_name) as file:
        array = [row.strip() for row in file]
        a = array[0]
        b = array[1]
        n = len(a)
    c = sum_of_binary_numbers(n, a, b)
    print(c)


reading_from_file("input.txt")
