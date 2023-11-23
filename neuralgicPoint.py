# * / 
# + -
# < > == !=
# ( ) 
# =

# PN operadosRelacional

#SI SE PUEDE TENER VARIOS RELACIONALES SIEMPRE Y CUANDO HAYA UNO LOGICO
from semanticCube import *
matchTypes = typesMatching()

from memoryUse import useOfMemory
virtualMemory = useOfMemory()


class NP:
    def __init__(self):
        self.operandsStack = []
        self.typesStack = []
        self.operatorsStack = []
        self.jumpsStack = []
        self.actualAritmeticScope = 'noInitialized'

        self.funcDir = {}
        #returnType = TIPO
        #varTable = VAR = TIPO
        #varCounter = #
        #paramTable = PARAM = TIPO
        #paramCounter = #
        #numOfQuadruples = NUM
        #numOfTemporalVars = NUM

        self.actualFuncProcessingName = 'noInitialized'
        self.actualFuncProcessingType = 'noInitialized'

        self.actualFuncProcessingLocalVarType = 'noInitialized'
        self.actualFuncProcessingParamVarType = 'noInitialized'

        #self.actualFuncProcessingStartingTemporalVar = 0
        self.actualFuncProcessingStartingQuadruple = 0


        
        self.actualCallingFuncName = 'noInitialized'
        self.actualCallingFuncProcessedArguments = 0



        self.temporalsCounter = 0

        self.quadraplesCounter = 0
        self.quadruplesDictionary = {}



        self.actualGlobalVarTypeToRegisterInVirtualMemory = 'noInitialized'
        self.actualLocalVarTypeToRegisterInVirtualMemory = 'noInitialized'
        self.actualFuncParamVarTypeToRegisterInVirtualMemory = 'noInitialized'

        self.momentaniumAddressOperandsStack = []
        self.addressOperandsStack = []
        self.addressQuadruplesCounter = 0
        self.addressQuadruplesDictionaryNormalTemporals = {}
        self.addressQuadruplesDictionary = {}

        self.momentaniumAddressQuadrupleCounter = 0
        self.momentaniumQuadrupleDictionary = {}



        self.arraysData = {}
        self.arraysIndexData = {}  #[baseDir, start, end]
        self.globalProcessingArrayType = 'noInitialized'
        self.localProcessingArrayType = 'noInitialized'


    def setActualAritmeticScope(self, scope):
        self.actualAritmeticScope = scope

    def getActualAritmeticScope(self):
        return self.actualAritmeticScope

    def addToOperandsStack(self, operand):
        self.operandsStack.append(operand)
        print(" ")
        print("Adding ", operand)
        print("Result operandStack:", self.operandsStack)

    def addToOperatorsStack(self, operator):
        self.operatorsStack.append(operator) 
        print(" ")
        print("Processing: " + operator + "..........................................")
        print(self.operatorsStack)
        print(" ")

    def addIntCteToOperands(self, operand):
        self.operandsStack.append(operand)
        self.typesStack.append('int')

        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("Adding int cte////////////////////////////////////////////////////////////////")
        # print(operand)
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("operatorStack: ", self.operatorsStack)
        # print("Result operandStack:", self.operandsStack)
        # print("Result typeStack:", self.typesStack)

    def addFloatCteToOperands(self, operand):
        self.operandsStack.append(operand)
        self.typesStack.append('float')

        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("Adding float cte////////////////////////////////////////////////////////////////")
        # print(operand)
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("#==============================================================================")
        # print("operatorStack: ", self.operatorsStack)
        # print("Result operandStack:", self.operandsStack)
        # print("Result typeStack:", self.typesStack)




    def addToTypesStack(self, type):
        self.typesStack.append(type)

    

    def processAdditionOrSubstraction(self):
        length = len(self.operatorsStack)
        index = length - 1

        print(" ")
        print("processAdditionOrSubstraction/////////////////////////////////////////////")
        print("Length: ", length)
        print("operatorStack: ", self.operatorsStack)
        
        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            found = True
            
            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-')):
                print("TRIED")
                if(length > 0):
                    print("LENGTH PASSED")
                    if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-'):
                        print("PRE OPERATOR FOUND")
                        print("=======================================")
                        print("Pre: ", self.operandsStack)
                        print("Pre: ", self.typesStack)
                        print("Pre: ", self.operatorsStack)
                        print("Found +, -, * or /: ", True)

                    
                        #//////////////////////////////////////
                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        #//////////////////////////////////////
                        rightAddressOperand = self.addressOperandsStack.pop()
                        leftAddressOperand = self.addressOperandsStack.pop()
                        #//////////////////////////////////////
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        
                        self.temporalsCounter = self.temporalsCounter + 1
                        #/////////////////////////////////////////////////
                        self.quadraplesCounter = self.quadraplesCounter + 1
                        #/////////////////////////////////////////////////
                        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                        #/////////////////////////////////////////////////

                        strTemporal = str(self.temporalsCounter)
                        string = "t" + strTemporal

                        #=============================================================================
                        ##############################################################################
                        #/////////////////////////////////////////////////////////////////////////////
                        temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                        print("TemporalAddress: ", temporalAddress)
                        #/////////////////////////////////////////////////////////////////////////////
                        ##############################################################################
                        #=============================================================================

                        #/////////////////////////////////////////////////////////
                        quadruple = [operator, leftOperand, rightOperand, string]
                        #/////////////////////////////////////////////////////////
                        addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                        #/////////////////////////////////////////////////////////

                        #////////////////////////////////////////////////////////////
                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                        #////////////////////////////////////////////////////////////
                        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                        #////////////////////////////////////////////////////////////

                        #////////////////////////////////////////////////////////////
                        self.operandsStack.append(string)
                        #////////////////////////////////////////////////////////////
                        self.addressOperandsStack.append(temporalAddress)
                        #////////////////////////////////////////////////////////////
                        self.typesStack.append(resultingType)

                        #self.operatorsStack.pop()
                        print("Post: ", self.operandsStack)
                        print("Post: ", self.typesStack)
                        print("Post: ", self.operatorsStack)

                        length = len(self.operatorsStack)
                        index = length - 1
                        print("New index: ", index)

                        if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-'):
                                print("POST FOUND TRUE")
                            else:
                                found = False
                                print("Found +, -, * or /: ", False)
                        else:
                            found = False
                            print("Found +, -, * or /: ", False)

                    else:
                        print("Found +, -, * or /: ", False)
                        found = False
                found = False
        print(" ")

    def processMultiplicationOrDivision(self):
        length = len(self.operatorsStack)
        index = length - 1

        print(" ")
        print("processMultiplicationOrDivision/////////////////////////////////////////////")
        print("Length: ", length)
        print("operatorStack: ", self.operatorsStack)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            found = True

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/')):
                if(length > 0):
                    if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/'):
                        print("=======================================")
                        print("Pre: ", self.operandsStack)
                        print("Pre: ", self.typesStack)
                        print("Pre: ", self.operatorsStack)
                        print("Found * or /: ", True)
                        #self.operatorsStack.pop()
                        



                        #////////////////////////////////////////////////////////////
                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        #////////////////////////////////////////////////////////////
                        rightAddressOperand = self.addressOperandsStack.pop()
                        leftAddressOperand = self.addressOperandsStack.pop()
                        #////////////////////////////////////////////////////////////
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        self.temporalsCounter = self.temporalsCounter + 1
                        #////////////////////////////////////////////////////////////
                        self.quadraplesCounter = self.quadraplesCounter + 1
                        #////////////////////////////////////////////////////////////
                        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                        #////////////////////////////////////////////////////////////

                        strTemporal = str(self.temporalsCounter)
                        string = "t" + strTemporal





                        #=============================================================================
                        ##############################################################################
                        #/////////////////////////////////////////////////////////////////////////////
                        temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                        print("TemporalAddress: ", temporalAddress)
                        #/////////////////////////////////////////////////////////////////////////////
                        ##############################################################################
                        #=============================================================================





                        #////////////////////////////////////////////////////////////
                        quadruple = [operator, leftOperand, rightOperand, string]
                        #////////////////////////////////////////////////////////////
                        addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                        #////////////////////////////////////////////////////////////

                        #////////////////////////////////////////////////////////////
                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                        #////////////////////////////////////////////////////////////
                        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                        #////////////////////////////////////////////////////////////

                        #////////////////////////////////////////////////////////////
                        self.operandsStack.append(string)
                        #////////////////////////////////////////////////////////////
                        self.addressOperandsStack.append(temporalAddress)
                        #////////////////////////////////////////////////////////////
                        self.typesStack.append(resultingType)




                        print("Post: ", self.operandsStack)
                        print("Post: ", self.typesStack)
                        print("Post: ", self.operatorsStack)

                        length = len(self.operatorsStack)
                        index = length - 1
                        print("New index: ", index)

                        if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/'):
                                found = True
                            else:
                                found = False
                        else:
                            found = False
                            print("Found +, -, * or /: ", False)
                    else:
                        print("Found * or /: ", False)
                        found = False
                found = False
        print(" ")

    #SI SE PUEDE TENER DOS OPERADORES RELACIONALES EN LA MISMA LDC SIEMPRE QUE SE USE OPERADORES RELACIONALES: | O &
    def processRelationalOperator(self):
        length = len(self.operatorsStack)
        index = length - 1

        print(" ")
        print("processRelationalOperator/////////////////////////////////////////////")
        print("Length: ", length)
        print("operatorStack: ", self.operatorsStack)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            found = True

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-')):
                if(length > 0):
                    if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-'):
                        print("=======================================")
                        print("Pre: ", self.operandsStack)
                        print("Pre: ", self.typesStack)
                        print("Pre: ", self.operatorsStack)
                        print("Found *, /, +, -, <, >, ==, !=: ", True)
                        #self.operatorsStack.pop()




                        #////////////////////////////////////////////////////////////
                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        #////////////////////////////////////////////////////////////
                        rightAddressOperand = self.addressOperandsStack.pop()
                        leftAddressOperand = self.addressOperandsStack.pop()
                        #////////////////////////////////////////////////////////////
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        self.temporalsCounter = self.temporalsCounter + 1
                        #////////////////////////////////////////////////////////////
                        self.quadraplesCounter = self.quadraplesCounter + 1
                        #////////////////////////////////////////////////////////////
                        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                        #////////////////////////////////////////////////////////////

                        strTemporal = str(self.temporalsCounter)
                        string = "t" + strTemporal





                        #=============================================================================
                        ##############################################################################
                        #/////////////////////////////////////////////////////////////////////////////
                        temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                        print("TemporalAddress: ", temporalAddress)
                        #/////////////////////////////////////////////////////////////////////////////
                        ##############################################################################
                        #=============================================================================





                        #////////////////////////////////////////////////////////////
                        quadruple = [operator, leftOperand, rightOperand, string]
                        #////////////////////////////////////////////////////////////
                        addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                        #////////////////////////////////////////////////////////////


                        #////////////////////////////////////////////////////////////
                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                        #////////////////////////////////////////////////////////////
                        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                        #////////////////////////////////////////////////////////////

                        #////////////////////////////////////////////////////////////
                        self.operandsStack.append(string)
                        #////////////////////////////////////////////////////////////
                        self.addressOperandsStack.append(temporalAddress)
                        #////////////////////////////////////////////////////////////
                        self.typesStack.append(resultingType)




                        print("Post: ", self.operandsStack)
                        print("Post: ", self.typesStack)
                        print("Post:", self.operatorsStack)

                        length = len(self.operatorsStack)
                        index = length - 1
                        print("New index: ", index)

                        if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-' or self.operatorsStack[index] == '<' or self.operatorsStack[index] == '>' or self.operatorsStack[index] == '==' or self.operatorsStack[index] == '!='):
                                found = True
                            else:
                                found = False
                        else:
                            found = False
                            print("Found +, -, * or /: ", False)
                    else:
                        print("Found *, /, +, -, <, >, ==, !=: ", False)
                        found = False
                found = False
        print(" ")

    def processRightParenthesis(self):
        length = len(self.operatorsStack)
        index = length - 1

        print(" ")
        print("processRightParenthesis/////////////////////////////////////////////")
        print("operatorStack: ", self.operatorsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '(')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Found +, -, *, /, <, >, == or !=: ", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////

                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    print("Post: ", self.operandsStack)
                    print("Post: ", self.typesStack)
                    print("Post: ", self.operatorsStack)

                    length = len(self.operatorsStack)
                    index = length - 1
                    print("New index: ", index)

                    if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] != ')'):
                                print("POST FOUND TRUE")
                            else:
                                found = False
                                print("Found +, -, *, /, <, >, == or !=: ", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >, == or !=: ", False)
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '(')):
                print("( FOUND, POPING FALSE BOTTOM MARK")
                print("PRE:", self.operatorsStack)
                #////////////////////////////////////////////////////////////
                self.operatorsStack.pop()
                #////////////////////////////////////////////////////////////
                #ESTE SE DEBERIA DE OMITIR, DADO QUE NO SE AÑADE EN EL STACK DE OPERANDS ADDRESS
                #////////////////////////////////////////////////////////////
                print("POST:", self.operatorsStack)
        print(" ")

    def processRelationalOperatorPostExpresion(self):
        length = len(self.operatorsStack)
        index = length - 1

        print(" ")
        print("processRelationalOperatorPostExpresion/////////////////////////////////////////////")
        print("operatorStack: ", self.operatorsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '<' and self.operatorsStack[index] != '>' and self.operatorsStack[index] != '==' and self.operatorsStack[index] != '!=')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Found +, -, *, /", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////

                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    print("Post: ", self.operandsStack)
                    print("Post: ", self.typesStack)
                    print("Post: ", self.operatorsStack)

                    length = len(self.operatorsStack)
                    index = length - 1
                    print("New index: ", index)

                    if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] != ')'):
                                print("POST FOUND TRUE")
                            else:
                                found = False
                                print("Found +, -, *, /, <, >: ", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >: ", False)
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '<' or self.operatorsStack[index] == '>' or self.operatorsStack[index] == '==' or self.operatorsStack[index] == '!=')):
                print("FOUND RELATIONAL OPERATOR, POPING OPERATOR")
                print("Pre: ", self.operandsStack)
                print("Pre: ", self.typesStack)
                print("PRE:", self.operatorsStack)




                #self.operatorsStack.pop()
                #////////////////////////////////////////////////////////////
                rightOperand = self.operandsStack.pop()
                leftOperand = self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                rightAddressOperand = self.addressOperandsStack.pop()
                leftAddressOperand = self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////
                rightType = self.typesStack.pop()
                leftType = self.typesStack.pop()
                operator = self.operatorsStack.pop()

                print("TYPE MATCHING DATA")
                print([operator, leftType, rightType])
                        
                #CHECAR COMPATIBILIDAD DE TIPOS.
                resultingType = matchTypes.match((operator, leftType, rightType))

                self.temporalsCounter = self.temporalsCounter + 1
                #////////////////////////////////////////////////////////////
                self.quadraplesCounter = self.quadraplesCounter + 1
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                #////////////////////////////////////////////////////////////

                strTemporal = str(self.temporalsCounter)
                string = "t" + strTemporal





                #=============================================================================
                ##############################################################################
                #/////////////////////////////////////////////////////////////////////////////
                temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                print("TemporalAddress: ", temporalAddress)
                #/////////////////////////////////////////////////////////////////////////////
                ##############################################################################
                #=============================================================================





                #////////////////////////////////////////////////////////////
                quadruple = [operator, leftOperand, rightOperand, string]
                #////////////////////////////////////////////////////////////
                addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                #////////////////////////////////////////////////////////////


                #////////////////////////////////////////////////////////////
                self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                self.operandsStack.append(string)
                #////////////////////////////////////////////////////////////
                self.addressOperandsStack.append(temporalAddress)
                #////////////////////////////////////////////////////////////
                self.typesStack.append(resultingType)




                print("Post: ", self.operandsStack)
                print("Post: ", self.typesStack)
                print("POST:", self.operatorsStack)
        print(" ")

