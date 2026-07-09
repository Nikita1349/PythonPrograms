#--------------------------------------------------------------------------------------------------------
#10. Write a program which accepts a number from the user and returns the addition (sum) of digits in that number.
#nput: 5187934   Output: 37
# -------------------------------------------------------------------------------------
def SumDigit(No):
        Sum = 0
        while(No > 0):
            Digit = No % 10
            Sum = Sum + Digit
            No = No // 10
        return Sum
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = SumDigit(Num1)
    
    print("Count is :" , Ret)
   
    
if __name__ == "__main__":
    main()