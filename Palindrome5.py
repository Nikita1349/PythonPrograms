#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and check number is palindrome or not 
# Input = 12321  Op= yes
#-------------------------------------------------------------------------------------------------------
def Palindrome(Reverse):
    Original = Reverse
    Temp = Original
    Rev = 0
    
    while(Original != 0):
        digit = Original % 10
        Rev = Rev * 10 + digit
        Original = Original // 10 
        
    if(Temp == Rev):
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")

def main():
    print("Enter a number:")
    no = int(input())
    
    Palindrome(no)
    
    
if __name__ == "__main__":
    main()