def find_message(text):
    """Find a secret message"""
    message = []

    for letter in text:

        if letter.istitle() == True:
            message.append(letter[0])
        else:
            pass

    print ''.join(message)


print "How are you? Eh, ok. Low or Lower? Ohhh."
message = find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
print "HELLO WORLD!!!"
message = find_message("HELLO WORLD!!!")
