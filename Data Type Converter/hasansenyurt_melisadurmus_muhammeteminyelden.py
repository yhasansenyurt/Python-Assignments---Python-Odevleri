
'''
NAME: Hasan Senyurt - Melisa Durmus - Muhammet Emin Yelden
ID: 150120531 - 150119727 - 150119527

Purpose of the Program : This program takes 3 type input from .txt file. These types are signed integers
unsigned integers and float numbers. It takes them and converts to binary representation. After that it
converts binary to hexadecimal value. Every operation is used manually. No functions are 
used from other libraries.


'''
#it takes binary value and byte to convert hexadecimal.
def binaryToHex(binary,byte):
    hexadecimal = ""
    
    for i in range(0,byte*8,4):
        power = 3
        result = 0
        for j in range(0,4):
            result += int(binary[i+j])*(2**power)
            power -= 1
        if(result == 10):
            result = "A"
        elif(result == 11):
            result = "B"
        elif(result == 12):
            result = "C"
        elif(result == 13):
            result = "D"
        elif(result == 14):
            result = "E"
        elif(result == 15):
            result = "F"
        
        hexadecimal += str(result)
    return hexadecimal

#this function is for rounding or arranging fraction part of float value.
def roundFraction(fraction_binary,f_bits):
    
    #fraction_binary is fraction part of float number which represented by binary representation.
    #f_bits are bits that are used for fraction part of float number. (IEEE)
    rounded = ""
    
    #checking if there are less bits than f_bits.
    if(len(fraction_binary)< f_bits):   
        for i in range(0,len(fraction_binary)):
            rounded += fraction_binary[i]
        for i in range(len(rounded),f_bits):
            rounded+= "0"
        return rounded
    elif(len(fraction_binary) == f_bits):
        return fraction_binary
            
    #if there is no problem about amount of bits, now it is time to round fraction part according to byte.
    else:
        result = 0
        power = -1
        for i in range(0,f_bits -1):
            rounded += fraction_binary[i]
        for i in range(f_bits,len(fraction_binary)):
            result += int(fraction_binary[i])*(2**power)
            power -= 1
        if(result < 0.5):
            rounded += "0"
        else:
            rounded += "1"
        return rounded

#if number is denormalized, this function is used to convert it.
def denormalized(positive,exponentbit,binary_right,f_bits):
    sign = ""
    #checking sign.
    if(positive):
        sign = "0"
    else:
        sign = "1"
    
    #exponent binary will be all zero.
    exponentBinary = ""
    for i in range(0,exponentbit):
        exponentBinary += "0"
    fraction = ""
    
    #after the exponent part, fraction part will be filled with this algorithm.
    for i in range(2,len(binary_right)): #2 because E = 1 -bias -> bias = 3
        fraction += binary_right[i]
        
    fraction = roundFraction(fraction,f_bits)
    return sign + exponentBinary + fraction

#this function takes unsigned value turns into binary. after that converting to hexadecimal. it returns
#hexadecimal according to endian input.
def unsignedConvertion(number,endian):
    
    #converting to binary.
    binary = ""
    while(number != 0):
        if(number %2 == 1):
            binary += "1"
            number //= 2
        elif(number %2 == 0):
            binary += "0"
            number //= 2
    for i in range(len(binary),16):
        binary += "0"
    binary = binary[::-1]
    
    #converting to hexadecimal via function that is written manually.
    hexadecimal = binaryToHex(binary, 2)
    
    #checking endian input.
    if(endian == "Little Endian"):
        hexadecimal = hexadecimal[2] +  hexadecimal[3] + " "+ hexadecimal[0] + hexadecimal[1]
        return hexadecimal
    elif(endian == "Big Endian"):
        hexadecimal = hexadecimal[0] +  hexadecimal[1] + " "+ hexadecimal[2] + hexadecimal[3]
        return hexadecimal
    else:
        return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"
    
#this function takes signed value turns into binary. after that converting to hexadecimal.
#it returns hexadecimal according to endian input.
def signedConvertion(number,endian):
    
    #converting to binary.
    number = -1 * number
    binary = ""
    while(number != 0):
        if(number %2 == 1):
            binary += "0"
            number //= 2
        elif(number %2 == 0):
            binary += "1"
            number //= 2
    for i in range(len(binary),16):
        binary += "1"
    
    binary2 = list()
    #TWO'S COMPLEMENTATION.
    for i in binary:
        binary2.append(i)
    
    if(binary2[0] == "0"):
        binary2[0] = "1"
    else:
        for i in range(0,len(binary2)):
            if(binary2[i] != "0"):
                binary2[i] = "0"
            else:
                binary2[i] = "1"
                break
            
    binary2.reverse()
    #converting to hexadecimal via function that is written manually.
    hexadecimal = binaryToHex(binary2,2)
    
    #checking endian input.
    if(endian == "Little Endian"):
        hexadecimal = hexadecimal[2] +  hexadecimal[3] + " "+ hexadecimal[0] + hexadecimal[1]
        return hexadecimal
    elif(endian == "Big Endian"):
        hexadecimal = hexadecimal[0] +  hexadecimal[1] + " "+ hexadecimal[2] + hexadecimal[3]
        return hexadecimal
    else:
        return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"

