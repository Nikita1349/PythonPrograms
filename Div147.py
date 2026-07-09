#-------------------------------------------------------------------------------
# Write a Lambda function which accept one number and return True if divisible by 5
#--------------------------------------------------------------------------------
Div = lambda Value1 : (Value1 % 5 == 0) 

def main():
    No1 = int(input("Enter a Number :" ))
  
    Ret =  Div(No1)
    
    if(Ret == True):
        print("Number is divisible by 5 :",Ret)
    else:
        print("Number is not divisible by 5 :", Ret)

if __name__ == "__main__":
    main()
