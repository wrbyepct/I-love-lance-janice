
test_word_should_return_encryption = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"


# Convert to the mirror character
def decrypt(c):
    # The ascii value that 'z' + 'a'
    # Also is 'y' + 'b'
    # Because whenever a character -1, other will + 1
    # this is like a "a + b = c" question
    # now c is 219
    # given a or b, return what value the other is
    measure_value = 219
    return chr(measure_value - ord(c))


def decipher(word):
    deciphered_text = ""
    for c in word:
        if c.islower():
            deciphered_text += decrypt(c)
        else:
            deciphered_text += c

    return deciphered_text


print(decipher(test_word_should_return_encryption))
