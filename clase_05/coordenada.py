class Coordenada:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otra_coordenada):
		x_diff = (self.x - otra_coordenada.x) ** 2
		y_diff = (self.y - otra_coordenada.y) ** 2

		distancia = (x_diff + y_diff) ** 0.5
		return distancia


coord_1 = Coordenada(3, 30)
coord_2 = Coordenada(4, 8)

print(coord_1.distancia(coord_2))
print(coord_2.distancia(coord_1))

# print(f'Coordenada 1 tiene {coord_1.x} en el eje X y {coord_1.y} en el eje Y')
# print(f'Coordenada 2 tiene {coord_2.x} en el eje X y {coord_2.y} en el eje Y')

# x_diff = (coord_1.x - coord_2.x) ** 2
# y_diff = (coord_1.y - coord_2.y) ** 2

# diferencia = (x_diff + y_diff) ** 0.5
# print(f'La diferencia entre la coordenada 1 y la coordenada 2 es {diferencia}')



# x_diff = (coord_2.x - coord_1.x) ** 2
# y_diff = (coord_2.y - coord_1.y) ** 2

# diferencia = (x_diff + y_diff) ** 0.5
# print(f'La diferencia entre la coordenada 2 y la coordenada 1 es {diferencia}')
