def Even(no):
    for i in range(2, no + 1, 2):
        print(i)

def main():
    print("Enter the number to print even numbers : ")
    n = int(input())

    Even(n)

if __name__ == "__main__":
    main()