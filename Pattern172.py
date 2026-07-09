#----------------------------------------------------------------------------------
#2. Write a program which accepts one number and displays the below pattern.
#Input: 5
#Output:
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#-----------------------------------------------------------------------------------------------------------------
def Pattern(No1):
    for i in range(No1):
         for j in range(No1):
              print("*", end = " ")
         print()
           
def main():

    Num1 = int(input("enter a number : " ))
    Pattern(Num1)
    
if __name__ == "__main__":
    main()