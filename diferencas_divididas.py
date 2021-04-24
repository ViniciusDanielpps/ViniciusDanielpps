import matplotlib.pyplot as plt
from numpy import linspace as np
"""programa com a finalidade de objter um polinomio generico de grau n, a partir de seus coeficientes .
"""
def fu(x,coeficiente):
	funcao=0
	n=0
	for i in coeficiente:
		funcao+=i* x **n
		n+= 1	
	return funcao
	
constantes=[1,2,-3,5,-5]
"""
for i in constantes:
	print(i)
metodo no qual faz a funcao receber uma lista com cada elemento da lista sendo um  parametro, melhor que utilizar o 
def f(x,*args)
"""
	
#print("\n",fu(20,constantes))

x= np(1,10,30)

y=(fu(x,constantes))

plt.plot(x,y)
plt.show()






