from math import pi

def radians_to_degrees(radians):
    return radians * (180 / pi)

def main():
    radians = float(input("radians: "))
    deg = radians_to_degrees(radians)
    print("degrees:",deg)
if __name__ == "__main__":
    main()