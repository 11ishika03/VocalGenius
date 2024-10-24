def maze_puzzle():
    print("Welcome to the Maze Puzzle!")
    maze = [
        ["S", " ", "X", "X", "X", "X", "X"],
        ["X", " ", "X", " ", " ", " ", "X"],
        ["X", " ", "X", " ", "X", " ", "X"],
        ["X", " ", " ", " ", "X", " ", "E"],
        ["X", "X", "X", "X", "X", "X", "X"]
    ]
    
    start = (0, 0)
    end = (3, 6)
    current_position = start

    while current_position != end:
        for row in maze:
            print(" ".join(row))
        move = input("Enter your move (up, down, left, right): ").lower()
        
        row, col = current_position
        if move == "up" and row > 0 and maze[row-1][col] == " ":
            maze[row][col] = " "
            maze[row-1][col] = "S"
            current_position = (row-1, col)
        elif move == "down" and row < len(maze)-1 and maze[row+1][col] == " ":
            maze[row][col] = " "
            maze[row+1][col] = "S"
            current_position = (row+1, col)
        elif move == "left" and col > 0 and maze[row][col-1] == " ":
            maze[row][col] = " "
            maze[row][col-1] = "S"
            current_position = (row, col-1)
        elif move == "right" and col < len(maze[0])-1 and maze[row][col+1] == " ":
            maze[row][col] = " "
            maze[row][col+1] = "S"
            current_position = (row, col+1)
        else:
            print("Invalid move! Try again.")

    print("Congratulations! You've completed the maze!")

if __name__ == "__main__":
    maze_puzzle()