#-------------------------------------------------------------------------------
# Write a Lambda function which accept two number and return maximum number
#--------------------------------------------------------------------------------
Maximum = lambda Value1,Value2 : Value1 if Value1 > Value2 else Value2

def main():
    No1 = int(input("Enter first Number :" ))
    No2 = int(input("Enter second Number :" ))
    
    Ret =  Maximum(No1,No2)
    
    print("Maximun number is :", Ret)

if __name__ == "__main__":
    main()
