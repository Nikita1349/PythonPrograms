#----------------------------------------------------------------------------------------------------------------------
#WAP that accept one number from user and check whether it is divisible by 3 and 5  input = 15 Op = Divisible by 3 and 5 
#-----------------------------------------------------------------------------------------------------------------------
def Divisible(Value):
    if ((Value % 3 == 0) & (Value % 5 == 0)):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
    
    return Value
    
def main():
    print("enter a number:")
    No = int(input())
    
    Ret = Divisible(No)
    
if __name__ == "__main__":
    main()