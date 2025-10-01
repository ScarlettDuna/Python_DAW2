"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""
def get_count(sentence):
    counter = 0
    for letter in sentence:
        if ((letter == "a") or (letter == "e") or (letter == "i") or (letter == "o") or (letter == "u")):
            counter += 1
    return counter

"""def getCount(s):
    return sum(c in 'aeiou' for c in s)
"""