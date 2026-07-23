#-----------------------------------------------------------------------------------------------------
#10. Design a Python application that creates two threads named Sum and Product.
#Question
#Thread 1 should compute the sum of elements from a list.
#Thread 2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.
#-----------------------------------------------------------------------------------------------------
import threading

Sum = 0
Product = 1

def Addition(arr):
    global Sum

    for no in arr:
        Sum = Sum + no

def Multiplication(arr):
    global Product

    for no in arr:
        Product = Product * no
        
        
        
def main():
    size = int(input("Enter number of elements in list :"))
    arr = []
    
    print("Enter the elements :")
    
    for i in range(size):
        no = int(input())
        arr.append(no)
        
    t1 = threading.Thread(target = Addition , args= (arr,))
    t2 = threading.Thread(target = Multiplication , args= (arr,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Sum of elements :", Sum)
    print("Product of elements :", Product)
    print("Exit from main thread")

    
if __name__ == "__main__":
    main()