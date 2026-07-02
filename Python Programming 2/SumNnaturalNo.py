def Summation(no):
    Sum = 0
    for i in range(1, no + 1):
        Sum = Sum + i
    return Sum

def main():
    print("Enter the number of elements : ")
    n = int(input())

    Ret = Summation(n)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()