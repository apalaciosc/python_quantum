import os

# Imprimir los nombres de los archivos en una lista
listado = os.listdir('/Users/apc/Downloads')
for i in listado:
	print(i)

# Listar los archivos a manera de objeto DirEntry
escaneo = os.scandir('/Users/apc/Downloads')
with escaneo as entries:
	for entry in entries:
		print(entry.path)

# Utilizando isdir verifica si la ruta que se le está pasando es un directorio o no.
listado = os.listdir('/Users/apc/Downloads')
for i in listado:
	if os.path.isdir(os.path.join('/Users/apc/Downloads', i)):
		print(i)

try:
	os.mkdir('/Users/apc/Desktop/quantum_clase7')
except FileExistsError:
	print('El directorio ya existe.')

try:
	os.rename('/Users/apc/Desktop/quantum_clase7/test_1', '/Users/apc/Desktop/quantum_clase7/test_2')
except:
	print('Hubo un error')












