# 31 leer un numero entero y determinar si es igual a 10

try:
	numero = int(input("ingresa un numero entero"))
	if numero == 10:
	   print("el numero ingresado es igual a 10")

	else:
	   print("el numero ingresado es diferente a 10")


except valuError:
    print("error...")	 