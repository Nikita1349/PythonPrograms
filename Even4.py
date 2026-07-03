#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print all Even no till that number  
# 2+4+6+8 =20
#-------------------------------------------------------------------------------------------------------
def Even(Value):
    Sum = 0
    for i in range(2,Value+1,2):
         print(i, end=" ")

def main():
    print("Enter a number:")
    no = int(input())
    
    Even(no)
    
    

if __name__ == "__main__":
    main()