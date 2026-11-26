import math

#takes in a number and return a string containing its binary representation as an 8 bit signed number
def toBinary(num):
    binaryNum = ""
    neg = False

    #detect negative numbers
    if num < 0:
        neg = True
        num = math.Abs(num)

    #edge case
    if num == 0:
        return "00000000"

    while(num > 0):
        if num % 2 == 1:    
            binaryNum = "1" + binaryNum
            num -= 1 
        else:
            binaryNum = "0" + binaryNum
        num /= 2
    for i in range(8 - len(binaryNum)):
        binaryNum = "0" + binaryNum
    if neg:
        binaryNum = twosCompliment(binaryNum)

    return binaryNum
        
def twosCompliment(num):
    negativeNum =""

    return negativeNum


def main():
    num = input("Please enter a number between -128 and +127\n")
    try:
        num = int(num)
    except ValueError:
        print("Please enter a number")
        return 
    if num > 127 or num < -128:
        print(f"{num} is not a valid number")
    else:
        print(f"{num} is a valid number")
        newNum = toBinary(num)
        print(f"{num} in binary with 8 bits is {newNum}")


main()