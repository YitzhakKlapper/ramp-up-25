#pie_chart({ "a": 1, "b": 2 }) ➞ { "a": 120, "b": 240 }

def pieChart(data):
    TOTAL = 360
    toRet = {}
    for key in data:
        temp = ((data[key] / sum(data.values())) * TOTAL)
        temp = round(temp,1)
        toRet[key] = temp
    return toRet
    
def main():
    data = {"a": 34, "b": 35,"c": 31,"d": 54, "e": 45,"f": 131}
    result = pieChart(data)
    print(result)

if __name__ == "__main__":
    main()