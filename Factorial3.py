#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and return factorial of that number  
# Product of all Positive Intergers if no is 5 then 5*4*3*2*1 = 120
#-------------------------------------------------------------------------------------------------------
def Factorial(Value):
    Fact = 1
    for i in range(1,Value+1):
        Fact = Fact * i
    return Fact

def main():
    print("Enter a number:")
    no = int(input())
    
    ret = Factorial(no)
    print("Factorial is:",ret)
    

if __name__ == "__main__":
    main()