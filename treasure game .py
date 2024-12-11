import random
from collections import deque

"""
grid legend
- = player
0 = free space
T = trap
P = power up
X = treasure
"""



def main():
    print("welcome to the treasure game")
    grid = creategrid()
    menuChoice = 0
    playerHealth = 3
    while menuChoice != 4:
        print("1.Move\n2.Search\n3.Check HP\n4.Quit")
        try:
            menuChoice = int(input())
        except(ValueError):
            print("invalid input")
        if menuChoice == 1:
            print("\nChoose a direction:\n1. UP\n2. DOWN\n3. LEFT\n4. RIGHT\n5. QUIT")
            choice = input("Enter your choice (1-5): ") 
            #dictionary translates number choice to a direction. This prevents crashing in a more efficient way than using try except statements
            direction_map = {
                '1': 'UP',
                '2': 'DOWN',
                '3': 'LEFT',
                '4': 'RIGHT'
            }
            #checks if the users input is valid in the dictionary
            if choice in direction_map:
                result = move(grid, direction_map[choice], playerHealth)
                if result == False:
                    break
            else:
                print("invalid choice")

        if menuChoice == 2:
            for i in range(5):
                print("\n", grid[i])
            searchChoice = 0
            print("which type of search would you like to do")
            print("1.BS\n2.BFS\n3.DFS")
            searchChoice = int(input())
            if searchChoice == 1:
                print("treasure is at: ", binary_search(grid))
            if searchChoice == 2:
                bfs(grid)
            if searchChoice == 3:
                pass

        if menuChoice == 3:
            checkHP(playerHealth)

        if menuChoice == 4:
            break
    print("thanks for playing")

def creategrid():
    #initialises grid with 0s. points on grid can be accessed with [row][collumn]
    grid = [[0 for i in range(5)] for i in range(5)]
    #creates traps at a random point
    for i in range(8):
        grid[random.randint(0,4)][random.randint(0,4)] = 'T'
    #Creates a power up at random points
    for i in range(5):
        grid[random.randint(0,4)][random.randint(0,4)] = 'P'
    # #X is treasure. creates a treasure at a random point
    grid[random.randint(0,4)][random.randint(0, 4)] = 'X'
    #creates the player/pointer. this will be used to interact with traps, powerups and the treasure
    grid[0][random.randint(0,4)] = '-'
    return(grid)

def find_player(grid):
    for row_idx,row in enumerate(grid): #enumerate allows the grids row/collumn values to be split into two seperate variables
        for col_idx, cell in enumerate(row):
            if cell =='-':
                return (row_idx, col_idx)

def find_treasure(grid):
    for row_idx,row in enumerate(grid): #enumerate allows the grids row/collumn values to be split into two seperate variables
        for col_idx, cell in enumerate(row):
            if cell =='X':
                return (row_idx, col_idx)

def move(grid, direction, playerHealth):
    menuChoice=0
    #finds player position
    player_position = find_player(grid) 
    print("player position is ", player_position)
    #stores the players row and column position
    row, col = player_position
    #creates a variable for the new player positions. This is so I can delete the old player position later. If i didnt do this the grid would be full of different player positions causing issues.
    new_row, new_col = row, col

    if direction == 'UP':
        new_row -= 1
    elif direction == 'DOWN':
        new_row += 1
    elif direction == 'LEFT':
        new_col -= 1
    elif direction == 'RIGHT':
        new_col += 1
    
    #checks if within boundries of the grid 
    if 0 <= new_row < 5 and 0 <= new_col < 5:
        #deletes the old player position1
        grid[row][col] = 0

        if grid[new_row][new_col] == 'T':
            grid[new_row][new_col] = '-'
            print("You have moved to ", find_player(grid))
            print("you walked into a trap and lose 1HP!")
            playerHealth -= 1
            if playerHealth == 0:
                print("you ran out of HP and died... sorry...")
                return False
            return grid, True
        elif grid[new_row][new_col] == 'X':
            grid[new_row][new_col] = '-'
            print("You have moved to ", find_player(grid))
            print("you found the treasure! Congrats!")
            return False
        if grid[new_row][new_col] == 'P':
            grid[new_row][new_col] = '-'
            print("You have moved to ", find_player(grid))
            print("you found a powerup!")
            playerHealth += 1
            print("your health is now ", playerHealth)
            return grid, True

        #moves player marker to new player position after movement
        grid[new_row][new_col] = '-'
        print("You have moved to ", find_player(grid))
        return grid, True
    else:
        print("cannot move out of bounds")
    return grid, True

def binary_search(grid):
    #turns 2d grid into 1d list for binary search
    rows = len(grid)
    cols = len(grid[0])

    flat_grid = [grid[r][c] for r in range(rows) for c in range(cols)]

    left = 0
    right = len(flat_grid) - 1

    while left<= right:
        mid = (left + right)//2 #calculates the middle of the list
        #converts 1d index back into 2d grid cordinates
        row = mid//cols
        col = mid%cols
        if grid[row][col] == 'X':
            print(row, col)
        left  += 1
        right -= 1
        
    #grid is randomised so it doesnt really make any sense to do a binary search as for a binary search to work the list needs to be ordered
    #doing linear search instead (which is already done at find_treasure())
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                return (r, c)
      
    return (row, col)

def bfs(grid):
    #possible moves pointer can make (left right down up)
    moves = [ [-1,0], [1,0], [0,-1], [0,1]]
    rows=len(grid)
    cols=len(grid[0])

    start = find_player(grid)
    #array to store visited nodes on grid
    visited = [[False] * cols for i in range(rows)]
    #array to store coords of the cell that led to current cell
    parent = [[None]* cols for i in range(rows)]

    queue = deque([start])
    
    visited[start[0]][start[1]] = True
    while len(queue):
        current_row, current_col = queue.popleft()
        
        if grid[current_row][current_col] == 'X':
            #reconstructs path taken to get to treasure
            path = []
            while (current_row, current_col)!= start:
                path.append((current_row, current_col))
                current_row, current_col = parent[current_row][current_col]
            path.append(start)
            path.reverse()

            print("shortest path to treasure:")
            for step in path:
                print(step)
            return path
        
        #explores surrounding cells 
        for dx, dy in moves:
            new_row = current_row + dx
            new_col = current_col + dy
            #checks if next move is in bounds and not already visited 
            if (0 <= new_row <rows and
                0<= new_col < cols and
                not visited[new_row][new_col]):

                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (current_row, current_col)
    print("An error has occured and there is no path to treasure")

def dfs(grid):
    pass

def checkHP(playerHealth):
    print("HP = ",playerHealth)

if __name__ == "__main__":
    main()