#-------------------------------------------------------------------------------
# Write a Lambda function which accept one number and return True if no is Even otherwise false
#--------------------------------------------------------------------------------
ChkEven = lambda Value1 : (Value1 % 2 == 0) 

def main():
    No1 = int(input("Enter a Number :" ))
  
    Ret =  ChkEven(No1)
    
    if(Ret == True):
        print("Number is even :",Ret)
    else:
        print("Number is Odd :", Ret)

if __name__ == "__main__":
    main()
