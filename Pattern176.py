#--------------------------------------------------------------------------------------------------------
# 6. Write a program which accepts one number and displays the below pattern.
#Input: 5      Output:
#*   *   *   *   *
#*   *   *   *
#*   *   *
#*   *
#*
#-------------------------------------------------------------------------------------------------------
def Pattern(No):
    for i in range(1, No + 1):
        for j in range(No - i + 1):
            print("*" , end = " ")
        print()
    
def  main():
    Num1 = int(input("Enter a Number : " ))
    
    Ret = Pattern(Num1)
   
    
if __name__ == "__main__":
    main()