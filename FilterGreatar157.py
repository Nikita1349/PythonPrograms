#-----------------------------------------------------------------------------------------------
#Write a Lambda function using filter() which accept list of string and returns list of string having length gratar than 5
#---------------------------------------------------------------------------------------------------
Greatar = lambda str : len(str) > 5

def main():
    Data = ["Hello","Nikita","Hi","Good","Marvellous"]
    
    print("Data is : ", Data)
    
    Fdata = list(filter(Greatar,Data))
    
    print("List of greator than 5 : " ,Fdata)
    
    
if __name__ == "__main__":
    main()

