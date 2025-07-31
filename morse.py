morse_lista = {'.-': 'a', '-...' : 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
               '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
               '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
               '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
               '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x','-.--': 'y', 
               '--..': 'z',
               '/': ' ', '-.-.--': '!', '.-.-.-': '.', '..--..': '?', '--..--': ',',
               '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
               '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
               }

reverse_morse = {ertek: kulcs for kulcs, ertek in morse_lista.items()}

choice = input('Válaszd ki hogy "decode"-ot szeretnél irni vagy "encode"-olni: ')
if choice == 'decode':
    decode = input(f'Adja meg a betüket morse codeban használja ezeket a pontnak:"." és a vonalnak:"-" \n Itt kezdje a morse code-ot: ')

    blocks = decode.split()
    decode_hosz = len(blocks)

    while 0 < decode_hosz:
        print(morse_lista[(blocks.pop(0))],end='')
        decode_hosz -= 1
elif choice == 'encode':
    encode = input(f'Adja be a code-olásra szánt söveget: ')
    
    betu = len(encode)
    betu = list(encode)
    encode_hosz = len(encode)
    
    while 0 < encode_hosz:
        print(reverse_morse[(betu.pop(0))],end=' ')
        encode_hosz -=1