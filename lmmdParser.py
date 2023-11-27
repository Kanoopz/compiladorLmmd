import pprint


import ply.yacc as yacc
from lmmdLexer import tokens

from varsTable import declaredScopedVars
scopedDeclaredVars = declaredScopedVars()

from neuralgicPoint import NP
np = NP()

resultinQuadruplesDictionary = {}


def p_programa(t):
    '''
    programa : PROGRAM ID ';' pn_start_of_program pn_set_global dec_var def_func pn_reset_local_and_temporal_scopes pn_passArrayDataToNp impl_main pn_end_of_program pn_aritmetic_expressions_print pn_get_vars_table print_funcs_data print_virtual_memory_data print_arrays_index_data
    '''

def p_dec_var(t):
    '''
    dec_var : VARS tipos ':' id_dec_var ';' dec_var_prime
    '''

def p_tipos(t):
    '''
    tipos : INT pn_set_type pn_module_definition_2_and_3_part_1 pn_set_actual_global_type_to_register_on_virtual_memory pn_set_param_type_to_register_on_vitual_memory pn_set_processing_global_array_type pn_set_processing_local_array_type
	    | FLOAT pn_set_type pn_module_definition_2_and_3_part_1 pn_set_actual_global_type_to_register_on_virtual_memory pn_set_param_type_to_register_on_vitual_memory pn_set_processing_global_array_type pn_set_processing_local_array_type
	    | CHAR pn_set_type pn_module_definition_2_and_3_part_1 pn_set_actual_global_type_to_register_on_virtual_memory pn_set_param_type_to_register_on_vitual_memory pn_set_processing_global_array_type pn_set_processing_local_array_type
    '''

def p_id_dec_var(t):
    '''
    id_dec_var : ID pn_add_var '[' CTE_INT ']' pn_register_global_array_var pn_add_array_to_var_table id_dec_var_prime
	    | ID pn_add_var pn_register_global_var id_dec_var_prime 
    '''

def p_id_dec_var_prime(t):
    '''
    id_dec_var_prime : ',' ID pn_add_var '[' CTE_INT ']' pn_register_global_array_var pn_add_array_to_var_table id_dec_var_prime
        | ',' ID pn_add_var pn_register_global_var id_dec_var_prime
        | null
    '''

def p_dec_var_prime(t):
    '''
    dec_var_prime : tipos ':' id_dec_var ';' dec_var_prime
        | null
    '''



def p_def_func(t):
    '''
    def_func : pn_scope_temporals_restart FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 pn_register_param_as_local param_prime ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 pn_reset_local_and_temporal_scopes def_func_prime pn_reset_local_and_temporal_scopes
        | pn_scope_temporals_restart FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 pn_reset_local_and_temporal_scopes def_func_prime pn_reset_local_and_temporal_scopes
        | null pn_reset_local_and_temporal_scopes
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
    param_prime : ',' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 pn_register_param_as_local param_prime
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
    f_tipos : INT pn_set_type pn_module_definition_4_1 pn_set_actual_local_type_to_register_on_virtual_memory
	    | FLOAT pn_set_type pn_module_definition_4_1 pn_set_actual_local_type_to_register_on_virtual_memory
	    | CHAR pn_set_type pn_module_definition_4_1 pn_set_actual_local_type_to_register_on_virtual_memory
    '''

def p_f_id_dec_var(t):
    '''
    f_id_dec_var : ID pn_add_var pn_module_definition_4_2 '[' CTE_INT ']' pn_register_local_array_var pn_add_array_to_var_table_2 f_id_dec_var_prime
	    | ID pn_add_var pn_module_definition_4_2 pn_register_local_var f_id_dec_var_prime
    '''
    #print(t[1])

def p_f_id_dec_var_prime(t):
    '''
    f_id_dec_var_prime : ',' ID pn_add_var pn_module_definition_4_2 '[' CTE_INT ']' pn_register_local_array_var pn_add_array_to_var_table_2 f_id_dec_var_prime
        | ',' ID pn_add_var pn_module_definition_4_2 pn_register_local_var f_id_dec_var_prime
        | null
    '''

def p_f_dec_var_prime(t):
    '''
    f_dec_var_prime : f_tipos ':' f_id_dec_var ';' f_dec_var_prime
        | null
    '''





def p_func_return(t):
    '''
    func_return : RETURN '(' pn_func_return_1 hiper_exp pn_func_return_2 ')' pn_func_return_3 ';'
        | null
    '''

