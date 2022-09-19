
#ENTRY POINT: Punto de entrada. "if __name__ == "__main__":" Es un claro ejemplo.

#def Suma(A,B);
#    return A

#if __name__ == "__main__": #Variables de sistema (Python)
#    pass #Para que el sistema no haga nada.


# Para obtener direcicon de memoria de una variable (Localidad de memoria) se va usar id:

#x = 1
#print(x,"Direccion de Memoria:",id(x))

#print(int:=10)

#def suma1(a,b):
#    return a+b

#def suma2(a:int, b:int) -> int:
#    return a+b

#suma1(2,2)
#suma2(3,3)

#print(suma1(2,2))
#print(suma2(3,3))


"""
Escribir una funcion que reciba un mensaje y un nombre, y reciba en pantalla "<mensaje> <nombre>".

"""
"""
def FuncionMensaje(Mensaje: str, Nombre: str):
    print(Mensaje,"",Nombre)
"""
"""
Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de
salida tiene que ser: "Hola <nombre> tienes <edad> años".

"""
"""
def FuncionEdadUno(Nombre: str, Edad: int):
    print("Hola", Nombre,"tienes", Edad, "años.")
"""
"""

Escribir una funcion que reciba el año actual y el año de nacimiento, usando la funcion anterior enviando
esta como argumento obtenga el mensaje:
"Hola <nombre> tienes <edad> años".

"""
"""
def FuncionEdadDos(AnioActual: int, AnioNacimiento: int, Nombre:str):
    #print("Hola", Nombre, "tienes ", AnioActual-AnioNacimiento, " años.")
    Edad = AnioNacimiento - AnioActual
    return Edad

"""
""""
if __name__ == "__main__":

    Mensaje = 'Buenos días'
    Nombre = 'Gabriel Gudiño'
    AnioNacimiento = '2003'
    AnioActual = '2022'
    Edad = 19
    print(FuncionMensaje(Mensaje, Nombre))
    print(FuncionEdadUno(Nombre, Edad))
    print(Nombre, "tienes", FuncionEdadDos(AnioActual, AnioNacimiento,"años."))
    
    Declarar variables posibles dentro de una función:

    



def sumar(a: int | float, b: int | float) -> int | float:
    return a + b

def sumar2(a,b):
    return a+b

if __name__ == "__main__":
"""
"""
    print("1. ",sumar("5","6"))
    print("2. ",sumar2(5,6))



import SUMA as S #Para llamar al archivo "SUMA.py". El "as" es para asignar un apodo a ese archivo.
import RESTAR as R
import MULTIPLICAR as M
import DIVIDIR as D
import CUADRADO as C

if __name__ == "__main__":
    print(S.sumar(5,6))
    print(R.restar(10, 6))
    print(M.Multiplicar(5, 5))
    print(D.Dividir(10, 2))
    print(C.Cuadrado(3))

#from OPERACIONES import *

"""
"""
#n1 = 10
#msg = "Hola"
#print(n1, msg)
#print(str(n1)+msg) #Para convertir "n1" como string.

# INDECCIÓN DE VARIABLES O INTERPOLACION DE CADENAS (fstrings)
#print(f"{n1} {msg}")

#   HACER UNA FUNCIÓN QUE RECIBA EL NOMBRE DE UNA PERSONA EL AÑO DE NACIMIENTO Y EL AÑO ACTUAL. RETORNADO EN
#   MENSAJE "HOLA _NOMBRE_, TIENES _AÑOS_".

def Mensaje1(Nombre:str, anio_nacimiento:int, anio_actual:int) -> str:
    Edad = anio_actual - anio_nacimiento
    return f"Hola {Nombre}, tienes {Edad} años."

def Mensaje2(Nombre: str, anio_nacimiento: int, anio_actual: int) -> str:
    return f"Hola {Nombre}, tienes {anio_actual- anio_nacimiento} años."

def CalcularEdad(anio_nacimiento: int, anio_actual: int) -> int:
    return anio_actual- anio_nacimiento

def Mensaje3(Nombre: str, anio_nacimiento: int, anio_actual: int) -> str:
    return f"Divide y vencerás: Hola {Nombre}, tienes {CalcularEdad(anio_actual,anio_nacimiento)} años."

if __name__ == "__main__":
    print(Mensaje1("Alex",1980,2022))
    print(Mensaje2("Walter", 1990, 2022))
    print(Mensaje3("Gudino", 1990, 2022))
    #print("INGRESE EL NOMBRE:")

# LISTAS (CON DIFERENCIA A TUPLAS, LA LISTA SI PUEDE CRECER)

Alumnos = ["Hugo", "Paco", "Luis", "Lupita"]

print(f"Alumnos: {Alumnos}")


for i in range(len(Alumnos)):
    print(f"Alumnos: {Alumnos[i]}\n")

# TUPLAS

Alumnos2 = ("Hugo", "Paco", "Luis", "Lupita")
print(f"Alumnos: {Alumnos2}\n")

# SETS O CONJUNTOS

Alumnos3 = {"Hugo", "Paco", "Luis", "Lupita"}
print(f"Alumnos: {Alumnos3}\n")

# DICCIONARIOS
AlumnosCalificaciones = {"Nombre": "Hugo", "Materia1": 10, "Materia2": 5}
print(f"Diccionario \"Alumnos\": {AlumnosCalificaciones}")
print(f"Alumno: {AlumnosCalificaciones['Nombre']}")
print(f"Alumno: {AlumnosCalificaciones['Nombre']}", f"con una calificación de: {AlumnosCalificaciones['Materia1']}")

Numero_Lista = [1,2,5,6,3,4,5,2,5,3,2,5,6,7,2,2,1]

Numero_SET = {1,2,5,6,3,4,5,2,5,3,2,5,6,7,2,2,1} #CAMBIA LAS LLAVES, EN EL CONJUNTO O SET SE USAN LLAVES, EN LISTA CORCHETES.

print(Numero_Lista)
print(Numero_SET)

# EJERCICIO SIMULACION DE UNA BASE DE DATOS

Encabezado = ["Nombre", "Est Dat", "Prof Func", "Inglés"]
Estudiantes = ["Hugo", "Paco", "Luis", "Lupita"]
Calificaciones = [9,10,8,9.5]
Calificaciones2 = [9.1,6,8,5,10]
Calificaciones3 = [10,7,8,8]

#PUEDE REEMPLAZAR EL "10" POR UNA VARIABLE "ANCHO = 15".

print(f"{Encabezado[0]:^10}{Encabezado[1]:^10}{Encabezado[2]:^10} {Encabezado[3]:^10}")

for a in range(len(Estudiantes)):
    print(f"{Estudiantes[a]:^10}{Calificaciones[a]:^10}{Calificaciones2[a]:^10}{Calificaciones3[a]:^10}")

"""

