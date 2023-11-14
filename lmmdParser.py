import ply.yacc as yacc
from lmmdLexer import tokens

from varsTable import declaredScopedVars
scopedDeclaredVars = declaredScopedVars()



def p_programa(t):
    '''
    programa : PROGRAM ID ';' pn_set_global dec_var def_func impl_main pn_get_vars_table
    '''

def p_dec_var(t):
    '''
    dec_var : VARS tipos ':' id_dec_var ';' dec_var_prime
    '''

def p_tipos(t):
    '''
    tipos : INT pn_set_type
	    | FLOAT pn_set_type
	    | CHAR pn_set_type
    '''
    #print(t[1])

def p_id_dec_var(t):
    '''
    id_dec_var : ID pn_add_var '[' CTE_INT ']' id_dec_var_prime
	    | ID pn_add_var id_dec_var_prime
    '''
    #print(t[1])

def p_id_dec_var_prime(t):
    '''
    id_dec_var_prime : ',' ID pn_add_var '[' CTE_INT ']' id_dec_var_prime
        | ',' ID pn_add_var id_dec_var_prime
        | null
    '''

def p_dec_var_prime(t):
    '''
    dec_var_prime : tipos ':' id_dec_var ';' dec_var_prime
        | null
    '''



def p_def_func(t):
    '''
    def_func : FUNCTION tipos_func ID pn_set_scope '(' tipos ID pn_add_var param_prime ')' func_dec_var '{' est est_prime func_return '}' def_func_prime
        | FUNCTION tipos_func ID pn_set_scope '(' ')' func_dec_var '{' est est_prime func_return '}' def_func_prime
        | null
    '''

def p_tipos_func(t):
    '''
    tipos_func : INT
        | FLOAT
        | CHAR
        | VOID
    '''
    #print(t[1])
    #ESTE ES SOLO PARA EL RETORNO DE LAS FUNCIONES, NO SE USA EN VARIABLES

def p_param_prime(t):
    '''
    param_prime : ',' tipos ID pn_add_var param_prime
        | null
    '''

def p_func_dec_var(t):
    '''
    func_dec_var : dec_var
        | null
    '''

def p_func_return(t):
    '''
    func_return : RETURN '(' hiper_exp ')' ';'
        | null
    '''

def p_def_func_prime(t):
    '''
    def_func_prime : FUNCTION tipos_func ID pn_set_scope '(' tipos ID pn_add_var param_prime ')' func_dec_var '{' est est_prime func_return '}' def_func_prime
        | null
    '''

def p_impl_main(t):
    '''
    impl_main : MAIN '(' ')' '{' est est_prime '}'
    '''


def p_est(t):
    '''
    est : est_asig
        | est_llam_func
        | lectura
        | escritura
        | est_deci
        | est_rep_con
        | est_rep_no_con
    '''

def p_est_prime(t):
    '''
    est_prime : est_asig est_prime
        | est_llam_func est_prime
        | lectura est_prime
        | escritura est_prime
        | est_deci est_prime
        | est_rep_con est_prime
        | est_rep_no_con est_prime
        | null
    '''

def p_est_asig(t):
     '''
     est_asig : var_id '=' hiper_exp ';'
    '''
     
def p_var_id(t):
     '''
     var_id : ID
        | ID '[' hiper_exp ']'
     '''
     
def p_hiper_exp(t):
     '''
     hiper_exp : super_exp
        | super_exp '&' super_exp
        | super_exp '|' super_exp
    '''
     
def p_super_exp(t):
     '''
     super_exp : exp
        | exp '<' exp
        | exp '>' exp
        | exp IGUAL_QUE exp
        | exp DIFERENTE_QUE exp
    '''
     
def p_exp(t):
     '''
     exp : term
        | term '+' term
        | term '-' term
    '''
     
def p_term(t):
     '''
     term : factor
        | factor '*' factor
        | factor '/' factor
    '''
     
def p_factor(t):
     '''
     factor : var_id
        | ctes
        | est_llam_func
        | sub_exp
    '''
     
def p_ctes(t):
     '''
     ctes : CTE_INT
        | CTE_FLOAT
        | CTE_CHAR
        | CTE_LETRERO
    '''
     
def p_sub_exp(t):
     '''
     sub_exp : '(' factor ')'
    '''
     
def p_est_llam_func(t):
     '''
     est_llam_func : ID '(' llam_func_param ')' ';'
        | ID '(' llam_func_param ')'
    '''
     
def p_llam_func_param(t):
     '''
     llam_func_param : hiper_exp llam_func_param_prime
        | null
    '''
     
def p_llam_func_param_prime(t):
     '''
     llam_func_param_prime : ',' hiper_exp llam_func_param_prime
        | null
    '''
     
def p_lectura(t):
     '''
     lectura : READ '(' llam_lect_param ')' ';'
    '''
     
def p_llam_lect_param(t):
     '''
     llam_lect_param : var_id llam_lect_param_prime
        | null
    '''
     
def p_llam_lect_param_prime(t):
     '''
     llam_lect_param_prime : ',' var_id llam_lect_param_prime
        | null
    '''
     
def p_escritura(t):
     '''
     escritura : WRITE '(' escritura_param ')' ';'
    '''
     
def p_escritura_param(t):
     '''
     escritura_param : hiper_exp escritura_param_prime
        | null
    '''
     
def p_escritura_param_prime(t):
     '''
     escritura_param_prime : ',' hiper_exp escritura_param_prime
        | null
    '''

def p_est_deci(t):
     '''
     est_deci : IF '(' hiper_exp ')' '{' est est_prime '}' deci_else
    '''
     
def p_deci_else(t):
     '''
     deci_else : ELSE '{' est est_prime '}'
        | null
    '''
     
def p_est_rep_con(t):
     '''
     est_rep_con : WHILE '(' hiper_exp ')' DO '{' est est_prime '}'
    '''
     
def p_est_rep_no_con(t):
     '''
     est_rep_no_con : FOR ID est_rep_no_con_id '=' hiper_exp TO hiper_exp DO '{' est est_prime '}'
    '''
     
def p_est_rep_no_con_id(t):
     '''
     est_rep_no_con_id : '[' exp ']'
        | null
    '''
     
    

    




def p_null(t):
    '''
    null :
    '''
    pass

def p_error(t):
    '''
    '''
    raise Exception("Error en linea " + str(t.lineno))

#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================


def p_pn_add_var(t):
     '''
     pn_add_var : null
     '''
     print(t[-1])
     scopedDeclaredVars.addVar(t[-1])
        
     

def p_pn_set_global(t):
     '''
     pn_set_global : null
     '''
     print("Scope Global==================================")
     scopedDeclaredVars.setActualScope('Global')

def p_pn_set_scope(t):
     '''
     pn_set_scope : null
     '''
     print("Scope " + t[-1] +  "==================================")
     scopedDeclaredVars.setActualScope(t[-1])

def p_pn_set_type(t):
     '''
     pn_set_type : null
     '''
     print("Type " + t[-1])
     scopedDeclaredVars.setActualType(t[-1])

def p_pn_get_vars_table(t):
     '''
     pn_get_vars_table : null
     '''
     scopedDeclaredVars.getVarTable()




parser = yacc.yacc()
    





