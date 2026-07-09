#--------------------------------------------------------------------------------------------------------
# 4. Write a program which accepts one number from the user and returns the addition of its factors.
#Input: 12    Output: 16    (1 + 2 + 3 + 4 + 6)
#-------------------------------------------------------------------------------------------------------
def SumFactorial(No):
    Sum = 0
    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i

    return Sum
        
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = SumFactorial(Num1)
    print("Factorial is :" , Ret)
    
if __name__ == "__main__":
    main()