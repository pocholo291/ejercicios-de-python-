# 1 leer un número entero y determinar  si es un  numero terminado  en 4

try:
	numero = int(input("digite el numero:"))
	
	if numero % 10 == 4:
	   print("El numero termina en 4")
	else:
	   print("El numero no termina en 4")


except valuError:
   print("Digite un nuemero entero...")