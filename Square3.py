#-----------------------------------------------------------------------------------------------
# 3.WAP that accept one no and return square of that number. ex input = 5 ,Op = 25
#-------------------------------------------------------------------------------------------------
def Square(Value1):
    return Value1*Value1
    
    
def main():
    print("Enter a Number :")
    No1 = int(input()) 
    
    Ret = Square(No1)
    
    print("Square of number is:",Ret)

if __name__ == "__main__":
    main()