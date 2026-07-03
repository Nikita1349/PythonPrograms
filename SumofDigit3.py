#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print Sum of digit in that number 
# Input = 342455  Op= 23
#-------------------------------------------------------------------------------------------------------
def DigitSum(Value):
    sum = 0
    while(Value != 0):
        digit = Value % 10
        sum = sum + digit
        Value = Value // 10
        
    return sum  

def main():
    print("Enter a number:")
    no = int(input())
    
    Ret = DigitSum(no)
    
    print("Sum of digit is:",Ret)
    
    
    
if __name__ == "__main__":
    main()