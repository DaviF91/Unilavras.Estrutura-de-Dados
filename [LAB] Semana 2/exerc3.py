#Faça um programa em Python que leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor desta matriz.

m = []
maiorValor = 0
lMaior = ''
cMaior = ''

for linha in range(4):
    linhas = []
    for coluna in range(4):
        num = float(input(f'Linha: {linha} | Coluna {coluna}: '))
        if num > maiorValor:
            maiorValor = num
            lMaior = linha
            cMaior = coluna
        linhas.append(num)
    m.append(linhas)
print()

for c in range(len(m)):
    print(m[c])
print()
print("Maior valor: %.2f" %(maiorValor))
print(f'[Posição: Linha {lMaior} | Coluna {cMaior}]')