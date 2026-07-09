#-----------------------------------------------------------------------------------------------
#Write a Lambda function using filter() which accept list od numbers and return Odd list of nos
#---------------------------------------------------------------------------------------------------
Even = lambda No : (No % 2 != 0)

def main():
    Data = [4,6,8,3,5,9,34,66,45,36]
    
    print("Data is :" , Data)
    
    Fdata = list(filter(Even,Data))
    
    print("Odd filtered data is : " , Fdata)
    
    
if __name__  == "__main__":
    main()