#==============================================================================
#==============================================================================
#==============================================================================

    def processSequentialStatutePostStatute(self):
        length = len(self.operatorsStack)
        index = length - 1

        # print(" ")
        # print("processSequentialStatutePostStatute/////////////////////////////////////////////")
        # print("operatorStack: ", self.operatorsStack)
        # print("Length: ", length)

        if(length > 0):
            # print("=======================================")
            # print("index: ", index)
            # print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-' or self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '<' or self.operatorsStack[index] == '>' or self.operatorsStack[index] == '==' or self.operatorsStack[index] == '!=')):
                if(length > 0):
                    # print("PRE OPERATOR FOUND")
                    # print("=======================================")
                    # print("Pre: ", self.operandsStack)
                    # print("Pre: ", self.typesStack)
                    # print("Pre: ", self.operatorsStack)
                    # print("Found +, -, *, /, <, >, ==, !=", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////

                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    # print("Post: ", self.operandsStack)
                    # print("Post: ", self.typesStack)
                    # print("Post: ", self.operatorsStack)

                    length = len(self.operatorsStack)
                    index = length - 1
                    print("New index: ", index)

                    if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] != ')'):
                                print("POST FOUND TRUE")
                            else:
                                found = False
                                print("Found +, -, *, /, <, >, ==, !=", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >, ==, !=", False)
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '=')):
                # print("FOUND RELATIONAL OPERATOR, POPING OPERATOR")
                # print("Pre: ", self.operandsStack)
                # print("Pre: ", self.typesStack)
                # print("PRE:", self.operatorsStack)




                #self.operatorsStack.pop()
                #////////////////////////////////////////////////////////////
                rightOperand = self.operandsStack.pop()
                leftOperand = self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                rightAddressOperand = self.addressOperandsStack.pop()
                leftAddressOperand = self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////
                rightType = self.typesStack.pop()
                leftType = self.typesStack.pop()
                operator = self.operatorsStack.pop()

                print("TYPE MATCHING DATA FOR ASIGNATION OPERATOR (=)")
                print([operator, leftType, rightType])
                        
                #CHECAR COMPATIBILIDAD DE TIPOS.
                resultingType = matchTypes.match((operator, leftType, rightType))

                #self.temporalsCounter = self.temporalsCounter + 1
                #////////////////////////////////////////////////////////////
                self.quadraplesCounter = self.quadraplesCounter + 1
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                quadruple = [operator, rightOperand, ' ', leftOperand]
                #////////////////////////////////////////////////////////////
                addrQuadruple = [operator, rightAddressOperand, ' ', leftAddressOperand]
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                #////////////////////////////////////////////////////////////

                #########self.operandsStack.append(self.temporalsCounter)
                #self.typesStack.append(resultingType)




                # print("Post: ", self.operandsStack)
                # print("Post: ", self.typesStack)
                # print("POST:", self.operatorsStack)
            elif((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '=')):
                raise TypeError("ERROR: NO ASIGNATION OPERATOR FOUND.")
        print(" ")

