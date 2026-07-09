#-------------------------------------------------------------------------------
# Write a Lambda function which accept one number and return True if no is Even otherwise false
#--------------------------------------------------------------------------------
ChkOdd = lambda Value1 : (Value1 % 2 != 0) 

def main():
    No1 = int(input("Enter a Number :" ))
  
    Ret =  ChkOdd(No1)
    
    if(Ret == True):
        print("Number is Odd :",Ret)
    else:
        print("Number is Even :", Ret)

if __name__ == "__main__":
    main()
