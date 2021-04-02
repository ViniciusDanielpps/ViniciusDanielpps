# Método da bisseção em python
# Descrição : PROGRAMA ENCONTRA SOLUÇÕES PARA EQUAÇÕES USANDO O MÉTODO DA BISSEÇÃO.

# Escolhendo os Intervalos a, b ( estes são os extremos de intervalo) e I ( amplitude final de [a , b]
print("Digite o o valor dos intervalos da função")

a = float( input(" Digite a para o intervalo [a,b] = "))
b = float(input("Digite a para o intervalo [a,b] = "))

# Importando as bibliotecas necessarias:

import math

# criando a função f(x).

def f(x):
    return  (8.0 - 4.5*(x- math.sin(x)))


c = (a - b) # c é a amplitude do intervalo [a, b].

x0= (a + b)/2.0 # x0 é o ponto médio, função geradora de aproximações.

I = 0.001 # amplitude final, ou distancia final entre [a,b]
tol = 0.0001

n = 0
ni = 100
while (c > I or math.fabs(f(x0)) > tol):
    if f(a) * f(x0) < 0.0:
        b = x0
    elif f(a) * f(x0)  > 0.0:
        a= x0

    c = b - a
    x0 = (a + b)/2.0
    n += 1
    if (n >= ni) :
        break

print('o VALOR DA ENCONTRADO É {} \nForam necessarias {} Interações \nf(x0) é igual á {}'.format(x0,n,f(x0)))