#==============================================================================

# Lectura 
    def processWrite(self):
        print(" ")
        # print("WRITE QUADRUPLE GENERATION")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        resultOperand = self.operandsStack.pop()
        #////////////////////////////////////////////////////////////
        resultAddressOperand = self.addressOperandsStack.pop()
        #////////////////////////////////////////////////////////////
        self.typesStack.pop()


        print(['Write', ' ', ' ' , resultOperand])
                            
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple = ['Write', ' ', ' ' , resultOperand]
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['Write', ' ', ' ' , resultAddressOperand]
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////


        length = len(self.operandsStack)
        index = length - 1

        if(self.operandsStack[index] != '('):
            raise TypeError("ERROR: NOT (")
        elif(self.operandsStack[index] == '('):
            print("FOUND (, PROCESS CORRECT.")

            #////////////////////////////////////////////////////////////
            self.operandsStack.pop()
            #////////////////////////////////////////////////////////////
            #ESTE SE DEBE OMITIR DADO QUE EN EL ADDRESS_OPERANDS_STACK NUNCA SE LE HIZO APPEND
            #////////////////////////////////////////////////////////////
        else:
            print("SOMETHING WENT BAD, WRONG LOGIC")
            raise TypeError("SOMETHING WENT BAD, WRONG LOGIC")




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)
        # print(" ")  

    def preProcessWriteQuadruple(self):
        length = len(self.operandsStack)
        index = length - 1
        indexForWriteQuadruple = index - 1

        # print(" ")
        # print("PROCESS HIPER EXP OF WRITE/////////////////////////////////////////////")
        # print("operandsStack: ", self.operandsStack)
        # print("Length: ", length)

        if(length > 0):
            # print("=======================================")
            # print("index: ", index)
            # print("Last element: ", self.operandsStack[index])
            # print("index - 1: ", indexForWriteQuadruple)
            # print("Last element - 1: ", self.operandsStack[indexForWriteQuadruple])


            while((len(self.operatorsStack) > 0) and (self.operandsStack[indexForWriteQuadruple] != '(')):
                if(length > 0):
                    # print("PRE OPERATOR FOUND")
                    # print("=======================================")
                    # print("Pre: ", self.operandsStack)
                    # print("Pre: ", self.typesStack)
                    # print("Pre: ", self.operatorsStack)
                    # print("Not found ( as index - 1 of operands", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////

                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    # print("Post: ", self.operandsStack)
                    # print("Post: ", self.typesStack)
                    # print("Post: ", self.operatorsStack)

                    length = len(self.operandsStack)
                    index = length - 1
                    indexForWriteQuadruple = index - 1

                    # print("New index: ", index)
                    # print("New last element: ", self.operandsStack[index])
                    # print("Index - 1: ", indexForWriteQuadruple)
                    # print("New last element - 1: ", self.operandsStack[indexForWriteQuadruple])

                    if(length > 0):
                            #print("New last element: ", self.operatorsStack[index])

                            if(self.operandsStack[indexForWriteQuadruple] != '('):
                                print("POST FOUND FALSE, STILL NOT ( AS INDEX FOR WRITE QUADRUPLES")
                            else:
                                found = False
                                print("FOUND: ( AS INDEX FOR WRITE QUADRUPLE")
                    else:
                        print("STACK EMPTY")
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '(')):
                print("///////////////////////////////////////////////////////")
                print("FOUND ( AS INDEX FOR WRITE QUADRUPLE")
                print("///////////////////////////////////////////////////////")
        print(" ")

    #HAY QUE AÑADIR UN PARENTESIS EN OPERADORES TAMBIEN
    def addWritePreProcessToOperandsStack(self):
        # print("///////////////////////////////////////////////////////")
        # print("PRE PRCOESS OF HIPER EXP OF WRITE////////////////////////////////")
        # print("///////////////////////////////////////////////////////")

        #////////////////////////////////////////////////////////////
        self.operandsStack.append('(') 
        #////////////////////////////////////////////////////////////
        #ESTE SE DEBERIA PODER OMITIR DADO QUE LA LOGICA QUE SE VA A SEGUIR ES LA DE LAS VARIABLES NORMALES
        #////////////////////////////////////////////////////////////
        # print(" ")
        # print("Processing: (..........................................")
        # print(self.operandsStack)
        # print(" ")



