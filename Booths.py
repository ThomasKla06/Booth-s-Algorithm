#takes in a number and return a string containing its binary representation as an 8 bit signed number
def toBinary(num):
    binaryNum = ""
    neg = False

    #detect negative numbers
    if num < 0:
        neg = True
        num = abs(num)

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
        binaryNum = twosComplement(binaryNum)

    return binaryNum

# takes two binary strings and returns a string that is the binary representation of their sum
def add(num, addTo):
    carry = "0"
    newNum = ""
    size = len(num)
    for i in range(size):
        if num[size - 1 - i] == "0" and addTo[size - 1 - i] == "0" and carry == "0":
            newNum = "0" + newNum
            carry = "0"
        elif num[size - 1 - i] == "1" and addTo[size - 1 - i] == "0" and carry == "0":
            newNum = "1" + newNum
            carry = "0"
        elif num[size - 1 - i] == "1" and addTo[size - 1 - i] == "1" and carry == "0":
            newNum = "0" + newNum
            carry = "1"
        elif num[size - 1 - i] == "1" and addTo[size - 1 - i] == "0" and carry == "1":
            newNum = "0" + newNum
            carry = "1"
        elif num[size - 1 - i] == "1" and addTo[size - 1 - i] == "1" and carry == "1":
            newNum = "1" + newNum
            carry = "1"
        elif num[size - 1 - i] == "0" and addTo[size - 1 - i] == "1" and carry == "0":
            newNum = "1" + newNum
            carry = "0"
        elif num[size - 1 - i] == "0" and addTo[size - 1 - i] == "1" and carry == "1":
            newNum = "0" + newNum
            carry = "1"
        elif num[size - 1 - i] == "0" and addTo[size - 1 - i] == "0" and carry == "1":
            newNum = "1" + newNum
            carry = "0"
    return newNum

# converts a positive binary number to its twos complement negative version
def twosComplement(num):
    negativeNum =""
    for i in range(len(num)):
        if num[i] == "1":
            negativeNum += "0"
        elif num[i] == "0":
            negativeNum += "1"
    negativeNum = add(negativeNum, "00000001")
    return negativeNum


def main():
    num = input("Please enter a number between -128 and +127\n")
    num2 = input("Please enter a second number between -128 and +127\n")
    try:
        num = int(num)
        num2 = int(num2)
    except ValueError:
        print("Please enter a number")
        return 
    if num > 127 or num < -128 or num2 > 127 or num2 < -128:
        print(f"{num} or {num2} is not a valid number")
    else:
        print(f"{num} and {num2} are valid numbers")
        newNum = toBinary(num)
        newNum2 = toBinary(num2)
        print(f"{num} in binary with 8 bits is {newNum}")
        print(f"{num2} in binary with 8 bits is {newNum2}")
        print(f"Adding {num2} to {num}...")
        num3 = add(newNum, newNum2)
        print(f"{num} and {num2} added together is {num3} in binary")


main()