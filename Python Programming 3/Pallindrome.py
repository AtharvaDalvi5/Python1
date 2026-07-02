def Pallindrome(no):
    temp = no
    rev = 0
    while no > 0:
        dig = no % 10
        rev = rev * 10 + dig
        no = no // 10
    if temp == rev:
        print("Pallindrome Number")
    else:
        print("Not a Pallindrome Number")

def main():
    print("Enter the number : ")
    no = int(input())

    Pallindrome(no)

if __name__ == "__main__":
    main()