# Escritura: EL METODO DE VARIABLES / OPERANDOS DEBERÍA GUARDAR AUTOMATICAMENTE EL OPERANDO DENTRO DE LOS PARENTESIS DEL READ.
    def processReadSaveVar(self, varId, type):
        print(" ")
        print("READ SAVE VAR ID")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)

        print("varId to add: ", varId)
        print("Type of varId to add: ", type)




        #////////////////////////////////////////////////////////////
        self.operandsStack.append(varId)
        #////////////////////////////////////////////////////////////
        result = virtualMemory.getVarAddressGlobalOrLocal(type, varId)
        self.addressOperandsStack.append(result[0])
        #self.momentaniumAddressOperandsStack.append(result[0])
        #////////////////////////////////////////////////////////////
        self.typesStack.append(type)




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")

    def processReadVar(self):
        print(" ")
        print("READ PROCESS VAR ID QUADRUPLE")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        resultOperand = self.operandsStack.pop()
        #////////////////////////////////////////////////////////////
        resultAddressOperand = self.addressOperandsStack.pop()
        #////////////////////////////////////////////////////////////
        self.typesStack.pop()


        print(['Read', ' ', ' ' , resultOperand])

        #////////////////////////////////////////////////////////////        
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple = ['Read', ' ', ' ' , resultOperand]
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['Read', ' ', ' ' , resultAddressOperand]
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")


# #============================================================================== 

    def processDecisionPostConditionalStatute(self):
        # print(" ")
        # print("IF GO TO QUADRUPLE GENERATION")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        resultOperand = self.operandsStack.pop()
        #////////////////////////////////////////////////////////////
        resultAddressOperand = self.addressOperandsStack.pop()
        #////////////////////////////////////////////////////////////
        resultType = self.typesStack.pop()

        print("resultType: ", resultType)

        if(resultType != 'bool'):
            raise TypeError("ERROR: IF EXPRESSION TYPE MISMATCH (NOT BOOL).")
        elif(resultType == 'bool'):
            print("RESULTING TYPE BOOL: CORRECT")


        print(['goToF', resultOperand, ' ' , '#'])
                            
        #CHECAR COMPATIBILIDAD DE TIPOS.
        #resultingType = matchTypes.match((operator, leftType, rightType))

        #self.temporalsCounter = self.temporalsCounter + 1
        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]
        #////////////////////////////////////////////////////////////
        quadruple = ['goToF', resultOperand, ' ' , '#']
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['goToF', resultAddressOperand, ' ' , '#']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////
        self.jumpsStack.append(self.quadraplesCounter)

        #self.operandsStack.append(self.temporalsCounter)
        #self.typesStack.append(resultingType)




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)
        # print(" ")

    def processDecisionPostStatement(self):
        # print(" ")
        # print("IF POST STATEMENT: FILL PENDING JUMPS")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        counter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        addressCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        pendingJump = self.jumpsStack.pop()
        #////////////////////////////////////////////////////////////
        quadruple = self.quadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////
        addressQuadruple = self.addressQuadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////

        # print("quadruple: ", quadruple)
        # print("quadruple[0]: ", quadruple[0])
        # print("quadruple[1]: ", quadruple[1])
        # print("quadruple[2]: ", quadruple[2])
        # print("quadruple[3]: ", quadruple[3])

        #////////////////////////////////////////////////////////////
        quadruple[3] = counter
        #////////////////////////////////////////////////////////////
        addressQuadruple[3] = addressCounter
        #////////////////////////////////////////////////////////////

        print("New quadruple with counter: ", quadruple)

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[pendingJump] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[pendingJump] = addressQuadruple
        #////////////////////////////////////////////////////////////




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)
        # print(" ")

    #EL 3 LLENA EL 2
    def processDecisionElse(self):
        # print(" ")
        # print("IF POST STATEMENT: FILL PENDING JUMPS")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        counter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        addressCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////


        pendingJump = self.jumpsStack.pop()
        #////////////////////////////////////////////////////////////
        quadruple = self.quadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////
        addressQuadruple = self.addressQuadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple[3] = counter
        #////////////////////////////////////////////////////////////
        addressQuadruple[3] = addressCounter
        #////////////////////////////////////////////////////////////

        print("New quadruple with counter: ", quadruple)

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[pendingJump] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[pendingJump] = addressQuadruple
        #////////////////////////////////////////////////////////////



        #////////////////////////////////////////////////////////////
        elseQuadruple = ['goTo', ' ', ' ', '#']
        #////////////////////////////////////////////////////////////
        elseQuadruple = ['goTo', ' ', ' ', '#']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = elseQuadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = elseQuadruple
        #////////////////////////////////////////////////////////////
        self.jumpsStack.append(self.quadraplesCounter)




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)
        # print(" ")

#==============================================================================
#==============================================================================
#==============================================================================

    def processWhileCyclePreExpression(self):
        # print(" ")
        # print("WHILE PRE EXPRESSION TO QUADRUPLE GENERATION")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        contador = self.quadraplesCounter + 1
        self.jumpsStack.append(contador)




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)

        # print("quadruplesDictionary: ")
        # print(self.quadruplesDictionary)
        # print(" ")

    def processWhileCyclePostExpression(self):
        # print(" ")
        # print("WHILE POST EXPRESSION QUADRUPLE GENERATION")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        resultType = self.typesStack.pop()

        if(resultType != 'bool'):
            raise TypeError("ERROR: IF EXPRESSION TYPE MISMATCH (NOT BOOL).")
        elif(resultType == 'bool'):
            print("RESULTING TYPE BOOL: CORRECT")
        

        #////////////////////////////////////////////////////////////
        resultOperand = self.operandsStack.pop()
        #////////////////////////////////////////////////////////////
        resultAddressOperand = self.addressOperandsStack.pop()
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        print(['goToF', resultOperand, ' ' , '#'])

        #////////////////////////////////////////////////////////////
        quadruple = ['goToF', resultOperand, ' ' , '#']
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['goToF', resultAddressOperand, ' ' , '#']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        counter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        addressCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////


        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////
        self.jumpsStack.append(self.quadraplesCounter)




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)

        # print("quadruplesDictionary: ")
        # print(self.quadruplesDictionary)
        # print(" ")

    def processWhileCyclePostStatement(self):
        # print(" ")
        # print("WHILE POST STATEMENT: FILL PENDING JUMPS")
        # print("=======================================")
        # print("Pre: ", self.operandsStack)
        # print("Pre: ", self.typesStack)
        # print("Pre: ", self.operatorsStack)
        # print("Pre: ", self.jumpsStack)




        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        counter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        addressCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////


        pendingJump = self.jumpsStack.pop()
        #////////////////////////////////////////////////////////////
        quadruple = self.quadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////
        addressQuadruple = self.addressQuadruplesDictionary[pendingJump]
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple[3] = counter
        #////////////////////////////////////////////////////////////
        addressQuadruple[3] = addressCounter
        #////////////////////////////////////////////////////////////

        print("New quadruple with counter: ", quadruple)

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[pendingJump] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[pendingJump] = addressQuadruple
        #////////////////////////////////////////////////////////////



        preExpressionNumberOfQuadruple = self.jumpsStack.pop()

        #////////////////////////////////////////////////////////////
        newQuadrupleToAdd = ['goTo', ' ', ' ', preExpressionNumberOfQuadruple]
        #////////////////////////////////////////////////////////////
        newAddressQuadrupleToAdd = ['goTo', ' ', ' ', preExpressionNumberOfQuadruple]
        #////////////////////////////////////////////////////////////
        
        print(newQuadrupleToAdd)

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = newQuadrupleToAdd
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = newAddressQuadrupleToAdd
        #////////////////////////////////////////////////////////////




        # print("Post: ", self.operandsStack)
        # print("Post: ", self.typesStack)
        # print("Post: ", self.operatorsStack)
        # print("Post: ", self.jumpsStack)

        # print("quadruplesDictionary: ")
        # print(self.quadruplesDictionary)
        # print(" ")

