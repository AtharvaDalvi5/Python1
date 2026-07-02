def Table(no):
    for i in range(1,11):
        print(no * i)

def main():
    print("Enter the number prints multiplication Table : ")
    no = int(input())
    Table(no)

if __name__ == "__main__":
    main()
