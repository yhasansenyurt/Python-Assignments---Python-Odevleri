#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A1
#########################################################################################

#########################################################################################
# QUESTION II
# Description: This program sorts numbers which have quantity 1000,5000,10000,25000,50000,100000,200000
# and calculates the each time of sorting algorithms.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:")
print("Perform a benchmark analysis of the following sorting algorithms:")


import os
import time

def bubbleSort(file):
    passorNot = True
    while passorNot:
        passorNot = False
        for i in range(len(file) - 1):
            if file[i] > file[i+1]:
                t = file[i]
                file[i] = file[i+1]
                file[i+1] = t
                passorNot = True
    print("Bubble =",file)

def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin, currentMinIndex = lst[i], i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin, currentMinIndex = lst[j], j

        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin


def insertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[0..i-1] so that
        #   lst[0..i] is sorted.
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement



def mergeSort(list):
    if len(list) > 1:
        # Merge sort the first half
        firstHalf = list[: len(list) // 2]
        mergeSort(firstHalf)

        # Merge sort the second half
        secondHalf = list[len(list) // 2:]
        mergeSort(secondHalf)

        # Merge firstHalf with secondHalf into list
        merge(firstHalf, secondHalf, list)


# Merge two sorted lists */
def merge(list1, list2, temp):
    current1 = 0  # Current index in list1
    current2 = 0  # Current index in list2
    current3 = 0  # Current index in temp

    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current3 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1


def quickSort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quickSort(x[:i])
        second_part = quickSort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part



def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    print("Heap =",arr)
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)



      sublistcount = sublistcount // 2
    print("Shell =",alist)

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue



def main():
    file_list= [".filesForAssignment1file1000",".filesForAssignment1file5000",".filesForAssignment1file10000",".filesForAssignment1file25000"
                ,".filesForAssignment1file50000",".filesForAssignment1file100000",".filesForAssignment1file200000"]
    bubble_sortStats = []
    selection_sortStats = []
    insertion_sortStats = []
    shell_sortStats = []
    merge_sortStats= []
    quick_sortStats = []
    heap_sortStats = []
    sort_file = open("sortStats.txt", "w")
    for i in range(7):
        file = open(file_list[i], "r")
        list = []
        for i in file:
            list.append(int(i))
        a = time.time()
        bubbleSort(list)
        b = time.time()
        bubble_sortStats.append(b-a)
    sort_file.write("Bubble :" + " ")
    for i in range(7):
        sort_file.write(str(bubble_sortStats[i]) + ", ")
    sort_file.write("\n")


    for i in range(7):
        file1 = open(file_list[i], "r")
        list1 = []
        for j in file1:
            list1.append(int(j))
        a = time.time()
        selectionSort(list1)
        b = time.time()
        selection_sortStats.append(b-a)
        print("Selection =", list1)
    sort_file.write("Selection :" + " ")
    for i in range(7):
        sort_file.write(str(selection_sortStats[i])+ ", ")
    sort_file.write("\n")



    for i in range(7):
        file2 = open(file_list[i], "r")
        list2 = []
        for k in file2:
            list2.append(int(k))
        a = time.time()
        insertionSort(list2)
        b = time.time()
        insertion_sortStats.append(b-a)
        print("Insertion =",list2)
    sort_file.write("Insertion :"+ " ")
    for i in range(7):
        sort_file.write(str(insertion_sortStats[i])+ ", ")
    sort_file.write("\n")


    for i in range(7):
        file6 = open(file_list[i], "r")
        list6 = []
        for b in file6:
            list6.append(int(b))
        a = time.time()
        shellSort(list6)
        b = time.time()
        shell_sortStats.append(b-a)
    sort_file.write("Shell :" + " ")
    for i in range(7):
        sort_file.write(str(shell_sortStats[i])+", ")
    sort_file.write("\n")



    for i in range(7):
        file3 = open(file_list[i], "r")
        list3 = []
        for m in file3:
            list3.append(int(m))
        a = time.time()
        mergeSort(list3)
        b = time.time()
        merge_sortStats.append(b-a)
        print("Merge =",list3)
    sort_file.write("Merge :" + " ")
    for i in range(7):
        sort_file.write(str(merge_sortStats[i])+", ")
    sort_file.write("\n")

    for i in range(7):
        file4 = open(file_list[i], "r")
        list4 = []
        for n in file4:
            list4.append(int(n))
        a = time.time()
        print("Quick =",quickSort(list4))
        b = time.time()
        quick_sortStats.append(b-a)
    sort_file.write("Quick:" + " ")
    for i in range(7):
        sort_file.write(str(quick_sortStats[i])+", ")
    sort_file.write("\n")

    for i in range(7):
        file5 = open(file_list[i], "r")
        list5 = []
        for a in file5:
            list5.append(int(a))
        a = time.time()
        heapSort(list5)
        b = time.time()
        heap_sortStats.append(b-a)
    sort_file.write("Heap :"+ " ")
    for i in range(7):
        sort_file.write(str(heap_sortStats[i])+ ", ")


main()