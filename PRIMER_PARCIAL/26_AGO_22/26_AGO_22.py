import SUMA as S #Para llamar al archivo "SUMA.py". El "as" es para asignar un apodo a ese archivo.
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