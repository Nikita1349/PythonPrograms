#---------------------------------------------------------------------------------------------------------
#4. Write a program which accepts N numbers from the user and stores them into a List. Accept another number
# from the user and return the frequency of that number from the List.
#Input   Number of elements : 11               13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5  Output  3
#--------------------------------------------------------------------------------------------------------------------------
def Frequency(data ,value):
    Count = 0
    
    for no in data:
        if (no == value):
             Count = Count + 1
        
    return Count

def main():
    Size = 0
    Arr = list()
    
    print("Enter the Number of Elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
        
    Search = int(input("Enter Number to search"))
        
    Ret = Frequency(Arr , Search)
    
    print("Frequency is : ", Ret)
    
    
if __name__ == "__main__":
    main()