def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

num1 = float(input(f'Adja meg az első számot: '))
num2 = float(input(f'Adja meg a második számot: '))
choice = int(input(f' 1: szorzás \n 2: osztás \n 3: hatvány \n Válasza ki hogy mit szeretne velük csinálni: '))

while choice not in (1,2,3):
    choice = int(input(f'Hiba! \n 1: szorzás \n 2: osztás \n 3: hatvány \n Válasza ki hogy mit szeretne velük csinálni: '))

if choice == 1:
    print(multiply(num1, num2))
elif choice == 2:
    print(division(num1, num2))
else:
    print(power(num1, num2))