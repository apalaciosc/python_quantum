class Carro:
	def __init__(self, modelo, marca, color):
		self.modelo = modelo
		self.marca = marca
		self.color = color
		self.estado = 'En reposo'
		self.motor = Motor(cilindros = 4)


class Motor:
	def __init__(self, cilindros, tipo='gasolina'):
		self.cilindros = cilindros
		self.tipo = tipo
		self.temperatura = 0
		self.gasolina = 0

	def inyecta_gasolina(self, cantidad):
		self.gasolina += cantidad


carro_1 = Carro('X', 'Toyota', 'Rojo')
print(carro_1.modelo)
print(carro_1.marca)
print(carro_1.color)
print(carro_1.estado)
print(carro_1.motor.gasolina)
carro_1.motor.inyecta_gasolina(100)
print(carro_1.motor.gasolina)

