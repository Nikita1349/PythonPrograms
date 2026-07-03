#--------------------------------------------------------------------------------------------------------
# WAP that accept one no and print Binary Equivalent
# 
#-------------------------------------------------------------------------------------------------------
def Binary(num):
    binary = "" 

    while (num > 0):
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Binary Equivalent =", binary)


def main():
    print("Enter Number:")
    No1 = int(input())

    Binary(No1)


if __name__ == "__main__":
    main()