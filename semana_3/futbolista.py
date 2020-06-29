class futbolista:
  edad= 19
  alturacentimetros= 180
  numero= 16
  posicion= 3
  seleccion="mexicana"
  
  def correr(self):
    print("correr")
  def ganar(self):
    print("Ganar")
  def perder(self):
    print("perder")

  def __init__(self):
      pass

class CHICHARITO(futbolista):
    
    goles= 2000
    estatura= "1.70"

    def bueno(self):
        print("Buen jugador")
    def profecional(self):
        print("profecional")

    def __init__(self):
        print("CHICARITO")
        pass
objeto =CHICHARITO()
print("Edad: "+str(objeto.edad))
print("Altura en cm: "+str(objeto.alturacentimetros))
print("Numero: "+str(objeto.numero))
print("Posicion: "+str(objeto.posicion))
print("Seleccion"+str(objeto.seleccion))
print("Goles: "+str(objeto.goles))
print("Estatura"+str(objeto.estatura))
objeto.correr()
objeto.ganar()
objeto.perder()
objeto.bueno()
objeto.profecional()
