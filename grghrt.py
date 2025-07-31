def label(x, n, index):
    if index == 0:  # label1 logika
        if n < 10:
            x += 15
        elif n <= 20:
            x += 20
        elif n <= 80:
            x += 30
        else:
            x += 10
    elif index == 1:  # label2 logika
        if n < 10:
            x += 10
        elif n <= 20:
            x *= 2
        elif n <= 80:
            x *= 3
        else:
            x -= 10
    elif index == 2:  # label3 logika
        if n < 10:
            x *= 2
        elif n <= 20:
            x *= 3
        elif n <= 80:
            x -= 5
    else:  # label4 logika
        if n < 10:
            x *= 2
        elif n <= 20:
            x += 20
        elif n <= 80:
            x += 80
        else:
            x *= 3
    return x

# --- Főprogram ---
numbers = [int(input(f"Szám {i+1}: ")) for i in range(4)]

x = 0
for i, n in enumerate(numbers):
    x = label(x, n, i)
    
x -= sum(numbers) / 2

# Eredmény alapján döntés
if x <= 0:
    print(1, 2, 3, 4)
elif x <= 19.5:
    print(1, 2, 4, 3)
elif x <= 49.5:
    print(4, 3, 2, 1)
elif x <= 89.5:
    print(2, 4, 1, 3)
else:
    print(3, 1, 2, 4)
