def Reverse_String(sentences):

    words = sentences.split()
    lists = words[::-1]
    return ' '.join(lists)

order = Reverse_String('Update your skills day-to-day')
print(order)