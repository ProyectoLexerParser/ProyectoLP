import ply.lex as lex
resultadoLexer = []
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
    global resultadoLexer
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),str(t.lexpos))
    resultadoLexer.append(estado)
    t.lexer.skip(1)

# Testing

def testLexer(data):
    global resultadoLexer

    analizador = lex.lex()
    analizador.input(data)

    resultadoLexer.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        #resultadoLexer.append(estado)
        tok = lex.token()
        resultadoLexer.append(tok)
    return resultadoLexer

 # instancia del lexer
analizador = lex.lex()

# if __name__ == '__main__':
#     while True:
#         data = input("ingrese: ")
#         testLexer(data)
#         print("Resultador lexer:" + resultadoLexer)