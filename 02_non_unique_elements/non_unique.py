def checkio(data):
    for i in data:
        if data.count(i) == 1:
            data.remove(i)
    print data

def myCheckio(data):
    newList = []
    for i in data:
        if data.count(i) > 1:
            newList.append(i)
    print newList

checkio([1, 2, 3, 1, 3])
myCheckio([1, 2, 3, 1, 3])