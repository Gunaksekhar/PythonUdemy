def blackjack(x, y, z):
    if sum([x,y,z]) <= 21:
        return sum([x,y,z])
    elif 11 in [x, y, z] and sum([x, y, z]) <= 31-10:
        return sum([x, y, z])
    else:
        return 'BUST'
rt = blackjack(10,8,3)
print(rt)