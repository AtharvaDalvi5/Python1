def Sum(no):
    Sum = 0
    while no != 0:
        Sum = Sum + (no % 10)
        no = no // 10
    return Sum

def main():
    print("Enter the number: ")
    no = int(input())

    ret = Sum(no)
    print("Sum of digits : ", ret)

if __name__ == "__main__":
    main()