retazec = input("Zadaj text:")
print(retazec)
for i, znak in enumerate(retazec):
    print(i, znak)
print(retazec)
for i, znak in enumerate(retazec[::-1]):
    print(-1-i, znak)

#for i in range(len(retazec)):
#    print(i, retazec[i]

#for i in range(-1, -len(retazec) - 1, -1):
#    print(i, retazec[i]