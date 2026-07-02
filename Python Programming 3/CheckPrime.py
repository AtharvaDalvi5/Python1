def Prime(no):
        if no % 2 == 0:
            print("Not Prime Number")
        else:
            print("Prime Number ")

def main():
    print("Enter the number : ")
    no = int(input())
    Prime(no)

if __name__ == "__main__":
    main()
