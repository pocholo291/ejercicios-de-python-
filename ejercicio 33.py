#33 leer un numero entero  y determinar si termina en 7

try:
	numero = int(input("Digite el numero"))

	if numero % 10 == 7:
	 print("el numero  terminar en 7")

	else:
	 print("el numero no termina en 7")



except valuError:
    print("digite un numero entero...")	 	