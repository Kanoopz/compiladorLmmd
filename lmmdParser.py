import ply.yacc as yacc
from lmmdLexer import tokens

from varsTable import declaredScopedVars
scopedDeclaredVars = declaredScopedVars()

from neuralgicPoint import NP
np = NP()



#operandsStack = []
#typesStack = []
#operatorsStack = []
#actualAritmeticScope = 'noInitialized'

#temporalsCounter = 0
#quadruplesDictionary = {}



def p_programa(t):
    '''
    programa : PROGRAM ID ';' pn_set_global dec_var def_func impl_main pn_aritmetic_expressions_print pn_get_vars_table print_funcs_data
    '''

def p_dec_var(t):
    '''
    dec_var : VARS tipos ':' id_dec_var ';' dec_var_prime
    '''

def p_tipos(t):
    '''
    tipos : INT pn_set_type pn_module_definition_2_and_3_part_1
	    | FLOAT pn_set_type pn_module_definition_2_and_3_part_1
	    | CHAR pn_set_type pn_module_definition_2_and_3_part_1
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
    def_func : FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 param_prime ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 def_func_prime
        | FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 def_func_prime
        | null
    '''

def p_tipos_func(t):
    '''
    tipos_func : INT pn_module_definition_1_2
        | FLOAT pn_module_definition_1_2
        | CHAR pn_module_definition_1_2
        | VOID pn_module_definition_1_2
    '''
    #print(t[1])
    #ESTE ES SOLO PARA EL RETORNO DE LAS FUNCIONES, NO SE USA EN VARIABLES

def p_param_prime(t):
    '''
    param_prime : ',' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 param_prime
        | null
    '''

def p_func_dec_var(t):
    '''
    func_dec_var : f_dec_var
        | null
    '''





def p_f_dec_var(t):
    '''
    f_dec_var : VARS f_tipos ':' f_id_dec_var ';' f_dec_var_prime
    '''

def p_f_tipos(t):
    '''
    f_tipos : INT pn_set_type pn_module_definition_4_1 
	    | FLOAT pn_set_type pn_module_definition_4_1
	    | CHAR pn_set_type pn_module_definition_4_1
    '''
    #print(t[1])

def p_f_id_dec_var(t):
    '''
    f_id_dec_var : ID pn_add_var pn_module_definition_4_2 '[' CTE_INT ']' f_id_dec_var_prime
	    | ID pn_add_var pn_module_definition_4_2 f_id_dec_var_prime
    '''
    #print(t[1])

def p_f_id_dec_var_prime(t):
    '''
    f_id_dec_var_prime : ',' ID pn_add_var pn_module_definition_4_2 '[' CTE_INT ']' f_id_dec_var_prime
        | ',' ID pn_add_var pn_module_definition_4_2 f_id_dec_var_prime
        | null
    '''

def p_f_dec_var_prime(t):
    '''
    f_dec_var_prime : f_tipos ':' f_id_dec_var ';' f_dec_var_prime
        | null
    '''





def p_func_return(t):
    '''
    func_return : RETURN '(' hiper_exp ')' ';'
        | null
    '''

def p_def_func_prime(t):
    '''
    def_func_prime : FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 param_prime ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 def_func_prime
        | FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 def_func_prime
        | null
    '''

def p_impl_main(t):
    '''
    impl_main : MAIN pn_set_aritmetic_expressions_scope_global '(' ')' '{' est est_prime '}'
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
        | null
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
     est_asig : ID pn_sequential_statute_1 '=' pn_sequential_statute_2 hiper_exp pn_sequential_statute_3 ';'
        | ID pn_sequential_statute_1 '[' hiper_exp ']' '=' pn_sequential_statute_2 hiper_exp pn_sequential_statute_3 ';'
    '''
     
def p_hiper_exp(t):
     '''
     hiper_exp : super_exp super_exp_prime
    '''

def p_super_exp(t):
     '''
     super_exp : exp exp_prime
     '''

def p_super_exp_prime(t):
     '''
     super_exp_prime : '&' hiper_exp
                    | '|' hiper_exp
                    | null
     '''

def p_exp_prime(t):
    '''
    exp_prime : '>' pn_aritmetic_expressions_8 super_exp pn_aritmetic_expressions_9
              | '<' pn_aritmetic_expressions_8 super_exp pn_aritmetic_expressions_9
              | IGUAL_QUE pn_aritmetic_expressions_8 super_exp pn_aritmetic_expressions_9
              | DIFERENTE_QUE pn_aritmetic_expressions_8 super_exp pn_aritmetic_expressions_9
              | null
    '''

def p_exp(t):
    '''
    exp : term term_prime
    '''

def p_term_prime(t):
    '''
    term_prime : pn_aritmetic_expressions_4 '+' pn_aritmetic_expressions_2 exp
               | pn_aritmetic_expressions_4 '-' pn_aritmetic_expressions_2 exp
               | null
    '''

def p_term(t):
    '''
    term : factor factor_prime
    '''

