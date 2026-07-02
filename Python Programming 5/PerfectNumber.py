def Perfect(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum += i
    if sum == no:
        print("The number is a perfect number")
    else:
        print("The number is not a perfect number")

def main():
    print("Enter a number : ")
    num = int(input())

    Perfect(num)    

if __name__ == "__main__":
    main()