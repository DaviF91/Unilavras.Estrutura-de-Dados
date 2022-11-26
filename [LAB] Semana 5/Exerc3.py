#Pesquise e implemente um exemplo em Python que produza um gráfico de pizza.

from pylab import *

vendedores = ['Obi-Wan Kenobi', 'Luke Skywalker', 'Chewbacca', 'Darth Vader', 'R2-D2']
quantidadeVendasMes = [3, 5, 1, 7, 8]
cores = ['m', 'r', 'y', 'g', 'b']

pie(quantidadeVendasMes, labels=vendedores, colors=cores, radius=1,
        autopct='% .2f %%')

title('Percentual de Vendas no Mês') 