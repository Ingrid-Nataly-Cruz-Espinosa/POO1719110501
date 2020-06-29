class string:
	cadenas = ""

	def __init__(self, cadenas):
		self.cadena = cadenas

	def separado(self):

		for caracter in self.cadena:
			print(caracter)

	def tipo_dato(self):
		dato = ""
		print("Cadena de forma separada")
		for caracter in self.cadena:
			if caracter.isdecimal() == True:
				dato = "Numero"
			elif caracter.isalpha() == True:
				dato = "Letra"
			elif caracter.isdecimal() == False and caracter.isdigit() == False:
				dato = "Simbolo"

			print("siguiente : " + str(caracter) + " es un: " +str(dato))

	def longiud(self):
		print("longitud de la cadena :" + str(len(self.cadenas)) +
		      " caracteres")

	def no_espacios(self):
		sin_espacio = self.cadenas.replace(" ", "")
		print("logintud de la cadena :" +
		      str(len(sin_espacio)) + " caracteres")
		print("La cadena se muestra sin espacios: " + str(sin_espacio))


devolver = "Si"
while devolver == "Si" or devolver == "si":
	cadenas = input("¿Que cadena deceas analizar? :\n")
	objetocadenas = string(cadenas)
	print(objetocadenas.cadenas)
	objetocadenas.longiud()
	objetocadenas.separado()
	objetocadenas.tipo_dato()
	objetocadenas.no_espacios()
	devolver = input("¿Quieres repetir el proceso?\nsi\nno\n")
     


