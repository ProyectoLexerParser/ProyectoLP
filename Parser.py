import ply.yacc as yacc

from Lexer import lexer


class Parser(lexer):
    def p_option(self, p):
        '''opt : assign
                | print
                | if
                | elif
                | else
                | lista'''
        p[0] = p[1]

    def p_assign(self, p):
        '''assign : var lista
                | var string
                | var float
                | var number
                | var bool'''
        p[0] = p[2]

    def p_lista(self, p):
        'lista : LCORCH contenido RCORCH'
        p[0] = p[1] + p[2] + p[3]

    def p_contenido(self, p):
        '''contenido : items
                    | items COMA contenido'''
        if len(p) == 2:
            p[0] = str(p[1])
        elif len(p) == 4:
            p[0] = str(p[1]) + p[2] + p[3]

    def p_items(self, p):
        '''items : string
                | number
                | float
                | bool
                | lista'''
        p[0] = p[1]

    def p_print(self, p):
        'print : PRINT LPAREN string RPAREN'
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_var(self, p):
        'var : text EQUALS'
        p[0] = p[1] + p[2]

    def p_text(self, p):
        'text : NAME'
        p[0] = p[1]

    def p_string(self, p):
        'string : COMILLA text COMILLA'
        p[0] = p[1] + p[2] + p[3]

    def p_bool(self, p):
        ''' bool : TRUE
                | FALSE'''
        p[0] = p[1]

    def p_float(self, p):
        'float : FLOAT'
        p[0] = p[1]

    def p_number(self, p):
        'number : NUMBER'
        p[0] = p[1]

    # ENTRADA por bloque

    def p_sentencia(self, p):
        'sentencia : ESPACIO print'
        p[0] = p[1] + p[2]

    def p_if(self, p):
        '''if : IF LPAREN condicion RPAREN TWOPOINT
                    | IF condicion TWOPOINT'''
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_elif(self, p):
        '''elif : ELIF LPAREN condicion RPAREN TWOPOINT
                    | ELIF condicion TWOPOINT'''
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_else(self, p):
        '''else : ELSE TWOPOINT'''
        p[0] = p[1] + p[2]

    def p_condicion(self, p):
        '''condicion : string IN string
                    | string IN lista
                    | number IN string
                    | bool IN lista
                    | float IN lista'''
        p[0] = str(p[1]) + p[2] + p[3]

    def p_error(self, p):
        print("Syntax error!")

    def buildP(self, **kwargs):
        self.parser = yacc.yacc(module=self,**kwargs)


    def probarParser(self,entrada):
        res = self.parser.parse(entrada)
        print(res)