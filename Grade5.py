#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print Grade
# 
#-------------------------------------------------------------------------------------------------------
def Grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    print("Enter Marks:")
    No1 = int(input())

    Grade(No1)


if __name__ == "__main__":
    main()