#-----------------------------------------------------------------------------------------------
#Write a Lambda function using reduce() which accept list of numbers and return addition of nos
#---------------------------------------------------------------------------------------------------
from functools import reduce
Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [3,5,6,85,75,75,76,56,44]
    
    print("Data is : ", Data)
    
    Rdata = reduce(Addition,Data)
    
    print("Addition is :", Rdata)
    
if __name__ == "__main__":
    main()

