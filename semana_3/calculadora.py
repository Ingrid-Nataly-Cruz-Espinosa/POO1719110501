class calculadora:
  funciones= 10
  dijitos= 100
  color= "Gis"
  Modelo= "MG23"
  marca= "CASIO"
  Tamaño= "20CM Cuadrados"

  def encender(self):
    print("Enseder")
  def apagar(self):
    print("Apagado automatico")

  def __init__(self):
    pass

class SIENTIFICA(calculadora):
  muchas= 50
  profecional= "si"

  def escolar(self):
    print("Util para la estudiantes")
  def trabajo(self):
    print("Util para trabajar")
  
  def __init__(self):
    print("CIENTIFICA")
    pass
objeto =SIENTIFICA()
print("FUNCIONES: "+str(objeto.funciones))
print("Dijitos: "+str(objeto.dijitos))
print("Color: "+str(objeto.color))
print("Modelo: "+str(objeto.Modelo))
print("Marca: "+str(objeto.marca))
print("Tamaño: "+str(objeto.Tamaño))
print("FUNCIONES: "+str(objeto.muchas))
print("profecional: "+str(objeto.profecional))
objeto.encender()
objeto.apagar()
objeto.escolar()
objeto.trabajo()


