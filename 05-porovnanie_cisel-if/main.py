"""
a = int(input("Zadaj cislo a: "))
b = int(input("Zadaj cislo b: "))
c = int(input("Zadaj cislo c: "))
if a == b == c:
    print("Cisla sa rovnaju")
else:
    if a > b:
        if a > c:
            print("Najvacsie cislo je ", a)
        else:
            print("Najvacsie cislo je", c)
    else:
        if b > c:
            print("Najvacsie cislo", b)
        else:
            print("Najvacsie cislo je",c)
"""
a = int(input("Zadaj cislo a: "))
b = int(input("Zadaj cislo b: "))
c = int(input("Zadaj cislo c: "))
d = int(input("Zadaj cislo d: "))
e = int(input("Zadaj cislo e: "))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print("Najvacsie cislo je:", max)

