def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

intgers = almost_there(107)
print(intgers)