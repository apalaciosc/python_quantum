def obtener_trimestre(mes):
	if mes >= 1 and mes <= 3:
		print('Primer trimestre')
	elif mes >= 4 and mes <= 6:
		print('Segundo trimestre')
	elif mes >= 7 and mes <= 9:
		print('Tercer trimestre')
	elif mes >= 10 and mes <= 12:
		print('Cuarto trimestre')
	else:
		print('El mes no es válido')

mes = int(input('Ingrese el mes en número: '))
obtener_trimestre(mes)
