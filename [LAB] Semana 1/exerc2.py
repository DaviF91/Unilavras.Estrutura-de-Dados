#Faça um programa que preencha uma lista com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.

list = []
somaneg = 0
somapos = 0
for i in range(10):
    num = float(input(f"Digite o {i + 1}º número: "))
    if num < 0:
        somaneg += 1
    else:
        somapos += num
    list.append(num)

print(f"Quantidade de números negativos : {somaneg}")
print(f"Soma dos valores positivos : {somapos:.2f}")