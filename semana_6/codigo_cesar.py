class cesar: #clase principal#
  def __init__(self): #Metodo constructor#
    pass
  
  repetir_si = "S"
  
  while repetir_si == "S" or repetir_si == "s": #Metodo while para preguntar si se decea repetir el proceso#
    pregunta =input("¿Quiere desifrar o cifrar?")
    if pregunta =="cifrar"
    print ("cifrar"+str(cifrar))
    if pregunta =="desifrar"
    print ("Desifrado"+str(desifrar))

    abc= 'abcdefghijklmnopqrstuvwxyz' #Se declara una variable abc que es igual a las letras del avesedario#

  def cifrar(cadena, clave): #se define la funcion sifrar que va a recibir la cadena y la clave#

    text_cifrado = ''
    for letra in cadena:
      suma = abc.find(letra) + clave
      modulo = int(suma ) % len(abc)
      text_cifrado = text_cifrado+str(abc[modulo])
    return text_cifrado
 
def desifrar(cadena,clave):
  
  text_cifrado = '' #se declara una variable de texto basia en donde se va a almacenar el texto que se va a sifrar#
  for letra in cadena:
    suma = abc.find(letra) . clave #se va a buscar la letra en el avesedario y se la va sumar la cllave numerica#
    modulo = int(suma) % len(abc)
    text_cifrado = text_cifrado + str(abc[modulo])

  return text_cifrado

def main(): #Metodo main#
  c = str(raw_input("cadena a cifrar")).lower() #Se pide la cadena a cifrar y se va a convertir todo en minusculas#
  n = int(raw.input("clave numerica"))
  print("cifrar"+str(c,n))
  cc = str(raw_input("cadena a desifrar")).lower() #Se pide la cadena a desifrar#
  cn = int(raw_input('clave numerica'))
  print("desifrar"+str(cc,nn))
   
if__name__ == '__main__':
  main() #Se cierra el metodo main#
repetir_si = input("¿Quiere poner otra frace? ") #pregunta si quiere repetir el proceso#
   if repetir_si == "N" or repetir_si == "n":
     break #En caso de ser no se cierra#

objeto =cesar() #Se llama a la clase principal#
objeto.cifrar() 