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
        return 'o'

def check_board():
    if '_' in board_alap:
        return True
    else:
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
                lepes_szam +=1
                print_board()
            else:
                print('ez a mezö már foglalt')
        except ValueError:
            print("Hiba valamit roszul adtál meg")
    step = 'not_valid'
print('A tábla megtelt döntetlen.')