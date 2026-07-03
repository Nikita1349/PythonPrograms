#--------------------------------------------------------------------------------------------------------
# WAP that accept one number and prints factor of that no
# Input = 12  Op= 1,2,3,4,6,12
#-------------------------------------------------------------------------------------------------------
def Factor(Value): 
    for i in range(1,Value+1):
        if (Value % i == 0):
            print(i, end=" ")

def main():
    print("Enter a Number:")
    no = int(input())
    
    Factor(no)
    
    
if __name__ == "__main__":
    main()