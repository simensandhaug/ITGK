import numpy as np
import pandas as pd
import re

def read_file(filename):
    f = open(filename, "r")
    arr = []
    for i in range(9):
        line = f.readline().strip("\n")
        arr.append(line)
    for i in range(len(arr)):
        arr[i] = list(map(lambda x: f"{x}" if x != '0' else int(x), arr[i].split(" ")))
    return arr

def save_to_file(board, filename):
    with open(rf"{filename}.txt", 'w') as f:
        for row in board:
            f.write(f"{' '.join(map(str, row))}\n")
        f.close()

f_name = input("Skriv inn filen du vil åpne (eller ingenting hvis du vil generere et nytt brett): ")
board = read_file("board.txt") if f_name == '' else read_file(f"{f_name}.txt")


def print_board(board):
    header = '    0 1 2   3 4 5   6 7 8 '
    divider = '  +-------+-------+-------+'
    print(header)
    for i, v in enumerate(board):
        if(int(i)%3 == 0):
            print(divider)
        tmp = f"{i} "
        for j, c in enumerate(v):
            if((j)%3 == 0):
                tmp += '| '
            if(c == 0):
                tmp += f"{c} "
            elif(len(c) == 2):
                tmp += f"\033[91m{c[0]} \033[0m"
            else:
                tmp += f"\033[94m{c[0]} \033[0m"
        tmp += "|"
        print(tmp)
    print(divider)
    
def validate_input(input):
    return True if re.match("^[0-8] [0-8] [0-9]$", input) else False


def validate_move(x, y, n, board):
    #Rader og Kolonner
    row = y
    col = x
    found = []
    if(board[y][x] != 0 and len(board[y][x]) == 2):
        return False
    for dig in board[y]:
        if dig not in found:
            found.append(str(dig)[0])
    for i in range(9):
        if board[i][x] not in found:
            found.append(str(board[i][x])[0])
    
    #3x3 boks
    # starting pair of index for each square
    index = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    i = 0
    j = 0
    for t in index:
        if( x <= t[0] + 2 and x >= t[0] and y >= t[1] and y <= t[1] + 2):
            i = t[0]
            j = t[1]
    cube = [board[i+m][j+n] for m in range(3) for n in range(3)]
    for dig in cube:
        if dig not in found:
            found.append(str(dig)[0])
    return not str(n) in found

def checkWin(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True
            
                    
        
        
        
while True:
    #Printer board
    print_board(board)
    print("\033[95mSkriv 'save [filename]' for å lagre brettet til fil\033[0m")
    user_input = input("Skriv inn en rute og et tall [x y n] eller lagre: ")
    if(user_input[0:4] == "save"):
        save_to_file(board, user_input[5:])
        break
    if(not validate_input(user_input)):
        print("'\033[93mFeil input\033[0m")
        continue
    user_input = user_input.split(" ") 
    x = int(user_input[0])
    y = int(user_input[1])
    n = int(user_input[2])
    if(not validate_move(x, y, n, board) and n != 0):
        print(f"\033[93m {n} finnes allerede i den raden, kolonnen eller boksen \033[0m")
        continue
    #Gjør trekket
    board[y][x] = f"{n}" if n != 0 else 0
    if(checkWin(board)):
        print_board(board)
        print("Gratulerer du vant!")
        break
    
    