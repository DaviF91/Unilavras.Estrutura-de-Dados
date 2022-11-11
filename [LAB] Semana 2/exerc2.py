#Faça um programa em Python que leia uma matriz 3 x 3. O programa deverá preencher com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz original e a matriz obtida após o processamento.

m = []

line = 3
column = 3


for i in range(line):
    line = []
    for j in range(column):
        line.append(float(input("Linha %d | Coluna %d:" %(i,j))))
    m.append(line)
print()

for i in range(len(m[i])):
        print(f'{m[i]}', end='')
        print()
print()

for i in range(0,3):
    for j in range(0,3):
        if m[i] == m[j]:
            m[i][j] = 1
        else:
            m[i][j] = 0
    print(m[i])

    
    


