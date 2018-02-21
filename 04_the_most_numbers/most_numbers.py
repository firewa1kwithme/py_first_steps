def checkio(args):
    if len(args) != 0:
        difference = max(args) - min(args)
        print difference
    else:
        return 0

test1 = [1, 2, 3]
print test1
checkio(test1)
test2 = [5, -5]
print test2
checkio(test2)
test3 = [10.2, -2.2, 0, 1.1, 0.5]
print test3
checkio(test3)
test4 = []
print test4
checkio(test4)
