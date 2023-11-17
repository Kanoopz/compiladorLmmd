# * / 
# + -
# < > == !=
# ( ) 
# =

# PN operadosRelacional

#SI SE PUEDE TENER VARIOS RELACIONALES SIEMPRE Y CUANDO HAYA UNO LOGICO
from semanticCube import *
matchTypes = typesMatching()

class NP:
    def __init__(self):
        self.operandsStack = []
        self.typesStack = []
        self.operatorsStack = []
        self.jumpsStack = []
        self.actualAritmeticScope = 'noInitialized'

        self.temporalsCounter = 0

        self.quadraplesCounter = 0
        self.quadruplesDictionary = {}


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

                    
                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        self.temporalsCounter = self.temporalsCounter + 1
                        self.quadraplesCounter = self.quadraplesCounter + 1

                        quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                        self.operandsStack.append(self.temporalsCounter)
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
                        



                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        self.temporalsCounter = self.temporalsCounter + 1
                        self.quadraplesCounter = self.quadraplesCounter + 1

                        quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                        self.operandsStack.append(self.temporalsCounter)
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

    #¿DEBERIA PROCESAR TOD ANTES DE METER EL OPERADOR?
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




                        rightOperand = self.operandsStack.pop()
                        leftOperand = self.operandsStack.pop()
                        rightType = self.typesStack.pop()
                        leftType = self.typesStack.pop()
                        operator = self.operatorsStack.pop()

                        print("TYPE MATCHING DATA")
                        print([operator, leftType, rightType])
                        
                        #CHECAR COMPATIBILIDAD DE TIPOS.
                        resultingType = matchTypes.match((operator, leftType, rightType))

                        self.temporalsCounter = self.temporalsCounter + 1
                        self.quadraplesCounter = self.quadraplesCounter + 1

                        quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                        self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                        self.operandsStack.append(self.temporalsCounter)
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

    #DEBE PROCESAR TOD LO QUE QUEDE ENTRE EL PARENTESIS IZQUIERDO, ¿TAMBIEN OPERADORES RELACIONALES?
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




                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    self.quadraplesCounter = self.quadraplesCounter + 1

                    quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                    self.operandsStack.append(self.temporalsCounter)
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
                self.operatorsStack.pop()
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




                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    self.quadraplesCounter = self.quadraplesCounter + 1

                    quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                    self.operandsStack.append(self.temporalsCounter)
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
                rightOperand = self.operandsStack.pop()
                leftOperand = self.operandsStack.pop()
                rightType = self.typesStack.pop()
                leftType = self.typesStack.pop()
                operator = self.operatorsStack.pop()

                print("TYPE MATCHING DATA")
                print([operator, leftType, rightType])
                        
                #CHECAR COMPATIBILIDAD DE TIPOS.
                resultingType = matchTypes.match((operator, leftType, rightType))

                self.temporalsCounter = self.temporalsCounter + 1
                self.quadraplesCounter = self.quadraplesCounter + 1

                quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                self.operandsStack.append(self.temporalsCounter)
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

        print(" ")
        print("processSequentialStatutePostStatute/////////////////////////////////////////////")
        print("operatorStack: ", self.operatorsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operatorsStack[index])

            while((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '+' or self.operatorsStack[index] == '-' or self.operatorsStack[index] == '*' or self.operatorsStack[index] == '/' or self.operatorsStack[index] == '<' or self.operatorsStack[index] == '>' or self.operatorsStack[index] == '==' or self.operatorsStack[index] == '!=')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Found +, -, *, /, <, >, ==, !=", True)
                    #self.operatorsStack.pop()




                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    self.quadraplesCounter = self.quadraplesCounter + 1

                    quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                    self.operandsStack.append(self.temporalsCounter)
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
                                print("Found +, -, *, /, <, >, ==, !=", False)
                    else:
                        found = False
                        print("Found +, -, *, /, <, >, ==, !=", False)
            
            if((len(self.operatorsStack) > 0) and (self.operatorsStack[index] == '=')):
                print("FOUND RELATIONAL OPERATOR, POPING OPERATOR")
                print("Pre: ", self.operandsStack)
                print("Pre: ", self.typesStack)
                print("PRE:", self.operatorsStack)




                #self.operatorsStack.pop()
                rightOperand = self.operandsStack.pop()
                leftOperand = self.operandsStack.pop()
                rightType = self.typesStack.pop()
                leftType = self.typesStack.pop()
                operator = self.operatorsStack.pop()

                print("TYPE MATCHING DATA FOR ASIGNATION OPERATOR (=)")
                print([operator, leftType, rightType])
                        
                #CHECAR COMPATIBILIDAD DE TIPOS.
                resultingType = matchTypes.match((operator, leftType, rightType))

                #self.temporalsCounter = self.temporalsCounter + 1
                self.quadraplesCounter = self.quadraplesCounter + 1

                quadruple = [operator, rightOperand, ' ', leftOperand]

                self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                #########self.operandsStack.append(self.temporalsCounter)
                #self.typesStack.append(resultingType)




                print("Post: ", self.operandsStack)
                print("Post: ", self.typesStack)
                print("POST:", self.operatorsStack)
            elif((len(self.operatorsStack) > 0) and (self.operatorsStack[index] != '=')):
                raise TypeError("ERROR: NO ASIGNATION OPERATOR FOUND.")
        print(" ")

#==============================================================================

# Lectura 
    def processWrite(self):
        print(" ")
        print("WRITE QUADRUPLE GENERATION")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        resultOperand = self.operandsStack.pop()
        self.typesStack.pop()


        print(['Write', ' ', ' ' , resultOperand])
                            
        self.quadraplesCounter = self.quadraplesCounter + 1

        quadruple = ['Write', ' ', ' ' , resultOperand]

        self.quadruplesDictionary[self.quadraplesCounter] = quadruple


        length = len(self.operandsStack)
        index = length - 1

        if(self.operandsStack[index] != '('):
            raise TypeError("ERROR: NOT (")
        elif(self.operandsStack[index] == '('):
            print("FOUND (, PROCESS CORRECT.")
            self.operandsStack.pop()
        else:
            print("SOMETHING WENT BAD, WRONG LOGIC")
            raise TypeError("SOMETHING WENT BAD, WRONG LOGIC")




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")  

    def preProcessWriteQuadruple(self):
        length = len(self.operandsStack)
        index = length - 1
        indexForWriteQuadruple = index - 1

        print(" ")
        print("PROCESS HIPER EXP OF WRITE/////////////////////////////////////////////")
        print("operandsStack: ", self.operandsStack)
        print("Length: ", length)

        if(length > 0):
            print("=======================================")
            print("index: ", index)
            print("Last element: ", self.operandsStack[index])
            print("index - 1: ", indexForWriteQuadruple)
            print("Last element - 1: ", self.operandsStack[indexForWriteQuadruple])


            while((len(self.operatorsStack) > 0) and (self.operandsStack[indexForWriteQuadruple] != '(')):
                if(length > 0):
                    print("PRE OPERATOR FOUND")
                    print("=======================================")
                    print("Pre: ", self.operandsStack)
                    print("Pre: ", self.typesStack)
                    print("Pre: ", self.operatorsStack)
                    print("Not found ( as index - 1 of operands", True)
                    #self.operatorsStack.pop()




                    rightOperand = self.operandsStack.pop()
                    leftOperand = self.operandsStack.pop()
                    rightType = self.typesStack.pop()
                    leftType = self.typesStack.pop()
                    operator = self.operatorsStack.pop()

                    print("TYPE MATCHING DATA")
                    print([operator, leftType, rightType])
                        
                    #CHECAR COMPATIBILIDAD DE TIPOS.
                    resultingType = matchTypes.match((operator, leftType, rightType))

                    self.temporalsCounter = self.temporalsCounter + 1
                    self.quadraplesCounter = self.quadraplesCounter + 1

                    quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]

                    self.quadruplesDictionary[self.quadraplesCounter] = quadruple

                    self.operandsStack.append(self.temporalsCounter)
                    self.typesStack.append(resultingType)




                    print("Post: ", self.operandsStack)
                    print("Post: ", self.typesStack)
                    print("Post: ", self.operatorsStack)

                    length = len(self.operandsStack)
                    index = length - 1
                    indexForWriteQuadruple = index - 1

                    print("New index: ", index)
                    print("New last element: ", self.operandsStack[index])
                    print("Index - 1: ", indexForWriteQuadruple)
                    print("New last element - 1: ", self.operandsStack[indexForWriteQuadruple])

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
        print("///////////////////////////////////////////////////////")
        print("PRE PRCOESS OF HIPER EXP OF WRITE////////////////////////////////")
        print("///////////////////////////////////////////////////////")

        self.operandsStack.append('(') 
        print(" ")
        print("Processing: (..........................................")
        print(self.operandsStack)
        print(" ")



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




        self.operandsStack.append(varId)
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




        resultOperand = self.operandsStack.pop()
        self.typesStack.pop()


        print(['Read', ' ', ' ' , resultOperand])
                            
        self.quadraplesCounter = self.quadraplesCounter + 1

        quadruple = ['Read', ' ', ' ' , resultOperand]

        self.quadruplesDictionary[self.quadraplesCounter] = quadruple




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")


