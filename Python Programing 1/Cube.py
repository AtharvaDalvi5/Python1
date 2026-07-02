def Cube(no):
    return no * no * no

def main():
    print("Enter the number : ")
    value = int(input())
    
    Ret = Cube(value)
    
    print("Cube of number is:", Ret)

if __name__ == "__main__":
    main()