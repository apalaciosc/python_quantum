# tipo_cambio = 0.27
# monto = input('Ingrese el valor en soles: ')
# monto_en_usd = float(monto) * tipo_cambio

# print(f'El monto en USD es: {monto_en_usd}')




# mensaje = """
# Hola, este es un conversor de monedas
# Ingresa cualquiera de estas 3 opciones:
# 1 = Soles - Dolares
# 2 = Euros - Dolares
# 3 = COP - Dolares
# """

# print(mensaje)
# opcion = int(input('Ingresa la opción: '))
# if opcion == 1:
#     monto = input('Ingrese el valor en soles: ')
#     monto_en_usd = round(float(monto) * 0.27, 2)
#     print(f'El monto en USD es: {monto_en_usd}')
# elif opcion == 2:
#     monto = input('Ingrese el valor en euros: ')
#     monto_en_usd = round(float(monto) * 1.21, 2)
#     print(f'El monto en USD es: {monto_en_usd}')
# elif opcion == 3:
#     monto = input('Ingrese el valor en COP: ')
#     monto_en_usd = round(float(monto) * 0.00028, 2)
#     print(f'El monto en USD es: {monto_en_usd}')
# else:
#     print('Elige un opción válida.')

def convertir_moneda(tipo_de_cambio, moneda):
    monto = input(f'Ingrese el valor en {moneda}: ')
    monto_en_usd = round(float(monto) * tipo_de_cambio, 2)
    print(f'El monto en USD es: {monto_en_usd}')

mensaje = """
Hola, este es un conversor de monedas
Ingresa cualquiera de estas 3 opciones:
1 = Soles - Dolares
2 = Euros - Dolares
3 = COP - Dolares
"""

print(mensaje)
opcion = int(input('Ingresa la opción: '))

if opcion == 1:
    convertir_moneda(0.27, 'soles')
elif opcion == 2:
    convertir_moneda(1.21, 'euros')
elif opcion == 3:
    convertir_moneda(0.00028, 'COP')
else:
    print('Elige un opción válida.')

