
while True:
    n = int(input("Zadaj n(Pre ukoncenie zadaj 0): "))
    print("Prvocisla:", end=" ")
    for cislo in range(2, (n // 2) + 1):
        pocet = 0
        for delitel in range(1, n + 1):
            if cislo % delitel == 0:
                pocet += 1     # pocet = pocet + 1
        if pocet == 2:
            print(cislo, end=" ")
    print()
    if n == 0:
         break