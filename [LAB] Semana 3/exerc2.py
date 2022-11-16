#Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 3 filmes.

filmes = {}

for i in range(3):
    filme = input("[Filme %d]Informe o nome do filme: " %(i+1))
    filmes[filme] = dict(vilao = input("[Filme %d]Informe o vilão do filme: " %(i+1)),ano = int(input("[Filme %d]Informe o ano do filme: " %(i+1))))
    print()
    

print(filmes)