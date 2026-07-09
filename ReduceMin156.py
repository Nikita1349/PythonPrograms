#-----------------------------------------------------------------------------------------------
#Write a Lambda function using reduce() which accept list of numbers and return Minimum of nos
#---------------------------------------------------------------------------------------------------
from functools import reduce
Min = lambda No1, No2 :No1 if No1 <= No2 else No2

def main():
    Data = [3,5,7,8,8,6,8,11]
    
    print("Data is : ", Data)
    
    Rdata = reduce(Min,Data)
    
    print("Minimum is :", Rdata)
    
if __name__ == "__main__":
    main()

