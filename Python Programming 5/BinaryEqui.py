def Binary(no):
    if no > 0:
        Binary(no // 2)
    print(no % 2)

def main():
    print("Enter a number : ")
    num = int(input())

    Binary(num)
    
if __name__ == "__main__":
    main()