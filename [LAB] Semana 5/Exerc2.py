#Crie um programa em Python que produza um gráfico, baseado no que vimos na semana 5.

from pylab import plot, arange

x = arange(0, 10, 0.6)  
y = 1 * x
y1 = 4 * x
y2 = x**2.4


plot(x, y, x, y1, x, y2)