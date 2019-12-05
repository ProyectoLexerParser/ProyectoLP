import ply.lex as lex
resultadoLexer = []

tokens = [
        'NAME', 'NUMBER', 'EQUALS', 'COMILLA', 'FLOAT','TWOPOINT', 'AND','SQRT', 'EXP', 'DIV', 'TIMES','GET', 'MINUS', 'MATH',
        'COS','SIN', 'ASIN','LPAREN', 'RPAREN','LCORCH', 'RCORCH','COMA', 'POINT', 'ILLAVE', 'DLLAVE','KEYS', 'PLUS'
]

reservadas = {
    'input': 'INPUT',
    'in':'IN',
    'if':'IF',
    'else':'ELSE',
    'print':'PRINT',
    'return' : 'RETURN',
    'from' : 'FROM',
    'import' :'IMPORT'
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
t_POINT = r'\.'
t_ILLAVE = r'\{'
t_DLLAVE= r'\}'

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_GET(t):
    r'get'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_KEYS(t):
    r'keys'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_MATH(t):
    r'math'
    return t

def t_ITEMS(t):
    r'items'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_FROM(t):
    r'from'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_SQRT(t):
    r'sqrt'
    return t

def t_COS(t):
    r'cos'
    return t

def t_SIN(t):
    r'sin'
    return t

def t_ASIN(t):
    r'asin'
    return t

def t_EXP(t):
    r'\*{2}'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_AND(t):
    r'and'
    return t

def t_FLOAT(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-z0-9_\-]*'
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

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        testLexer(data)
        print("Resultador lexer:", resultadoLexer)