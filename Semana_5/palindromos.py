class cadena_palindromo: #clase principal#
  def __init__(self): #Este es el metodo constructor#
    pass
  
  def cadena_tex(self): #aqui se encarga de las comparaciones#
    repetir_si = "S" #se declara la variable para repetir el proceso#
    while repetir_si == "S" or repetir_si == "s": #señala que si se cumple se vulve a correr el codigo#
      frace = input("Ponga una frace= ") #S lee el valor ingresado por el teclado#
      num_espacios = 0 #guarda los espacios#
      cadena_tex = frace.lower() #Se enrga de hacer todas las letras en minusculas#
      for espacio in cadena_tex: #aniliza la cadena#
        if espacio in " ": #Aqui se cuentan los espacios#
          num_espacios+=1 #analiza y encuentra los espacios #
      print("El numero de espacios en tu frace es: "+str(num_espacios))
      frace = frace.lower()
      frace = frace.replace(" ","") #se eliminan espacios#
      frace=frace.replace("à","a") #Comienza a remplazar las de acento por las que no tiene acento#


      frace = frace.replace("è","e")
      frace = frace.replace("ì","i")
      frace = frace.replace("ò","o")
      frace = frace.replace("ù","u")

      num_vocales = 0
      for vocal in cadena_tex:
        if vocal in "aeiouàèìòù": #Compara las vocales#
          num_vocales += 1 #Contaviliza las vocales#
      print("La frace tiene un total de vocales de: "+str(num_vocales)) #Una vez que cuenta da su valor#
      alreves = "" #Se lee la race de manera alreves#
      for i in frace: #Toma como primer valor el del final#
        alreves = i + alreves
      if frace == alreves: #compara y analiza si es palindromo o no#
        print("palindromo") #Imprime que es palindromo#
      else: #si no lo es ejecuta lo imprime el siguiente mensaje#
        print("Esta frace no es polindromo")
      repetir_si = input("¿Quiere poner otra frace? ") #pregunta si quiere repetir el proceso#
      if repetir_si == "N" or repetir_si == "n":
        break
      
objeto = cadena_palindromo() #Aqui se menciona la clase principal#
objeto.cadena_tex()


