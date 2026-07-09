#---------------------------------------------------------------------------------------------------------
#Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all prime numbers 
# from that List.
#The main Python file accepts N numbers from the user and passes each number to the ChkPrime() function, which is a part of the user-defined module named MarvellousNum. The name of the function in the main Python file should be ListPrime().
#Input    Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output     Addition of prime numbers is : 54
#--------------------------------------------------------------------------------------------------------------------------
import MarvellousNum

def ListPrime(Data):

    Sum = 0

    for no in Data:
        if MarvellousNum.ChkPrime(no):
            Sum = Sum + no

    return Sum

def main():

    Arr = []

    print("Enter number of elements:")
    Size = int(input())

    print("Enter elements:")
    for i in range(Size):
        Arr.append(int(input()))

    Ans = ListPrime(Arr)

    print("Addition of prime numbers is:", Ans)

if __name__ == "__main__":
    main()