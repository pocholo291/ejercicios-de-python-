"""28. Leer un número entero menor que 50 y positivo y determinar si es un número primo."""

try:
	numero = int(input("Ingrese un numero entero menor a 50: "))

	if numero >= 0 and numero < 50:

		if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11 or numero == 13 or numero == 17 or numero == 19 or numero == 23 or numero == 29 or numero == 31 or numero == 37 or numero == 41 or numero == 43 or numero == 47:
			print("El numero ingresado es primo")
		else:
			print("El numero ingresado no es primo")

	elif numero < 0:
			print("El numero debe ser positivo")

	else:
		print("El numero debe ser menor a 50")

except ValueError:
	print("Error...")