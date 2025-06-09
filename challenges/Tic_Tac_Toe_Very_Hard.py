
def compare(graph,s):
    for i in range(3):
        if graph[i][0] == s and graph[i][1] == s and graph[i][2] == s:
            return True
    for i in range(3):
        if graph[0][i] == s and graph[1][i] == s and graph[2][i] == "s":
            return True
    if graph[0][0] == s and graph[1][1] == s and graph[2][2] == s:
        return True
    if graph[0][2] == s and graph[1][1] == s and graph[2][0] == s:
        return True
def check(graph):
    if compare(graph, "X"):
        return "X won"
    if compare(graph, "O"):
        return "O won"
# added a main function that lets in user input for the game
def main():
    graph = [[None,None,None], [None,None,None], [None,None,None]]
    for i in range(3):
        for j in range(3):
            print("Enter X or O:")
            graph[i][j] = input().upper()
    for i in graph:
        print(i)
    result = check(graph)
    print(result)

if __name__ == "__main__": 
    main()