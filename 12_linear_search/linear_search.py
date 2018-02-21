import random

# ! возвращает рандомное число number и последовательность рандомных чисел numbers
def numbers_simulation(n):

    numbers = [0]*n
    for i in range(n):
        numbers[i] = random.randint(0, 5)

    number = random.randint(0, 5)
    return numbers, number

# ! выполняет линейный поиск
def linear_search(arr, v):

    for i in range(0, len(arr)):
        if arr[i] == v:
            return i
    return 'NIL'


n = 10
numbers, number = numbers_simulation(n)
result = linear_search(numbers, number)
print(result)
