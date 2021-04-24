import numpy as np
#ma_a= np.array([[3, -1 ,-2], [0.1, 7, - 0.3],[0.3, -0.2 , 10]])

#ma_b= np.array([[7.85, -19.3, 71.4]])

def eliminacao_triangular(ma_a,ma_b):
	n= np.size(ma_b)
	m= 0

	for j in range( n-1):
		for i in range(j+1,n):
		#	print("\n",ma_a)
		#	print("\n",ma_b)
			m=ma_a[i,j]/ma_a[j,j]
			ma_a[i,:]=ma_a[i,:] -m*ma_a[j,:]
			ma_b[i]=ma_b[i] -m*ma_b[j]
	x= ma_a
	y= ma_b
	return f"Eliminação triangular\n{x} \nResultado da matriz B\n{y}"
	


#matriz_a=np.array([[2,-6,-1],[-3,-1,7],[-8,1,-2]])
#matriz_b= np.array([-38,-34,-20])
"""
exemplo para utilizacao da funcao
eliminacao_triangular(matriz_a,matriz_b)
"""

#Matriz triangular superior resolvida


def eliminacao_gauss(ma_a,ma_b):
	"""eliminacao triangular"""
	n= np.size(ma_b)
	m= 0

	for j in range( n-1):
		for i in range(j+1,n):
		#	print("\n",ma_a)
		#	print("\n",ma_b)
			m=ma_a[i,j]/ma_a[j,j]
			ma_a[i,:]=ma_a[i,:] -m*ma_a[j,:]
			ma_b[i]=ma_b[i] -m*ma_b[j]
			
	"""Resolucao da matriz triangular"""
	
	x=np.zeros(n)
	x[-1]=ma_b[-1]/ma_a[-1,-1]
	
	for i in reversed(range(n-1)):
		s=0
		for j in range(i+1,n):
			s +=ma_a[i,j]*x[j]
		x[i] = (ma_b[i] - s)/ma_a[i,i]
		
	return f'valor das variaveis é\n{x}'
"""	
(eliminacao_gauss(matriz_a,matriz_b)
"""
