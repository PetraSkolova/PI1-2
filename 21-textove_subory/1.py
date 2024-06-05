fmena = open('mena.txt',  'r', encoding='utf-8') #otvori subor mena.txt na citanie r-citanie, w-zapis   #relativna cesta, utf-8 = kodovanie
# fmena = open('C:/dokumenty/mena.txt',  'r') #absolutna cesta suboru

while True:
    riadok = fmena.readline()
    if riadok == '':
        break
    print(riadok[:-1]) #[:-1] vypise vsretky znaky od 0 po predposledny



fmena.close() #zatvorenie suboru, vzdy treba!!!