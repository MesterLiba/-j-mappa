# 1 feladat
szam = int(input("Adj meg egy számot:"))

if szam % 2 == 0:
    szam2 = int(input("Adj meg egy számot:"))
    if szam == szam2:
        print(f"A két beadott szám egyenlő ezek voltak a számaid: {szam}, {szam2}")
    else:
        print(f"A két beadott szám nem egyenlő ezek voltak a számaid: {szam}, {szam2}")
else:
    print(f'{szam} nem páros')