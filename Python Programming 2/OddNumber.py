def Odd(no):
    for i in range(1, no + 1, 2):
        print(i)

def main():
    print("Enter the number to print odd numbers : ")
    n = int(input())

    Odd(n)

if __name__ == "__main__":
    main()