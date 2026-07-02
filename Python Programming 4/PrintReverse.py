def PrintRev(n):
    for i in range(n, 0, -1):
        print(i)

def main():
    print("Enter the Number : ")
    no = int(input())

    PrintRev(no)

if __name__ == "__main__":
    main()