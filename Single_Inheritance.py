# Based on the Inheritance concept
class parents():

    def __init__(self, daughter, son):
        self.mydaughter = daughter
        self.myson = son

    def persons(self):
        print(self.mydaughter)
        print(self.myson)

class child(parents):

    def __int__(self, daughter, son, firstname):
        self.name = firstname
        self.mycity = city
        parents.__init__(self, daughter, son)

    def details(self):
        print('Firstname of malik is {}'.format('sabam'))
        print('Kaveri is belongs to {} city'.format('Hyderabad'))



family = child('kaveri', 'Malik')
family.persons()
family.details()