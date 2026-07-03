#--------------------------------------------------------------------------------------------------------
# WAP that accept one number and prints many no starting from 1
# Input = 5  Op= 1,2,3,4,5
#-------------------------------------------------------------------------------------------------------
def  ManyNo(Value1):
    while(Value1 >= 1):
        print(Value1, end=" ")
        Value1 = Value1-1

def main():
    print("Enter first Number:")
    No1 = int(input())
    
    ManyNo(No1)
    
    
if __name__ == "__main__":
    main()