import ply.yacc as yacc
from Lexer import tokens
from Lexer import analizador

variable =[]
dicValor = ''
resultadoParser = []

def p_option(p):
    '''opt : assign
            | if
            | else
            | funcionReturn
            | funcionFrom
            | sentenciaPrint'''
    p[0] = p[1]

def p_assign(p):
    '''assign : var string
            | var diccionario
            | var input
            | var cargarDatoDiccionario
            | var restaLongitudAltitud
            | var funcionCalcularA
            | var funcionCalcularC
            | var funcionCalcularKm'''
    p[0] = p[1] + p[2]

def p_input(p):
    'input : INPUT LPAREN string RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_diccionario(p):
    '''diccionario : ILLAVE info DLLAVE '''
    p[0] = p[1] + p[2] + p[3]

def p_info(p):
    '''info : keys TWOPOINT lista
            | keys TWOPOINT lista COMA info'''
    if len(p) == 4:
        p[0] = str(p[1]) + p[2] + str(p[3])
    elif len(p) ==6:
        p[0] = str(p[1]) + p[2] + str(p[3]) + p[4] + p[5]

def p_keys(p):
    '''keys : string
            | number
            | float'''
    p[0] = p[1]

def p_lista(p):
    'lista : LCORCH contenido RCORCH'
    p[0] = p[1] + p[2] + p[3]

def p_contenido(p):
    '''contenido : items
                | items COMA contenido'''
    if len(p) == 2:
        p[0] = str(p[1])
    elif len(p) == 4:
        p[0] = str(p[1]) + p[2] + p[3]

def p_items(p):
    '''items : string
            | number
            | float
            | lista'''
    p[0] = p[1]

def p_var(p):
    'var : text EQUALS'
    p[0] = p[1] + p[2]
    variable.append(p[1])

def p_text(p):
    'text : NAME'
    p[0] = p[1]

def p_string(p):
    'string : COMILLA text COMILLA'
    p[0] = p[1] + p[2] + p[3]

def p_float(p):
    'float : FLOAT'
    p[0] = p[1]

def p_number(p):
    'number : NUMBER'
    p[0] = p[1]

def p_cargarDatoDiccionario(p):
    '''cargarDatoDiccionario :  obtencionValorDiccionario obtencionIndex'''
    # if p[1] in variables and p[3] in variables:
    p[0] = p[1] + p[2]

def p_obtencionValorDiccionario(p):
    'obtencionValorDiccionario : text POINT GET LPAREN text RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_obtencionIndex(p):
    'obtencionIndex : LCORCH number RCORCH'
    p[0] = p[1] + str(p[2]) + p[3]

def p_sentenciaPrint(p):
    '''sentenciaPrint : PRINT LPAREN string RPAREN
                | PRINT LPAREN string COMA text RPAREN
                | PRINT LPAREN text RPAREN'''
    if len(p) == 5:
        p[0] = p[1] + p[2] + p[3] + p[4]
    else:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_if(p):
    '''if : IF LPAREN condicion RPAREN TWOPOINT
                | IF condicion TWOPOINT'''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]

def p_else(p):
    '''else : ELSE TWOPOINT'''
    p[0] = p[1] + p[2]

def p_condicion(p):
    '''condicion : text IN funcionItems AND text IN funcionItems'''
    # if p[1] != p[5]:
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] +p[7]

def p_funcionItems(p):
    'funcionItems : text POINT KEYS LPAREN RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4] +p[5]

def p_restaLongitudAltitud(p):
    'restaLongitudAltitud : text MINUS text'
    p[0] = p[1] + p[2] + p[3]

def p_funcionCalcularA(p):
    'funcionCalcularA : funcionSinGeneral TIMES funcionSin2'
    p[0] = p[1] + p[2] + p[3]

def p_funcionSinGeneral(p):
    'funcionSinGeneral : funcionSin1 PLUS funcionCos'
    p[0] = p[1] + p[2] +p[3]

def p_funcionSin1(p):
    'funcionSin1 : SIN LPAREN text DIV number RPAREN EXP number '
    if p[5] == 2 and p[8] == 2:
        p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + str(p[8])

def p_funcionSin2(p):
    'funcionSin2 : SIN LPAREN text DIV number RPAREN EXP number '
    if p[5] == 2 and p[8] == 2:
        p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + str(p[8])

def p_funcionCos(p):
    'funcionCos : COS LPAREN text RPAREN TIMES COS LPAREN text RPAREN'
    if p[3] != p[8]:
        p[0] = p[1] + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + p[8] +p[9]

def p_funcionCalcularC(p):
    'funcionCalcularC : number TIMES ASIN LPAREN SQRT LPAREN text RPAREN RPAREN'
    if p[1] == 2:
        p[0] = str(p[1]) + p[2] + p[3] + p[4] + str(p[5]) + p[6] + p[7] + p[8] +p[9]

def p_funcionCalcularKm(p):
    'funcionCalcularKm : number TIMES text'
    if p[1] == 6367:
        p[0] = str(p[1]) + p[2] + p[3]

def p_funcionReturn(p):
    'funcionReturn : RETURN text'
    p[0] = p[1] + p[2]

def p_funcionFrom(p):
    'funcionFrom : FROM MATH IMPORT TIMES'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_error(p):
    global resultadoParser
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(p)
        print(resultado)
    resultadoParser.append(resultado)

# instanciar el parser
parser = yacc.yacc()

def testParser(data):
    global resultadoParser
    resultadoParser.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultadoParser.append(str(gram))
        else:
            print("Datos vacio")

    #print("Resultado Parser: ", resultadoParser)
    return resultadoParser

# if __name__ == '__main__':
#     while True:
#         try:
#             s = input(' ingresa dato >>> ')
#         except EOFError:
#             continue
#         if not s: continue
#         testParser(s)