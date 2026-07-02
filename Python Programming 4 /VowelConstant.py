def CheckVowel(c):
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        print("The character is a vowel ")
    else:
        print("The character is not a vowel ")

def main():
    print("Enter the Character : ")
    c = input()

    CheckVowel(c)

if __name__ == "__main__":
    main()
    
