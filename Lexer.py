import ply.lex as lex

class lexer:
    errors = []

    # tokens = [
    #     'NAME', 'NUMBER', 'EQUALS', 'COMILLA', 'FLOAT', 'TWOPOINT', 'ESPACIO',
    #     'LPAREN', 'RPAREN', 'LCORCH', 'RCORCH', 'COMA', 'IN', 'IF',  'ELSE', 'ELIF','PRINT','TRUE','FALSE'
    # ]

    tokens = [
        'NAME', 'NUMBER', 'EQUALS', 'COMILLA', 'FLOAT', 'TWOPOINT', 'ESPACIO',
        'LPAREN', 'RPAREN', 'LCORCH', 'RCORCH', 'COMA'
    ]
    reservadas = {
        'in': 'IN',
        'if': 'IF',
        'else': 'ELSE',
        'elif': 'ELIF',
        'print': 'PRINT',
        'True': 'TRUE',
        'False': 'FALSE'
    }
    tokens += list(reservadas.values())

    # t_IN = r'in'
    # t_IF = r'if'
    # r_ELIF = r'elif'
    # r_ELSE = r'else'
    # r_PRINT = r'print'
    # r_TRUE = r'True'
    # r_FALSE = r'False'
    t_ignore = ' \t'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LCORCH = r'\['
    t_RCORCH = r'\]'
    t_COMA = r'\,'
    t_EQUALS = r'='
    t_TWOPOINT = r':'
    t_ESPACIO = r'\s'

    def t_NAME(self,t):
        r'[a-z_][a-zA-z0-9_\-]*'
        if(t.value in reservadas.keys()):
            t.type = reservadas[t.value]
            return t
        return t

    def t_FLOAT(self,t):
        r'\d+\.\d*'
        t.value = float(t.value)
        return t

    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_TRUE(self,t):
        r'True'
        if t.value in reservadas.keys():
            t.type = reservadas[t.value]
            return t
        return t

    def t_FALSE(self,t):
        r'False'
        if t.value in reservadas.keys():
            t.type = reservadas[t.value]
            return t
        return t

    def t_COMILLA(self,t):
        r'"|\''
        return t

    def t_COMMENT(self,t):
        r'\#.*'
        pass

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # def test(self,data):
    #     self.errors = []
    #     self.lexer.input(data)
    #     while True:
    #          tok = self.lexer.token()
    #          if not tok: break
    #          print(tok)
    #
    # def report(self):
    #     return self.errors