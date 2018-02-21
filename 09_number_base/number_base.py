def CharToNumber(x):
    if x.isdigit():
        return int(x)
    else:
        return ord(x) - 55

def checkio(str_number, radix):
    position = 0
    result = 0
    for char in str_number[::-1]:
        number = CharToNumber(char)
        if number > radix:
            return -1
        else:
            result += number * radix ** position
            position += 1
    return result



print checkio('AF', 16)
print checkio('101', 2)
