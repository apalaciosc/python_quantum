def espacios(lista):
	palabra = ''
	resultado = []
	for i in lista:
		palabra += i
		resultado.append(palabra)
	return resultado

print(espacios(['i', 'have', 'no', 'space']))
print(espacios(['a', '123', 'csc', 'hola', 'mundo', 'clase', 'python', 'quantum', '123']))


# ['i', 'have', 'no', 'space']
#
# 'i'
# 'ihave'
# 'ihaveno'
# 'ihavenospace'
