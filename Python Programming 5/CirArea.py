def Area(Radius,PI = 3.14):
    Ans = PI * Radius * Radius
    return Ans

def main():
    print("Enter the radius : ")
    r = int(input())

    ret = Area(r)

    print("The area of the circle is:", ret)

if __name__ == "__main__":
    main()