# CLASE 02/09/22

"""
Encabezado = ["Nombre", "Est Dat", "Prof Func", "Inglés"]
Estudiantes = ["Hugo", "Paco", "Luis", "Lupita"]
Calificaciones = [9,10,8,9.5]
Calificaciones2 = [9.1,6,8,5,10]
Calificaciones3 = [10,7,8,8]


def Reporte(fmt:int):

    print(f"{Encabezado[0]:^{fmt}}{Encabezado[1]:^{fmt}}{Encabezado[2]:^{fmt}} {Encabezado[3]:^{fmt}}")
    for a in range(len(Estudiantes)):
        print(f"{Estudiantes[a]:^{fmt}}{Calificaciones[a]:^{fmt}}{Calificaciones2[a]:^{fmt}}{Calificaciones3[a]:^{fmt}}")

if __name__ == "__main__":

    Reporte(25)

    NumeroBig = 12123456712356
    print(f"{NumeroBig:,d}") # SEPARAR CON COMAS UNA CANTIDAD.
    NumeroPI = 3.141596235345
    print(f"{NumeroPI:.3f}") # MOSTRAR UN VALOR REAL CON UN NUMERO DETERMINADO DE DECIMALES.
    print(f"{NumeroPI:.2e}") # MOSTRAR UN VALOR COMO NOTACIÓN CIENTFIFICA
    NumeroPorciento = 0.2564534
    print(f"{NumeroPorciento:%}") # NUMERO REPRESENTADO EN PORCENTAJE
    print(f"{NumeroPorciento:.2%}") # NUMERO REPRESENTADO EN PORCENTAJE CON UN NUMERO DETERMINADO DE DECIMALES
    print(f"{255:b}") # NUMERO BINARIO
    print(f"{72:c}")  # MOSTRAR UNICODES
    print(f"{72:o}")  # MOSTRAR OCTAL
"""
# ESCRIBA UNA FUNCIÓN QUE GENERE UNA TABLA DE MULTIPLICAR RECIBIENDO COMO ARGUMENTO LA CANTIDAD DE NUMEROS
# A GENERAR
"""
def TablaMultiplicar(Numero:int, Cantidad:int):
    for i in range(1, Cantidad + 1):
        #print(Numero * i)
        print(f"{Cantidad:^10}x{i:^10}= {Numero * i}")
if __name__ == "__main__":
    TablaMultiplicar(7,20)
    
"""
"""
def Producto(NumeroA:int, NumeroB:int) -> int: return NumeroA * NumeroB


def TablasMultiplicar(Numero:int, Cantidad:int, FMT: int):
    for i in range(1, Numero + 1):
        #print(Numero * i)
       TablaMultiplicar(Numero, i, FMT)

def TablaMultiplicar(Numero: int, Cantidad: int, FMT: int):
    for i in range(1, Numero + 1):
        print(f"{Cantidad:^10}x{i:^10}= {Producto(i, Cantidad)}")
    print()
    # print(Numero * i)

if __name__ == "__main__":
    TablasMultiplicar(5,2,2) # [NUMERO A MULTIPLICAR]

"""


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
print(ListaUno)