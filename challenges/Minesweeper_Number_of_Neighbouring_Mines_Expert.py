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
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
def makeGrid():
    clear_screen()
    diffuculty = float(input("Enter the difficulty level (0 to 1): "))
    a = int(input("Enter the number of columns: "))
    b = int(input("Enter the number of rows: "))
    return (np.random.choice([0, 1], size=(a, b), p=[1 - diffuculty,diffuculty]),np.full((a, b), "\u2588", dtype=str))
def main():
    clear_screen()
    print("Welcome to the Minesweeper game!")
    input("press any key to start")
    board,playerBoard = makeGrid()
    keyBoard = fix(board)
    boardTrack = board.copy()
    win = False
    lose = False
    while not win and not lose:
        clear_screen()
        for i in playerBoard:
            for j in i:
                print(j," ",end = "")
            print()
        
            
        print("Enter your move")
        row = int(input("Row: "))
        col = int(input("Column: "))

        if input("do you want to put a flag(y)?").upper() == 'y'.upper():
            playerBoard[row][col] = '\u2691'
            continue
        if board[row][col] == 1:
            clear_screen()
            print("Game over.")
            if input("do you want to play again(y)?").upper() == 'y'.upper():
                main()
            lose = True
        else:
            playerBoard[row][col] = keyBoard[row][col]
            boardTrack[row][col] = 1
            if np.all(boardTrack == 1):
                clear_screen()
                print("You have revealed all non-mine cells.")
                print("Congratulations! You've cleared the grid.")
                win = True
        
    print("Original Grid:")
    print(board)

if __name__ == "__main__":
    main()
