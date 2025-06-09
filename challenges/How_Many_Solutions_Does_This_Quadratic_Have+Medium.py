
def count(a,b,c):
    if(b**2 - 4*a*c < 0):
        return 0
    elif(b**2 - 4*a*c == 0):
        return 1
    else:
        return 2

def main():
    a = int(input("Enter the coefficient a: "))
    b = int(input("Enter the coefficient b: "))
    c = int(input("Enter the coefficient c: "))

    numberOfSulutions = count(a,b,c)
    print("Number of solutions:", numberOfSulutions)


if __name__ == "__main__":
    main()