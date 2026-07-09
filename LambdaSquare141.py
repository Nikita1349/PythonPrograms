#-------------------------------------------------------------------------------
# Write a Lambda function which accept one number and return square of that number
#--------------------------------------------------------------------------------
Square = lambda Value : Value * Value

def main():
    No = int(input("Enter a Number :" ))
    Ret =  Square(No)
    
    print("Square is :", Ret)

if __name__ == "__main__":
    main()
