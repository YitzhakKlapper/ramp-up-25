def length(num):
    temp = str(num)
    count = 0
    for i in temp:
        if i.isdigit():
            count += 1
    return count

def main():
    num = input("Enter a number: ")
    print(length(num))

if __name__ == "__main__":
    main()