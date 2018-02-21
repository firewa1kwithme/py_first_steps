import random


def random_citizens(k):

    people = [0]*k
    for i in range(k):
        people[i] = random.randint(1, 100)
    return people


def bubble_sort(n, arr):

    for j in range(k):
        while (j >= 0) and (arr[j - 1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

def insertion_sort(n, arr):
    
    for j in range(1, k):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] > key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr


def selection_sort(k, arr):

    for i in range(k):
        mini = i
        for j in range(i + 1, k):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]
    return arr


def shell_sort(k, arr):

    def half(k):
        i = int(k / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i/2.2))
            yield i

    for part in half(k):
        for i in range(part, k):
            for j in range(i, part - 1, -part):
                if arr[j - part] < arr[j]:
                    break
                arr[j], arr[j - part] = arr[j - part], arr[j]
    return arr


n = 5
array = random_citizens(n)
print(array)
a = bubble_sort(n, array)
b = insertion_sort(n, array)
c = selection_sort(n, array)
d = shell_sort(n, array)
print(a, b, c, d)
