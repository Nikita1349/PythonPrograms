#-------------------------------------------------------------------------------
# Write a Lambda function which accept two number and return addition
#--------------------------------------------------------------------------------
Addition = lambda Value1,Value2 : Value1 + Value2 

def main():
    No1 = int(input("Enter a Number :" ))
    No2 = int(input("Enter a Number :" ))
  
    Ret = Addition(No1,No2)
    
    print("Additions is : " ,Ret)

if __name__ == "__main__":
    main()
