#-------------------------------------------------------------------------------------------------
# Write a program which accepts a name from the user and displays the length of the name.
#Input: Marvellous            #Output: 10
#-----------------------------------------------------------------------------------------------------

def Displaylen(str):
    return len(str)
    
    for i in range(2,21,2):
        print(i , end = " ")
    
    
def main():
    
    Name = input("Enter String :")
    
    Ret = Displaylen(Name)
    
    print("Length is :" , Ret)
    
if __name__ == "__main__":
    main()