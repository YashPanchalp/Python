#CREATE CLASS OF CIRCLE

class Circle:

    #R=TAKING THE DIMENTION
    def dimentions(self, radius):
        self.radius = radius

    #Calculating the Area
    def area(self):
        return (3.14)*(self.radius**2)
    
    #Calculating the Perimeter
    def peri(self):
        return 2*(3.14)*self.radius
    
#CREATING ANOTHER CLASS 
circle1=Circle()
circle1.dimentions(5)
print(f"The Radius Given : {circle1.radius} ")
print("The Area = ",circle1.area())
print("The Perimeter = ",circle1.peri())