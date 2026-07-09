#--------------------------------------------------------------------------------------------------------
# 5. Write a program which accepts one number from the user and checks whether the number is prime or not.
#Input:5 Output: It is Prime Number
#-------------------------------------------------------------------------------------------------------
def CheckPrime(No):
    Count = 0
    for i in range(1, No + 1):
        if(No % i == 0):
            Count = Count + 1

    if(Count == 2):
        print("Prime Number")
    else:
        print("Not Prime")
        
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = CheckPrime(Num1)
   
    
if __name__ == "__main__":
    main()