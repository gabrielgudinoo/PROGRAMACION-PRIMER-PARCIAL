# UNIDAD 1: PRIMERA PARCIAL "PROGRAMACIÓN FUNCIONAL". 
## WALTER ALEXANDER
### ESTUDIANTE: GUDIÑO MÉNDEZ GABRIEL ALEJANDRO
#### 1. FUNCIONES EN PYTHON
Desde los primeros días de clase vimos detalladamente las funciones en <b>Python</b> y cada una de sus características, formas de implementación, argumentos, etc. Aprendimos como hacer darles el uso adecuado a las funciones en este lenguaje de programación. En las primeras sesiones programando escribimos varias líneas de código, en donde aplicamos el uso de funciones. Realizamos unos pequeños ejercicios que consistía en lo siguiente:

  - "Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla "<mensaje> <nombre>".
  - "Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser:   "Hola <nombre> tienes <edad> años".
  - "Escribir una funcion que reciba el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años".
  
   En la cuál los códigos fuentes de la funciones anteriores fueron las siguientes:
El cual este fue el resultado de programar las funciones de esos ejercicios de la siguiente forma:
~~~
def FuncionMensaje(Mensaje: str, Nombre: str) -> str:
    return f"{Mensaje} {Nombre}"
    
def FuncionEdadUno(Nombre: str, Edad: int) -> str:
    return f"Hola {Nombre} tienes {Edad} años"
    
def FuncionEdadDos(AnioActual:int, AnioNacimiento:int, Nombre:str) -> str:
    Edad = AnioActual - AnioNacimiento
    return f"¡Hola {Nombre} tienes {Edad} años!"
~~~
Desde la función principal lo que hicimos fue llamar cada función que se definieron anteriormente. El bloque de código del cuerpo o función principal es la siguiente:
~~~
if __name__ == "__main__":

    print(FuncionMensaje("Hola", "Gabo"))
    print(FuncionEdadUno("Gabo", 19))
    print(FuncionEdadDos(2022, 2003, "Gabo"))
~~~
