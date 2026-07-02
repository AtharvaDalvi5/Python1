def Area(l,w):
    Ans = l * w
    return Ans

def main():
    print("Enter the length : ")
    lin = int(input())

    print("Enter the width : ")
    wid = int(input())

    area = Area(lin, wid)

    print("The area of the rectangle is:", area)

if __name__ == "__main__":
    main()
