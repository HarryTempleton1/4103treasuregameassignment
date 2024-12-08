import random

def main():
    print("welcome to the treasure game")
    grid = creategrid()
    menuChoice = 0
    playerHealth = 1
    while menuChoice != 4:
        print("1.Move\n2.Search\n3.Check HP\n4.Quit")
        menuChoice = int(input())
        if menuChoice == 1:
            print("\nChoose a direction:\n1. UP\n2. DOWN\n3. LEFT\n4. RIGHT\n5. QUIT")
            choice = input("Enter your choice (1-5): ")
            #dictionary translates number choice to a direction
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
            print(grid)
        if menuChoice == 3:
            checkHP(playerHealth)
        if menuChoice == 4:
            break
    print("thanks for playing")

def creategrid():
    #initialises grid with 0s. points on grid can be accessed with [row][collumn]
    grid = [[0 for i in range(5)] for i in range(5)]
    # #X is treasure. creates a treasure at a random point in the bottom row
    grid[4][random.randint(0, 4)] = 'X'
    #creates traps at a random point in rows 2-4 (not on row 1 as that is where the player will spawn)
    grid[1][random.randint(0,4)] = 'T'
    grid[2][random.randint(0,4)] = 'T'
    grid[3][random.randint(0,4)] = 'T'
    #Creates a power up at a random point on rows 2 and 4
    grid[1][random.randint(0,4)] = 'P'
    grid[3][random.randint(0,4)] = 'P'
    #creates the player/pointer. this will be used to interact with traps, powerups and the treasure
    grid[0][random.randint(0,4)] = '-'
    return(grid)

def find_player(grid):
    for row_idx,row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell =='-':
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
        #deletes the old player position
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
    
    print("cannot move out of bounds")
    return grid, True

def search():
    searchChoice = 0
    print("which type of search would you like to do")
    print("1.BS\n2.DFS\n3.BFS")
    searchChoice = int(input())
    if searchChoice == 1:
        pass
    if searchChoice == 2:
        pass
    if searchChoice == 3:
        pass
    else:
        print("invalid input")
    

def checkHP(playerHealth):
    print("HP = ",playerHealth)

if __name__ == "__main__":
    main()