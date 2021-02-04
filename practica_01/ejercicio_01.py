def ensure_question(palabra):
	if len(palabra) == 0:
		print('Cadena no válida')
	else:
		print(f'{palabra}?')


palabra = input('Escriba una palabra: ')
ensure_question(palabra)
