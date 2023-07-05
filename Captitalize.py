def old_macdonald(donaldoo):
    Brand = donaldoo[0]
    logo = donaldoo[1:3]
    Publicity = donaldoo[3]
    advertisement = donaldoo[4:]

    return Brand.upper() + logo + Publicity.upper() + advertisement

food = old_macdonald('macdonald')
print(food)