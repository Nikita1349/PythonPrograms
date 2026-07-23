#------------------------------------------------------------------------------------------------------------------
#1. Write a program which contains one lambda function which accepts one parameter and returns power of two.
#Example:  Input : 4      Output : 16
#Input : 6         Output : 64
#-------------------------------------------------------------------------------------------------------------------
Power = lambda Num : Num * Num
def main():
    
    No = int(input("Enter a Number :" ))
    
    Ret = Power(No)
    
    print("Power is : ", Ret)

if __name__ == "__main__":
    main()