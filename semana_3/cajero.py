class cajero:
  funciones= 10
  confidencial= "si"
  impreciondebaucher= "si"
  depositobilletes= 1
  depositodemonedas= 1
  lectordetarjeta= 1
  funcional= "si"

  def deposito(self):
    print("Realiza depositos")
  def retiros(self):
    print("Permite realizar retiros")
  def movimientos(self):
    print("Realiza movimientos bancarios")

    def __init__(self):
      pass
class BBVA(cajero):
  retiro= "sin tarjeta"

  def electricidad(self):
    print("Necesita electricidad")
  def dinero(self):
    print("Necesita dinero para funcionar")

    def __init__(self):
      print("BBVA")
      pass
objeto =BBVA()
print("Funciones: "+str(objeto.funciones))
print("Confidencial: "+str(objeto.confidencial))
print("Imprenta de baucher: "+str(objeto.impreciondebaucher))
print("Deposito billetes: "+str(objeto.depositobilletes))
print("Lector de tarjetas:"+str(objeto.lectordetarjeta))
print("Funciones"+str(objeto.funcional))
print("Retiro"+str(objeto.retiro))
objeto.deposito()
objeto.retiros()
objeto.movimientos()
objeto.electricidad()
objeto.dinero()