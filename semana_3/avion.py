class Avion:
  alas= 2
  asientos= 2
  ventanillas= 4
  baños= 1
  llantas= 3
  televicion= 2
  sinturonesdeseguridad= 4

  def vuela(self):
    print("vuela")
  def arranca(self):
    print("Arranca")
    pass

class Air(Avion):

    capacidad_pasajeros= 200
    color= "Blanco y verde"

    def aeromosa(self):
        print("Areomosas")

    def combustible(self):
        print("Combustible especial")

    def __init__(self):
        print("AIR")
        pass

objeto =Air()

print("Alas= "+str(objeto.alas))
print("Asientos"+str(objeto.asientos))
print("Ventanillas="+str(objeto.ventanillas))
print("Baños="+str(objeto.baños))
print("Llantas="+str(objeto.llantas))
print("televicion="+str(objeto.televicion))
print("sinturones de seguridad="+str(objeto.sinturonesdeseguridad))
print("Capacidad de pasajeros="+str(objeto.capacidad_pasajeros))
print("Color= "+str(objeto.color))
objeto.vuela()
objeto.arranca()
objeto.aeromosa()
objeto.combustible()

   
  