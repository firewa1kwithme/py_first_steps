def checkio(numbers_array):
    print sorted(numbers_array, key = abs)

def myCheck(numbers_array):
    numbers = list(numbers_array)
    for i in range(len(numbers) - 1):
        if abs(numbers[i]) >= abs(numbers[i + 1]):
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    print numbers

checkio((-20, -5, 10, 15))
myCheck((-20, -5, 10, 15))