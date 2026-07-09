#---------------------------------------------------------------------------------------------------------
#3. Write a program which accepts N numbers from the user and stores them into a List. Return Minimum number from that List.
#Input  Number of elements : 4      13 5 45 7
#Output 5
#--------------------------------------------------------------------------------------------------------------------------
def Minimum(data):
    Min = data[0]
    
    for no in data:
        if (no < Min):
            Min = no
        
    return Min


def main():
    Size = 0
    Arr = list()
    
    print("Enter the Number of Elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
        
    Ret = Minimum(Arr)
    
    print("Minimum no is : ", Ret)
    
    
    
if __name__ == "__main__":
    main()