from Lexer import *
from Parser import *

if __name__=='__main__':
    entrada = "print('dfsvfsdfvdfd')"
    entrada1 = "var = ['cs', True , ['csdc',1]]"
    entrada2 = "if('csc' in ['cdsac']):"
    entrada3 = "elif('csc' in'string'):"
    entrada4 = "else:"
    entrada5 = "var={\"rutaSur\":[\"lasValdivias\",\"puertoMoro\"]}"
    entrada6 = "for(clave,valor in dic.items()):"
    entrada8 = "if(variable in dic):"
    entrada7 = "variable = input('sdvfs')"
    listaPrueba = [entrada, entrada1, entrada2,entrada3,entrada4,entrada5,entrada6,entrada7]

    for li in range(len(listaPrueba)):
        resultado_lexico = testLexer(listaPrueba[li])
        print("Resultador Lexer: ", resultado_lexico)
        resultado_parser = testParser(listaPrueba[li])
        print("Resultado Parser: ", resultado_parser)
        print("\n")

