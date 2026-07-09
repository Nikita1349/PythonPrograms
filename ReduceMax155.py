#-----------------------------------------------------------------------------------------------
#Write a Lambda function using reduce() which accept list of numbers and return Maximum of nos
#---------------------------------------------------------------------------------------------------
from functools import reduce
Max = lambda No1, No2 :No1 if No1 >= No2 else No2

def main():
    Data = [3,5,7,8,3,6,8,11]
    
    print("Data is : ", Data)
    
    Rdata = reduce(Max,Data)
    
    print("Maximum is :", Rdata)
    
if __name__ == "__main__":
    main()

