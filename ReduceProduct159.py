#-----------------------------------------------------------------------------------------------
#Write a Lambda function using reduce() which accept list of numbers and return product of all nos
#---------------------------------------------------------------------------------------------------
from functools import reduce
Product = lambda No1 , No2 : No1 * No2
def main():
    
    Data = [3,4,1,2,1]
    
    print("Data is : ", Data)
    
    Fdata = reduce(Product,Data)
    
    print("Product of number is : ", Fdata)
    
if __name__ == "__main__":
    main()
