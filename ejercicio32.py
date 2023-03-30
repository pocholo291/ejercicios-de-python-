#32 leer un numero entero  y determinar  si es multiplo de 7 

try:
	numero = int(input("ingrese un numero: "))
	if numero % 7 == 0:
		print("EL numero   es  multiplo de 7 ")

	else:
		print("el  numero  no  es multiplo de 7")



except valueError:
   print("el numero es incorreto....") 
	  