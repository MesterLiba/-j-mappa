a = int(input('Szám 1: '))
b = int(input('Szám 2: '))
c = int(input('Szám 3: '))
d = int(input('Szám 4: '))

def label1(a):
    x = 0
    if a < 10:
        x += 15
    elif 10 <= a <= 20:
        x += 20
    elif 20 < a <= 80:
        x += 30
    else:
        x += 10
    return x

def label2(x, b):
    if b < 10:
        x += 10
    elif 10 <= b <= 20:
        x *= 2
    elif 20 < b <= 80:
        x *= 3
    else:
        x -= 10
    return x

def label3(x, c):
    if c < 10:
        x *= 2
    elif 10 <= c <= 20:
        x *= 3
    elif 20 < c <= 80:
        x -= 5
    else:
        x
    return x

def label4(x, d):
    if d < 10:
        x *= 2
    elif 10 <= d <= 20:
        x += 20
    elif 20 < d <= 80:
        x += 80
    else:
        x *= 3
    return x

eredmeny1 = label1(a)
eredmeny2 = label2(eredmeny1, b)
eredmeny3 = label3(eredmeny2, c)
eredmeny4 = label4(eredmeny3, d)

eredmeny4 -= (a + b + c + d)/2

if eredmeny4 <= 0:
    print(1, 2, 3, 4)
elif 0.5 <= eredmeny4 <= 19.5:
    print(1, 2, 4, 3)
elif 20 <= eredmeny4 <= 49.5:
    print(4, 3 ,2 ,1)
elif 50 <= eredmeny4 <= 89.5:
    print(2, 4, 1, 3)
else:
    print(3, 1, 2, 4)