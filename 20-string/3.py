# sifrovanie cezarovou sifrou
retazec = input("Zadaj retazec: ")
posun = int(input("Zadaj posun pre kodovanie: "))
for i in range(len(retazec)):
    #print(retazec[i], ":", ord(retazec[1]))
    print(f"{retazec[i]}:{ord(retazec[i])}")

retazec_kod = ""
for i in range(len(retazec)):
    retazec_kod += chr(ord(retazec[i]) + posun)

print(f"Zakodovany retazec: {retazec_kod}")
