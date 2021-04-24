
import math
import numpy as np
""" funcoes"""
def  funcao_f(x): #função
	return (math.e**-x ) -x

"""Derivadas"""
def derivada_f(x): # Derivada Algebrica
	return (- math.e**-x) - 1

def der_n_f(x):# Derivada Numerica
	h= 1e-10
	fun=(funcao_f(x+h) -funcao_f(x))/h
	return fun

def der2_n_f(x): #Segunda Derivada Numerica
	h= 1e-10
	print(h)
	fun2= (der_n_f(x+h))-( der_n_f(x))/h
	return fun2
	
def derivada_2f(x): #Derivada Algebrica
	return math.e**-x
	
	
erro_max= 1e-8	
ni= float(input("Entre com o valor inicial = "))
cont= 0
while abs(funcao_f(ni))> erro_max:
	cont += 1
	ni = ni- (funcao_f(ni)/ der_n_f(ni))

	print(ni)
	if erro_max > funcao_f(ni):
		print(ni)
		break
print("Foram realizadas {} Interacões , antes de alcancar o valor  final da raiz  aproximada {} para a Função dada".format(cont, ni))
print("1° Derivada Numerica ", der_n_f(ni),"\n2° Derivada Numerica ", der2_n_f(ni)," \n2° Derivada Algebrica", derivada_2f(ni))
"""Calculo do Erro"""
#erro_f = (der2_n_f(ni))/2* (der_n_f(ni))
erro_f = - (derivada_2f(ni))/(2* (der_n_f(ni)))
conta= 0
while erro_f > 1e-4:
	conta += 1
	erro_f =derivada_2f(ni)* (erro_f)**2
	print(erro_f)
	if 0.00009 > erro_f:
		print("O erro é de aproximação é de \n", erro_f, "foram necessarias", conta," interações para obter o valor final para o  erro maximo.")


		
