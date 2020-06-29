class classroom:
  funciones= 30
  segura= "si"
  clasificacion= "educativa"
  nombre="classroom"
  usuarios=("Millones de usuarios")
  seguro="si"

  def online(self):
    print("online")
  def app(self):
    print("aplicacion")
  def enviodearchivos(self):
    print("Permite enviar archivos")
    def __init__(self):
      pass
class maestros(classroom):
  facil= "si"
  califica= "Permite calificar a los alumnos"
  def video(self):
    print("Video conferencias")
  def calificar(self):
    print("Permite calificar a los alumnos")
    def __init__(self):
      print("Maestros")
      pass
objeto =maestros()
print("Funciones: "+str(objeto.funciones))
print("Segura: "+str(objeto.segura))
print("Clasificacion: "+str(objeto.clasificacion))
print("Usuario: "+str(objeto.usuarios))
print("Seguro:"+str(objeto.seguro))
print("Facil: "+str(objeto.facil))
print("Calica: "+str(objeto.califica))
objeto.online()
objeto.app()
objeto.enviodearchivos()
objeto.video()
objeto.calificar()