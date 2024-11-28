import random

def main():
    print("welcome to the treasure game")
    creategrid()
    menuChoice = 0
    playerHealth = 3
    while menuChoice != 4:
        print("1.Move\n2.Search\n3.Check HP\n4.Quit")
        menuChoice = int(input())
        if menuChoice == 1:
            move()
        if menuChoice == 2:
            search()
        if menuChoice == 3:
            checkHP()
        if menuChoice == 4:
            break
        else:
            print("invalid input please input a number 1-4")
    print("thanks for playing!")

def creategrid():
    row1 = ['1','2','3','4','5']
    row2 = ['1','2','3','4','5']
    row3 = ['1','2','3','4','5']
    row4 = ['1','2','3','4','5']
    row5 = ['1','2','3','4','5']
    #O is treasure. creates a treasure at a random point in the bottom row
    row5[random.randint(0, 4)] = 'O'
    #X is a trap. creates traps at a random point in rows 1-4
    row1[random.randint(0, 4)] = 'X'
    row2[random.randint(0, 4)] = 'X'
    row3[random.randint(0, 4)] = 'X'
    row4[random.randint(0, 4)] = 'X'
    #P is a power up. creates a power up at a random point in rows 2 and 4
    row2[random.randint(0,4)] = 'P'
    row4[random.randint(0,4)] = 'P'

def move():
    pass

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
    

def checkHP():
    print("HP = ", )


if __name__ == "__main__":
    main()