def p_def_func_prime(t):
    '''
    def_func_prime : pn_scope_temporals_restart FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' tipos ID pn_add_var pn_module_definition_2_and_3_part_2 pn_register_param_as_local param_prime ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 pn_reset_local_and_temporal_scopes def_func_prime
        | pn_scope_temporals_restart FUNCTION tipos_func ID pn_set_scope pn_set_aritmetic_expressions_scope pn_module_definition_1_1 '(' ')' func_dec_var '{' est est_prime func_return '}' pn_module_definition_6 pn_module_definition_7 pn_reset_local_and_temporal_scopes def_func_prime
        | null pn_reset_local_and_temporal_scopes
    '''

def p_impl_main(t):
    '''
    impl_main : MAIN pn_set_aritmetic_expressions_scope_global pn_start_of_main '(' ')' pn_scope_temporals_restart '{' est est_prime '}'
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
        | funcs_especiales
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
        | funcs_especiales est_prime
        | null
    '''

def p_funcs_especiales(t):
    '''
    funcs_especiales : media_func
    | moda_func
    | varianza_func
    '''

def p_media_func(t):
    '''
    media_func : MEDIA '(' ID check_array_id ')' process_meda_invocation 
        | MEDIA '(' ID check_array_id ')' process_meda_invocation ';'
    '''

def p_moda_func(t):
    '''
    moda_func : MODA '(' ID check_array_id ')' process_moda_invocation  
        | MODA '(' ID check_array_id ')' process_moda_invocation ';'
    '''

def p_varianza_func(t):
    '''
    varianza_func : VARIANZA '(' ID check_array_id ')' process_varianza_invocation  
        | VARIANZA '(' ID check_array_id ')' process_varianza_invocation ';'
    '''

def p_check_array_id(t):
    '''
    check_array_id : null
    '''
    np.checkArrayParam(t[-1])

def p_process_meda_invocation(t):
    '''
    process_meda_invocation : null
    '''
    np.generateMediaQuadruple(t[-3])

def p_process_moda_invocation(t):
    '''
    process_moda_invocation : null
    '''
    np.generateModaQuadruple(t[-3])

def p_process_varianza_invocation(t):
    '''
    process_varianza_invocation : null
    '''
    np.generateVarianzaQuadruple(t[-3])



def p_est_asig(t):
     '''
     est_asig : ID pn_sequential_statute_1 '=' pn_sequential_statute_2 ID pn_function_calling_1 '(' llam_func_param ')' pn_function_calling_6 pn_function_calling_7 ';' pn_asignation_on_function_call 
        | ID pn_sequential_statute_1 pn_array_invocation '[' pn_array_index_start hiper_exp pn_array_index_end ']' '=' pn_sequential_statute_2 hiper_exp pn_sequential_statute_3 ';'
        | ID pn_sequential_statute_1 '=' pn_sequential_statute_2 hiper_exp pn_sequential_statute_3 ';' 
        | ID pn_sequential_statute_1 '=' pn_sequential_statute_2 MEDIA '(' ID check_array_id ')' process_meda_invocation pn_sequential_statute_3 ';'
        | ID pn_sequential_statute_1 '=' pn_sequential_statute_2 MODA '(' ID check_array_id ')' process_moda_invocation pn_sequential_statute_3 ';'
        | ID pn_sequential_statute_1 '=' pn_sequential_statute_2 VARIANZA '(' ID check_array_id ')' process_varianza_invocation pn_sequential_statute_3 ';'
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
     factor : est_llam_func
        | ID pn_aritmetic_expressions_1 pn_array_invocation_2 '[' pn_array_index_start hiper_exp pn_array_index_end ']'
        | ID pn_aritmetic_expressions_1
        | ctes
        | sub_exp
     '''
     
def p_ctes(t):
     '''
     ctes : CTE_INT pn_add_int_cte pn_register_int_constant 
        | CTE_FLOAT pn_add_float_cte pn_register_float_constant
        | CTE_CHAR
        | CTE_LETRERO pn_add_string_cte pn_register_string_constant
    '''
     
def p_sub_exp(t):
     '''
     sub_exp : '(' pn_aritmetic_expressions_6 hiper_exp ')' pn_aritmetic_expressions_7
    '''
     
def p_est_llam_func(t):
     '''
     est_llam_func : ID pn_function_calling_1 '(' llam_func_param ')' pn_function_calling_6 pn_function_calling_7
        | ID pn_function_calling_1 '(' llam_func_param ')' pn_function_calling_6 pn_function_calling_7 ';'
    '''
     
