def Reverse(no):
    rev = 0
    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10
    return rev

def main():
    print("Enter the number : ")
    no = int(input())

    ret = Reverse(no)

    print("Reverse of digits : ", ret)

if __name__ == "__main__":
    main()