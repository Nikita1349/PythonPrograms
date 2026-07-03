#--------------------------------------------------------------------------------------------------------
# WAP that accept length ans width of rectangle and print area
# Input = 5  Op= 1,2,3,4,5
#-------------------------------------------------------------------------------------------------------
def  Area(Length,Width):
    RectangleArea = Length * Width
    return RectangleArea

def main():
    print("Enter Length:")
    No1 = float(input())
    
    print("Enter Width:")
    No2 = float(input())
    
    Ret = Area(No1,No2)
    
    print("Area of Rectangle is : ",Ret)
    
    
if __name__ == "__main__":
    main()