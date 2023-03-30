5# leer dos numeros y mostrar  todos los numeros  termiados en 4 compredidos entre ellos


try:
	num1 = int(input("Ingrese un numero1 entero: "))
	num2 = int(input("Ingrese un numero2 entero: "))

	if num1 < num2:
		print("Los numeros terminados en 4 comprendidos entre",num1,"y",num2,"son: ")
		for i in range(num1, num2 + 1):
			if i % 10 == 4:
				print(i)
	elif num2 < num1:
		print("Los numeros terminados en 4 comprendidos entre",num2,"y",num1,"son: ")
		for i in range(num2, num1 + 1):
			if i % 10 == 4:
				print(i)
	else:
		print("Los numeros ingresados son iguales")


except ValueError:
	print("Error...")