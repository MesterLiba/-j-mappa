hex_matrix = {'61': 'a', '62': 'b',
              '63': 'c', '64': 'd',
              '65': 'e', '66': 'f',
              '67': 'g', '68': 'h',
              '69': 'i', '6a': 'j',
              '6b': 'k', '6c': 'l',
              '6d': 'm', '6e': 'n',
              '6f': 'o', '70': 'p',
              '71': 'q', '72': 'r',
              '73': 's', '74': 't',
              '75': 'u', '76': 'v',
              '77': 'w', '78': 'x',
              '79': 'y', '7a': 'z',
            }

hex_code = input('Adja me a hex code-ot spacekel elválasztva: ')
hex_lista = hex_code.split()
hex_lista2 = list(hex_lista)
i = 4
while 0 < i:
    print(hex_matrix.get(hex_lista2.pop(0)),end='')
    i-=1