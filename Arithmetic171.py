#----------------------------------------------------------------------------------
#Create one module named Arithmetic which contains the following four functions: Add  for addition,Sub  for subtraction,
# Mult  for multiplication and Div ,All functions should accept two parameters as numbers and perform the respective operation.
# Write a Python program that accepts two numbers from the user and calls all the functions from the Arithmetic
# module to display the results.
#-----------------------------------------------------------------------------------------------------------------
import ArithmeticModule

def main():
    
    Num1 = int(input("Enter First Number : "))
    Num2 = int(input("Enter Second Number : "))
    
    Ret1 = ArithmeticModule.Add(Num1,Num2)
    Ret2 = ArithmeticModule.Sub(Num1,Num2)
    Ret3 = ArithmeticModule.Mult(Num1,Num2)
    Ret4 = ArithmeticModule.Div(Num1,Num2)
    
    print("Addition is : ", Ret1)
    print("Subtraction is : ", Ret2)
    print("Multiplication is : ", Ret3)
    print("Division is : ", Ret4)
    
if __name__ == "__main__":
    main()