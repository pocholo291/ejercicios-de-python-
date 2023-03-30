#44. Leer un número y calcularle su factorial.

try:
	num = int(input("Ingrese un numero entero: "))
	print("******************************************")
	factorial = 1

	for i in range(num):
		print(factorial,"*",num)
		factorial *= num
		num -= 1 
		
	print("******************************************")
	print("El factorial del numero ingresado es: ",factorial)

except ValueError:
	print("Error...")