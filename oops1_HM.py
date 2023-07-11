class cylinder():

    pi = 3.14

    def __init__(self,height = 2, radius = 2):
        self.height = height
        self.radius = radius

    def volume(self):
        print('volume of cylinder:' , self.pi*self.radius**2*self.height)

    def surface_area(self):
        print('surface area of cylinder:', 2*self.pi*self.radius*self.height + self.pi*self.radius**2*self.height)
cyl = cylinder()
cyl.volume()
cyl.surface_area()
