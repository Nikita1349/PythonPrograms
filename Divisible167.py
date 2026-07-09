#-------------------------------------------------------------------------------------------------
# Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5; otherwise, return False.
#Input: 8            Output: False
#Input: 25            Output: True
#-----------------------------------------------------------------------------------------------------

def Divisible (Value):
    if(Value % 5 == 0):
        return True
    else:
        return False
    
def main():
    No1 = int(input("Enter Number : "))
    Ret = Divisible(No1)
    
    if(Ret == True):
        print("True")
    else:
        print("False")
    
    
if __name__ == "__main__":
    main()