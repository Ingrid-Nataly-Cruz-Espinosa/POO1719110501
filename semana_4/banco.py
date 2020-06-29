class banco:
  #atributos
  cajeros= 5
  ventanillas= 7
  empleados= 30
  camarasseguridad= 10
  alarmas= 3
  sucursales= 6
  oficinas= 6
  
  def prestamos(self):
    print("prestamos")
  def seguridad(self):
    print("seguridad") 

def __init__(self):
  pass

class Banamex(banco):

  #atributos
  horario="lunes a sabado de 8 am  a 4 pm"
  
  #metodos
  def serviciocajero(self):
    print("servicio cajero 24 horas")
  
  def retirar(self):
    print("Retiro en efectivo")

  def __init__(self):
    print("BANAMEX")
  def prestamos(self):
    print("Banamex te presta dinero")
  def seguridad(self):
    print("Obten la mejor seguridad de tus datos con Banamex")
  def serviciocajero(self):
    print("Retira y deposita desde nuestros cajeros")
  def retirar(self):
    print("Retira efectivo en Banamex")

objeto =Banamex()

print("Cajeros="+str(objeto.cajeros))
print("Ventanillas="+str(objeto.ventanillas))
print("Empleado="+str(objeto.empleados))
print("Camaras de seguridad="+str(objeto.camarasseguridad))
print("alarmas="+str(objeto.alarmas))
print("sucursales="+str(objeto.sucursales))
print("oficnas"+str(objeto))
objeto.prestamos()
objeto.seguridad()
objeto.serviciocajero()
objeto.retirar()