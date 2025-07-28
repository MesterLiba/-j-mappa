wires = int(input('Add meg a kábelek számát: '))

a = 'none'
b = 'none'
c = 'none'
d = 'none'
e = 'none'
if wires == 3:
    a = input('1szin: ')
    b = input('2szin: ')
    c = input('3szin: ')
    if a or b or c == 'red':
        print('vágd el az "1" kábelt')
    elif a or b or c == 'white':
        print('vágd el az "2" kábelt')
    else:
        print('vágd el az "3" kábelt')
elif wires == 4:
    a = input('1szin: ')
    b = input('2szin: ')
    c = input('3szin: ')
    d = input('4szin: ')
    if a or b or c or d != 'green':
        print('vágd el az "1" kábelt')
    elif a or b or c or d != 'blue':
        print('vágd el az "2" kábelt')
    elif a or b or c or d != 'white':
        print('vágd el az "3" kábelt')
    else:
        print('vágd el az "4" kábelt')
else:
    a = input('fény szin: ')
    if a == 'red':
        print('vágd el az "1" kábelt')
    elif a == 'green':
        print('vágd el az "2" kábelt')
    elif a == 'blue':
        print('vágd el az "3" kábelt')
    elif a == 'yellow':
        print('vágd el az "4" kábelt')
    else:
        print('vágd el az "5" kábelt')
