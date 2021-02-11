def pluck(objetos, propiedad):
	resultado = []
	for objeto in objetos:
		if propiedad in objeto:
			valor = objeto[propiedad]
			resultado.append(valor)
		else:
			resultado.append(None)

	print(resultado)

pluck([{'a':1}, {'a':2}], 'a')        # -> [1,2]
pluck([{'a':1, 'b':3}, {'a':2}], 'b')  # -> [3, None]
pluck([{'a':1, 'b':3}, {'a':2}, {'a':10, 'b':'Hola', 'c':'Mundo', 'd':'Quantum'}], 'c')  # -> [None, None, 'Mundo']
