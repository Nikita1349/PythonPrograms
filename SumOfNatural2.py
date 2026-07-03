#----------------------------------------------------------------------------------------------------------
# 2.WAP which accept one number and prints sum of first N Natural Numbers. input 5 Op 15
#Natural nos are positive counting nos !+2+3+4+5 = 15  
#---------------------------------------------------------------------------------------------------------
def Natural(Value):
    Total = 0
    for i in range(1,Value+1):
        Total = Total + i
    return Total
        

def main():
    print("Enter a number:")
    No = int(input())
    
    Ret = Natural(No)
    print("Sum of Natural no is",Ret)

if __name__ == "__main__":
    main()