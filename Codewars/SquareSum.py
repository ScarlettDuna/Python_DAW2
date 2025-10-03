# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because
def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

print(square_sum([1, 2, 2]))
print(square_sum([0, 3, 4, 5]))

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)