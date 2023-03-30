# 2 Leer 10 enteros alamacenarlo en  una  lista y determinar en que posicion de lista está el mayor número par leido 
 

try:
	lista=[]
	listas_pares=[]
	lista_pos=[]
	mayor=0
	pos=0

	for l in range (10):
	    numero=int(input("INGRESE UN NUMERO ENTERO:"))
	    lista.append(numero)
	print("La lista original es:",lista)

        
	for k in range(len(lista)):
	    if lista[k] % 2 == 0:
	     listas_pares.append(lista[k])
	     lista_pos.append(k)

	print("la lista de los numeros pares es:",listas_pares)

	for i in range(len(listas_pares)):
	    if  listas_pares[i] > mayor:
	         mayor = listas_pares[i]
	         pos = lista_pos [i]
	print("EL numero mayor par de la lista es",mayor," y se encuentra en la posicion",pos)

except ValueError:
   print("ERROR...")