def p_llam_func_param(t):
     '''
     llam_func_param : pn_function_calling_2 hiper_exp pn_function_calling_3 llam_func_param_prime
        | null
    '''
     
def p_llam_func_param_prime(t):
     '''
     llam_func_param_prime : ',' pn_function_calling_2 hiper_exp pn_function_calling_3 llam_func_param_prime
        | null
    '''
     
def p_lectura(t):
     '''
     lectura : READ '(' llam_lect_param ')' ';'
    '''
     
def p_llam_lect_param(t):
     '''
     llam_lect_param : ID pn_read_save_ID pn_array_invocation_3 '[' pn_array_index_start hiper_exp pn_array_index_end_2 ']' pn_read llam_lect_param_prime
        | ID pn_read_save_ID pn_read llam_lect_param_prime
        | null
    '''
     
def p_llam_lect_param_prime(t):
     '''
     llam_lect_param_prime : ',' ID pn_read_save_ID pn_array_invocation_3 '[' pn_array_index_start hiper_exp pn_array_index_end_2 ']' pn_read llam_lect_param_prime
        | ',' ID pn_read_save_ID pn_read llam_lect_param_prime
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
     print(t[2])
     
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
     np.setActualAritmeticScope('Global')

def p_pn_set_aritmetic_expressions_scope(t):
     '''
     pn_set_aritmetic_expressions_scope : null
     '''
     np.setActualAritmeticScope(t[-2])

#////////////////////////////////////////////
#///////ADDRESS TO OPERANDS//////////////////
#////////////////////////////////////////////
def p_pn_aritmetic_expressions_1(t):
     '''
     pn_aritmetic_expressions_1 : null
     '''

     actualScope = np.getActualAritmeticScope()
     print("ACTUAL SCOPE:", actualScope)
     print("ID:", t[-1])
     varInDictionary = scopedDeclaredVars.checkVar(t[-1], actualScope)
     
     if(varInDictionary[0] == True):
        np.addToOperandsStack(t[-1])
        np.addToTypesStack(varInDictionary[1])

        np.processGlobalAndLocalOnAddressOperandStack(varInDictionary[1], t[-1])


def p_pn_aritmetic_expressions_2(t):
     '''
     pn_aritmetic_expressions_2 : null
     '''

     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_3(t):
     '''
     pn_aritmetic_expressions_3 : null
     '''

     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_4(t):
     '''
     pn_aritmetic_expressions_4 : null
     '''

     np.processAdditionOrSubstraction()

def p_pn_aritmetic_expressions_5(t):
     '''
     pn_aritmetic_expressions_5 : null
     '''

     np.processMultiplicationOrDivision()

def p_pn_aritmetic_expressions_6(t):
     '''
     pn_aritmetic_expressions_6 : null
     '''

     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_7(t):
     '''
     pn_aritmetic_expressions_7 : null
     '''

     np.processRightParenthesis()

def p_pn_aritmetic_expressions_8(t):
     '''
     pn_aritmetic_expressions_8 : null
     '''

     np.processRelationalOperator()
     np.addToOperatorsStack(t[-1])

def p_pn_aritmetic_expressions_9(t):
     '''
     pn_aritmetic_expressions_9 : null
     '''

     np.processRelationalOperatorPostExpresion()

#////////////////////////////////////////////
#///////ADDRESS TO INT CTE///////////////////
#////////////////////////////////////////////
def p_pn_add_int_cte(t):
     '''
     pn_add_int_cte : null
     '''
     np.addIntCteToOperands(t[-1])
     np.processIntCteOnAddressOperandsStack(t[-1])

#////////////////////////////////////////////
#///////ADDRESS TO FLOAT CTE/////////////////
#////////////////////////////////////////////
def p_pn_add_float_cte(t):
     '''
     pn_add_float_cte : null
     '''
     np.addFloatCteToOperands(t[-1])
     np.processFloatCteOnAddressOperandsStack(t[-1])

def p_pn_add_string_cte(t):
     '''
     pn_add_string_cte : null
     '''
     np.printPre("process add of string")
     print("Adding string constant: ", t[-1])
     np.addStringCteToOperands(t[-1])
     np.processStringCteOnAddressOperandsStack(t[-1])
     np.printPost("process add of string")



def p_pn_aritmetic_expressions_print(t):
     '''
     pn_aritmetic_expressions_print : null
     '''

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

        np.processGlobalAndLocalOnAddressOperandStack(varInDictionary[1], t[-1])

def p_pn_sequential_statute_2(t):
     '''
     pn_sequential_statute_2 : null
     '''
     np.printPre("ASIGNACION PN2")

     np.addToOperatorsStack(t[-1])

     np.printPost("ASIGNACION PN2")

def p_pn_sequential_statute_3(t):
     '''
     pn_sequential_statute_3 : null
     '''
     np.printPre("ASIGNACION PN3")

     np.processSequentialStatutePostStatute()

     np.printPost("ASIGNACION PN3")

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

#==============================================================================

def p_pn_func_return_1(t):
    '''
    pn_func_return_1 : null
    '''
    np.preProcessFuncReturnExpression()

def p_pn_func_return_2(t):
    '''
    pn_func_return_2 : null
    '''
    np.processEndOfFuncReturnExpression()

def p_pn_func_return_3(t):
    '''
    pn_func_return_3 : null
    '''
    np.processSaveFuncReturnValue()

#==============================================================================

def p_pn_function_calling_1(t):
    '''
    pn_function_calling_1 : null
    '''
    np.processVerifyFuncName(t[-1]) 

def p_pn_function_calling_2(t):
    '''
    pn_function_calling_2 : null
    '''
    np.addToOperandsStack('{')
    np.addToOperatorsStack('{')

def p_pn_function_calling_3(t):
    '''
    pn_function_calling_3 : null
    '''
    np.processEndOfActualParam()

def p_pn_function_calling_6(t):
    '''
    pn_function_calling_6 : null
    '''
    np.processEndOfFuncCall()

def p_pn_function_calling_7(t):
    '''
    pn_function_calling_7 : null
    '''
    np.printPre("RETORNO VALORES")

    result = np.processReturnValueOnFuncCall(t[-6])

    if(result[0] == True):
        type = result[1]
        funcId = t[-6]

        print("type: ", type)
        print("id:", funcId)

        data = np.getFuncAddress(type, funcId)

        address = data[0]


        np.addToOperandsStack(funcId)
        np.addToAddressOperandsStack(address)
        np.addToTypesStack(type)

    

    np.printPost("RETORNO DE VALORES")

def p_pn_asignation_on_function_call(t):
    '''
    pn_asignation_on_function_call : null
    '''

    np.processAsignationOnReturnValueOnFuncCall()



#==============================================================================

def p_pn_start_of_program(t):
    '''
    pn_start_of_program : null
    '''
    np.processStartOfProgram()

def p_pn_start_of_main(t):
    '''
    pn_start_of_main : null
    '''
    np.processStartOfMain()

def p_pn_end_of_program(t):
    '''
    pn_end_of_program : null
    '''
    np.processEndOfProgram()

#==============================================================================

def p_pn_scope_temporals_restart(t):
    '''
    pn_scope_temporals_restart : null
    '''
    np.processTemporalsRestartOnChangeOfScope()

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

def p_pn_set_actual_global_type_to_register_on_virtual_memory(t):
    '''
    pn_set_actual_global_type_to_register_on_virtual_memory : null
    '''
    np.processGlobalVarTypeOnVirtualMemory(t[-3])

def p_pn_register_global_var(t):
    '''
    pn_register_global_var : null
    '''
    np.processGlobalVarOnVirtual(t[-2])

def p_pn_register_global_array_var(t):
    '''
    pn_register_global_array_var : null
    '''

#==============================================================================

def p_pn_set_actual_local_type_to_register_on_virtual_memory(t):
    '''
    pn_set_actual_local_type_to_register_on_virtual_memory : null
    '''
    np.processLocallVarTypeOnVirtualMemory(t[-3])

def p_pn_register_local_var(t):
    '''
    pn_register_local_var : null
    '''
    np.processLocalVarOnVirtual(t[-3])

def p_pn_register_local_array_var(t):
    '''
    pn_register_local_array_var : null
    '''

#==============================================================================

def p_pn_set_param_type_to_register_on_vitual_memory(t):
    '''
    pn_set_param_type_to_register_on_vitual_memory : null
    '''
    np.processParamVarTypeOnVirtualMemory(t[-4])

def p_pn_register_param_as_local(t):
    '''
    pn_register_param_as_local : null
    '''
    np.processFuncParamOnVirtualMemory(t[-3])

#==============================================================================

def p_pn_reset_local_and_temporal_scopes(t):
    '''
    pn_reset_local_and_temporal_scopes : null
    '''
    np.processResetOfLocalAndTemporalScope()

#==============================================================================

def p_pn_register_int_constant(t):
    '''
    pn_register_int_constant : null
    '''
    newAddress = np.processIntCteOnVirtualMemory(t[-2])

def p_pn_register_float_constant(t):
    '''
    pn_register_float_constant : null
    '''
    newAddress = np.processFloatCteOnVirtualMemory(t[-2])

def p_pn_register_string_constant(t):
    '''
    pn_register_string_constant : null
    '''
    print("ADDING ADDRESS STRING")
    newAddress = np.processStringCteOnVirtualMemory(t[-2])
    
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

def p_pn_add_array_to_var_table(t):
    '''
    pn_add_array_to_var_table : null
    '''
    arraysDictionary = scopedDeclaredVars.addArray(t[-6], t[-3])
    
    scope = scopedDeclaredVars.getActualScope()
    np.setArraysDataDictionary(arraysDictionary)
    np.setArrayIndexData(t[-6], t[-3], scope)

def p_pn_add_array_to_var_table_2(t):
    '''
    pn_add_array_to_var_table_2 : null
    '''
    arraysDictionary = scopedDeclaredVars.addArray(t[-7], t[-3])
    scope = scopedDeclaredVars.getActualScope()
    np.setArraysDataDictionary(arraysDictionary)
    np.setArrayIndexData(t[-7], t[-3], scope)

def p_pn_set_processing_global_array_type(t):
    '''
    pn_set_processing_global_array_type : null
    '''
    np.setProcessingGlobalArrayType(t[-5])


def p_pn_set_processing_local_array_type(t):
    '''
    pn_set_processing_local_array_type : null
    '''
    np.setProcessingLocalArrayType(t[-6])

#==============================================================================

def p_pn_array_invocation(t):
    '''
    pn_array_invocation : null
    '''
    scope = np.getActualAritmeticScope()
    arrayData = scopedDeclaredVars.checkArray(t[-2], scope)

def p_pn_array_invocation_2(t):
    '''
    pn_array_invocation_2 : null
    '''
    scope = np.getActualAritmeticScope()
    arrayData = scopedDeclaredVars.checkArray(t[-2], scope)
    

##ESTE ES PARA LOS PARAMETROS DE LECTURA####
def p_pn_array_invocation_3(t):
    '''
    pn_array_invocation_3 : null
    '''
    scope = np.getActualAritmeticScope()
    arrayData = scopedDeclaredVars.checkArray(t[-2], scope)

def p_pn_array_index_start(t):
    '''
    pn_array_index_start : null
    '''
    np.preProcessArrayInvocation()

def p_pn_array_index_end(t):
    '''
    pn_array_index_end : null
    '''
    np.processEndOfExpArrayInvocation(t[-6])

def p_pn_array_index_end_2(t):
    '''
    pn_array_index_end_2 : null
    '''
    np.processEndOfExpArrayInvocation(t[-7])

#==============================================================================

def p_pn_passArrayDataToNp(t):
    '''
    pn_passArrayDataToNp : null
    '''
    arraysData = scopedDeclaredVars.getArrayDic()
    np.setArraysDataDictionary(arraysData)

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

def p_print_funcs_data(t):
    '''
    print_funcs_data : null
    '''
    # print("#==============================================================================")
    # print("#==============================================================================")
    # print("#==============================================================================")
    # print("PRINTING FUNCS DATA:")
    # np.printFuncsData() 
    # print("#==============================================================================")
    # print("#==============================================================================")
    # print("#==============================================================================")

def p_print_virtual_memory_data(t):
    '''
    print_virtual_memory_data : null
    '''
    # print("FINAL DICTONARIES://///////////////////////////////////////////////")
    # print(" ")
    # np.npPrintVirtualMemory()

def p_print_arrays_index_data(t):
    '''
    print_arrays_index_data : null
    '''
    # print(" ")
    # print("ARRAYS INDEX DATA://///////////////////////////////////////////////")
    # np.printArraysIndexData()

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

resultinQuadruplesDictionary = np.getResultingQuadruples()
constantsMemoryAddresses = np.getConstantsMemory()
funtionsDictionary = np.getFuncsDictionary()
variablesInformation = scopedDeclaredVars.getVarTableData()
    

parser = yacc.yacc()


    





