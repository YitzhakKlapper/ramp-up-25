def flip(x):
    x = str(x)
    flipped = []
    for i in x:
        if i == '0':
            flipped.append('1')
        elif i == '1':
            flipped.append('0')
    return flipped

def numToBinary(num):
    return format(int(num), '032b')

def binaryToNum(binary):
    num = int(binary,2)
    return num

def main():
    num = input("enter num: ")
    bi = numToBinary(num)
    print("binary:", bi)
    flipped = flip(bi)
    print("flipped:", ''.join(flipped))
    flipped_num = binaryToNum(''.join(flipped))
    print("flipped num:", flipped_num)

if __name__ == "__main__":
    main()