#==============================================================================
#==============================================================================
#==============================================================================

    def processFuncName(self, funcName):
        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")

        print("ACTUAL PROCESSING NAME:", self.actualFuncProcessingName)

        self.actualFuncProcessingName = funcName
        self.funcDir[funcName] = {}
        self.funcDir[funcName]['returnType'] = self.actualFuncProcessingType
        #self.funcDir[funcName]['returnType'] = funcReturnType
        self.actualFuncProcessingStartingQuadruple = self.quadraplesCounter
        
        print("FUNC NAME ADDING", funcName)
        print("NEW ACTUAL PROCESSING NAME:", self.actualFuncProcessingName)

        print("FUNC DIR:")
        print(self.funcDir)

        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")

    def processFuncType(self, funcReturnType):
        #self.funcDir[funcName] = {}
        #self.funcDir[self.actualFuncProcessingName]['returnType'] = funcReturnType
        self.actualFuncProcessingType = funcReturnType

    def processFuncParamVarType(self, paramVarType):
        self.actualFuncProcessingParamVarType = paramVarType

    def processNewFuncParamVarName(self, paramName):
        alreadyDeclaredDictionary = self.funcDir[self.actualFuncProcessingName].get('paramTable', 'notDeclared')

        if(alreadyDeclaredDictionary == 'notDeclared'):
            self.funcDir[self.actualFuncProcessingName]['paramTable'] = {}
            self.funcDir[self.actualFuncProcessingName]['paramCounter'] = 0

            self.funcDir[self.actualFuncProcessingName]['paramTable'][paramName] = self.actualFuncProcessingParamVarType
            self.funcDir[self.actualFuncProcessingName]['paramCounter'] = self.funcDir[self.actualFuncProcessingName]['paramCounter'] + 1
        else:
            self.funcDir[self.actualFuncProcessingName]['paramTable'][paramName] = self.actualFuncProcessingParamVarType
            self.funcDir[self.actualFuncProcessingName]['paramCounter'] = self.funcDir[self.actualFuncProcessingName]['paramCounter'] + 1



        alreadyDeclaredDictionary2 = self.funcDir[self.actualFuncProcessingName].get('localVarTable', 'notDeclared')

        if(alreadyDeclaredDictionary2 == 'notDeclared'):
            self.funcDir[self.actualFuncProcessingName]['localVarTable'] = {}
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = 0

            self.funcDir[self.actualFuncProcessingName]['localVarTable'][paramName] = self.actualFuncProcessingParamVarType
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = self.funcDir[self.actualFuncProcessingName]['localVarCounter'] + 1
        else:
            self.funcDir[self.actualFuncProcessingName]['localVarTable'][paramName] = self.actualFuncProcessingParamVarType
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = self.funcDir[self.actualFuncProcessingName]['localVarCounter'] + 1

    def processFuncLocalVarType(self, localVarType):
        self.actualFuncProcessingLocalVarType = localVarType

    def processNewFuncLocalVarName(self, localVarName):
        alreadyDeclaredDictionary = self.funcDir[self.actualFuncProcessingName].get('localVarTable', 'notDeclared')

        if(alreadyDeclaredDictionary == 'notDeclared'):
            self.funcDir[self.actualFuncProcessingName]['localVarTable'] = {}
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = 0

            self.funcDir[self.actualFuncProcessingName]['localVarTable'][localVarName] = self.actualFuncProcessingLocalVarType
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = self.funcDir[self.actualFuncProcessingName]['localVarCounter'] + 1
        else:
            self.funcDir[self.actualFuncProcessingName]['localVarTable'][localVarName] = self.actualFuncProcessingLocalVarType
            self.funcDir[self.actualFuncProcessingName]['localVarCounter'] = self.funcDir[self.actualFuncProcessingName]['localVarCounter'] + 1

    def processNumberOfQuadruples(self):
        numberOfQuadruples = self.quadraplesCounter - self.actualFuncProcessingStartingQuadruple
        self.funcDir[self.actualFuncProcessingName]['quadrupleCounter'] = numberOfQuadruples

    def processEndOfFunc(self):
        self.actualFuncProcessingName = 'noInitialized'
        self.actualFuncProcessingType = 'noInitialized'

        self.actualFuncProcessingLocalVarType = 'noInitialized'
        self.actualFuncProcessingParamVarType = 'noInitialized'

        self.actualFuncProcessingStartingTemporalVar = 0
        self.actualFuncProcessingStartingQuadruple = 0

        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple = ['endFunc', ' ', ' ', ' ']
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['endFunc', ' ', ' ', ' ']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////

