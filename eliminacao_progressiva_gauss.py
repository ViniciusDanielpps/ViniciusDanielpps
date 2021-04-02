import numpy as np
matriz_a= np.array([[3, -1 ,-2], [0.1, 7, - 0.3],[0.3, -0.2 , 10]])

matriz_b= np.array([[7.85, -19.3, 71.4]])

n= np.size(matriz_b)
print("matriz dos coeficientes \n",matriz_a)
etapa= 0
m= matriz_a[1,0]/ matriz_a[0,0]
print(m)
matriz_a[1,:]= matriz_a[1,:] - m* matriz_a[0,:]
print(m*matriz_a[0,:])
print(" ")
print(matriz_a)
etapa = 1

m = matriz_a[2,0]/ matriz_a[0,0]
print(m)
matriz_a[2,:]= matriz_a[2,:] - m* matriz_a[0,:]
print(" ")
print(matriz_a)
print(" ")
""" Como fazer para zera a segunda coluna?"""
m= matriz_a[2,1]/matriz_a[1,1]
print(m)

matriz_a[2,:]= matriz_a[2,:] - m*matriz_a[1,:]
print(matriz_a)


