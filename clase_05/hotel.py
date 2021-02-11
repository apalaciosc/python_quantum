class Hotel:
	def __init__(self, nombre, numero_max_huespedes, lugares_de_estacionamiento):
		self.nombre = nombre
		self.numero_max_huespedes = numero_max_huespedes
		self.lugares_de_estacionamiento = lugares_de_estacionamiento
		self.huespedes = 0

	def anadir_huespedes(self, cantidad_de_huespedes):
		self.huespedes += cantidad_de_huespedes

	def checkout(self, cantidad_de_huespedes):
		self.huespedes -= cantidad_de_huespedes

	def imprimir_huespedes(self):
		print(f'Tiene {self.huespedes} huespedes')

hotel_1 = Hotel('Hotel X', 30, 0)
hotel_1.imprimir_huespedes()
hotel_1.anadir_huespedes(2)
hotel_1.imprimir_huespedes()
hotel_1.anadir_huespedes(3)
hotel_1.imprimir_huespedes()
hotel_1.checkout(5)
hotel_1.imprimir_huespedes()


print('-------')
hotel_2 = Hotel('Hotel Y', 50, 3)
hotel_2.imprimir_huespedes()
hotel_2.anadir_huespedes(10)
hotel_2.imprimir_huespedes()
hotel_2.anadir_huespedes(5)
hotel_2.imprimir_huespedes()
hotel_2.checkout(5)
hotel_2.imprimir_huespedes()


# print(f'El primer hotel es {hotel_1.nombre} y tiene capacidad para: {hotel_1.numero_max_huespedes} personas y actualmente tiene {hotel_1.huespedes} huespedes')
# print('---------------')
# print(f'El segundo hotel es {hotel_2.nombre} y tiene capacidad para: {hotel_2.numero_max_huespedes} personas y actualmente tiene {hotel_2.huespedes} huespedes')