#==============================================================================

    def processVerifyFuncName(self, funcId):
        alreadyDeclaredDictionary = self.funcDir.get(funcId, 'notDeclared')

        if(alreadyDeclaredDictionary == 'notDeclared'):
            raise TypeError("ERROR: INVALID INVOCATION OF FUNC ID")
        else:
            #////////////////////////////////////////////////////////////
            self.quadraplesCounter = self.quadraplesCounter + 1
            #////////////////////////////////////////////////////////////
            self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
            #////////////////////////////////////////////////////////////

            #////////////////////////////////////////////////////////////
            quadruple = ['Era', funcId, ' ', ' ']
            #////////////////////////////////////////////////////////////
            addressQuadruple = ['Era', funcId, ' ', ' ']
            #////////////////////////////////////////////////////////////

            #////////////////////////////////////////////////////////////
            self.quadruplesDictionary[self.quadraplesCounter] = quadruple
            #////////////////////////////////////////////////////////////
            self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
            #////////////////////////////////////////////////////////////

            self.actualCallingFuncName = funcId

            return True
        
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!" + funcId + "!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def processEndOfActualParam(self):
        length = len(self.operatorsStack)
        index = length - 1

        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")
        print("processEndOfActualParam/////////////////////////////////////////////")
        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")
        print("operatorStack: ", self.operatorsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '{')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Found +, -, *, /, <, >, == or !=: ", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    print("Post: ", self.operandsStack)
                    print("Post: ", self.typesStack)
                    print("Post: ", self.operatorsStack)

                    length = len(self.operatorsStack)
                    index = length - 1
                    print("New index: ", index)

                    if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] != '{'):
                                print("{ STILL NOT FOUND: TRUE")
                            else:
                                found = False
                                print("Found +, -, *, /, <, >, == or !=: ", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >, == or !=: ", False)
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '{')):
                print("{ FOUND, POPING IT")
                print("Pre: ", self.operandsStack)
                print("Pre: ", self.typesStack)
                print("Pre: ", self.operatorsStack)
                self.operatorsStack.pop()
                #////////////////////////////////////////////////////////////
                paramForQuadruple = self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                addressParamForQuadruple = self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                #self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////
                sendedArgumentType = self.typesStack.pop()

                actualProcessingParamNumber = self.actualCallingFuncProcessedArguments + 1

                print(" ")
                print("SENDED ARGUMENT TYPE: ", sendedArgumentType)
                print("FOR PARAM NUMBER: ", actualProcessingParamNumber)
                print("OF INVOCATION OF FUNC:", self.actualCallingFuncName)
                
                print(" ")

                funcParamTable = self.funcDir[self.actualCallingFuncName]['paramTable']
                paramName = list(funcParamTable)[self.actualCallingFuncProcessedArguments]
                paramType = list(funcParamTable.values())[self.actualCallingFuncProcessedArguments]


                #===========================================================
                ############################################################
                #////////////////////////////////////////////////////////////
                print("SENDING OPERAND (NORMAL):", paramForQuadruple)
                print("SENDING OPERAND (ADDRESS):", addressParamForQuadruple)


                isString = isinstance(paramForQuadruple, str)
                print("Is addressParamForQuadruple a string ? : ", isString)
            

                if(isString == False):
                    result = virtualMemory.checkIfCte(sendedArgumentType, addressParamForQuadruple) 

                    print("")
                    virtualMemory.printDictionaries()
                    print("")
                    if(result[0] == True):
                        print("IT WAS A CONSTANT: ")
                        print(result)
                        addressParamForQuadruple = result[1]
                    else:
                        print("IT WAS NOT A CONSTANT: ")
                        print(result)

                #////////////////////////////////////////////////////////////
                ############################################################
                #===========================================================


                print("ORIGINAL PARMA: ", paramName)
                print("OF TYPE: ", paramType)
                print(" ")

                if(sendedArgumentType == paramType):
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.actualCallingFuncProcessedArguments = self.actualCallingFuncProcessedArguments + 1

                    strProcessedArgument = str(self.actualCallingFuncProcessedArguments)
                    string = "param" + strProcessedArgument

                    #////////////////////////////////////////////////////////////
                    quadruple = ["Param", paramForQuadruple, ' ', string]
                    #////////////////////////////////////////////////////////////
                    addressQuadruple = ["Param", addressParamForQuadruple, ' ', string]
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
                    #////////////////////////////////////////////////////////////
                else:
                    raise TypeError("ERROR: MISMATCH OF TYPES OF SENDED ARGUMENT AND PARAMETER OF THE FUNC.")

                print("Post: ", self.operandsStack)
                print("Post: ", self.typesStack)
                print("Post: ", self.operatorsStack)
        print(" ")

    def processEndOfParams(self):
        numberOfParams = self.funcDir[self.actualCallingFuncName]['paramCounter']

        print("NUMBER OF PARAMS: ", numberOfParams)
        print("NUMBER OF SENDED ARGUMENTS: ", self.actualCallingFuncProcessedArguments)

        if(numberOfParams != self.actualCallingFuncProcessedArguments):
            raise TypeError("ERROR: MISMATCH OF NUMBER OF SENDED ARGUMENTS AND NUMBER OF PARAMETERS OF THE FUNC.")

    def processEndOfFuncCall(self):
            numberOfParams = self.funcDir[self.actualCallingFuncName]['paramCounter']

            print("NUMBER OF PARAMS: ", numberOfParams)
            print("NUMBER OF SENDED ARGUMENTS: ", self.actualCallingFuncProcessedArguments)

            if(numberOfParams != self.actualCallingFuncProcessedArguments):
                raise TypeError("ERROR: MISMATCH OF NUMBER OF SENDED ARGUMENTS AND NUMBER OF PARAMETERS OF THE FUNC.")
            else:
                #////////////////////////////////////////////////////////////
                self.quadraplesCounter = self.quadraplesCounter + 1
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                quadruple = ['goSub', self.actualCallingFuncName, ' ', ' ']
                #////////////////////////////////////////////////////////////
                addressQuadruple = ['goSub', self.actualCallingFuncName, ' ', ' ']
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
                #////////////////////////////////////////////////////////////

                self.actualCallingFuncName = 'noInitialized'
                self.actualCallingFuncProcessedArguments = 0

#==============================================================================

    def processStartOfProgram(self):
        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple = ['goTo', ' ', ' ', '#']
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['goTo', ' ', ' ', '#']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////

    def processStartOfMain(self):
        quadrupleNumber = self.quadraplesCounter + 1

        #////////////////////////////////////////////////////////////
        newQuadruple = self.quadruplesDictionary[1]
        #////////////////////////////////////////////////////////////
        newAddressQuadruple = self.addressQuadruplesDictionary[1]
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        newQuadruple[3] = quadrupleNumber
        #////////////////////////////////////////////////////////////
        newAddressQuadruple[3] = quadrupleNumber
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[1] = newQuadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[1] = newAddressQuadruple
        #////////////////////////////////////////////////////////////
        print("ENTERING MAIN.")
        print("PRE:")
        virtualMemory.printDictionaries()
        virtualMemory.resetLocalAndTemporalScope()
        print("POST:")
        virtualMemory.printDictionaries()

    def processEndOfProgram(self):
        #////////////////////////////////////////////////////////////
        self.quadraplesCounter = self.quadraplesCounter + 1
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        quadruple = ['End', ' ', ' ', ' ']
        #////////////////////////////////////////////////////////////
        addressQuadruple = ['End', ' ', ' ', ' ']
        #////////////////////////////////////////////////////////////

        #////////////////////////////////////////////////////////////
        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        #////////////////////////////////////////////////////////////
        self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
        #////////////////////////////////////////////////////////////

#==============================================================================

    def processTemporalsRestartOnChangeOfScope(self):
        self.temporalsCounter = 0

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

    def processGlobalVarTypeOnVirtualMemory(self, type):
        self.actualGlobalVarTypeToRegisterInVirtualMemory = type

    def processGlobalVarOnVirtual(self, varId):
        address = virtualMemory.saveAddress('Global', self.actualGlobalVarTypeToRegisterInVirtualMemory, varId)



    def processLocallVarTypeOnVirtualMemory(self, type):
        self.actualLocalVarTypeToRegisterInVirtualMemory = type
        print("SET LOCAL SCOPE VAR TYPE TO:", type)

    def processLocalVarOnVirtual(self, varId):
        address = virtualMemory.saveAddress('Locals', self.actualLocalVarTypeToRegisterInVirtualMemory, varId)
        print("PROCESSED LOCAL VAR: ", varId)
        print("TO THE ADDRESS: ", address)
        return address

    def processResetOfLocalAndTemporalScope(self):
        #virtualMemory.printDictionaries()
        virtualMemory.resetLocalAndTemporalScope()

    

    def processParamVarTypeOnVirtualMemory(self, type):
        self.actualFuncParamVarTypeToRegisterInVirtualMemory = type
        print("SET LOCAL SCOPE OF PARAM TYPE TO:", type)
    
    def processFuncParamOnVirtualMemory(self, paramId):
        ########FALTAN LOS PARAMS COMO VARS LOCALES
        address = virtualMemory.saveAddress('Locals', self.actualFuncParamVarTypeToRegisterInVirtualMemory, paramId)
        print("PROCESSED PARAM VAR: ", paramId)
        print("TO THE ADDRESS: ", address)
        return address
    




    def processGlobalAndLocalOnAddressOperandStack(self, type, varId):
        result = virtualMemory.getVarAddressGlobalOrLocal(type, varId)
        self.addressOperandsStack.append(result[0])
        self.momentaniumAddressOperandsStack.append(result[0])

        self.momentaniumAddressQuadrupleCounter = self.momentaniumAddressQuadrupleCounter + 1
        self.momentaniumQuadrupleDictionary[self.momentaniumAddressQuadrupleCounter] = result

    def processIntCteOnAddressOperandsStack(self, cte):
        address = virtualMemory.saveAddress('Constants', 'int', cte)
        self.addressOperandsStack.append(address)
        self.momentaniumAddressOperandsStack.append(address)

        self.momentaniumAddressQuadrupleCounter = self.momentaniumAddressQuadrupleCounter + 1
        self.momentaniumQuadrupleDictionary[self.momentaniumAddressQuadrupleCounter] = [address, cte]

    def processFloatCteOnAddressOperandsStack(self, cte):
        address = virtualMemory.saveAddress('Constants', 'float', cte)
        self.addressOperandsStack.append(address)
        self.momentaniumAddressOperandsStack.append(address)

        self.momentaniumAddressQuadrupleCounter = self.momentaniumAddressQuadrupleCounter + 1
        self.momentaniumQuadrupleDictionary[self.momentaniumAddressQuadrupleCounter] = [address, cte]

    
 



    def processIntCteOnVirtualMemory(self, varId):
        address = virtualMemory.saveAddress('Constants', 'int', varId)
        return address
    
    def processFloatCteOnVirtualMemory(self, varId):
        address = virtualMemory.saveAddress('Constants', 'float', varId)
        return address

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

    def setArraysDataDictionary(self, arraysDataDic):
        self.arraysData = arraysDataDic

