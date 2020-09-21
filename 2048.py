import msvcrt
import random
import os

def clear():
    '''
    It clears the screen.
    '''

    os.system('cls')

def InitMatrix():
    '''
    It initializes the matrix as a board game.
    '''

    m = [[0 for i in range(4)] for j in range(4)]
    for i in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while m[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        m[x][y] = 2

    return m


def ShowMatrix():
    '''
    It displays the matrix on the screen.
    '''

    for col in m:
        for elem in col:
            print("{:6d}".format(elem), end = " ")
        print()

def MoveDown():
    '''
    When the down key is pressed it computes to the bottom of the matrix the
    adjacent elements with the same value and moves the other elements in the
    same direction if there are empty cells.
    '''

    global movement
    for j in range(4):
        for i in range(3, -1, -1):
            x = i - 1
            while x > -1:
                if m[i][j] != 0 and m[i][j] != m[x][j] and m[x][j] != 0:
                    break
                elif m[x][j] == m[i][j] and m[i][j] != 0:
                    aux = m[i][j]
                    m[i][j] = m[x][j] + aux
                    m[x][j] = 0
                    movement = True
                    break
                elif m[i][j] == 0 and m[x][j] != 0:
                    m[i][j] = m[x][j]
                    m[x][j] = 0
                    movement = True
                x -= 1


def MoveUp():
    '''
    It computes to the matrix upper side the adjacent elements with the same
    value and moves the other elements to the same side if there are empty cells
    when the up key is pressed.
    '''

    global movement
    for j in range(4):
        for i in range(3):
            x = i + 1
            while x < 4:
                if m[i][j] != 0 and m[i][j] != m[x][j] and m[x][j] != 0:
                    break
                elif m[x][j] == m[i][j] and m[i][j] != 0:
                    aux = m[i][j]
                    m[i][j] = m[x][j] + aux
                    m[x][j] = 0
                    movement = True
                    break
                elif m[i][j] == 0 and m[x][j] != 0:
                    m[i][j] = m[x][j]
                    m[x][j] = 0
                    movement = True
                x += 1


def MoveLeft():
    '''
    It computes to the matrix left side the adjacent elements with the same
    value and moves the other elements to the same side if there are empty cells
    when the left key is pressed.
    '''

    global movement
    for i in range(4):
        for j in range(3):
            x = j + 1
            while x < 4:
                if m[i][j] != 0 and m[i][j] != m[i][x] and m[i][x] != 0:
                    break
                elif m[i][x] == m[i][j] and m[i][j] != 0:
                    aux = m[i][j]
                    m[i][j] = m[i][x] + aux
                    m[i][x] = 0
                    movement = True
                    break
                elif m[i][j] == 0 and m[i][x] != 0:
                    m[i][j] = m[i][x]
                    m[i][x] = 0
                    movement = True
                x += 1


def MoveRight():
    '''
    It computes to the matrix right side the adjacent elements with the same
    value and moves the other elements to the same side if there are empty cells
    when the right key is pressed.
    '''

    global movement
    for i in range(4):
        for j in range(3, -1, -1):
            x = j - 1
            while x > -1:
                if m[i][j] != 0 and m[i][j] != m[i][x] and m[i][x] != 0:
                    break
                elif m[i][x] == m[i][j] and m[i][j] != 0:
                    aux = m[i][j]
                    m[i][j] = m[i][x] + aux
                    m[i][x] = 0
                    movement = True
                    break
                elif m[i][j] == 0 and m[i][x] != 0:
                    m[i][j] = m[i][x]
                    m[i][x] = 0
                    movement = True
                x -= 1

def SupplyElem():
    '''
    It inserts a new element (2 or 4) in an random empty cell if at least the two
    adjacent elements have been computed or an element has been moved to a new
    cell.
    '''

    if movement == True:
        RandomElem()

def RandomElem():
    '''
    It generates the position where the new element will be inserted.
    '''

    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while m[x][y] != 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    m[x][y] = random.randrange(2, 5, 2)

#===========================================================


m = InitMatrix()
max_value = 2

while max_value <= 2048:

    movement = False
    clear()
    print("2048")
    ShowMatrix()

    keypress = ord(msvcrt.getch())
    if keypress == 224:
        keypress = ord(msvcrt.getch())

    if keypress == 75:
        MoveLeft()
        SupplyElem()
    if keypress == 72:
        MoveUp()
        SupplyElem()
    if keypress == 77:
        MoveRight()
        SupplyElem()
    if keypress == 80:
        MoveDown()
        SupplyElem()
    if keypress == 27: # ESC
        break

    min_value = min(map(min, m))
    max_value = max(map(max, m))

    if movement == False and min_value != 0:
        clear()
        print("\nYOU HAVE LOST!")
        print(f"\nSCORE: {max_value}")
        with open("D:/Work/Jocuri/2048/Score.txt", "a") as scorefile:
            scorefile.write(f" {str(max_value)}")
        with open("D:/Work/Jocuri/2048/Score.txt", "r") as scorefile2:
            score_read = scorefile2.read()
            list_score = score_read.split()
            list_score = [int(elem) for elem in list_score]
            print(f"\nHigh score: {max(list_score)}")
        quit()

    if max_value == 2048:
         print("\nYOU HAVE WON!")
         print(f"\nSCORE: {max_value}")
         with open("D:/Work/Jocuri/2048/Score.txt", "a") as scorefile:
             scorefile.write(f" {str(max_value)}")
         with open("D:/Work/Jocuri/2048/Score.txt", "r") as scorefile2:
             score_read = scorefile2.read()
             list_score = score_read.split()
             list_score = [int(elem) for elem in list_score]
             print(f"\nHigh score: {max(list_score)}")
         quit()
