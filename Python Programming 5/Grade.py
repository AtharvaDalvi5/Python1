def Grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Division")
    elif marks >= 50:
        print("Second Division")
    else:
        print("Fail")

def main():
    print("Enter the marks : ")
    m = int(input())

    Grade(m)

if __name__ == "__main__":
    main()