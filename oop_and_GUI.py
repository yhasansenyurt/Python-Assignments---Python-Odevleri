#########################################################################################
# Name:           Hasan Şenyurt
# Student ID:     64180008
# Department:     Computer Engineering
#
# Assignment ID:  A6
#########################################################################################
#########################################################################################
# QUESTION I
# Description: This program includes Rectangle Class which contains width,height,area and
# perimeter.Also to find area and perimeter, it uses math operations.
#########################################################################################
print("SOLUTION OF QUESTION I:")
print("Write a test program that creates two Rectangle objects—one with width 4 and height 40 and the other\n\
with width 3.5 and height 35.7.")
print("")
class Rectangle:
    def __init__(self,width=1.0,height=2.0):
        self.width = width
        self.height=height

    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return self.width*2 + self.height*2

def main():
    result1 = Rectangle(4,40)
    result2= Rectangle(3.5,35.7)
    print("Rectangle 1")
    print("-----------")
    print("Width:",result1.width,"Height:",result1.height,"\nArea:",result1.getArea(),"Perimeter:",result1.getPerimeter())
    print("\nRectangle 2")
    print("-----------")
    print("Width:",result2.width,"Height:",result2.height,"\nArea:","{0:.2f}".format(result2.getArea()),"Perimeter:",result2.getPerimeter())
main()

#########################################################################################
# QUESTION II
# Description: This program creates a stock object and its properties.Also uses percentage
# operation for change in price.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:")
print("Write a test program that creates a Stock object with the stock symbol INTC, the name Intel Corporation,\n\
the previous closing price of 20.5, and the new current price of 20.35, and display the price-change percentage.")
print("")
class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getPrev(self):
        return self.__previousClosingPrice
    def getCurrent(self):
        return self.__currentPrice
    def setPrev(self,previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    def setCurrent(self,currentPrice):
        self.__currentPrice = currentPrice

    def getChangePercent(self):
        return 100 - (100*self.__currentPrice/self.__previousClosingPrice)


def main():
    stock= Stock(symbol="INTC",name="Intel Corporation",previousClosingPrice=20.5,currentPrice=20.35)
    print("Symbol:",stock.getSymbol(),"\nName:",stock.getName(),"\nPrevious Closing Price:",stock.getPrev(),"\nCurrent Price:",
          stock.getCurrent(),"\nPrice-change Percentage: %","{0:.2f}".format(stock.getChangePercent()),"decrease")
main()

#########################################################################################
# QUESTION III
# Description: This program uses while loop to compare two strings' letters.Every letter
# has a number in string. It uses this property.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:")
print("Write a method that returns the longest common prefix of two strings.")
def prefix(s1,s2):

    a = 0
    b = 0
    if s1[0] != s2[0]:
        print("")
    else:
        print("Longest common prefix is:", end=" ")
    while True:
        if s1[a] == s2[b]:
            print(s1[a], end="")
        else:
            break
        if len(s1) == 1 or len(s2) == 1:
            break
        a += 1
        b += 1

def main():
    s1 = str(input("Enter a string:"))
    s2 = str(input("Enter a string:"))
    prefix(s1,s2)

main()

#########################################################################################
# QUESTION IV
# Description: This program contains tkinter library to use graphical user interface.
# Main goal of this program is calculate the assessment value and property tax according
# to user's input.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:")
print("Write a GUI program that displays the assessment value and property tax when a user enters the actual\n\
value of a property.")
from tkinter import *
class Property:

    def __init__(self,window):
        self.window = window
        self.entry = StringVar()
        window.geometry("210x85")
        self.l1 = Label(window, text="Enter the property value: $")
        self.l1.place(x=0, y=0)
        self.value = StringVar()
        self.tax = StringVar()
        self.l2 = Label(window, text="Assessment Value:")
        self.l2.place(x=48, y=20)
        self.l3 = Label(window, text="Property Tax:")
        self.l3.place(x=65, y=40)
        Label(window, textvariable=self.value).place(x=157, y=20)
        Label(window, textvariable=self.tax).place(x=147, y=40)
        self.l4 = Label(window,text="")
        self.l4.place(x=148,y=20)
        self.l5 = Label(window,text="")
        self.l5.place(x=137, y=40)
        self.b1 = Button(window, text="Calculate",command=self.computeValueandTax)
        self.b1.place(x=55, y=60)
        self.b2 = Button(window, text="Quit",command=self.getQuit())
        self.b2.place(x=115, y=60)
        self.e1 = Entry(window,textvariable=self.entry)
        self.e1.place(x=145, y=0)

    def getQuit(self):
        return self.window.quit
    def computeValueandTax(self):
        self.f = float(self.entry.get())*3/5
        self.value.set("{0:.1f}".format(self.f))
        self.t = (self.f*3/400)
        self.tax.set("{0:.2f}".format(self.t))
        self.l4.configure(text="$")
        self.l5.configure(text="$")
def main():
    window1 = Tk()
    result = Property(window1)
    window1.mainloop()
main()


