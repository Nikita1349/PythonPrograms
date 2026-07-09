#-------------------------------------------------------------------------------
# Write a Lambda function which accept two number and return Multiplication
#--------------------------------------------------------------------------------
Multiplication = lambda Value1,Value2 : Value1 * Value2 

def main():
    No1 = int(input("Enter first Number :" ))
    No2 = int(input("Enter Second Number :" ))
  
    Ret = Multiplication(No1,No2)
    
    print("Additions is : " ,Ret)

if __name__ == "__main__":
    main()
