#1 leer 10 enteros.alamacenarlo en una lista y determinar en que posicion de la lista está el mayor número leido

try:
	lista=[]
	mayor=0
	pos=0

	for k in range(10):
	    numero=int(input("Ingrese un numero entero"))
	    lista.append(numero)  
	print("la lista es:",lista)

	for k in range(len(lista)):
 	    if lista[k] > mayor:
	       mayor = lista[k]
	       pos = k
	print("El numero mayor de la lista es",mayor," y se encuentra en la posicion", pos)
 	



except ValueError:
   print("Error...") 	 					 
 	  	