#------------------------------------------------------------------------------------------------------------------
#2. Write a program which contains one lambda function which accepts two parameters and returns their multiplication.
#Example:  Input : 4 3    Output : 12
#Input : 6 3      Output : 18
#-------------------------------------------------------------------------------------------------------------------
Mult = lambda Num1 , Num2 : Num1 * Num2

def main():
    
    No1 = int(input("enter first Number : "))
    No2 = int(input("Enter Second Number : "))
    
    Ret = Mult(No1, No2)
    
    print("Multiplication is : " , Ret)

if __name__ == "__main__":
    main()
