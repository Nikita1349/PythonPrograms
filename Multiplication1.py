#----------------------------------------------------------------------------------------------------------------------------
#WAP that accept one no from from user and prints multiplication table of that number Input 4 Op= 4 8 12 16 20 24 28 32 36 40
#-----------------------------------------------------------------------------------------------------------------------------
def Multiplication(Value):
    for i in range(1,11):
        print(Value * i, end=" " )
        
def main():
    print("Enter a number:")
    No = int(input())
    
    Multiplication(No)


if __name__ == "__main__":
    main()