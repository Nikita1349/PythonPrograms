#-----------------------------------------------------------------------------------------------
#Write a Lambda function using filter() which accept list of numbers and return count of even nos
#---------------------------------------------------------------------------------------------------
EvenCount = lambda No1  : No1 % 2 == 0 
def main():
    
    Data = [3,4,1,2,1,7,8,9,77,45]
    
    print("Data is : ", Data)
    
    Fdata = list(filter(EvenCount,Data))
    
    print("count of even number is : ", len(Fdata))
    
if __name__ == "__main__":
    main()
