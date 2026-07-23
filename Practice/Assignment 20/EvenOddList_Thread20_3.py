#-------------------------------------------------------------------------------------------------------------
#3. Design a Python application that creates two threads named EvenList and OddList.
#Question    Accept a list of integers.
#EvenList      Extract even numbers.   #Display their sum.
#OddList       Extract odd numbers.     Display their sum.
#Threads should run concurrently.
#-----------------------------------------------------------------------------------------------
import threading

def EvenList(arr):
    sum_even = 0
    
    print("Even elements are : " , end = " ")
    
    for i in arr:
        if( i % 2 == 0 ):
            print(i , end = " ")
            sum_even = sum_even + i 
            
    print("\n Sum of even elements : " , sum_even)
    
def OddList(arr):
    sum_odd = 0
    
    print("odd elements are : " , end = " ")
    
    for i in arr:
        if( i % 2 != 0 ):
            print(i , end = " ")
            sum_odd = sum_odd + i 
            
    print("\n Sum of odd elements : " , sum_odd)


def main():
    size = int(input("Enter number of elements :"))
    arr = []
    
    print("enter the elements : ")
    for i in range(size):
        no = int(input())
        arr.append(no)
        
    t1 = threading.Thread(target = EvenList , args = (arr,))
    t2 = threading.Thread(target = OddList , args = (arr,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()