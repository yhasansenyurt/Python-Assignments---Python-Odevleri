#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A5
#########################################################################################
#########################################################################################
# QUESTION I
# Description: This program converts milliseconds to hours,minutes and seconds with using
# operands.
#########################################################################################
print("SOLUTION OF QUESTION I:")
print("Write a function that con- verts milliseconds to hours, minutes, and seconds:")
def convertMillis(ms):
    ms = int(input("Enter a value(ms): "))
    s = (ms//1000)%60
    m = (ms//60000)%60
    h = (ms//3600000)
    print(str(h) + ":" + str(m)+ ":"+str(s))
convertMillis("ms")

#########################################################################################
# QUESTION II
# Description: This program uses class and functions to create two objects which are fans.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:")
print("Write a test program that creates two Fan objects. For the first object, assign the maximum speed,\n\
radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the\n\
second object. Display each object’s speed, radius, color, and on properties.")
class Fan:

    def __init__(self, speed=3, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

        if speed == 1:
           self.__speed = "Fast"
        elif speed == 2:
           self.__speed = "Medium"
        elif speed == 3:
           self.__speed = "Slow"



    def getSpeed(self):
        return self.__speed
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def getOn(self):
        return self.__on


def main():
    f1 = Fan(speed=1,radius=10,color="yellow",on=True)

    f2 = Fan(speed=2,radius=5,color="blue",on=False)
    print("Fan1 Speed:",f1.getSpeed(),"\nFan1 Radius:",f1.getRadius(),"\nFan1 Color:",f1.getColor(),"\nFan1 Power:",f1.getOn(),"\n")
    print("Fan2 Speed:",f2.getSpeed(),"\nFan2 Radius:",f2.getRadius(),"\nFan2 Color:",f2.getColor(),"\nFan2 Power:",f2.getOn())
main()




#########################################################################################
# QUESTION III
# Description: This program includes operands,classes and functions to solve linear equation.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:")
print("Write a test program that prompts the user to enter a, b, c, d, e, and f and displays the result.")
class LinearEquation:

    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f


    def geta(self):
        return self.a
    def getb(self):
        return self.b
    def getc(self):
        return self.c
    def getd(self):
        return self.d
    def gete(self):
        return self.e
    def getf(self):
        return self.f
    def isSolvable(self):
        if self.a*self.d - self.b*self.c != 0:
            return True
    def getX(self):
        if self.isSolvable() == True:
            return((self.e*self.d - self.b*self.f)/(self.a*self.d - self.b*self.c))
        else:

            return("The equation has no solution.")

    def getY(self):
        if self.isSolvable() == True:
            return ((self.a*self.f - self.e*self.c)/(self.a*self.d - self.b*self.c))
        else:
            return("a".strip("a"))





def main():
    a,b,c,d,e,f = eval(input("Enter the numbers(a,b,c,d,e,f): "))
    result = LinearEquation(a,b,c,d,e,f)
    if result.isSolvable() == True:
        print("x:",result.getX(),"\ny:",result.getY())
    else:
        print(result.getX())


main()



#########################################################################################
# QUESTION IV
# Description: This program uses discriminant to find root of equations.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:")
print("Write a test program that prompts the user to enter values for a, b, and c and displays the result based\n\
on the discriminant. If the discriminant is positive, display the two roots. If the discriminant is 0, display\n\
the one root. Otherwise, display “The equation has no roots.”")

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getDiscriminant(self):
        return ((self.b)**2 ) - (4*(self.a*self.c))
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return ("The equation has no roots.")
        elif self.getDiscriminant() ==0:
            return (-self.b + ((self.b ** 2) - (4 * self.a * self.c)) ** 0.5) / (2 * self.a)
        else:
            return (-self.b + ((self.b**2)-(4*self.a*self.c))**0.5)/(2*self.a)

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return ("a".strip("a"))
        elif self.getDiscriminant() ==0:
            return ("a".strip("a"))
        else:
            return (-self.b - ((self.b**2)-(4*self.a*self.c))**0.5)/(2*self.a)

def main():
    a,b,c = eval(input("Enter the numbers(a,b,c): "))
    x = QuadraticEquation(a,b,c)
    if x.getDiscriminant() < 0:
        print(x.getRoot1())
    elif x.getDiscriminant() ==0:
        print("The root is",x.getRoot1())
    else:
        print("The roots are",x.getRoot1(),"and",x.getRoot2())

main()

