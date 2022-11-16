# Faça um programa que receba duas listas, a primeira com nomes de pessoas e a segunda com a idade de cada uma dessas pessoas (a quantidade de pessoas deve ser informada pelo usuário), faça o que se pede:
  #crie um dicionário a partir das duas listas informadas, a chave virá da lista de nomes e o valor da lista de idades (Dica: para criar um dicionário percorra todos os elementos das listas).

qtdPessoas = int(input("Informe a quantidade de pessoas: "))

pessoas = []
idades = []
for pessoa in range(qtdPessoas):
    pessoas.append(input("[%dª pessoa] Digite o nome: " %(pessoa +1)))
print()
for idade in range(qtdPessoas):
    idades.append(int(input("[%dª pessoa] Digite a idade: " %(idade +1))))

pessoaIdade = dict(zip(pessoas, idades))


  
print("\nLista de nomes:")
print(pessoas)
print("\nLista de idades:")
print(idades)
print("\nDicionário de pessoas:")
print(pessoaIdade)


