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

def TablaMultiplicar(Numero:int, Cantidad:int):
    for i in range(1, Cantidad + 1):
        #print(Numero * i)
        print(f"{Cantidad:^10}x{i:^10}= {Numero * i}")
if __name__ == "__main__":
    TablaMultiplicar(7,20)

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