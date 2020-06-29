class coche:
  numerodellantas=4
  modelo=2020
  puertas=4
  capasidad= 5
  asientos= 3
  color= "rojo"
  aireacondicionado= "si"
  quemacocos= "si"

  def arrancar(self):
    print("Arrancar")
  def frenar(self):
    print("Frenar")
  def conbustible(self):
    print("Uso de Conbsutible")

  def __init__(self):
      pass
class DEPORTIVO(coche):

    velocidad= "360 km/h"
    rines= "cromados"

    def escape(self):
        print("Escape")
    def motor(self):
        print("Motor")

    def __init__(self):
        print("DEPOPRTIVO ROJO")
    def arrancar(self):
      print("Enciendeme desde el control de alarma")
    def frenar(self):
      print("Freno mediante un pedal")
    def conbustible(self):
      print("Necesesito gasolina")
    def escape(self):
      print("Escape cromado")
    def motor(self):
      print("Motor muy potente")
       
objeto= DEPORTIVO()
print("Numero de llantas: "+str(objeto.numerodellantas))
print("Modelo: "+str(objeto.modelo))
print("Puertas:"+str(objeto.puertas))
print("Capacidad: "+str(objeto.capasidad))
print("Asientos: "+str(objeto.asientos))
print("Color: "+str(objeto.color))
print("Aire acondicionado: "+str(objeto.aireacondicionado))
print("Quemacocos: "+str(objeto.quemacocos))
objeto.arrancar()
objeto.frenar()
objeto.conbustible()
objeto.escape()
objeto.motor()