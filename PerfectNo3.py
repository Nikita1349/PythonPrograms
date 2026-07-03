#--------------------------------------------------------------------------------------------------------
# WAP that accept one no check whether it is perfect ,o or not
# in = 6 op = Perfect no (is a no equal to the sum of its proper factor)
#-------------------------------------------------------------------------------------------------------
def  Perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if (sum == num):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    print("Enter Number:")
    No1 = int(input())
    
    Ret = Perfect(No1)
    
if __name__ == "__main__":
    main()