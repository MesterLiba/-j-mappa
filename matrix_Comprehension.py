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
    if '_' not in board_alap:
        return False
    return True  
 
playing = True
step = 'not_valid'
lepes_szam = 0

while playing == True:
    while step != 'valid' :
        p1i = int(input(f"Hova szeretnéd rakni 1-9 : "))-1
        if board_alap[p1i] == '_':
            board_alap[p1i] = change_mark()
            step = 'valid'
            lepes_szam +=1
            print_board()
            playing = check_board()
        else:
            print("Ez a mező már foglalt!")
        step = 'not_valid'
        

    
            





    

    












# def for_loop(n):
#     my_list = []
#     for x in range(n):
#         my_list.append(x)
#     return my_list

# result = for_loop(25)

# my_new_list = [x for x in range(21) if x %2 == 0 ]
# print(my_new_list)