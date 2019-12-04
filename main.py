from Lexer import *
from Parser import *

if __name__=='__main__':
    entrada = "dicc={\"urdesa\":[15,24],\"guasmo\":[34,47]}"
    entrada1 = "if(origen in dicc.keys() and destino in dicc.keys()):"
    entrada2 = "log = dicc.get(origen)[0]"
    entrada3 = "dict={\"urdesa\":['da','das']}"
    entrada4 = "a=sin(dlta/2)**2 * sin(dlta/2)**2 * cos(var1) * cos(var2)"
    entrada6 = "lat = var1 - var2"
    entrada5 = "else:"
    entrada7 = "c=2*asin(sqrt(a))"
    entrada8 = "km = 6367 * c"
    entrada9 = "return km"
    entrada10 = "from math import *"
    algoritmo = "from math import *\n dicc={\"urdesa\":[15,24],\"guasmo\":[34,47], \"trinitaria\":[150,4]} \n origen = input('CoordenadaOrigen')\n destino = input('CoordenadaDestino') \n if(origen in dicc.keys() and destino in dicc.keys()): \n log1 = dicc.get(origen)[0] \n lat1 = dicc.get(origen)[1] \n log2 = dicc.get(destino)[0] \n lat2 = dicc.get(destino)[1] \n dlog = log2 - log1 \n lat = lat2 - lat1 \n a=sin(dlta/2)**2 * sin(dlta/2)**2 * cos(var1) * cos(var2)\n c=2*asin(sqrt(a)) \n km = 6367 * c\n return km \n else: \n print('ERROR')"
    # listaPrueba = [entrada, entrada1, entrada2, entrada3, entrada4, entrada5,entrada6,entrada7,entrada8,entrada9, entrada10]
    lista = algoritmo.split('\n')
    print(lista)
    for li in range(len(lista)):
        resultado_lexico = testLexer(lista[li])
        print("Resultador Lexer: ", resultado_lexico)
        resultado_parser = testParser(lista[li])
        print("Resultado Parser: ", resultado_parser)
        print("\n")


