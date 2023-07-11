def summer_69(num):

    total = 0
    add = True

    for arr in num:
        while add:
            if arr!= 6:
                total += arr
                break
            else:
                add = False
        while not add:
            if arr != 9:
                break
            else:
                add = True
                break
    return total

baag = sum([4, 5, 6, 7, 8, 9])
print(baag)