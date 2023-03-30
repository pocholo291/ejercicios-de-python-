# 10 leer un número entero  de dos digitos  y  determinar si los dos digitos  son iguales.

try:
	numero = int(input("Digite un numero de dos digitos: "))

	if numero >= 10 and numero <= 99:

		digito1 = numero // 10
		digito2 = numero % 10

		if digito1 == digito2:
			print("Los digitos son iguales")
		else:
			print("Los digitos son diferentes")

	elif numero <= -10 and numero >= -99:

		numero *= -1
		digito1 = numero // 10
		digito2 = numero % 10

		if digito1 == digito2:
			print("Los digitos son iguales")
		else:
			print("Los digitos son diferentes")

	else:
		print("El numero ingresado no contine 2 digitos")

except ValueError:
	print("Error. El dato debe ser numerico.")