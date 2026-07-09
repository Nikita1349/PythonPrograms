#---------------------------------------------------------------------------------------------------------
#2. Write a program which accepts N numbers from the user and stores them into a List. Return Maximum number from that List.
#Input Number of elements : 7               13 5 45 7 4 56 34
#Output   56
#--------------------------------------------------------------------------------------------------------------------------
def Max(data):
    max = data[0]
    
    for no in data:
        if (no > max):
            max = no
        
    return max


def main():
    Size = 0
    Arr = list()
    
    print("Enter the Number of Elements : ")
    Size = int(input())
    
    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Arr.append(No)
        
    Ret = Max(Arr)
    
    print("Maximum no is : ", Ret)
    
    
    
if __name__ == "__main__":
    main()