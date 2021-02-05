import random

def generador_contrasena():
	mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	simbolos = ['!', '@', '$', '%', '(', ')', '/', '&']
	numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

	caracteres = mayusculas + minusculas + simbolos + numeros
	contrasena = []

	for i in range(16):
		random_element = random.choice(caracteres)
		contrasena.append(random_element)

	contrasena_final = "".join(contrasena)
	return contrasena_final



contr = generador_contrasena()
print(contr)
