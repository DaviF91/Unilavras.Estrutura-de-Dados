#Faça um programa em Python que leia uma matriz 4 x 4. Mostre a matriz recebida, e escreva quantos valores maiores que 10 ela possui.

m = []

line = 4
column = 4


for i in range(line):
    line = []
    for j in range(column):
        line.append(float(input("Linha %d | Coluna %d:" %(i,j))))
    m.append(line)
print()

for i in range(len(m[i])):
        print(f'{m[i]}', end='')
        print()


valor = 0
for i in range(4):
    for j in range(4):
        if m[i][j] > 10:
            valor = valor + 1

print("\nExistem %d números > 10 na matriz informada!" %(valor))



