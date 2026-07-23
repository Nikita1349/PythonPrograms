#-------------------------------------------------------------------------------------------------------------------------
#3. Write a program which contains filter(), map() and reduce(). Python application contains one list of numbers accepted from the user.
#filter() should select numbers greater than or equal to 70 and less than or equal to 90.
#map() should increase each number by 10.
#reduce() should return the product of all mapped numbers.
#Example:     Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000
#----------------------------------------------------------------------------------------------------------------------------------
from functools import reduce
Greatar = lambda No : (No >= 70) and (No <= 90)
Increase = lambda No : No + 10
Product = lambda No1 , No2  : No1 * No2 

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    
    print("Input Data is : ", Data)
    
    FData = list(filter(Greatar , Data))
    print("List After filter : " , FData)
    
    MData = list(map(Increase , Data))
    print("List After Map : " ,MData)
    
    RData = reduce(Product , MData)
    print("Output of reduce : " , RData)

if __name__ == "__main__":
    main()
