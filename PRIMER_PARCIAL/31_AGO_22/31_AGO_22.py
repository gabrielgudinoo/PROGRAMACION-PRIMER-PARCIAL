# CLASE 31/08/22

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
