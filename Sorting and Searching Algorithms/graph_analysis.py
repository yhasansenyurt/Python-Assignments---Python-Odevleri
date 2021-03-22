#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A1
#########################################################################################

#########################################################################################
# QUESTION IV
# Description: This program draws graphs of some kind of datas.(search, sort, file datas.)
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:")
print("By using fileStats.txt and sortStats.txt, draw a multiple line chart as shown below. Draw bar chart graph for the searchStats.txt file.")


import matplotlib.pyplot as plt
import os


#################### FILESTATS #####################
list = []
read = []
file = open("fileStats.txt","r")
full_list = [1000,5000,10000,25000,50000,100000,200000]
a = 0

for Line in file:
    for i in Line.split(" ")[2::2]:
        if a <= 6:
            list.append(float(i))
        else:
            read.append(float(i))
        a +=1

print(list)
plt.plot(full_list,list)
plt.plot(full_list,read)
plt.legend(['y1 = Fill','y2 = Read'],loc='upper left')
plt.show()


#################### SEARCHSTATS #####################

file1 = open("searchStats.txt","r")
list1 = []
read1 = [0,50000,100000]

for line1 in file1:
    for i in line1.split(" ")[1:]:
        list1.append(float(i))
x_axis = ["Linear","Binary","Hash"]

plt.bar(x_axis,list1)
plt.axis([0,3,0,1])
plt.show()



#################### SORTSTATS #####################



file2 = open("sortStats.txt","r")
list2 = []
read2 = full_list

for line2 in file2:
    for i in line2.split(": ")[1:]:
        list2.append(i)

bubble = list2[0]
selection = list2[1]
insertion = list2[2]
shell = list2[3]
merge = list2[4]
quick = list2[5]
heap = list2[6]

#Creating float lists for each sorting algorithm.

list4 = []
for line3 in bubble.split(", "):
    list4.append(line3)
list4.remove("\n")
real_bubble = []
for i in range(len(list4)):
    real_bubble.append(float(list4[i]))

list5 = []
for line4 in selection.split(", "):
    list5.append(line4)
list5.remove("\n")
real_selection = []
for i in range(len(list5)):
    real_selection.append(float(list5[i]))

list6 = []
for line5 in insertion.split(", "):
    list6.append(line5)
list6.remove("\n")
real_insertion = []
for i in range(len(list6)):
    real_insertion.append(float(list6[i]))

list7 = []
for line6 in shell.split(", "):
    list7.append(line6)
list7.remove("\n")
real_shell = []
for i in range(len(list7)):
    real_shell.append(float(list7[i]))

list8 = []
for line7 in merge.split(", "):
    list8.append(line7)
list8.remove("\n")
real_merge = []
for i in range(len(list8)):
    real_merge.append(float(list8[i]))

list9 = []
for line8 in quick.split(", "):
    list9.append(line8)
list9.remove("\n")
real_quick = []
for i in range(len(list9)):
    real_quick.append(float(list9[i]))

list10 = []
for line9 in heap.split(", "):
    list10.append(line9)
list10.remove("")
real_heap = []
for i in range(len(list10)):
    real_heap.append(float(list10[i]))

plt.plot(full_list,real_bubble)
plt.plot(full_list,real_selection)
plt.plot(full_list,real_insertion)
plt.plot(full_list,real_shell)
plt.plot(full_list,real_merge)
plt.plot(full_list,real_quick)
plt.plot(full_list,real_heap)
plt.legend(['y1 = bubble','y2 = selection','y3 = insertion','y4 = shell','y5 = merge','y6 = quick','y7 = heap'],loc='upper left')
plt.show()

file.close()