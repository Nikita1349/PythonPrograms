#---------------------------------------------------------------------------------------------------
#Write a lambda function using map() which acccept list of number and return a list of square of each no
#--------------------------------------------------------------------------------------------------
Square = lambda No1 : No1 * No1

def main():
    Data = [1,2,3,4,5,6,7]
    
    print("List of data is : ", Data)
    
    Mdata = list(map(Square,Data))
    
    print("Data After Square : ", Mdata)
    

if __name__ == "__main__":
    main()