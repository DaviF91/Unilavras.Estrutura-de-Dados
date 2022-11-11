#Faça um programa que receba e armazene em uma lista 8 valores float, em seguida mostre:
  #lista preenchida com os valores recebidos.
  #maior valor dessa lista e em qual posição ele se encontra.
  #menor valor dessa lista e em qual posição ele se encontra.

list = []

for i in range(8):
    list.append(float(input(f"Digite o {i +1}º número: ")))

maior = list[0]
menor = list[0]
p = 0

pMaior = 0
pMenor = 0

for i in list:
    
    if i > maior:
        maior = i
        pMaior = p
    if i < menor:
        menor = i 
        pMenor = p
    p+=1

print(list)
print(f"O maior valor da lista é: {maior} e esta na posição {pMaior}")
print(f"O menor valor da lista é: {menor} e esta na posição {pMenor}")

