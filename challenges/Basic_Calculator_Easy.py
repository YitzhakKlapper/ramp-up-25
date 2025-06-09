def calculator(a,o,b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        if b == 0:
            return "Can't divide by 0!"
        return a / b

def main():
    a = float(input("a: "))
    o = input("operator: ").strip()
    b = float(input("b: "))
    
    result = calculator(a, o, b)
    print(f"The result of {a} {o} {b} is: {result}")

if __name__ == "__main__":
    main()