#-----------------------------------------------------------------------------------------------------
#2. Design a Python application that creates two threads named Maximum and Minimum.
#Question
#Thread 1 should calculate and display the maximum element from a list.
#Thread 2 should calculate and display the minimum element from the same list.
#The list should be accepted from the user.
#-----------------------------------------------------------------------------------------------------
import threading

def Maximum(arr):
    Max = arr[0]

    for no in arr:
        if (no > Max):
            Max = no

    print("Maximum element is :", Max)

def Minimum(arr):
    Min = arr[0]

    for no in arr:
        if (no < Min):
            Min = no

    print("Minimum element is :", Min)
            
def main():
    size = int(input("Enter a Number of elements : "))
    arr = []
    print("enter the elements : ")
    for i in range(size):
        no = int(input())
        arr.append(no)
        
    t1 = threading.Thread(target = Minimum , args = (arr,))
    t2 = threading.Thread(target = Maximum , args = (arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")


if __name__ == "__main__":
    main()