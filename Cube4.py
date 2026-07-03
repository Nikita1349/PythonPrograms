#----------------------------------------------------------------------------------------------------
# WAP which accpet a number and return cube of that number 
#----------------------------------------------------------------------------------------------------
def Cube(Value1):
    return Value1*Value1*Value1
    
    
def main():
    print("Enter a number")
    No1 = int(input()) 
    
    Ret = Cube(No1)
    
    print("Cube of number is :",Ret)

if __name__ == "__main__":
    main()