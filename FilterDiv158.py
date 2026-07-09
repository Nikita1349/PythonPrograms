#-----------------------------------------------------------------------------------------------
#Write a Lambda function using filter() which accept list of number and return list of number divisivle by 3 and 5
#---------------------------------------------------------------------------------------------------
Divisible = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = [5,8,90,54,56,30,22,67,92,15,25]
    
    print("Data is : ", Data)
    
    Fdata = list(filter(Divisible,Data))
    
    print("List of Divisible by 3 and 5 : " ,Fdata)
    
    
if __name__ == "__main__":
    main()

