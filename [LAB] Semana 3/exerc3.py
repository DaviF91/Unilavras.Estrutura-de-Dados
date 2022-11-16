#Escreva um programa que conte a quantidade de consoantes em um texto e armazena tal quantidade em um dicionário, onde a chave é a consoante considerada.

frase = str.lower(input("Digite uma frase: "))

lista = list(frase)

dic = {}

for elem in lista:
    if (elem != "a") and (elem !="e") and (elem !="i") and (elem !="o") and (elem !="u"):
        if not(elem in dic):
            dic[elem] = lista.count(elem)

print(dic)