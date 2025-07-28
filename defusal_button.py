szin = input('Add meg a gomb szinét: ')
text = input('Add meg a gombnak a szavát: ')

def clicks(num):
    if num >= 2:
        print(num)
        print('Up')
        return
    else:
        print(num)
        print('Down')
        return

if szin == 'blue' and text == 'detonate':
    click_count = 1
    eredmeny = clicks(click_count)
elif szin == 'red':
    click_count = 2
    eredmeny = clicks(click_count)
elif text == 'abort':
    click_count = 3
    eredmeny = clicks(click_count)
elif szin == 'grey' or 'white':
    click_count = 4
    eredmeny = clicks(click_count)