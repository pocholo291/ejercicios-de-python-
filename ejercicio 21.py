#21 Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor  digito


try:
	num1 = int(input("Ingrese un numero1 de dos cifras: "))
	num2 = int(input("Ingrese un numero2 de dos cifras: "))
	num3 = int(input("Ingrese un numero3 de dos cifras: "))

	if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99) and (num3 >= 10 and num3 <= 99):

		dig1 = num1 // 10
		dig2 = num1 % 10

		dig3 = num2 // 10
		dig4 = num2 % 10

		dig5 = num3 // 10
		dig6 = num3 % 10

		if (dig1 > dig2) and (dig1 > dig3) and (dig1 > dig4) and (dig1 > dig5) and (dig1 > dig6):
			print("El digito mayor se encuentra en el primer numero ingresado y es: ", dig1)

		elif (dig2 > dig1) and (dig2 > dig3) and (dig2 > dig4) and (dig2 > dig5) and (dig2 > dig6):
			print("El digito mayor se encuentra en el primer numero ingresado y es: ", dig2)

		elif (dig3 > dig1) and (dig3 > dig2) and (dig3 > dig4) and (dig3 > dig5) and (dig3 > dig6):
			print("El digito mayor se encuentra en el segundo numero ingresado y es: ", dig3)

		elif (dig4 > dig1) and (dig4 > dig2) and (dig4 > dig3) and (dig4 > dig5) and (dig4 > dig6):
			print("El digito mayor se encuentra en el segundp numero ingresado y es: ", dig4)

		elif (dig5 > dig1) and (dig5 > dig2) and (dig5 > dig3) and (dig5 > dig4) and (dig5 > dig6):
			print("El digito mayor se encuentra en el tercer numero ingresado y es: ", dig5)

		elif (dig6 > dig1) and (dig6 > dig2) and (dig6 > dig3) and (dig6 > dig4) and (dig6 > dig5):
			print("El digito mayor se encuentra en el tercer numero ingresado y es: ", dig6)
		else:
			print("Hay digitos iguales")

	else:
		print("Los numeros ingresados no son validos")

except ValueError:
	print("Error...")