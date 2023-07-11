class android():

    #class object attribute
    #same for any instance of a class
    ani = 'animal'

    def __init__(self, mobiles, ios):
        self.anroid_mob = mobiles
        self.os = ios

    def sells(self):
        print("{}, iphone is the secuired mobile product".format(self.os))

users = android('Google Pixcel', 'Apple')
print(users.anroid_mob)
print(users.os)
print(users.ani)
print(users.sells())

print()

class country():
    p = 3.14

    def __init__(self, radius = 1):
        self.ar = radius*radius*country.p

use = country(3)
print(use.ar)
print(use.p)

print()

class sys():

    city = 'Chennai'

    def __init__(self, street, flat_no):

        self.atstreet = street
        self.flat = flat_no

    def city_name(self):
        print('i am from the city named {}'.format(self.city))

address = sys('Mukalmadavan street', 126)
print(address.city_name())
print(address.atstreet)
print(address.flat)