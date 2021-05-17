"""Calculo de integral definida com metodo de aproximado
"""
#adicione a funcao
def f(x):
	f=0.2 + 25*x -200*x**2 +675*x**3 -900*x**4 +400*x**5
	return f

#calculo do trapezio divido em intervalos
#e soma

def integral_f(a,b,h=1e-5,funcao=f):
	x=a
	soma=0
	
	
	
	while (x+h)<= b:
		area_trapezio= (f(x) + f(x+h))*h/2		
		soma +=area_trapezio
		x+=h
	#	print(x+h)
	#	print(soma)
	return soma


print(integral_f(a=0,b=0.8))
print("Valor de f(0) ",f(x=0), "\nvalor de f(0.8)",f(0.8))
		
		
	
	



	
	
