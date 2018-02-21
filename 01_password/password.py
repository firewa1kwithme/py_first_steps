def some_checkio(data):

    import re

    is_strong_len = len(data) >= 10
    is_strong_digit = re.search(r"\d", data) is not None
    is_strong_upper = re.search(r"[A-Z]", data) is not None
    is_strong_lower = re.search(r"[a-z]", data) is not None
    is_strong = is_strong_len and is_strong_digit and is_strong_upper and is_strong_lower
    return is_strong


def checkio(data):
    if len(data) >= 10 and (checkNum(data) == True) and (checkUpper(data) == True) and (checkLower(data) == True):
        print('True')
    else:
        print("False")


def checkNum(string):
    for i in string:
        if i.isdigit():
            return True
            #break
        else:
            continue


def checkUpper(string):
    for i in string:
        if i.isupper():
            return True
            # break
        else:
            continue


def checkLower(string):
    for i in string:
        if i.islower():
            return True
            # break
        else:
            continue

checkio("qkjn23R")
checkio("123")
checkio("qwerty")
checkio("qwerty123TY")