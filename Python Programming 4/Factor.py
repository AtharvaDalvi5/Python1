def Factor(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i)

def main():
    print("Enter the Number : ")
    no = int(input())

    Factor(no)

if __name__ == "__main__":
    main()