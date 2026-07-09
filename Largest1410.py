#-------------------------------------------------------------------------------
# Write a Lambda function which accept Three number and return Largest Number
#--------------------------------------------------------------------------------
Largest = lambda a, b , c  : a if a >= b and a >= c else b if b >= a and b >= c else c
     

def main():
    No1 = int(input("Enter first Number :" ))
    No2 = int(input("Enter Second Number :" ))
    No3 = int(input("Enter Third Number :" ))
  
    Ret = Largest(No1,No2,No3)
    
    print("Largest number is : " ,Ret)

if __name__ == "__main__":
    main()
