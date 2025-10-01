# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# "found the needle at position " plus the index it found the needle.
def find_needle(haystack):
    index = 0
    for item in haystack:
        if item == "needle":
            return "found the needle at position " + str(index)
        index += 1
    return index
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    match operator:
        case "+":
            return value1 + value2
            block
        case "-":
            return value1 - value2
            block
        case "*":
            return value1 * value2
            block
        case "/":
            return value1 / value2
            block