#this function takes float number and turns into binary. after that turns into hexadecimal.
#it returns according to k and endian input. k is floating point size.
def floatConvertion(number,endian,k):
    
    #checking the sign of number.
    positive = True
    if(number < 0):
        positive = False
        number *= -1
    else:
        positive = True
    
    split = str(number).split(".")
    
    #spliting left and right part of float number.
    left = int(split[0])
    fraction = int(split[1])
    fraction = fraction*10**-(len(str(fraction)))
    
    binary_left = ""
    #binary rep. of left part.
    if(left == 0):
        binary_left = "0"
    else:
        while(left != 0):
            if(left %2 == 1):
                binary_left += "1"
                left //= 2
            elif(left %2 == 0):
                binary_left += "0"
                left //= 2
    binary_left = binary_left[::-1]
    
    #binary rep. of right part.
    binary_right = ""
    if(fraction == 0):
        binary_right = "0"
    while(fraction != 1):
        if(fraction == 1 or fraction == 0):
            break
        fraction *=2
        
        if(fraction < 1):
            binary_right += "0"
        else:
            binary_right += "1"
            fraction -= 1
    
    binary = binary_left + binary_right #binary part of all number.      
    exponent = len(binary_left) - 1 #finding exponent. (2^x) -> finding x
    fraction_binary = ""
    
    
    #fraction part of last shape of binary. (1.10100101001) finding number after the point(.)
    for i in range(1,len(binary)):
        fraction_binary += binary[i]
    rounded = ""
    exponentbit = 0
    
    #print(fraction_binary)
    #operations according to floating point size input.
    if(k == 1):
        
        try:
            #finding bias and exponent size.
            exponentbit = 3
            bias = 2**(exponentbit-1) - 1
            
            e = exponent + bias
            
            exponent_binary = ""
            lastBinary = ""
            #checking normalized or denormalized
            if(exponent == 0):
                lastBinary = denormalized(positive,exponentbit,binary_right,4)
                
            else:
            #finding exponent part (binary rep.)
                while(e != 0):
                    if(e %2 == 1):
                        exponent_binary += "1"
                        e //= 2
                    elif(e %2 == 0):
                        exponent_binary += "0"
                        e //= 2
                if(len(exponent_binary) < 3):
                    for i in range(0,3-len(exponent_binary)):
                        exponent_binary += "0"
                exponent_binary = exponent_binary[::-1]
                
                
                #rounding fraction part by using function that is written manually.
                rounded = roundFraction(fraction_binary,4)
                
                
                #importing sign numbers to last binary rep.
                if(positive):
                    lastBinary = "0" + exponent_binary + rounded
                else:
                    lastBinary = "1" + exponent_binary + rounded
        
            #turning into hex.
            hexadecimal = binaryToHex(lastBinary,1)
            return hexadecimal
            # if(endian == "Little Endian"):
            #     hexadecimal = hexadecimal[1] +  hexadecimal[0]
            #     return hexadecimal
            # elif(endian == "Big Endian"):
            #     hexadecimal = hexadecimal[0] +  hexadecimal[1]
            #     return hexadecimal
            # else:
            #     return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"
        except:
            return "Wrong byte Value"
        
    elif(k == 2):
        try:
            #finding bias and exponent size.
            exponentbit = 8
            bias = 2**(exponentbit-1) - 1
            
            e = exponent + bias
            exponent_binary = ""
            lastBinary = ""
            #checking normalized or denormalized
            if(exponent == 0):
                lastBinary = denormalized(positive,exponentbit,binary_right,7)
            else:
                #finding exponent part (binary rep.)
                while(e != 0):
                    if(e %2 == 1):
                        exponent_binary += "1"
                        e //= 2
                    elif(e %2 == 0):
                        exponent_binary += "0"
                        e //= 2
                if(len(exponent_binary) < 8):
                    for i in range(0,8-len(exponent_binary)):
                        exponent_binary += "0"
                exponent_binary = exponent_binary[::-1]
                
                #rounding fraction part by using function that is written manually.
                rounded = roundFraction(fraction_binary,7)
                
                
                #importing sign numbers to last binary rep.
                if(positive):
                    lastBinary = "0" + exponent_binary + rounded
                else:
                    lastBinary = "1" + exponent_binary + rounded
                
            #turning into hex.
            hexadecimal = binaryToHex(lastBinary,2)
            
            #checking endian input.
            if(endian == "Little Endian"):
                hexadecimal = hexadecimal[2] +  hexadecimal[3] + " "+ hexadecimal[0] + hexadecimal[1]
                return hexadecimal
            elif(endian == "Big Endian"):
                hexadecimal = hexadecimal[0] +  hexadecimal[1] + " "+ hexadecimal[2] + hexadecimal[3]
                return hexadecimal
            else:
                return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"
        except:
            return "Wrong byte Value"
                
    elif(k == 3):
        try:
            #finding bias and exponent size.
            exponentbit = 10
            bias = 2**(exponentbit-1) - 1
            
            e = exponent + bias
            exponent_binary = ""
            lastBinary = ""
            #checking normalized or denormalized
            if(exponent == 0):
                lastBinary = denormalized(positive,exponentbit,binary_right,13)
            else:
            
                #finding exponent part (binary rep.)
                while(e != 0):
                    if(e %2 == 1):
                        exponent_binary += "1"
                        e //= 2
                    elif(e %2 == 0):
                        exponent_binary += "0"
                        e //= 2
                if(len(exponent_binary) < 10):
                    for i in range(0,10-len(exponent_binary)):
                        exponent_binary += "0"
                exponent_binary = exponent_binary[::-1]
                
                #rounding fraction part by using function that is written manually.
                rounded = roundFraction(fraction_binary,13)
                
                
                #importing sign numbers to last binary rep.
                if(positive):
                    lastBinary = "0" + exponent_binary + rounded
                else:
                    lastBinary = "1" + exponent_binary + rounded
                    
                #turning into hex.
            hexadecimal = binaryToHex(lastBinary,3)
            
            #checking endian input.
            if(endian == "Little Endian"):
                hexadecimal = hexadecimal[4:6] + " " + hexadecimal[2:4] + " " + hexadecimal[0:2]
                return hexadecimal
            elif(endian == "Big Endian"):
                hexadecimal = hexadecimal[0:2] + " " + hexadecimal[2:4] + " " + hexadecimal[4:6]
                return hexadecimal
            else:
                return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"
        except:
            return "Wrong byte Value"
                
    elif(k == 4):
        try:
            #finding bias and exponent size.
            exponentbit = 12
            bias = 2**(exponentbit-1) - 1
            
            e = exponent + bias
            exponent_binary = ""
            lastBinary = ""
            #checking normalized or denormalized
            if(exponent == 0):
                lastBinary = denormalized(positive,exponentbit,binary_right,19)
            else:
                #finding exponent part (binary rep.)
                while(e != 0):
                    if(e %2 == 1):
                        exponent_binary += "1"
                        e //= 2
                    elif(e %2 == 0):
                        exponent_binary += "0"
                        e //= 2
                if(len(exponent_binary) < 12):
                    for i in range(0,12-len(exponent_binary)):
                        exponent_binary += "0"
                exponent_binary = exponent_binary[::-1]
                
                #rounding fraction part by using function that is written manually.
                rounded = roundFraction(fraction_binary,19)        
                
                
                #importing sign numbers to last binary rep.
                if(positive):
                    lastBinary = "0" + exponent_binary + rounded
                else:
                    lastBinary = "1" + exponent_binary + rounded
                    
                #turning into hex.
            hexadecimal = binaryToHex(lastBinary,4)
            
            #checking endian input.
            if(endian == "Little Endian"):
                hexadecimal = hexadecimal[6:8]+" "+hexadecimal[4:6]+" " +hexadecimal[2:4]+" "+hexadecimal[0:2]
                return hexadecimal
            elif(endian == "Big Endian"):
                hexadecimal = hexadecimal[0:2]+" "+hexadecimal[2:4]+ " "+hexadecimal[4:6]+" "+hexadecimal[6:8]
                return hexadecimal
            else:
                return "Wrong input. Please enter 'Little Endian' or 'Big Endian'"
        except:
            return "Wrong byte Value"
    else:
        return "Please enter byte value 1,2,3 or 4."
        

def main():
    file = open("input.txt","r")
    output = open("output.txt","w")
    items = list()
    for line in file:
        items.append(line.strip())
    
    endian = input("Byte Ordering: ")
    k = eval(input("Floating Point Size: "))
    
    for number in items:
        #checking type of number.
        Float = False
        Unsigned = False
        Signed = False
        #checking and arranging numbers.
        for i in range(0,len(number)):
            if(number[i] == "."):
                Float = True
                break
        for i in range(0,len(number)):
            if(number[i] == "u"):
                Unsigned = True
                break
            
        for i in range(0,len(number)):
            if(number[i] != "u" and number[i] != "."):
                Signed = True
            else:
                Signed = False
                break
        #main operations are called here according to the type of number.
        if(Unsigned):
            number = number[:-1]
            number = int(number)
            output.write(unsignedConvertion(number,endian)+"\n")
        elif(Signed):
            number = int(number)
            output.write(signedConvertion(number,endian)+"\n")
        elif(Float):
            number = float(number)
            output.write(floatConvertion(number,endian,k)+"\n")
    
    file.close()
main()