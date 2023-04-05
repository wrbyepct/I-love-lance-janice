
test_word_should_return_encryption = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"

'''
Problem type: 
    Converting problem

The gist of the problem:
    Converting english characters.
    [a..z] -> [z..a]
    Uppercase, and other symbols are ignored.

Input:
    Any length of string

Mainly concerned target:   
    Lowercase english characters

Goal:
    Make them mirror-converse.

Thinking thread:
    Fact 1:
        Because english character char is ASCII value in nature.
        E.g.
            a is 97
              .
              .
            z is 122

    Fact 2:
        The sum of the mirrored characters is always 219
        E.g.
            b(98) + y(121) = c(99) + x(120) = 219
    
    Fact 3:
        There are even number of english characters, which is 26

Conclusion:
    So you just use 219 to subtract one character 
    Then you will get the other character's value


Must do in order to achieve the goal:
    When checking a character
    There will only be 2 cases:
        1. Is lowercase
        2. Not lowercase
    These two cases must be covered    

-------------Definitions--------------

Text: String
encrypted_text: String
l: Int
i: Int
c: Char

convert(c):
    IF 
        c.islower -> c := chr(219 - ascii(c));  encrypted_text := encrypted_text + c
       ¬c.islower -> encrypted_text := encrypted_text + c
    FI  
---------------Steps-------------------

encrypted_text := ""
l := length(Text) 
i := 0

Loop condition                  Loop invariant 
{ i ≠ l   ∧   encrypted_text = ( sΣn | 0 ≤ n < i: convert(text[n]) )} NOTE: sΣ stands for "string sum" quantifier
                                                                            The identity element is empty string   
for c in Text:
    convert(c);
    i := i + 1

{  i = l ∧ encrypted_text = ( sΣn | 0 ≤ n < i: convert(text[n]) ) }

--------------------------------------

Complexity: Θ(n)

'''


# Convert to the mirror character
def decrypt(c):
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
