import ply.lex as lex

tokens = [
    'ID',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_CHAR',
    'CTE_LETRERO',
    'IGUAL_QUE',
    'DIFERENTE_QUE',
    'MAYOR_QUE',
    'MENOR_QUE'
]

reserved = {
    'program' : 'PROGRAM',
    'vars' : 'VARS',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'function' : 'FUNCTION',
    'void' : 'VOID',
    'return' : 'RETURN',
    'main' : 'MAIN',
    'read' : 'READ',
    'write' : 'WRITE',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO',
    'to' : 'TO',
    'for' : 'FOR'
}

#literals = ',;][}{)(=+-*/><=&|'
literals = ['(', ')', '[', ']', '{', '}', '+', '-', '*', '/', '|', '&', '>', '<', '=', ',', ':', ';']



tokens = tokens + list(reserved.values())



def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9<>\-\?]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTE_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_CTE_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_CHAR(t):
    r'\'[0-9A-Za-z_ ]{1}\''
    t.value = list(t.value)[1]
    return t

t_CTE_LETRERO = r'\"([^\\]|(\\.))*?\"'

t_IGUAL_QUE = r'\=\='
t_DIFERENTE_QUE = r'\!\='
t_MAYOR_QUE = r'\>\='
t_MENOR_QUE = r'\<\='


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)





lexer = lex.lex()
 
def test():
    print('Testing')
    file = open('./tests/fileToUse.lmmd')
    input_str = file.read()
    file.close()
    lexer.input(input_str)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

test()