class name():

    institute = 'Grandalaya insttitute of thechnology'

    def __init__(self, education, course):

        self.myeducation = education
        self.mycourse = course
        print(self.myeducation)

    def myfunc(self):
        print("I choose {} institute for my better future".format(self.institute))

myname = name('civil', 'B.Tech')
print(myname.mycourse)
myname.myfunc()