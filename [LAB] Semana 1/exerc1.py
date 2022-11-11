# Crie um programa que lê 6 valores inteiros, armazene-os em uma lista e, em seguida, percorra essa listra mostrando na tela cada um dos valores salvos.

list = []
for i in range(6):
    list.append(int(input(f"Digite {i + 1}º número ")))
    
for i in list:
    print(i)
