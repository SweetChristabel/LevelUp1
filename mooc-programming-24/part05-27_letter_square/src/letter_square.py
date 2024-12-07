# Write your solution here
layers = int(input("Layers: "))
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters2use = letters[:layers]
esu2srettel = letters2use[::-1]
matrix = []
row = []
lastrow = []
for nr in range(1, 2*layers):
    lastrow.append(letters2use[-1])

for nr in range(0, layers-1):


    for i in esu2srettel[:-1]:
        row.append(i)
    for i in letters2use:
        row.append(i)


    for ltr in letters2use[:nr+1]:
        letters2use[letters2use.index(ltr)] = letters2use[nr+1]
        
    esu2srettel = letters2use[::-1]
    matrix.append(row)
    row = []

matrix.append(lastrow)


for nr in range(1,len(matrix)):
    matrix.insert(nr-1,matrix[-nr])

for row in matrix:
    for letter in row:
        print(letter,end="")
    print()
