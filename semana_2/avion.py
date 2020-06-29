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

  def __init__(self):
    print("Avion privado")
    print(self.alas)
    print(self.asientos)
    print(self.ventanillas)
    print(self.baños)
    print(self.llantas)
    print(self.sinturonesdeseguridad)
    print(self.televicion)

objeto = Avion()
objeto.arranca
objeto.vuela