#==============================================================================

    def setArrayIndexData(self, arrayId, spaces, scope):
        print("ACTUAL ARITMETIC SCOPE:")
        print(self.actualAritmeticScope)

        scopeInDictionary = self.arraysIndexData.get(scope, 'notDeclared')

        if(scopeInDictionary == 'notDeclared'):
            self.arraysIndexData[scope] = {}


        isString = isinstance(spaces, str)

        if(isString == True):
            intSpaces = int(spaces)
            start = 0
            end = spaces - 1
        else:
            start = 0
            end = spaces - 1

        
        #if(self.actualAritmeticScope == 'Global'):
        if(scope == 'Global'):
            baseDir = virtualMemory.saveArray('Global', self.globalProcessingArrayType, arrayId, spaces)
        else:
            baseDir = virtualMemory.saveArray('Locals', self.localProcessingArrayType, arrayId, spaces)

        self.arraysIndexData[scope][arrayId] = [baseDir, start, end]

    def setProcessingGlobalArrayType(self, type):
        self.globalProcessingArrayType = type

    def setProcessingLocalArrayType(self, type):
        self.localProcessingArrayType =  type

#==============================================================================

    def preProcessArrayInvocation(self):
        print("preProcessing arrayInvocation:")
        print(" ")

        print("///////////////////////////////////////////////////////")
        print("//////////PRE PRCOESS OF ARRAY INVOCATION//////////////")
        print("///////////////////////////////////////////////////////")

        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)

        self.operatorsStack.append('{') 
        print(" ")
        print("Processing: {..........................................")
        print(self.operatorsStack)
        print(" ")

        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")

    def processEndOfExpArrayInvocation(self, arrayId):
        length = len(self.operatorsStack)
        index = length - 1
        indexMinusOne = index - 1

        print(" ")
        print("ACTUAL ARRAY INDEX DATA DICTIONARY:")
        print(self.arraysIndexData)
        print(" ")

        print("ACTUAL SCOPE:")
        print(self.actualAritmeticScope)
        print(" ")
        print("PROCESSING ARRAY:")
        print(arrayId)
        print(" ")

        arrayIndexData = self.arraysIndexData[self.actualAritmeticScope].get(arrayId, 'notDeclared')

        if(arrayIndexData == 'notDeclared' and self.actualAritmeticScope != 'Global'):
            arrayIndexData = self.arraysIndexData['Global'].get(arrayId, 'notDeclared')

        print("")
        print("PROCESSED ARRAY INDEX DATA:")
        print(arrayIndexData)

        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")
        print("processEndOfExpArrayInvocation/////////////////////////////////////////////")
        print("#==============================================================================")
        print("#==============================================================================")
        print("#==============================================================================")
        print("operatorStack: ", self.operatorsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '{')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Found +, -, *, /, <, >, == or !=: ", True)
                    #self.operatorsStack.pop()




                    #////////////////////////////////////////////////////////////
                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightAddressOperand = self.addressOperandsStack.pop()
                    leftAddressOperand = self.addressOperandsStack.pop()
                    #////////////////////////////////////////////////////////////
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.quadraplesCounter = self.quadraplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                    #////////////////////////////////////////////////////////////
                    strTemporal = str(self.temporalsCounter)
                    string = "t" + strTemporal





                    #=============================================================================
                    ##############################################################################
                    #/////////////////////////////////////////////////////////////////////////////
                    temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)
                    print("TemporalAddress: ", temporalAddress)
                    #/////////////////////////////////////////////////////////////////////////////
                    ##############################################################################
                    #=============================================================================





                    #////////////////////////////////////////////////////////////
                    quadruple = [operator, leftOperand, rightOperand, string]
                    #////////////////////////////////////////////////////////////
                    addrQuadruple = [operator, leftAddressOperand, rightAddressOperand, temporalAddress]
                    #////////////////////////////////////////////////////////////


                    #////////////////////////////////////////////////////////////
                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                    #////////////////////////////////////////////////////////////
                    self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addrQuadruple
                    #////////////////////////////////////////////////////////////

                    #////////////////////////////////////////////////////////////
                    self.operandsStack.append(string)
                    #////////////////////////////////////////////////////////////
                    self.addressOperandsStack.append(temporalAddress)
                    #////////////////////////////////////////////////////////////
                    self.typesStack.append(resultingType)




                    print("Post: ", self.operandsStack)
                    print("Post: ", self.typesStack)
                    print("Post: ", self.operatorsStack)

                    length = len(self.operatorsStack)
                    index = length - 1
                    print("New index: ", index)

                    if(length > 0):
                            print("New last element: ", self.operatorsStack[index])

                            if(self.operatorsStack[index] != '{'):
                                print("{ STILL NOT FOUND: TRUE")
                            else:
                                found = False
                                print("Found +, -, *, /, <, >, == or !=: ", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >, == or !=: ", False)
            
            print(" ")
            length = len(self.operatorsStack)
            index = length - 1
            indexMinusOne = index - 1
            print("LENGTH AFTER HAVING RESULT: ", length)
            print("INDEX AFTER HAVING RESULT: ", index)
            print("VALUE FOR INDEX: ", self.operatorsStack[index])
            print("INDEX MINUES ONE AFTER HAVING RESULT: ", indexMinusOne)
            print("VALUE FOR INDEX MINUES ONE: ", self.operatorsStack[indexMinusOne])

            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '{')):
                print("{ FOUND, GETTING (POPING) RESULT OF ARRAY INDEX EXP:")
                print("Pre: ", self.operandsStack)
                print("Pre: ", self.addressOperandsStack)
                print("Pre: ", self.typesStack)
                print("Pre: ", self.operatorsStack)
                self.operatorsStack.pop()
                #////////////////////////////////////////////////////////////
                #paramForQuadruple = self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                #addressParamForQuadruple = self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////

                resultingOperand = self.operandsStack.pop()
                resultinAddressOperand = self.addressOperandsStack.pop()

                #////////////////////////////////////////////////////////////
  #¿SE POPEA?   #self.operandsStack.pop()
                #////////////////////////////////////////////////////////////
                #self.addressOperandsStack.pop()
                #////////////////////////////////////////////////////////////
                #sendedArgumentType = self.typesStack.pop()
                resultingType = self.typesStack.pop()

                if(resultingType == 'int'):
                    print(" ")
                    print("CORRECT: FINAL OPERAND TYPE WAS INT")
                    print(" ")
                else:
                    raise TypeError("ERROR: FINAL OPERAND TYPE WASNT INT")

                #actualProcessingParamNumber = self.actualCallingFuncProcessedArguments + 1

                # print(" ")
                # print("SENDED ARGUMENT TYPE: ", sendedArgumentType)
                # print("FOR PARAM NUMBER: ", actualProcessingParamNumber)
                # print("OF INVOCATION OF FUNC:", self.actualCallingFuncName)
                
                # print(" ")

                # funcParamTable = self.funcDir[self.actualCallingFuncName]['paramTable']
                # paramName = list(funcParamTable)[self.actualCallingFuncProcessedArguments]
                # paramType = list(funcParamTable.values())[self.actualCallingFuncProcessedArguments]


                #===========================================================
                ############################################################
                #////////////////////////////////////////////////////////////
                print("RESULTING OPERAND (NORMAL):", resultingOperand)
                print("RESULTING OPERAND (ADDRESS):", resultinAddressOperand)


                isString = isinstance(resultingOperand, str)
                print("Is finalArrayExp a string ? : ", isString)


                #isNumericString = resultingOperand.isnumeric()
                print(" ")
                print("Type of array index exp final result:")
                print(type(resultingOperand))
            

                if(isString == False):
                    result = virtualMemory.checkIfCte(resultingType, resultingOperand) 

                    print("")
                    # virtualMemory.printDictionaries()
                    print("")
                    if(result[0] == True):
                        print("IT WAS A CONSTANT: ")
                        print(result)
                        addressParamForQuadruple = result[1]
                    else:
                        print("IT WAS NOT A CONSTANT: ")
                        print(result)

                #////////////////////////////////////////////////////////////
                ############################################################
                #===========================================================


                # print("ORIGINAL PARMA: ", paramName)
                # print("OF TYPE: ", paramType)
                # print(" ")

                # if(sendedArgumentType == paramType):
                #     #////////////////////////////////////////////////////////////
                #     self.quadraplesCounter = self.quadraplesCounter + 1
                #     #////////////////////////////////////////////////////////////
                #     self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                #     #////////////////////////////////////////////////////////////
                #     self.actualCallingFuncProcessedArguments = self.actualCallingFuncProcessedArguments + 1

                #     strProcessedArgument = str(self.actualCallingFuncProcessedArguments)
                #     string = "param" + strProcessedArgument

                #     #////////////////////////////////////////////////////////////
                #     quadruple = ["Param", paramForQuadruple, ' ', string]
                #     #////////////////////////////////////////////////////////////
                #     addressQuadruple = ["Param", addressParamForQuadruple, ' ', string]
                #     #////////////////////////////////////////////////////////////

                #     #////////////////////////////////////////////////////////////
                #     self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                #     #////////////////////////////////////////////////////////////
                #     self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
                #     #////////////////////////////////////////////////////////////
                # else:
                #     raise TypeError("ERROR: MISMATCH OF TYPES OF SENDED ARGUMENT AND PARAMETER OF THE FUNC.")



                #////////////////////////////////////////////////////////////
                self.quadraplesCounter = self.quadraplesCounter + 1
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1
                #////////////////////////////////////////////////////////////
                #self.actualCallingFuncProcessedArguments = self.actualCallingFuncProcessedArguments + 1

                #strProcessedArgument = str(self.actualCallingFuncProcessedArguments)
                #string = "param" + strProcessedArgument

                # #////////////////////////////////////////////////////////////
                # quadruple = ["EXP RESULT", resultingOperand, ' ', ' ']
                # #////////////////////////////////////////////////////////////
                # addressQuadruple = ["EXP RESULT", resultinAddressOperand, ' ', ' ']
                # #////////////////////////////////////////////////////////////

                # #////////////////////////////////////////////////////////////
                # self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                # #////////////////////////////////////////////////////////////
                # self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
                # #///////////////////////////////////////////////////////////

                self.operandsStack.pop()
                self.addressOperandsStack.pop()

                print("Post: ", self.operandsStack)
                print("Post: ", self.addressOperandsStack)
                print("Post: ", self.typesStack)
                print("Post: ", self.operatorsStack)

                print(" ")
                print("ADDING BACK ARRAY WITH INDEX IN OPERANDS STACKS")
                print(" ")

                print("Post: ", self.operandsStack)
                print("Post: ", self.addressOperandsStack)
                print("Post: ", self.typesStack)
                print("Post: ", self.operatorsStack)



                # print("")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("INDICES DE LOS LIMITTES")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")

                # print("INDICE: ", arrayIndexData[1])
                # print("INDICE: ", arrayIndexData[2])

                # result = virtualMemory.checkIfCte('int', arrayIndexData[1]) 

                # print(" ")
                # virtualMemory.printDictionaries()
                # print(" ")
                # print("CHEKING INDEX LIMIT INDEX 1: ", arrayIndexData[1])
                # print(" ")
                # if(result[0] == True):
                #     print("IT WAS A CONSTANT: ")
                #     print(result)
                #     addressParamForQuadruple = result[1]
                # else:
                #     print("IT WAS NOT A CONSTANT: ")
                #     print(result)

                

                # result2 = virtualMemory.checkIfCte('int', arrayIndexData[2]) 

                # print(" ")
                # virtualMemory.printDictionaries()
                # print(" ")
                # print("CHEKING LIMIT INDEX 2: ", arrayIndexData[2])
                # print(" ")
                # if(result2[0] == True):
                #     print("IT WAS A CONSTANT: ")
                #     print(result2)
                #     addressParamForQuadruple = result2[1]
                # else:
                #     print("IT WAS NOT A CONSTANT: ")
                #     print(result2)

                
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("///////////////////////////////////////////////////////////////////////////////////////")
                # print("")

                addresLimitOne = virtualMemory.saveAddress('Constants', 'int', arrayIndexData[1])
                addresLimitTwo = virtualMemory.saveAddress('Constants', 'int', arrayIndexData[2])



                #////////////////////////////////////////////////////////////
                quadruple = ["Ver", resultingOperand, arrayIndexData[1], arrayIndexData[2]]
                #////////////////////////////////////////////////////////////
                addressQuadruple = ["Ver", resultinAddressOperand, addresLimitOne, addresLimitTwo]
                #////////////////////////////////////////////////////////////

                #////////////////////////////////////////////////////////////
                self.quadruplesDictionary[self.quadraplesCounter] = quadruple
                #////////////////////////////////////////////////////////////
                self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple
                #///////////////////////////////////////////////////////////

                self.quadraplesCounter = self.quadraplesCounter + 1
                self.addressQuadruplesCounter = self.addressQuadruplesCounter + 1

                self.temporalsCounter = self.temporalsCounter + 1
                strTemporal = str(self.temporalsCounter)
                string = "t" + strTemporal

                temporalAddress = virtualMemory.saveAddress('Temporals', resultingType, string)

                string = '{' + string + '}'
                temporalAddress = '{' + str(temporalAddress) + '}'

                quadruple2 = ['+', resultingOperand, arrayIndexData[0], string]
                addressQuadruple2 = ['+', resultinAddressOperand, arrayIndexData[0], temporalAddress]

                self.quadruplesDictionary[self.quadraplesCounter] = quadruple2
                self.addressQuadruplesDictionary[self.addressQuadruplesCounter] = addressQuadruple2

                self.operandsStack.append(string)
                self.addressOperandsStack.append(temporalAddress)
        print(" ")

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

    def printFuncsData(self):
        print(" ")
        print("funcDir:")
        print(self.funcDir)
        print(" ")

    def printStacks(self):
        print(" ")
        print("operandsStack")
        print(self.operandsStack)
        print("operatorsStack")
        print(self.operatorsStack)
        print("typesStack")
        print(self.typesStack)
        print("actualAritmeticScope")
        print(self.actualAritmeticScope)
        print("temporalsCounter")
        print(self.temporalsCounter)

        print(" ")


        print("Quadruples:")
        print(self.quadruplesDictionary)

    def npPrintVirtualMemory(self):
        virtualMemory.printDictionaries()
        print(" ")
        print("momentaniumAddressOperandsStack with all the addresses to check")
        print(self.momentaniumAddressOperandsStack)
        print(" ")
        print("addressMomemntaniumOperandsDictionary:")
        print(self.momentaniumQuadrupleDictionary)
        print(" ")
        print("addressOperandsStack (this should be empty at the end):")
        print(self.addressOperandsStack)
        print(" ")
        print("finalMomentaniumQuadruplesDictionaryWithNormalTemporals:")
        print(self.addressQuadruplesDictionary)
        print(" ")
        print("copyOfArrayDataDictionary:")
        print(self.arraysData)

    def printArraysIndexData(self):
        print(" ")
        print("arraysIndexDataDictionary:")
        print(self.arraysIndexData)

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

    def getResultingQuadruples(self):
        return self.addressQuadruplesDictionary
    
    def getConstantsMemory(self):
        return virtualMemory.getConstantsVirtualMemory()
