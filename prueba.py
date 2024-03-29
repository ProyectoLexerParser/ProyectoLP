import ply.lex as lex
import ply.yacc as yacc

variable =[]
dicValor = ''
tokens = [
        'NAME', 'NUMBER', 'EQUALS', 'COMILLA', 'FLOAT','TWOPOINT','ESPACIO',
        'LPAREN', 'RPAREN','LCORCH', 'RCORCH','COMA', 'POINT', 'ILLAVE', 'DLLAVE'
    ]

reservadas = {
    'in':'IN',
    'if':'IF',
    'else':'ELSE',
    'elif':'ELIF',
    'print':'PRINT',
    'True': 'TRUE',
    'False': 'FALSE',
    'for' : 'FOR',
    'items' : 'ITEMS',
    'input' : 'INPUT'
}

tokens+=list(reservadas.values())

t_ignore = ' \t'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_COMA = r'\,'
t_EQUALS = r'='
t_TWOPOINT = r':'
t_ESPACIO = r'\s'
t_POINT = r'\.'
t_ILLAVE = r'\{'
t_DLLAVE= r'\}'

def t_NAME(t):
    r'[a-z_][a-zA-z0-9_\-]*'
    if t.value in reservadas.keys():
        t.type = reservadas[t.value]
        return t
    return t

def t_FLOAT(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TRUE(t):
    r'True'
    if t.value in reservadas.keys():
        t.type = reservadas[t.value]
        return t
    return t

def t_FALSE(t):
    r'False'
    if t.value in reservadas.keys():
        t.type = reservadas[t.value]
        return t
    return t

def t_COMILLA(t):
    r'"|\''
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

#Entrada por medio de variable

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
    print("Syntax error!")

parser = yacc.yacc()
entrada = "print('dfsvfsdfvdfd')"
entrada1 = "var = ['cs', True , ['csdc',1]]"
entrada2 = "if('csc' in ['cdsac']):"
entrada3 = "elif('csc' in'string'):"
entrada4 = "else:"
entrada5 = "var={\"rutaSur\":[\"lasValdivias\",\"puertoMoro\"]}"
entrada6 = "for(clave,valor in dic.items()):"
entrada8 = "if(variable in dic):"
entrada7 = "variable = input('sdvfs')"
res = parser.parse(entrada5)
print(res)

