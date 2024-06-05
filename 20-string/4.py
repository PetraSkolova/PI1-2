retazec = input("Zadaj vetu: ")
"""""
for i in range(retazec):
    print(f"{retazec[i]}:{ord(retazec[i])}")

    if "a" in "aeiouy":
        print("samohlaska")
    else:
        print("spolohlaska")"""

samohlasky = 0
spoluhlasky = 0
for znak in retazec:
    if znak in "aeiouy":
        samohlasky += 1
    else:
        spoluhlasky += 1
print(f"samohlasky: {samohlasky}\nspoluhlasky: {spoluhlasky}")

