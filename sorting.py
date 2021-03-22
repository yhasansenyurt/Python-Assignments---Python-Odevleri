#########################################################################################
# Name:           Hasan Şenyurt
# Student ID:     64180008
# Department:     Computer Engineering
#
# Assignment ID:  A8
#########################################################################################
#########################################################################################
# QUESTION I
# Description: This program provides that generate random numbers of each letter and
# shows them within a graph. In every button click, generates randomly again.
#########################################################################################
print("SOLUTION OF QUESTION I:Write a program that generates 1,000 lowercase letters randomly, counts the occurrence of each letter\n\
and displays a histogram for the occurrences.")
print("\n")

import random
from tkinter import *
list1 = list()

def buttonClick():
    list1.clear()
    canvas.delete("all")
    for i in range(1000):
        list1.append(chr(random.randint(97, 122)))

    x1 = 30
    y1 = 275
    x2 = 45
    y2 = y1 - list1.count(chr(97)) * 4
    letter = 98
    while True:
        canvas.create_text(x1+5,y1+5,text=chr(letter-1))
        canvas.create_rectangle(x1, y1, x2, y2)
        x1 += 15
        x2 += 15
        y2 = y1 - list1.count(chr(letter)) * 4
        letter += 1
        if letter == 124:
            break

window = Tk()
window.geometry("450x325")
canvas = Canvas(window)
canvas.place(height=400,width=500)
button = Button(window,text="Display Histogram",command=buttonClick)
button.place(x=175,y=290)
window.mainloop()

#########################################################################################
# QUESTION II
# Description: This program sorts lists with min function.
#########################################################################################
print("SOLUTION OF QUESTION II:Write the following function that sorts and merges two lists into a new sorted list:")
def merge(list1,list2):
    list4=[]
    list3 = list1+list2
    for i in range(0,len(list3)):
        list4.append(min(list3))
        list3.remove(min(list3))
    print(list4)
def main():
    list1 = [10,5,6,7]
    list2= [12,8,5,0,1]
    merge(list1,list2)

main()

#########################################################################################
# QUESTION III
# Description: This program sorts lists with bubble sort algorithm. But it can read only
# 8 numbers.
#########################################################################################
print()
print("SOLUTION OF QUESTION III:Write a Python program that read exactly 8 numbers. Use Bubble Sort algorithm to sort it.\n\
While sorting, display each iteration.")
a,b,c,d,e,f,g,h = eval(input("Enter 8 numbers with , (a,b,c,d...):"))
numbers = [a,b,c,d,e,f,g,h]

while True:
    for i in range(0,7):
        if numbers[i]>numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(numbers)

        else:
            print(numbers)
    if numbers[0]<=numbers[1] <= numbers[2]<=numbers[3] <= numbers[4]<=numbers[5] <= numbers[6]<=numbers[7]:
        break


#########################################################################################
# QUESTION V
# Description: This program uses parent and child classes to create triangle. Some
# properties of triangle comes from parent class.
#########################################################################################
print()
print("SOLUTION OF QUESTION V:Design a class named Triangle that extends the GeometricObject class.")

class GeometricObject():
    def __init__(self,fill,color):
        self.fill = fill
        self.color = color
    def getFill(self):
        if self.fill == 1:
            return ("filled")
        elif self.fill == 0:
            return("not filled")
        else:
            return("Filled input must be 1 or 0.")
    def getColor(self):
        return self.color

class Triangle(GeometricObject):
    def __init__(self, fill, color, side1 = 1, side2 = 1, side3 = 1):
        super().__init__(fill, color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getPerimeter(self):
        if self.side1 <= 0 or self.side2 <=0 or self.side3 <=0:
            raise RuntimeError("Sides cannot be zero or negative value.")
        else:
            return self.side1 + self.side2 +self.side3
    def getArea(self):
        x = self.getPerimeter()/2
        area = (x*(x-self.side1)*(x - self.side2)*(x - self.side3))**0.5
        if area <= 0:
            raise RuntimeError("\nThis triangle does not follow the sides rule!(side2-side1 < side3 < side2+side1).\n"
                   "Please enter suitable numbers.")
        else:
            return area
    def __str__(self):
        return "Triangle: Side1: "+str(self.side1)+" Side2: "+str(self.side2)+" Side3: "+str(self.side3)

def main():
    s1 = eval(input("Side1:"))
    s2 = eval(input("Side2:"))
    s3 = eval(input("Side3:"))
    color = input("Enter the color:")
    filled = eval(input("Filled -> 1 or not filled -> 0 :"))
    tri = Triangle(filled,color,s1,s2,s3)
    print()
    print(str(tri))
    print("Area of the triangle :",tri.getArea())
    print("Perimeter of the triangle :",tri.getPerimeter())
    print("Color :",tri.getColor())
    print("Filled or not :",tri.getFill())
main()

#########################################################################################
# QUESTION VI
# Description: This program uses dictionary to find keywords in python source code file.
#########################################################################################
print()
print("SOLUTION OF QUESTION VI:Write a program that reads in a Python source code file and counts the occurrence of each keyword and each\n\
identifier (variables, class and method names) in the file using two dictionaries: one for keywords and one for\n\
identifiers. Your program should prompt the user to enter the Python source code filename.")
print()
keywords= {"and":0,"as":0,"assert":0,"break":0,"class":0,"continue":0,"def":0,"del":0,"elif":0
    ,"else":0,"except":0,"False":0,"finally":0,"for":0,"from":0,"global":0,"if":0,"import":0
    ,"in":0,"is":0,"lambda":0,"None":0,"nonlocal":0,"not":0,"or":0,"pass":0,"raise":0,"return":0
    ,"True":0,"try":0,"while":0,"with":0,"yield":0}

identifiers = {}
file = input("Enter the .py location:")
openfile = open(file,"r")
finds = "="
for x in openfile:
    x = x.strip()
    text = x.split(" ")
    for word in text:
        if word in keywords:
            keywords[word] = keywords[word] + 1
        else:
            continue
print(keywords)
openfile.close()
