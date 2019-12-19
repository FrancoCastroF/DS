def Diccionario1(archivo):
  with open(archivo) as diccionario:
    diccionary = dict()
    for linea in diccionario:
      n = linea.split()
      diccionary[n[0]]= n[1:] 
  return diccionary

def Texto(archivo):
  with open(archivo) as texto:
    Dtexto = texto.read()
  palabras= Dtexto.split()
  return palabras

def cambio(dicc,tex):
  # copia=[]
  # cont=0
  # for palabra in tex:
  #   #print(palabra)
  #   for animal,sinonimo in dicc.items():
  #     if palabra not in copia:
  #        copia.append(palabra)
  #     elif palabra==animal and cont<=2:
  #       llave=palabra
  #       palabra=dicc[palabra][cont]
  #       dicc[llave].append(dicc[llave].pop()[cont])
  #       copia.append(palabra)
  #       cont= cont+1
  #     else:
  #       copia.append(palabra)
  #       cont=0
  # print(copia)
  # return copia

  copia=[]
  for palabra in tex:
    if palabra not in copia:
      copia.append(palabra)
    elif palabra in dicc:
      llave= palabra
      palabra=dicc[palabra][0]
      dicc[llave].append(dicc[llave].pop(0))
      copia.append(palabra)
    else:
      copia.append(palabra)
  print(copia)
  return copia

  # conta=-1
  # for animal,sinonimo in dicc.items():
  #   for palabra in tex:
  #     if conta <=2: 
  #       if animal == palabra:
  #         dato=tex.index(palabra)
  #         tex.remove(palabra)
  #         tex.insert(dato,sinonimo[conta])
  #         conta= conta+1
  #       elif conta == -1:
  #           conta=0       
  #     else:
  #       conta=0  

def escritura(Nombre, textoNuevo):
  with open(Nombre, "w") as t:
    letras= " ".join(textoNuevo)
    #print (letras)
    enter=0
    for i in letras:
      enter=enter+len(i)
      #print(enter)
      if enter == 61:
        t.write('\n')
        enter =0
      else:
        t.write(i)
  
    return letras
  

dicc=Diccionario1('diccionario.txt')
tex=Texto('texto.txt')

cam= cambio(dicc,tex)

escritura('textoNuevo.txt',cam)


#print(tex[5])

#print(tex)
