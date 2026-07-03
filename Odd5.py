#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print all Odd no till that number  
# 1+3+5+7 =16
#-------------------------------------------------------------------------------------------------------
def Odd(Value):
    Sum = 0
    for i in range(1,Value+1,2):
         print(i, end=" ")

def main():
    print("Enter a number:")
    no = int(input())
    
    Odd(no)
    
    

if __name__ == "__main__":
    main()