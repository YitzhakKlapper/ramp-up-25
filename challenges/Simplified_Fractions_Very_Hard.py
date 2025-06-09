def simplify(s):
    a = s.split('/')
    n = int(a[0])
    d = int(a[1])

    g = gcd(n, d)
    n /= g
    d /= g

    n = int(n)
    d = int(d)

    return "{}/{}".format(n, d)

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def main():
    s = input("enter fraction to simplify: ")
    print("simplified:", simplify(s))

if __name__ == "__main__":
    main()