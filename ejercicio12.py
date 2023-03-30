#leer un numero entero  y determinar si termina  en 12

try:
	num = int(input("ingrese un numero"))
	if num % 100 == 12:
		print("el numero termina en 12")
	else:
		print("el numero  no termina en 12")



except  valueError:
   print("erro...") 