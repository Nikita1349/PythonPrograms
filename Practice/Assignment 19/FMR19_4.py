#-------------------------------------------------------------------------------------------------------------------------
#4. Write a program which contains filter(), map() and reduce(). Python application contains one list of numbers accepted from the user.
#filter() should select all even numbers.
#map() should calculate the square of each number.
#reduce() should return the addition (sum) of all squared numbers.
#Example: Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204
#----------------------------------------------------------------------------------------------------------------------------------
from functools import reduce

def Even(Num):
    if(Num % 2 == 0):
        return Num
    
def Square(Squ):
    Squ = Squ * Squ
    return Squ

def Sum(No1 , No2):
    Nos = No1 + No2
    return Nos
    

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    print("Input list : " , Data)
    
    FData = list(filter(Even , Data))
    print("Filter after Even : " , FData)
    
    MData = list(map(Square , FData))
    print("Map after Square : " ,  MData)
    
    RData = reduce(Sum , MData)
    print("Output of Reduce after sum of Sqaure No :" , RData)
    
if __name__ == "__main__":
    main()