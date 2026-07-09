#-------------------------------------------------------------------------------------------------
# Write a program which contains one function that accepts one number from the user and returns True if the number is divisible by 5; otherwise, return False.
#Input: 8            Output: False
#Input: 25            Output: True
#-----------------------------------------------------------------------------------------------------

def PrintStar (Num):
    
    for i in range(Num):
        print("*",end = " ")
    
    
def main():
    No1 = int(input("Enter Number : "))
    PrintStar(No1)
    
if __name__ == "__main__":
    main()