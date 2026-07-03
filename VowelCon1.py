#--------------------------------------------------------------------------------------------------------
# WAP that accept one character and check whether it os vowel or consonant or not 
# Input = a  Op= Vowel
#-------------------------------------------------------------------------------------------------------
def CheckVowel(char1):     
    if ((char1 == 'a') or (char1 == 'e') or (char1 == 'i') or (char1 == 'o') or (char1 == 'u') or 
    (char1 == 'A') or (char1 == 'E') or (char1 == 'I') or (char1 == 'O') or (char1 == 'U')):
        print("Vowel")
    else:
        print("Consonant")

def main():
    print("Enter a character:")
    char = input()
    
    CheckVowel(char)
    
    
if __name__ == "__main__":
    main()