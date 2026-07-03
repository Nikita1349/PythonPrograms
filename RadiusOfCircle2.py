#--------------------------------------------------------------------------------------------------------
# WAP that accept Radius of circle and prints area of circle
# 
#-------------------------------------------------------------------------------------------------------
def  CircleRadius(r):
    Area = 3.14 * r *r
    return Area

def main():
    print("Enter Radius:")
    No1 = float(input())
    
    Ret = CircleRadius(No1)
    
    print("Area of circle is : ",Ret)
    
    
if __name__ == "__main__":
    main()