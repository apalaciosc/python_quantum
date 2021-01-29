print('Por favor ingrese el lado del cuadrado: ')
lado = input()

# area = float(lado) ** 2 # Es igual a lo de abajo
area = round(pow(float(lado), 2), 2)
print('El area del cuadrado es: ' + str(area))
