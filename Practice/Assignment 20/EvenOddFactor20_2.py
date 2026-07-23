#-------------------------------------------------------------------------------------------------------------
#2. Design a Python application that creates two threads named EvenFactor and OddFactor.
#Question Accept one integer.
#EvenFactor thread:      Find even factors.       Display their sum.
#OddFactor thread:       Find odd factors.         Display their sum.
#After completion display:      Exit from main
#-----------------------------------------------------------------------------------------------
import threading
def EvenFactor(No):
    sum_even = 0
    
    print("Even Factors are : " , end = " ")
    for i in range(2,No + 1,2):
        if (No % i == 0):
            print(i,end = " ")
            sum_even = sum_even +i
    
    print("\n Sum of even Factors :" , sum_even)
    
def OddFactor(No):
    sum_odd = 0
        
    print("Odd Factors are : ", end = " ")
    for i in range(1,No+1,2):
        if(No % i == 0):
            print(i , end = " ")
            sum_odd = sum_odd + i
                
    print("\n Sum of odd factors : ", sum_odd)
          
    
def main():
    
    no = int(input("Enter a Number : "))
    
    t1 = threading.Thread(target = EvenFactor , args = (no,))
    t2 = threading.Thread(target = OddFactor , args=(no,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()
    
    
