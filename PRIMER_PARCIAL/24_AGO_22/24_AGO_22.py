#   CLASE DEL 24 DE AGOSTO: TRABAJAR CON FUNCIONES Y ARGUMENTOS, HACIENDO USO DE HINTS.
#   Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla "<mensaje> <nombre>"
def FuncionMensaje(Mensaje: str, Nombre: str) -> str:
    return f"{Mensaje} {Nombre}"

#   Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de
#   salida tiene que ser:   "Hola <nombre> tienes <edad> años".

def FuncionEdadUno(Nombre: str, Edad: int) -> str:
    return f"Hola {Nombre} tienes {Edad} años"

#   Escribir una funcion que reciba el año actual y el año de nacimiento, usando la funcion anterior enviando
#   esta como argumento obtenga el mensaje:    "Hola <nombre> tienes <edad> años".

def FuncionEdadDos(AnioActual:int, AnioNacimiento:int, Nombre:str) -> str:
    Edad = AnioActual - AnioNacimiento
    return f"¡Hola {Nombre} tienes {Edad} años!"

if __name__ == "__main__":

    print(FuncionMensaje("Hola", "Gabo"))
    print(FuncionEdadUno("Gabo", 19))
    print(FuncionEdadDos(2022, 2003, "Gabo"))