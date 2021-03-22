#########################################################################################
# Name:           Hasan Şenyurt
# Student ID:     64180008
# Department:     Computer Engineering
#
# Assignment ID:  A7
#########################################################################################
#########################################################################################
# QUESTION I
# Description: This program uses random library to generate random list.
#########################################################################################
print("SOLUTION OF QUESTION I:")
print("Generate a list of 200 random values in the range 1–99. Determine, print and remove duplicate values from the list.\n")

import random
list1 = list()
for i in range(200):
    list1.append(random.randint(1,99))
print("Original list:",list1)
list2 = set([x for x in list1 if list1.count(x)>1])
print("Duplicate Values:",list2)
list3 = set([a for a in list1 if list1.count(a)<2])
print("Without Duplicate Values:",list3)

#########################################################################################
# QUESTION II
# Description:This program uses math and random library. Main goal of this program is
# calculating average, standard deviation and correlation of lists.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:")
print("Write the missing functions myAverage, myStandardDev, myMin, and myCorrelation in the following code.\n")
import math
import random
def myAvearage(lst):
    result = 0
    for i in range(len(lst)):

        result += lst[i]
    return result/len(lst)
def myStandardDev(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    result1 = 0
    for j in range(len(lst)):
        result1 += math.pow(lst[j],2)
    return math.sqrt((result1 - ((math.pow(result,2))/len(lst)))/(len(lst)-1))


def myMin(lst):
    return min(lst)
def myCorrelation(x, y):
    numerator =0
    denominator1 =0
    denominator2 = 0
    for i in range(len(x)):
        numerator += (x[i] - myAvearage(x))*(y[i]-myAvearage(y))
    for j in range(len(x)):
        denominator1 += math.pow((x[j] - myAvearage(x)),2)
        denominator2 += math.pow((y[j] - myAvearage(y)),2)
    return numerator/math.sqrt(denominator1*denominator2)



def main():
    aList = [10, 20, 30, 50, 80, 90, 100, 15, 125, 128, 150, 185, 200, 240, 260, 280]
    bList = [13, 25, 28, 45, 79, 85, 111, 115, 125, 256, 160, 195, 230, 270, 280, 320]
    cList = bList.copy()
    cList.reverse()
    dList = [random.randint(1,99) for x in range(len(aList))]
    print("Lists:")
    print("List A = " + str(aList))
    print("List B = " + str(bList))
    print("List C = " + str(cList))
    print("List D = " + str(dList))
    print()

    print("List A Average = " + str(myAvearage(aList)))
    print("Standart Deviation of List A = " + str(myStandardDev(aList)))
    print("Minimum of List A = " + str(myMin(aList)))
    print()

    print("List B Average = " + str(myAvearage(bList)))
    print("Standart Deviation of List B = " + str(myStandardDev(bList)))
    print("Minimum of List B = " + str(myMin(bList)))
    print()

    print("Correlation of List A and B = " + str(myCorrelation(aList, bList)))
    print("Correlation of List A and C = " + str(myCorrelation(aList, cList)))
    print("Correlation of List A and D = " + str(myCorrelation(aList, dList)))
main()

#########################################################################################
# QUESTION III
# Description: This program uses random library to create a system which dices roll
# and give a result randomly values.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:")
print("Write a program that takes an integer argument n, and rolls 11 fair six-sided dice, n times. Use an integer\n\
array to tabulate the number of times each possible total (between 11 and 66) occurs.\n")

import random
dice = [1,2,3,4,5,6]
b = 0
sum = [x for x in range(11,67)]
h = list()
for j in range(1000):
    for i in range(11):
        a = dice[(random.randint(0,5))]
        b += a
    h.append(b)
    b = 0
for k in range(11,67):
    print(k,":",h.count(k)*"*")

