#--------------------------------------------------------------------------------------------------------
#9. Write a program which accepts a number from the user and returns the number of digits in that number.
#Input: 5187934   Output:7
# -------------------------------------------------------------------------------------
def DigitNo(No):
     Count = 0
     while(No > 0):
        Count = Count + 1
        No = No // 10
     return Count
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = DigitNo(Num1)
    
    print("Count is :" , Ret)
   
    
if __name__ == "__main__":
    main()