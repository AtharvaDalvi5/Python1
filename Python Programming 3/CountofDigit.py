def Count(no):
    count = 0
    while(no > 0):
        no = no // 10
        count = count + 1
    return count

def main():
    print("Enter the number : ")
    no = int(input())

    ret = Count(no)

    print("Count of digits : ", ret)

if __name__ == "__main__":
    main()