def multiply(num):
    result = 1
    for numbers in num:
        result = result * numbers
    return result
mul = multiply([2, 3, 2, 1])
print(mul)