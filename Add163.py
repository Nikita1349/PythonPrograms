#-------------------------------------------------------------------------------------------------
# Write a program which contains one function named as Add() which accepts two numbers from the user and returns the addition of those two numbers.
#Input: 11 5
#Output: 16
#-----------------------------------------------------------------------------------------------------

def Add(Value1,Value2):
    
        return Value1 + Value2
    
def main():
    
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter First Number : "))
    
    Ret = Add(No1,No2)
    
    print("Addition is: " ,Ret)
    
if __name__ == "__main__":
    main()