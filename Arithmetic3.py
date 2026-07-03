#--------------------------------------------------------------------------------------------------------
# WAP that accept one number and prints factor of that no
# Input = 12  Op= 1,2,3,4,6,12
#-------------------------------------------------------------------------------------------------------
def Arithmetic(Value1,Value2):
    Add =  Value1 + Value2
    Sub =  Value1 - Value2
    Mul =  Value1 * Value2
    Div =  Value1 / Value2
    return Add,Sub,Mul,Div

def main():
    print("Enter first Number:")
    No1 = int(input())
    
    print("Enter Second Number:")
    No2 = int(input())
    
    Add1,Sub1,Mul1,Div1 = Arithmetic(No1,No2)
    print("Addition is :",Add1)
    print("Substraction is :",Sub1)
    print("Multiplication is :",Mul1)
    print("Division is :",Div1)
    
    
if __name__ == "__main__":
    main()