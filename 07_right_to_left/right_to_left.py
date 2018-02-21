def left_join(phrases):
    text = ','.join(phrases)
    text = text.replace("right", "left")
    print text

test1 = ("left", "right", "left", "stop")
print test1
left_join(test1)
test2 = ("bright aright", "ok")
print test2
left_join(test2)
test3 = ("brightness wright",)
print test3
left_join(test3)
test4 = ("enough", "jokes")
print test4
left_join(test4)
