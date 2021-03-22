#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A1
#########################################################################################


#########################################################################################
# QUESTION I
# Description: This program generates random numbers in a file and calculates the time of
# process.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION I:")
print("The objective of this question is to generate and read files that contain a list of random numbers.")

import random
import os
import time


def fillFile(fileSize, fileName):
    # Delete file if exists
    if os.path.exists(fileName):
        os.remove(fileName)
    # Open file
    FILE = open(fileName, "w")

    # Write to file
    for i in range(fileSize):
        r = random.randint(0, fileSize + 1000)
        FILE.write(str(r) + "\n")
    FILE.close()


def readFile(fileName):
    # Open file
    if os.path.exists(fileName):
        FILE = open(fileName, "r")
    else:
        print(fileName + " does not exist!")
        exit()

    # Read File
    alist = []
    for line in FILE:
        alist.append(int(line))

    FILE.close()

    return alist


def mainForFiles():
    # Dosyaları oluştur
    fileSizes = [1000, 5000, 10000, 25000, 50000, 100000, 200000]
    dirName = ".filesForAssignment1"

    # Delete fileStats.txt file if exists
    statFileName = "fileStats.txt"
    if os.path.exists(statFileName):
        os.remove(statFileName)

    # open stat file
    statFile = open(statFileName, "w")
    statFile.write("fillFile")

    print("WRITING TO FILES")

    for i in fileSizes:
        start = time.time()
        fillFile(i, dirName + "file" + str(i))
        finish = time.time()

        statFile.write("  " + str(finish - start))
        print("File Size = " + str(i) + "   Write Time = " + str(finish - start))

    statFile.write("\n")

    print("READING FILES")
    statFile.write("readFile")

    for i in fileSizes:
        fileName = dirName + "file" + str(i)

        # Dosyayı oku
        start = time.time()
        alist = readFile(fileName)
        finish = time.time()

        statFile.write("  " + str(finish - start))
        print("File Size = " + str(i) + "   Dosya Okuma Zamanı = " + str(finish - start))

    statFile.write("\n")
    statFile.close()


mainForFiles()