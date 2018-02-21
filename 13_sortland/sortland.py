import random


def random_citizens(k):

    people = [0]*k
    for i in range(k):
        people[i] = random.randint(1, 100)
    return people

# что с чем меняем местами
def sorting(n, arr):

    dArr = [(arr[i], i + 1) for i in range(n)]

    # с использованием лямбда-функции
    # dArr.sort(key=lambda tup: tup[0])
    # print(dArr)
    # return dArr[0][1], dArr[int((n - 1) / 2)][1], dArr[n - 1][1]

    # "в лоб"
    for j in range(1, n):
        i = j
        while (i > 0) and (dArr[i - 1][0] > dArr[i][0]):
            dArr[i - 1], dArr[i] = dArr[i], dArr[i - 1]
            print(dArr[i - 1][0], dArr[i][0])
            i -= 1
    print(dArr)
    return dArr[0][1], dArr[int((n - 1) / 2)][1], dArr[n - 1][1]

n = 5
arr = random_citizens(n)
print(arr)
c = sorting(n, arr)
print(c)
