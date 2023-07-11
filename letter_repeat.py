def letter_repeat(text):
    result = ' '
    for char in text:
        result += char*3
    return result

jack = letter_repeat('amitab ')
print(jack)