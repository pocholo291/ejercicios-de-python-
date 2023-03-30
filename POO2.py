#Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

# creamos nuestra clase Persona
class Persona:
	# inicializamos nuestros atributos
	def inicializar(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad
 
	# imprimimos los datos
	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Edad: ",self.edad)
 
	# comprobamos si es mayor de edad o no
	def mayor_edad(self):
		if self.edad >= 18:
			print("Es mayor de edad")
		else:
			print("No es mayor de edad")
 
 
# bloque principal
persona1=Persona()
persona1.inicializar("Dibala",23)
persona2=Persona()
persona2.inicializar("Carlos",17)
# imprimimos datos y comprobamos si es mayor de edad
persona1.imprimir()
persona1.mayor_edad()
persona2.imprimir()
persona2.mayor_edad()
 
         
    
