def ChkGreater(no1, no2):
    if no1 > no2:
        return True
    else:
        return False
    
def main():
    print("Enter first number")
    value1 = int(input())
    
    print("Enter second number")
    value2 = int(input())
    
    Ret = ChkGreater(value1, value2)
    
    if Ret == True:
        print("First number is greater")
    else:
        print("Second number is greater")

if __name__ == "__main__":
    main()
