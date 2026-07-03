#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and reverse that number 
# Input = 1234  Op= 4321
#-------------------------------------------------------------------------------------------------------
def Reverse(Value):
    sum = 0
    while(Value != 0):
        digit = Value % 10
        print(digit, end =" ")
        Value = Value // 10 

def main():
    print("Enter a number:")
    no = int(input())
    
    Reverse(no)
    
    
if __name__ == "__main__":
    main()