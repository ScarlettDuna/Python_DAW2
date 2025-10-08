"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1
"""
def roman2integer(letter):
    match letter:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000


def solution(roman) -> int:
    # transform string to array
    letters = [letter for letter in roman]
    print(letters)
    # transform array's roman numerals to integers
    integers = list(map(roman2integer, letters))
    print(integers)
    # if int to the left smaller than the right, add -
    for i in range(len(integers)-1):
        if integers[i] < integers[i+1]:
            integers[i] *= -1
    # sum all integers in the array
    print(sum(integers))
    return sum(integers)

solution("XC")