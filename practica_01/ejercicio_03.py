def temperature(temperatura_centigrados):
	# La formula es: (1 °C × 9/5) + 32
	# temperatura_fahrenheit = int((temperatura_centigrados * 9 / 5) + 32)
	temperatura_fahrenheit = round((temperatura_centigrados * 9 / 5) + 32, 0)
	print(f'La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}')

temperatura_centigrados = float(input('Ingresa temperatura en °C: '))
temperature(temperatura_centigrados)
