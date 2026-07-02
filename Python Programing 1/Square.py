def Square(no):
    return no * no

def main():
    print("Enter the number : ")
    value = int(input())
    
    Ret = Square(value)
    
    print("Square of number is:", Ret)

if __name__ == "__main__":
    main()