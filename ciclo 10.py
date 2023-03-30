

#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído


try:
	num = int(input("Ingrese un numero entero: "))
	suma = 0

	print("Los numeros comprendidos entre 1 y",num,"son: ")
	for i in range(1, num + 1):
		suma = suma + i
		print(i)

	print("El resultado de la suma de los numeros comprendidos entre 1 y",num,"es: ")
	print(suma)

except ValueError:
	print("Error...") 

