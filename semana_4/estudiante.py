class estudiante:
  matricula = 1719110501
  edad = 18
  promedio = 9
  grupo = 12
  numerodelista= 10

  #metodos
  def tomar_clases(self):
    print("tomar_clases")
  def horario(self):
    print("horario")
  def aprender(self):
    print("aprender")
    pass
class Emmanuel(estudiante):
  #atributos
  estado="Hidalgo"

  #metodos
  def guapo(self):
    print("Guapo")
  def lindo(self):
    print("Lindo")

  def __init__(self):
    print("Emmanuel")
  def tomar_clases(self):
    print("Tomo clases en linea")
  def horario(self):
    print("Horario espesifico")
  def aprender(self):
    print("Aprendo cosas nuevas")
  def guapo(self):
    print("Soy muy guapo")
  def lindo(self):
    print("Lindo con todos")

objeto = Emmanuel()
print("Matricula="+str(objeto.matricula))
print("Edad="+str(objeto.edad))
print("Promedio="+str(objeto.promedio))
print("Grupo="+str(objeto.grupo))
print("Numero de Lista="+str(objeto.numerodelista))
objeto.tomar_clases()
objeto.horario()
objeto.aprender()
objeto.guapo()
objeto.lindo()