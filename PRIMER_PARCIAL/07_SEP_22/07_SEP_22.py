# CLASE 07/09/22

"""

ListaUno = [1,2,3,4]
print(ListaUno)

ListaDos = [1,5.56,"Hola", True, [5,6,7],(1,3,6),{8,"B",5.5}] #En una lista podemos almacenar cualquier tipo de información.
print(ListaDos)

print(len(ListaUno)) #Tamaño de la primer lista.

print(len(ListaDos)) #Tamaño de la segunda lista.

print(ListaDos[6]) #Valor ubicado en la ultima posición de la lista.

#EJEMPLO LISTAS

ListaCal = []
print(ListaCal)
ListaCal.append(5) #AÑADIR UN VALOR HASTA EL FINAL DE LA LISTA.
print(ListaCal)
ListaCal.append(8)
print(ListaCal)
ListaCal.append(9)
print(ListaCal)
ListaCal.insert(0,5) #AÑADIR UN VALOR A UNA LISTA SELECCIONANDO EL INDICE.


# RELLENAR UNA LISTA CON LOS NUMEROS NATURALES DEL 1 AL 10:

ListaEjercicio = []

for i in range (1,11):
    ListaEjercicio.append(i)

print(ListaEjercicio)

# INDICES NEGATIVOS

print(ListaUno[-4]) # VA A INDICAR LA ULTIMA POSICIÓN DE LA LISTA.

# SLICES (REBANADAS)

ListaUno = [1,2,3,4,5,6,7,8,9,10]

print(ListaUno)
print(ListaUno[:])
print(ListaUno[0:10])
print(ListaUno[int(len(ListaUno)/2):])
print(ListaUno[:int(len(ListaUno)/2)])
print(ListaUno[0:-1]) # SE PUEDEN CONVINAR INDICES.
print(ListaUno[3:7])
print(ListaUno[-7:-3])

# MAS EJEMPLOS:

ListaUno = [1,"Dos",3,"Cuatro",5,6,7,8,9,10]
print(ListaUno)

ListaUno[1] = 2
print(ListaUno) # ASIGNAR UN NUEVO VALOR A LA LISTA.

# METODO PARA CONSERVAR UNA COPIA DE UNA LISTA.

ListaUno = [1,"Dos",3,"Cuatro",5]
ListaDos = ListaUno[:] # Cambia la dirección de memoria de la lista.
ListaUno[1] = 2
print(f"Lista principal: {ListaUno} Dirección: {id(ListaUno)}")
print(f"Lista de seguridad: {ListaDos}  Dirección: {id(ListaDos)}")

"""

# OTRO EJEMPLO DE LA MISMA CLASE DEL 07/05/22

ListaUno = [0,1,2,3,4]

for i in range (5,8):
    ListaUno.append(i)

print(ListaUno)

ListaUno = [0,1,2,3,4]
ListaDos = [5,6,7]
ListaUno[5:] = ListaDos #[5,6,7]
print(ListaUno)
ListaUno[len(ListaUno):] = ListaDos
print(ListaUno)

# INSERTAR AL INICIO DE LA LISTA VARIOS ELEMENTOS

ListaUno[:0] = ListaDos
print(ListaUno)

# OTRO METODO

ListaUno = [0,1,2,3,4]
ListaUno.append(ListaDos)   #   - FORMA INCORRECTA, VA IMPRIMIR: 0,1,2,3,4,[5,6,7]
print(ListaUno)
ListaUno.extend(ListaDos)   #   - FORMA CORRECTA
print(ListaUno)

# COMO ELIMINAR UN ELEMENTO:

del ListaUno[0]
print(ListaUno)

del ListaUno[2:5]
