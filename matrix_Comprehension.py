board_alap = ['_' for _ in range(9)]

def print_board():
    for i in range(0, len(board_alap), 3):
        row = board_alap[i:i+3]
        print('  '.join(row))
    print()

def change_mark():
    if lepes_szam %2 == 0:
        return 'x'
    else:
        return 'O'

def check_board():
    if '_' in board_alap:
        return True
    else:
        return False
    
def check_win():
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # sorok
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # oszlopok
        [0, 4, 8], [2, 4, 6]             # átlók
        ]
    for pos in win_positions:
        if board_alap[pos[0]] == board_alap[pos[1]] == board_alap[pos[2]] != '_':
            return True
    return False
    
step = 'not_valid'
lepes_szam = 0


while check_board() == True:
    while step != 'valid':
        try:
            p1i = int(input(f"Hova szeretnéd rakni 1-9 : "))-1
            if board_alap[p1i] == '_':
                board_alap[p1i] = change_mark()
                step = 'valid'
                print_board()
            else:
                print('ez a mezö már foglalt')
        except ValueError:
            print("Hiba valamit roszul adtál meg")
    step = 'not_valid'
    if check_win():
        print(f"A(z) {change_mark()} játékos nyert!")
        break
    lepes_szam +=1

print('A tábla megtelt döntetlen.')