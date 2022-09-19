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
La pantalla de respuesta al ejercicio anterior es la siguiente:<br><br>
![](https://i.imgur.com/KYAuiEC.png)
  
### 2. IMPORTACIONES DE ARCHIVOS EN PYTHON
En esta sección voy a explicar que fue lo que aprendimos en este tema de importaciones de módulo. Básicamente aprendimos como utilizar importando un archivo externo en nuestro archivo main de nuestro proyecto. Existe un módulo en Python para obtener acceso al código en otro módulo haciendo uso del proceso de importación. La instrucción <b>import</b> es la forma más común de invocar este proceso de importación. A continuación se observan los códigos realizados en clase:
~~~
import SUMA as S
import RESTAR as R
import MULTIPLICAR as M
import DIVIDIR as D
import CUADRADO as C

if __name__ == "__main__":

    NumeroUno = 15
    NumeroDos = 10
    print("SUMA:",S.sumar(NumeroUno,NumeroDos))
    print("RESTAR:",R.restar(NumeroUno,NumeroDos))
    print("MULTIPLICAR:",M.Multiplicar(NumeroUno,NumeroDos))
    print("DIVIDIR:",D.Dividir(NumeroUno,NumeroDos))
    print("ELEVAR EL PRIMER NUMERO AL CUADRADO:",C.Cuadrado(NumeroUno))
    print("ELEVAR EL SEGUNDO NUMERO AL CUADRADO:", C.Cuadrado(NumeroDos))  
~~~

 ### 3. MANEJO DE LAS F STRING EN PYTHON 3
En esta sección se abordaron muchos temas demasiado interesantes y útiles a la hora de programar, hablo de <b>formatted string literals</b> ó <b>Formateo literal de cadenas</b> 
  
  
