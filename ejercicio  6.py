#leer un numero entero  de dos digitos menor que 20  y determinar si es primo

try:
	numero = int(input("ingrese un numero  de dos digito menor a 20:"))

	if numero >= 10 and numero < 20:

	   if( numero == 11) or (numero == 13) or (numero == 17) or (numero == 19):
	      print("El numero es primo")
	   else:
	      print("El numero  no es primo")
	
	elif numero >= 20 and numero <=99:
	     print("El numero  debe ser  menor  que 20")
 
	else:
	    print("El numero  no tiene dos digito")


except valuError:
   print("Error...")	 