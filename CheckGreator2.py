#--------------------------------------------------------------------------------------------------------------
#Write a program which contains one function ChkGreator() which accepts two number and print greator input: 10 20 Output = 20
#--------------------------------------------------------------------------------------------------------------------
def ChkGreater(value1,value2):
    
    if(value1 > value2):
        return value1
    else:
        return value2
    

def main():
    print("Enter first number")
    no1 = int(input())
    
    print("Enter Second Number")
    no2 = int(input())
    
    Ret = ChkGreater(no1,no2)
    
    print("Greater Number is :",Ret)
    

if __name__ == "__main__":
    main()