def p_factor_prime(t):
    '''
    factor_prime : pn_aritmetic_expressions_5 '*' pn_aritmetic_expressions_3 term
                 | pn_aritmetic_expressions_5 '/' pn_aritmetic_expressions_3 term
                 | null
    '''

def p_factor(t):
     '''
     factor : ID pn_aritmetic_expressions_1
        | ID pn_aritmetic_expressions_1 '[' hiper_exp ']'
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
     sub_exp : '(' pn_aritmetic_expressions_6 hiper_exp ')' pn_aritmetic_expressions_7
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
     llam_lect_param : ID pn_read_save_ID pn_read llam_lect_param_prime
        | ID pn_read_save_ID pn_read '[' hiper_exp ']' llam_lect_param_prime
        | null
    '''
     
def p_llam_lect_param_prime(t):
     '''
     llam_lect_param_prime : ',' ID pn_read_save_ID pn_read llam_lect_param_prime
        | ',' ID pn_read_save_ID pn_read '[' hiper_exp ']' llam_lect_param_prime
        | null
    '''
     
def p_escritura(t):
     '''
     escritura : WRITE '(' escritura_param ')' ';'
    '''
     
def p_escritura_param(t):
     '''
     escritura_param : pn_add_pre_process_setup_write hiper_exp pn_pre_process_write pn_write escritura_param_prime
        | null
    '''
     
def p_escritura_param_prime(t):
     '''
     escritura_param_prime : ',' pn_add_pre_process_setup_write hiper_exp pn_pre_process_write pn_write escritura_param_prime
        | null
    '''

def p_est_deci(t):
     '''
     est_deci : IF '(' hiper_exp ')' pn_decision_conditional_statute_1 '{' est est_prime '}' deci_else
    '''
     
def p_deci_else(t):
     '''
     deci_else : ELSE pn_decision_conditional_statute_3 '{' est est_prime '}' pn_decision_conditional_statute_2
        | pn_decision_conditional_statute_2
    '''
     
