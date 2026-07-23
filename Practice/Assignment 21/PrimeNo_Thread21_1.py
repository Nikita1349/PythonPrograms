#-----------------------------------------------------------------------------------------------------
#1. Design a Python application that creates two threads named Prime and NonPrime.
#Question
#Both threads should accept a list of integers.
#The Prime thread should display all prime numbers from the list.
#The NonPrime thread should display all non-prime numbers from the list.
#--------------------------------------------------------------------------------------------------------
import threading

def Prime(arr):
    print("Prime numbers are :")
    
    for no in arr:
        count = 0
        
        for i in range(1, no+1):
            if(no % i == 0):
                count = count + 1
        if count == 2:
            print(no, end = " ")
    print()
    
def NonPrime(arr):
    print("NonPrime numbers are :")
    
    for no in arr:
        count = 0
        
        for i in range(1, no+1):
            if(no % i == 0):
                count = count + 1
        if count != 2:
            print(no, end = " ")
    print()
            
def main():
    size = int(input("Enter a Number of elements : "))
    arr = []
    print("enter the elements : ")
    for i in range(size):
        no = int(input())
        arr.append(no)
        
    t1 = threading.Thread(target = Prime , args = (arr,))
    t2 = threading.Thread(target = NonPrime , args = (arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")


if __name__ == "__main__":
    main()