# #============================================================================== 

    def processDecisionPostConditionalStatute(self):
        print(" ")
        print("IF GO TO QUADRUPLE GENERATION")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        resultOperand = self.operandsStack.pop()
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
        self.quadraplesCounter = self.quadraplesCounter + 1

        #quadruple = [operator, leftOperand, rightOperand, self.temporalsCounter]
        quadruple = ['goToF', resultOperand, ' ' , '#']

        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        self.jumpsStack.append(self.quadraplesCounter)

        #self.operandsStack.append(self.temporalsCounter)
        #self.typesStack.append(resultingType)




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")

    def processDecisionPostStatement(self):
        print(" ")
        print("IF POST STATEMENT: FILL PENDING JUMPS")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        counter = self.quadraplesCounter + 1
        pendingJump = self.jumpsStack.pop()
        quadruple = self.quadruplesDictionary[pendingJump]

        print("quadruple: ", quadruple)
        print("quadruple[0]: ", quadruple[0])
        print("quadruple[1]: ", quadruple[1])
        print("quadruple[2]: ", quadruple[2])
        print("quadruple[3]: ", quadruple[3])

        quadruple[3] = counter

        print("New quadruple with counter: ", quadruple)

        self.quadruplesDictionary[pendingJump] = quadruple




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")

    #EL 3 LLENA EL 2
    def processDecisionElse(self):
        print(" ")
        print("IF POST STATEMENT: FILL PENDING JUMPS")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        self.quadraplesCounter = self.quadraplesCounter + 1
        counter = self.quadraplesCounter + 1


        pendingJump = self.jumpsStack.pop()
        quadruple = self.quadruplesDictionary[pendingJump]

        quadruple[3] = counter

        print("New quadruple with counter: ", quadruple)

        self.quadruplesDictionary[pendingJump] = quadruple



        elseQuadruple = ['goTo', ' ', ' ', '#']

        self.quadruplesDictionary[self.quadraplesCounter] = elseQuadruple
        self.jumpsStack.append(self.quadraplesCounter)




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)
        print(" ")

