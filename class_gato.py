#Class gatos
class Gato():
	def __init__(self, nome,peso, cor, idade):
		self.nome= nome
		self.peso = float(peso)
		self.cor= cor
		self.idade=int(idade)
	def miar(self):
		return f"O gato  mia"
	def dorme(self):
		if self.idade >10:
			return f"O gato {self.nome} dorme"
		else:
			return f'O gato está acordado'
	def comer(self):
		return f" O gato está comendo"
	
if __name__== "__main__":
	din= Gato("din",43,"azul",11)
	print(type(din))
	print(din.miar())
	din.idade= int(input(f"Que a idade o {din.nome} possui ? "))
	print(din.dorme())
	print(din.peso)

#posso colocar dentro de objeto, outro objeto, por exemplo

class Gatos_dacasa():
	def __init__(self, casa= None,*gatos):
		pass
	

moradia= Gatos_dacasa("lar", din)
moradia.gatos= din
print(moradia.gatos)
"""aqui, criada uma classe de objeto, dentro do objeto fou colocado outro objeto de outra classe."""

#é possivel criar e remover atributos de um objeto especifico, mas a classe do objeto permanece sem este atributo. Isto sem necessariamente ir no comando def __init__()

"""criando um atributo no objeto moradia"""

moradia.endereco= "passagem liberdade"
""" basta colocar o nome do atributo :
		objeto.atributo
		"""
del moradia.gatos
"""remova um atributo de um objeto com del objeto.atributo"""
print(moradia)

"""é possivel ver todos os atributos de um objeto com """

print(din.__dict__) #__dict__

#atributos de classe

#serao atributos pertencentes a classe do objeto, sendo estes com valores iguais para todos os objetos da classe.
class Carros():
		rodas = 4
		portas = 4
		def __init__(self, cor, marca):
			self.cor = cor
			self.marca= marca
			pass
		
#caso um objeto tenha um atributo de classe diferente, é possivel alterar para ele especificamente 
camaro= Carros("amarelo"," camaro")
camaro.rodas= 5
print(camaro.__dict__)
del camaro.rodas
print(camaro.__dict__)


		
	
	
	
	

	