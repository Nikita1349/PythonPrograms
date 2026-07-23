#-------------------------------------------------------------------------------------------------------------------------
#5. Write a program which contains filter(), map() and reduce(). Python application contains one list of numbers accepted from the user. (You can also use normal functions instead of lambda functions.)
#filter() should select all prime numbers.
#map() should multiply each prime number by 2.
#reduce() should return the maximum number from the mapped list.
#Example:  Input List = [2, 70, 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
# #List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62
#----------------------------------------------------------------------------------------------------------------------------------
from functools import reduce

def Prime(Num):
    if Num < 2:
        return False
    for i in range(2,Num):
        if (Num % i == 0):
            return False
    return True

def Mult(No):
    return No * 2

def Max(No1 , No2):
    if (No1 > No2):
        return No1
    else:
        return No2
             

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]
    print("Input list : " , Data)
    
    FData = list(filter(Prime , Data))
    print("Filter after Prime : " , FData)
    
    MData = list(map(Mult , FData))
    print("Map after Multiply each prime no  : " ,  MData)
    
    RData = reduce(Max , MData)
    print("Output of Reduce for max no :" , RData)
    
if __name__ == "__main__":
    main()