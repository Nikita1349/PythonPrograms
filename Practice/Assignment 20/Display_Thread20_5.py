#-------------------------------------------------------------------------------------------------------------
#5. Design a Python application that creates two threads named Thread1 and Thread2.
#Question
#Thread1 displays numbers from 1 to 50.
#Thread2 displays numbers from 50 to 1.
#Thread2 starts only after Thread1 completes.
#-----------------------------------------------------------------------------------------------
import threading

def Thread1():
    print("Numbers from 1 to 50 :")
    for i in range(1,51):
        print(i,end = " ")
    print()
        
def Thread2():
    print("Numbers from 50 to 1 :")
    for i in range(50,0, -1):
        print(i,end = " ")
    print()
        
    
def main():
        
    t1 = threading.Thread(target = Thread1 , name = "Thread1")
    t2 = threading.Thread(target = Thread2 , name = "thread2")

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()