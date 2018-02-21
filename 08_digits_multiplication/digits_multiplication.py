def checkio(number):
    l = str(number).replace("0",'')
    multi = 1
    for i in l:
        if int(i) != 0:
            multi *= int(i)
    print multi

test1 = 123405
print test1
checkio(test1)
test2 = 999
print test2
checkio(test2)
test3 = 1000
print test3
checkio(test3)
test4 = 1111
print test4
checkio(test4)
