import numpy as np
def fix(inputGrid):
    grid = inputGrid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                grid[i][j] = 9
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = 0
            if grid[i][j] == 0:
                if i > 0 and grid[i - 1][j] == 9:
                    count += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 9:
                    count += 1
                if j > 0 and grid[i][j - 1] == 9:
                    count += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 9:
                    count += 1
                if i < len(grid) - 1 and j < len(grid[i]) - 1 and grid[i + 1][j + 1] == 9:
                    count += 1
                if i > 0 and j < len(grid[i]) - 1 and grid[i - 1][j + 1] == 9:
                    count += 1
                if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] == 9:
                    count += 1
                if i > 0 and j > 0 and grid[i - 1][j - 1] == 9:
                    count += 1
                grid[i][j] = count
    return grid
def makeGrid():
    diffuculty = float(input("Enter the difficulty level (0 to 1): "))
    a = int(input("Enter the number of columns: "))
    b = int(input("Enter the number of rows: "))
    return (np.random.choice([0, 1], size=(a, b), p=[1 - diffuculty,diffuculty]),np.full((a, b), '_', dtype=str))
def main():
    print("Welcome to the Minesweeper game!")
    board,playerBoard = makeGrid()
    keyBoard = fix(board)
    win = False
    lose = False
    print(playerBoard)
    while not win and not lose:
        print("Enter your move")
        row = int(input("Row: "))
        col = int(input("Column: "))
        if board[row][col] == 1:
            print("Game over.")
            lose = True
        else:
            playerBoard[row][col] = keyBoard[row][col]
            if np.all(playerBoard != '_'):
                print("You have revealed all non-mine cells.")
                print("Congratulations! You've cleared the grid.")
                win = True
        print(playerBoard)

    print("Original Grid:")
    print(board)

if __name__ == "__main__":
    main()