#---------------------------------------------------------------------------------------------------------
#1. Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all elements from that List.
#Input     Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output 130
#--------------------------------------------------------------------------------------------------------------------------
def Addition(data):
    Sum = 0
    for no in data:
        Sum = Sum + no 
    return Sum


def main():
    Size = 0
    Arr = list()
    
    print("Enter the Number of Elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
        
    Ret = Addition(Arr)
    
    print("Addition is : ", Ret)
    
    
    
if __name__ == "__main__":
    main()