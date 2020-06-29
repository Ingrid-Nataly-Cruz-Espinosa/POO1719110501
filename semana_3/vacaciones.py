class vacaciones:
    dias= 30
    costo= 7000
    vacacionistas= 4
    totaldeequipaje= 6
    mujeres= 2
    hombres= 2
    lugaresporvisitar= 7
    niños= 1
    adultos= 3

    def descanso(self):
        print("Descanso")
    def relajarse(self):
        print("Relajarse")

    def __init__(self):
        pass

class Acapulco(vacaciones):

    hoteles= "5 Estrellas"
    clima= "Soleado"

    def pasarlabien(self):
        print("Pasarla bien")

    def divercion(self):
        print("Divertirte")

    def __init__(self):
        print("ACAPULCO")
        pass
objeto =Acapulco()

print("Dias= "+str(objeto.dias))
print("Costo= "+str(objeto.costo))
print("Vacacionistas"+str(objeto.vacacionistas))
print("Total de equipaje"+str(objeto.totaldeequipaje))
print("Mujeres"+str(objeto.mujeres))
print("Hombres= "+str(objeto.hombres))
print("Lugares por visistar"+str(objeto.lugaresporvisitar))
print("Niños= "+str(objeto.niños))
print("Adualtos= "+str(objeto.adultos))
objeto.descanso()
objeto.relajarse()
objeto.pasarlabien()
objeto.divercion()
