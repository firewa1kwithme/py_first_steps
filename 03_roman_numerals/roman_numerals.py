def three(total, a, b, c, x):
    if x == 4:
        total.append(a + b)
    elif x == 9:
        total.append(a + c)
    elif x >= 5 and x < 9:
        total.append(b + a * (x - 5))
    else:
        total.append(a * x)

def checkio(data):
    total = []
    thousand = data // 1000
    hundreds = (data % 1000) // 100
    dozens = ((data % 1000) % 100) // 10
    units = (((data % 1000) % 100) % 10) // 1

    total.append('M' * thousand)
    three(total, 'C','D', 'M', hundreds)
    three(total, 'X','L', 'C', dozens)
    three(total, 'I', 'V', 'X', units)
    print ''.join(total)

def another(data):
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )

    result = []
    for d, r in coding:
        while data >= d:
            result.append(r)
            data -= d
    print ''.join(result)

print 'VI'
checkio(6)
another(6)
print 'LXXVI'
checkio(76)
another(76)
print 'CDXCIX'
checkio(499)
another(499)
print 'MMMDCCCLXXXVIII'
checkio(3888)
another(3888)