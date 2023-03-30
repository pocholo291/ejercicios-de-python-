11# Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro

try:
	num = int(input("Ingrese un numero de dos digitos: "))

	dig1 = num // 10
	dig2 = num % 10

	if num >= 10 and num <= 99:

		if dig1 < dig2:
			print("Los enteros comprendidos entre el digito",dig1,"y el digito",dig2,"son: ")
			for i in range(dig1, dig2 + 1):
				print(i)
		elif dig2 < dig1:
			print("Los enteros comprendidos entre el digito",dig2,"y el digito",dig1,"son: ")
			for i in range(dig2, dig1 + 1):
				print(i)
		else:
			print("Los digitos son iguales")

	else:
		print("El numero ingresado no tiene dos digitos")

except ValueError:
	print("Error...")