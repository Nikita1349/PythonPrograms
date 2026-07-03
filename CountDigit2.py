#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print count of digit in that number 
# Input = 342455  Op= 6
#-------------------------------------------------------------------------------------------------------
def CountDigit(Value):
    cnt = 0
    for i in str(Value):
        cnt += 1
    return cnt   

def main():
    print("Enter a number:")
    no = int(input())
    
    Ret = CountDigit(no)
    
    print("Count of digit is:",Ret)
    
    
    
if __name__ == "__main__":
    main()