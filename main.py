import Lexer as lex
import Parser as parser

if __name__=='__main__':
    le = lex.lexer()#constructor de la clase lexer
    le.build()
    # le.test('5')  # Test it
    # print(le.report())

    par = parser.Parser() # constructor de la clase parser
    par.buildP()

    # #le.probar('True')
    # par.cargarParser()
    entrada = "print('dfsd')"
    entrada1 = "var = ['cs', True , ['csdc',1]]"
    entrada2 = "if('csc' in ['cdsac']):"
    entrada3 = "elif('csc' in 'string'):"
    entrada4 = "else:"
    par.probarParser('True')


