import ply.yacc as yacc
from Lexer import tokens
from Lexer import analizador

variable =[]
dicValor = ''
resultadoParser = []

def p_option(p):
    '''opt : assign
            | print
            | if
            | elif
            | else
            | for
            | lista'''
    p[0] = p[1]

def p_assign(p):
    '''assign : var lista
            | var string
            | var float
            | var number
            | var bool
            | var diccionario
            | var input '''
    p[0] = p[2]

def p_input(p):
    'input : INPUT LPAREN string RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_diccionario(p):
    '''diccionario : ILLAVE info DLLAVE '''
    p[0] = p[1] + p[2] + p[3]

def p_info(p):
    '''info : keys TWOPOINT items
            | keys TWOPOINT items COMA info'''
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
            | bool
            | lista'''
    p[0] = p[1]

def p_print(p):
    'print : PRINT LPAREN string RPAREN'
    p[0] = p[1] + p[2] + p[3] + p[4]

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

def p_bool(p):
    ''' bool : TRUE
            | FALSE'''
    p[0] = p[1]

def p_float(p):
    'float : FLOAT'
    p[0] = p[1]

def p_number(p):
    'number : NUMBER'
    p[0] = p[1]

# ENTRADA por bloque

def p_sentencia(p):
    'sentencia : ESPACIO print'
    p[0] = p[1] + p[2]

def p_for(p):
    '''for : FOR LPAREN condicionfor RPAREN TWOPOINT
            | FOR condicionfor TWOPOINT'''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]

def p_condicionfor(p):
    '''condicionfor : NAME COMA NAME IN funcionitems '''
    if p[1] != p[3]:
        dicValor = p[3]
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_funcionitems(p):
    'funcionitems : NAME POINT ITEMS LPAREN RPAREN'
    p[0] = p[1] + p[2] + p[3] +p[4] + p[5]

def p_if(p):
    '''if : IF LPAREN condicion RPAREN TWOPOINT
                | IF condicion TWOPOINT'''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]

def p_elif(p):
    '''elif : ELIF LPAREN condicion RPAREN TWOPOINT
                | ELIF condicion TWOPOINT'''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]

def p_else(p):
    '''else : ELSE TWOPOINT'''
    p[0] = p[1] + p[2]

def p_condicion(p):
    '''condicion : string IN string
                | NAME IN lista
                | NAME IN string
                | string IN lista
                | number IN string
                | bool IN lista
                | float IN lista
                | NAME IN NAME'''
    #if p[1] == dicValor:
    p[0] = p[1] + p[2] + p[3]

    #p[0] = str(p[1]) + p[2] + p[3]

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