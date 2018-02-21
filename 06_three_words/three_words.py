def checkio(words):
    count = 0
    for word in words.split(" "):
        if word.isalpha():
            count += 1
            if count == 3:
                print True
        else:
            count = 0
    print False


print "123 World hello"
checkio("123 World hello")
print "one nine 977 606 six three three 228 112"
checkio("one nine 977 606 six three three 228 112")
print "bla bla bla bla"
checkio("bla bla bla bla")
