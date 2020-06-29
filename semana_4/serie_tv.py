class series:
  precio= 30
  diasdeduracion= 60
  clasificacion= "terro"
  trama= "muchosuspenso"
  nombre= "zombie"

  def entretener(self):
    print("Entretener")
  def pasatiempo(self):
    print("Pasa tiempo")
  def __init__(self):
      pass

class Zombies(series):

    duracion= "2 meses"
    capitulos= "17 capitulos"
    def entretenida(self):
        print("Muy chida")

    def unica(self):
        print("Unica temporada")

    def efectos(self):
        print("Muy buenos efectos")

    def __init__(self):
        print("ZOMBIES")
    def entretener(self):
      print("Una trama buena para entretener")
    def pasatiempo(self):
      print("Pasa un buen momento con alguien especial")
    def unica(self):
      print("No hay segunda temporada")
    def efectos(self):
      print("Los efectos te sorprenderan")
    
objeto= Zombies()
print("precio= "+str(objeto.precio))
print("dias de duracion= "+str(objeto.diasdeduracion))
print("Clasificacion= "+str(objeto.clasificacion))
print("Trama= "+str(objeto.trama))
print("Nombre= "+str(objeto.nombre))
print("Duracion= "+str(objeto.duracion))
print("Capitulos= "+str(objeto.capitulos))
objeto.entretener()
objeto.pasatiempo()
objeto.entretenida()
objeto.unica()