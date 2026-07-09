#--------------------------------------------------------------------------------------------------------
#7.8. Write a program which accepts one number and displays the below pattern.
#Input: 5  Output:
#1
#1   2
#1   2   3
#1   2   3   4
#1   2   3   4   5
#-------------------------------------------------------------------------------------------------------
def Pattern(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print()
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = Pattern(Num1)
   
    
if __name__ == "__main__":
    main()