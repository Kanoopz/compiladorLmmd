
class typesMatching:

    def __init__(self):
        self.cube = {
            ('+', 'int', 'int')         : 'int',
            ('+', 'int', 'float')        : 'float',
            ('+', 'float', 'int')        : 'float',
            ('+', 'float', 'float')       : 'float',
            ('-', 'int', 'int')         : 'int',
            ('-', 'int', 'float')        : 'float',
            ('-', 'float', 'int')        : 'float',
            ('-', 'float', 'float')       : 'float',
            ('*', 'int', 'int')         : 'int',
            ('*', 'int', 'float')        : 'float',
            ('*', 'float', 'int')        : 'float',
            ('*', 'float', 'float')       : 'float',
            ('/', 'int', 'int')         : 'int',
            ('/', 'int', 'float')        : 'float',
            ('/', 'float', 'int')        : 'float',
            ('/', 'float', 'float')       : 'float',
            ('&', 'bool', 'bool')       : 'bool',
            ('|', 'bool', 'bool')       : 'bool',
            ('>', 'int', 'int')         : 'bool',
            ('>', 'int', 'float')        : 'bool',
            ('>', 'float', 'int')        : 'bool',
            ('>', 'float', 'float')       : 'bool',
            ('<', 'int', 'int')         : 'bool',
            ('<', 'int', 'float')        : 'bool',
            ('<', 'float', 'int')        : 'bool',
            ('<', 'float', 'float')       : 'bool',
            ('==', 'int', 'int')        : 'bool',
            ('==', 'int', 'float')       : 'bool',
            ('==', 'float', 'int')       : 'bool',
            ('==', 'float', 'float')      : 'bool',
            ('==', 'char', 'char')        : 'bool',
            ('==', 'CTE_LETRERO', 'CTE_LETRERO')  : 'bool',
            ('==', 'bool', 'bool')      : 'bool',
            ('!=', 'int', 'int')        : 'bool',
            ('!=', 'int', 'float')       : 'bool',
            ('!=', 'float', 'int')       : 'bool',
            ('!=', 'float', 'float')      : 'bool',
            ('!=', 'char', 'char')        : 'bool',
            ('!=', 'CTE_LETRERO', 'CTE_LETRERO')  : 'bool',
            ('!=', 'bool', 'bool')      : 'bool',
            ('=', 'int', 'int')      : 'int',
            ('=', 'float', 'float')      : 'float',
            ('=', 'float', 'int')      : 'float',
            ('=', 'char', 'char')      : 'char',
            ('=', 'bool', 'bool')      : 'bool',
        }

    def match(self, tuple):
        type = self.cube.get(tuple, 'ERROR: MISMATCH')
    
        if(type != 'ERROR: MISMATCH'):
            return type
        elif(type == 'ERROR: MISMATCH'):
            raise TypeError("ERROR: MISMATCH ON RECEIVED VALUES COMPATIBILTY")
