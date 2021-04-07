import time

class Carro:
	
	def __init__(self,Direcao, Motor):
			self.Motor= Motor()
			self.Direcao= Direcao()
	
	def velocidade(self):
		return self.Motor.velocimetro()
	
	def acelerador(self):
		self.Motor.acelerar()
		
	def freio(self):
		self.Motor.frear()
	
	def localiza(self):
		self.Direcao.localiza()
		
	def esquerda(self):
		self.Direcao.girar_esquerda()
	
	def direita(self):
		return self.Direcao.girar_direita()
	

	
		
		
class Motor:
	def __init__(self,velocidade= 0):
		self.velocidade = velocidade
		
	def acelerar(self):
		if self.velocidade <=115:
				time.sleep(0.2)
				self.velocidade +=5
				print("Velocidade almentando!" ,self.velocidade, "km/h")
				if self.velocidade >120:
					self.frear()
	
					return f'Velocidade maxima alcançada! {self.velocidade} km/h'
		return f"O carro esta acelerando, ele está com {self.velocidade} km/h"
# existe uma funcao que determina a velocidade maxima ou minina com maior facilidade
#self.velocidade = max(0, self.velocidade) 
#self.velocidade = max(self.velocidade, 120) 

	def frear(self):
		if self.velocidade >=5 :
			self.velocidade -=5
			return print(" O carro está freando,  esta com" ,self.velocidade," km/h")
		if self.velocidade < 5:
			self.velocidade =0
			return f'O Carro parou, esta com velocidade 0! '
		if self.velocidade >= 121:
				self.velocidade = 120
				
		return f"O carro esta freiando, ele está com {self.velocidade} km/h"
		
	def velocimetro(self):
		return print('Velocidade atual',self.velocidade, "km/h")
	

norte= ("Norte")
sul = ("Sul")
leste= ("Leste")
oeste= ("Oeste")

class Direcao:
	def __init__(self,posicao= norte):
		self.posicao = posicao
		

	def girar_direita(self):
		if self.posicao == norte:
			self.posicao = leste
		elif self.posicao == leste:
			self.posicao = sul
		elif self.posicao == sul:
			self.posicao = oeste
		elif self.posicao== oeste:
			self.posicao = norte
		return print("Indo para o",self.posicao)
		
	def girar_esquerda(self):
		if self.posicao == norte:
			self.posicao = oeste
		elif self.posicao == leste:
			self.posicao = norte
		elif self.posicao == sul:
			self.posicao = leste
		elif self.posicao== oeste:
			self.posicao = sul
		return print("Indo para o",self.posicao)
		
	def localiza(self):
				return self.posicao
				



#exemplo
#existe uma forma de retirar tantos " if, elif "atraves de dicionarios

"""class objeto():
	girar_esquerda= {norte: oeste, oeste : sul, sul:leste, leste: norte}
	def girar_e(self):
		self.posicao= self.girar_esquerda(self.posicao)
"""
if __name__ == "__main__":
	
	car= Direcao()
#	print(car.localiza())
	eicu= Carro(Direcao, Motor)
#	print(eicu.Direcao.girar_esquerda())
	eicu.velocidade()
	eicu.acelerador()
	eicu.freio()
	eicu.direita()
	eicu.esquerda()
	eicu.direita()
	eicu.esquerda()
	

	

	
		
		
		
		
		
	
		
	