#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and check Whether it is prime or not 
# prime = a no which is divisible by only 1 and itself 2,3,5.,7
#-------------------------------------------------------------------------------------------------------
def Prime(Value):
    count = 0
    for i in range(1,Value+1):
        if (Value % i == 0):
            count += 1
        
    if (count == 2):
        print("Prime Number")
            
    else:
        print("Not a Prime Number")
            
        

def main():
    print("Enter a number:")
    no = int(input())
    
    Ret = Prime(no)
    
    
    
if __name__ == "__main__":
    main()