# 17 leer un numero  entero de tres digitos  y determinar en que posicion esta el mayor digito .

try:
	numero = int(input("Ingrese un numero de tres digitos: "))

	if numero >= 100 and numero <= 999:

		digito1 = numero // 100
		digito2 = (numero % 100) // 10
		digito3 = (numero % 100) % 10

		print("Posicion 1: ",digito1)
		print("Posicion 2: ",digito2)
		print("Posicion 3: ",digito3)

		if digito1 > digito2 and digito1 > digito3:
			print("El digito mayor esta en la posicion 1 y es: ",digito1)
		elif digito2 > digito1 and digito2 > digito3:
			print("El digito mayor esta en la posicion 2 y es: ",digito2)
		elif digito3 > digito1 and digito3 > digito2:
			print("El digito mayor esta en la posicion 3 y es: ",digito3)
		else:
			print("Hay digitos iguales")

	else:
		print("El numero ingresado no tiene tres digitos")

except ValueError:
	print("Error...")