#==============================================================================
#==============================================================================
#==============================================================================

    def processWhileCyclePreExpression(self):
        print(" ")
        print("WHILE PRE EXPRESSION TO QUADRUPLE GENERATION")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        contador = self.quadraplesCounter + 1
        self.jumpsStack.append(contador)




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)

        print("quadruplesDictionary: ")
        print(self.quadruplesDictionary)
        print(" ")

    def processWhileCyclePostExpression(self):
        print(" ")
        print("WHILE POST EXPRESSION QUADRUPLE GENERATION")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        resultType = self.typesStack.pop()

        if(resultType != 'bool'):
            raise TypeError("ERROR: IF EXPRESSION TYPE MISMATCH (NOT BOOL).")
        elif(resultType == 'bool'):
            print("RESULTING TYPE BOOL: CORRECT")
        

        resultOperand = self.operandsStack.pop()

        self.quadraplesCounter = self.quadraplesCounter + 1

        print(['goToF', resultOperand, ' ' , '#'])

        quadruple = ['goToF', resultOperand, ' ' , '#']

        counter = self.quadraplesCounter + 1


        self.quadruplesDictionary[self.quadraplesCounter] = quadruple
        self.jumpsStack.append(self.quadraplesCounter)




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)

        print("quadruplesDictionary: ")
        print(self.quadruplesDictionary)
        print(" ")

    def processWhileCyclePostStatement(self):
        print(" ")
        print("WHILE POST STATEMENT: FILL PENDING JUMPS")
        print("=======================================")
        print("Pre: ", self.operandsStack)
        print("Pre: ", self.typesStack)
        print("Pre: ", self.operatorsStack)
        print("Pre: ", self.jumpsStack)




        self.quadraplesCounter = self.quadraplesCounter + 1
        counter = self.quadraplesCounter + 1


        pendingJump = self.jumpsStack.pop()
        quadruple = self.quadruplesDictionary[pendingJump]

        quadruple[3] = counter

        print("New quadruple with counter: ", quadruple)

        self.quadruplesDictionary[pendingJump] = quadruple



        preExpressionNumberOfQuadruple = self.jumpsStack.pop()

        newQuadrupleToAdd = ['goTo', ' ', ' ', preExpressionNumberOfQuadruple]
        
        print(newQuadrupleToAdd)

        self.quadruplesDictionary[self.quadraplesCounter] = newQuadrupleToAdd




        print("Post: ", self.operandsStack)
        print("Post: ", self.typesStack)
        print("Post: ", self.operatorsStack)
        print("Post: ", self.jumpsStack)

        print("quadruplesDictionary: ")
        print(self.quadruplesDictionary)
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
