#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A1
#########################################################################################

#########################################################################################
# QUESTION III
# Description: This program uses linear, hash and binary search to find random numbers in a list
# and calculates each one of their process.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:")
print("Perform a benchmark analysis of the following searching methods:")


import os
import random
import time

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


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


class HashTable:
    def __init__(self):
        self.size = 110017
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


def main():
    file = open(".filesForAssignment1file100000", "r")
    list = []
    random_list = []
    file2 = open("searchStats.txt","w")
    for i in file:
        list.append(int(i))
    a = quickSort(list)

    for i in range(1000):
        random_list.append(random.randint(0,100000))
    x = time.time()
    for i in range(1000):
        orderedSequentialSearch(a,random_list[i])

    b = time.time()
    print("Linear search time :",b-x)
    file2.write("Linear_Search " + str(b-x) + "\n")


    x = time.time()
    for j in range(1000):
        binary_search(a,random_list[j])
    b = time.time()
    print("Binary search time :",b-x)
    file2.write("Binary_Search " + str(b-x) + "\n")

    H = HashTable()
    for i in range(100000):
        H.put(i,list[i])
    time1 = time.time()
    for i in range(1000):
        H.get(random_list[i])
    time2 = time.time()
    print("Hashing time :", time2-time1)
    file2.write("Hashing " + str(time2-time1))
    file2.close()


main()

