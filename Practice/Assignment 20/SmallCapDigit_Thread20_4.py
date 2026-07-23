#-------------------------------------------------------------------------------------------------------------
#4. Design a Python application that creates three threads named Small, Capital and Digits.
#Question  Accept a string.
#Small => Count lowercase letters.
#Capital => Count uppercase letters.
#Digits => Count numeric digits.
#Display: Thread ID          Thread Name
#-----------------------------------------------------------------------------------------------
import threading
def Small(s):
    count = 0
    
    for ch in s:
        if(ch.islower()):
            count = count + 1
    print("small letters count :" , count)
    print("Thread ID :" , threading.get_ident())
    print("Thread Name :" , threading.current_thread().name)

def Capital(s):
    count = 0
    
    for ch in s:
        if(ch.isupper()):
            count = count + 1
    print("Capital letters count :" , count)
    print("Thread ID :" , threading.get_ident())
    print("Thread Name :" , threading.current_thread().name)
    
def Digits(s):
    count = 0
    
    for ch in s:
        if(ch.isdigit()):
            count = count + 1
    print("Digit count :" , count)
    print("Thread ID :" , threading.get_ident())
    print("Thread Name :" , threading.current_thread().name)
    
def main():
    str = input("Enter a string :")
        
    t1 = threading.Thread(target = Small , args = (str,), name = "Small")
    t2 = threading.Thread(target = Capital , args = (str,) , name = "Capital")
    t3 = threading.Thread(target = Digits , args = (str,) , name = "Digits")
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()