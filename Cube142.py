#-------------------------------------------------------------------------------
# Write a Lambda function which accept one number and return square of that number
#--------------------------------------------------------------------------------
Cube = lambda Value : Value * Value * Value

def main():
    No = int(input("Enter a Number :" ))
    Ret =  Cube(No)
    
    print("Cube is :", Ret)

if __name__ == "__main__":
    main()