def p_est_rep_con(t):
     '''
     est_rep_con : WHILE pn_conditional_cycle_while_1 '(' hiper_exp ')' pn_conditional_cycle_while_2 DO '{' est est_prime '}' pn_conditional_cycle_while_3
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

#==============================================================================
#==============================================================================
#==============================================================================

def p_pn_set_aritmetic_expressions_scope_global(t):
     '''
     pn_set_aritmetic_expressions_scope_global : null
     '''
     #actualAritmeticScope = 'Global'
     #print("actualAritmeticScope: " + actualAritmeticScope + "/////////////////////////////////")
     np.setActualAritmeticScope('Global')

def p_pn_set_aritmetic_expressions_scope(t):
     '''
     pn_set_aritmetic_expressions_scope : null
     '''
     #actualAritmeticScope = t[-2]
     #print("actualAitmeticScope: " + actualAritmeticScope + "/////////////////////////////////")
     np.setActualAritmeticScope(t[-2])

def p_pn_aritmetic_expressions_1(t):
     '''
     pn_aritmetic_expressions_1 : null
     '''
     #print("New operand (PN1): " + t[-1])

     actualScope = np.getActualAritmeticScope()
     print("ACTUAL SCOPE:", actualScope)
     print("ID:", t[-1])
     #print("Checking var in dictionary:")
     #print(t[-1])
     #print(actualScope)
     varInDictionary = scopedDeclaredVars.checkVar(t[-1], actualScope)
     
     #print(varInDictionary)
     #print("varInDictionary[0]", varInDictionary[0])
     #print("varInDictionary[1]", varInDictionary[1])
     #print(" ")
     
     if(varInDictionary[0] == True):
        np.addToOperandsStack(t[-1])
        np.addToTypesStack(varInDictionary[1])

def p_pn_aritmetic_expressions_2(t):
     '''
     pn_aritmetic_expressions_2 : null
     '''
     #print("New operator (PN2): " + t[-1])
     #operatorsStack.append(t[-1])
     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_3(t):
     '''
     pn_aritmetic_expressions_3 : null
     '''
     #print("New operator (PN3): " + t[-1])
     #operatorsStack.append(t[-1])
     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_4(t):
     '''
     pn_aritmetic_expressions_4 : null
     '''
     #print("New operator (PN6): " + t[-1])
     #operatorsStack.append(t[-1])
     np.processAdditionOrSubstraction()

def p_pn_aritmetic_expressions_5(t):
     '''
     pn_aritmetic_expressions_5 : null
     '''
     #print("New operator (PN6): " + t[-1])
     #operatorsStack.append(t[-1])
     np.processMultiplicationOrDivision()

def p_pn_aritmetic_expressions_6(t):
     '''
     pn_aritmetic_expressions_6 : null
     '''
     #print("New operator (PN6): " + t[-1])
     #operatorsStack.append(t[-1])
     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_7(t):
     '''
     pn_aritmetic_expressions_7 : null
     '''
     #print("New operator (PN7): " + t[-1])
     #operatorsStack.append(t[-1])
     np.processRightParenthesis()

def p_pn_aritmetic_expressions_8(t):
     '''
     pn_aritmetic_expressions_8 : null
     '''
     #print("New relational operator (PN8): " + t[-1])
     #operatorsStack.append(t[-1])
     np.processRelationalOperator()
     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_9(t):
     '''
     pn_aritmetic_expressions_9 : null
     '''
     #print("New relational operator (PN8): " + t[-1])
     #operatorsStack.append(t[-1])
     #np.addToOperatorsStack(t[-1])
     np.processRelationalOperatorPostExpresion()



def p_pn_aritmetic_expressions_print(t):
     '''
     pn_aritmetic_expressions_print : null
     '''
     #print("Stacks:")
     #print(operandsStack)
     #print(operatorsStack)
     #print("temporal", temporalsCounter)
     np.printStacks()

#==============================================================================
#==============================================================================
#==============================================================================

def p_pn_sequential_statute_1(t):
     '''
     pn_sequential_statute_1 : null
     '''

     actualScope = np.getActualAritmeticScope()
     varInDictionary = scopedDeclaredVars.checkVar(t[-1], actualScope)
     
     if(varInDictionary[0] == True):
        np.addToOperandsStack(t[-1])
        np.addToTypesStack(varInDictionary[1])

def p_pn_sequential_statute_2(t):
     '''
     pn_sequential_statute_2 : null
     '''

     np.addToOperatorsStack(t[-1])

def p_pn_sequential_statute_3(t):
     '''
     pn_sequential_statute_3 : null
     '''
     np.processSequentialStatutePostStatute()

#==============================================================================

def p_pn_read_save_ID(t):
     '''
     pn_read_save_ID : null
     '''
     
     actualScope = np.getActualAritmeticScope()
     varInDictionary = scopedDeclaredVars.checkVar(t[-1], actualScope)
     
     if(varInDictionary[0] == True):
        np.processReadSaveVar(t[-1], varInDictionary[1])

def p_pn_read(t):
     '''
     pn_read : null
     '''
     np.processReadVar()


def p_pn_write(t):
     '''
     pn_write : null
     '''
     np.processWrite()

def p_pn_pre_process_write(t):
     '''
     pn_pre_process_write : null
     '''
     np.preProcessWriteQuadruple()

def p_pn_add_pre_process_setup_write(t):
     '''
     pn_add_pre_process_setup_write : null
     '''
     np.addWritePreProcessToOperandsStack()

#==============================================================================


def p_pn_decision_conditional_statute_1(t):
     '''
     pn_decision_conditional_statute_1 : null
     '''
     np.processDecisionPostConditionalStatute()

def p_pn_decision_conditional_statute_2(t):
     '''
     pn_decision_conditional_statute_2 : null
     '''
     np.processDecisionPostStatement()

def p_pn_decision_conditional_statute_3(t):
     '''
     pn_decision_conditional_statute_3 : null
     '''
     np.processDecisionElse()

#==============================================================================
#==============================================================================
#==============================================================================

def p_pn_conditional_cycle_while_1(t):
    '''
    pn_conditional_cycle_while_1 : null
    '''
    np.processWhileCyclePreExpression() 

def p_pn_conditional_cycle_while_2(t):
    '''
    pn_conditional_cycle_while_2 : null
    '''
    np.processWhileCyclePostExpression()   

def p_pn_conditional_cycle_while_3(t):
    '''
    pn_conditional_cycle_while_3 : null
    '''
    np.processWhileCyclePostStatement()     

#==============================================================================
#==============================================================================
#==============================================================================

def p_pn_module_definition_1_1(t):
    '''
    pn_module_definition_1_1 : null
    '''
    np.processFuncName(t[-3]) 

def p_pn_module_definition_1_2(t):
    '''
    pn_module_definition_1_2 : null
    '''
    np.processFuncType(t[-1]) 

def p_pn_module_definition_2_and_3_part_1(t):
    '''
    pn_module_definition_2_and_3_part_1 : null
    '''
    np.processFuncParamVarType(t[-2]) 

def p_pn_module_definition_2_and_3_part_2(t):
    '''
    pn_module_definition_2_and_3_part_2 : null
    '''
    np.processNewFuncParamVarName(t[-2]) 


def p_pn_module_definition_4_1(t):
    '''
    pn_module_definition_4_1 : null
    '''
    np.processFuncLocalVarType(t[-2]) 

def p_pn_module_definition_4_2(t):
    '''
    pn_module_definition_4_2 : null
    '''
    np.processNewFuncLocalVarName(t[-2]) 

def p_pn_module_definition_6(t):
    '''
    pn_module_definition_6 : null
    '''
    np.processNumberOfQuadruples()

def p_pn_module_definition_7(t):
    '''
    pn_module_definition_7 : null
    '''
    np.processEndOfFunc() 




def p_print_funcs_data(t):
    '''
    print_funcs_data : null
    '''
    print("#==============================================================================")
    print("#==============================================================================")
    print("#==============================================================================")
    print("PRINTING FUNCS DATA:")
    np.printFuncsData() 
    print("#==============================================================================")
    print("#==============================================================================")
    print("#==============================================================================")




parser = yacc.yacc()
    





