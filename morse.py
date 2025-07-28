morse_lista = {'.-': 'a', '-...' : 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
               '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
               '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
               '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
               '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x','-.--': 'y', 
               '--..': 'z',
               '/': ' ', '-.-.--': '!', '.-.-.-': '.', '..--..': '?', '--..--': ',',
               '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
               '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

code = input(f'Adja meg a betüket morse codeban használja ezeket a pontnak:"." és a vonalnak:"-" \n Itt kezdje a morse code-ot: ')

blocks = code.split()
code_hosz = len(blocks)

while 0 < code_hosz:
    print(morse_lista.get(blocks.pop(0)),end='')
    code_hosz -= 1
