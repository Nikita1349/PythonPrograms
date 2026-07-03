#--------------------------------------------------------------------------------------------------------
# WAP that accept one number and prints many no starting from 1
# Input = 5  Op= 1,2,3,4,5
#-------------------------------------------------------------------------------------------------------
def  ManyNo(Value1):
    for i in range(1,Value1+1):
        print(i, end=" ")

def main():
    print("Enter first Number:")
    No1 = int(input())
    
    ManyNo(No1)
    
    
if __name__ == "__main__":
    main()