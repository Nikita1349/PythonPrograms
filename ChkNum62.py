#-------------------------------------------------------------------------------------------------
# Write a program which contains one function named as ChkNum() which accepts one parameter as a number. If the number is even, then it should display "Even Number"; otherwise, display "Odd Number" on the console.
#Input: 11
#Output: Odd Number
#Input: 8
#Output: Even Number
#-----------------------------------------------------------------------------------------------------

def ChkNum(Value1):
    if(Value1 %2 == 0):
        return True
    else:
        return False
    
def main():
    
    No1 = int(input("Enter a Number : "))
    Ret = ChkNum(No1)
    
    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")
    
if __name__ == "__main__":
    main()