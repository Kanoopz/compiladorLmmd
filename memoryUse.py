        ############
        # GLOBALES #
        ############
        #1-10000
        # 0 [ 0001 -> 3333 : ent ]
        # 1 [ 3334 -> 6666 : flot ]
        # 2 [ 6667 -> 10000 : car ]
        ###########
        # LOCALES #
        ###########
        #10001-20000
        # 5 [ 10001 -> 13333 : ent ]
        # 6 [ 13334 -> 16666 : flot ]
        # 7 [ 16667 -> 20000 : car ]
        ############
        # TEMPORAL #
        ############
        #20001-30000
        # 10 [ 20001 -> 22500 : ent ]
        # 11 [ 22501 -> 25000 : flot ]
        # 12 [ 25001 -> 27500 : car ]
        # 14 [ 27501 -> 30000 : bool ]
        ##############
        # CONSTANTES #
        ##############
        #30001-40000
        # 16 [ 30001 -> 32500 : ent ]
        # 17 [ 32501 -> 35000 : flot ]
        # 18 [ 35001 -> 37500 : car ]
        # 19 [ 37501 -> 40000 : cadena ]

class useOfMemory:
    def __init__(self):
        self.memoryAddresses_vars_Dictionary = {}
        self.vars_memoryAddresses_Dictionary = {}

        self.memoryAddresses_vars_Dictionary['Global'] = {}
        self.memoryAddresses_vars_Dictionary['Locals'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals'] = {}
        self.memoryAddresses_vars_Dictionary['Constants'] = {}

        self.globalIntCounter = 0
        self.globalFloatCounter = 3333
        self.globalCharCounter = 6666

        self.memoryAddresses_vars_Dictionary['Global']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Global']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Global']['char'] = {}

        self.localIntCounter = 10000
        self.localFloatCounter = 13333
        self.localCharCounter = 16666

        self.memoryAddresses_vars_Dictionary['Locals']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Locals']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Locals']['char'] = {}

        self.temporalsIntCounter = 20000
        self.temporalsFloatCounter = 22500
        self.temporalsCharCounter = 25000
        self.temporalsBoolCounter = 27500

        self.memoryAddresses_vars_Dictionary['Temporals']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['char'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['bool'] = {}

        self.constantsIntCounter = 30000
        self.constantsFloatCounter = 32500
        self.constantsCharCounter = 35000
        self.constantsStringCounter = 37500

        self.memoryAddresses_vars_Dictionary['Constants']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Constants']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Constants']['char'] = {}
        self.memoryAddresses_vars_Dictionary['Constants']['string'] = {}


        self.vars_memoryAddresses_Dictionary['Global'] = {}
        self.vars_memoryAddresses_Dictionary['Locals'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals'] = {}
        self.vars_memoryAddresses_Dictionary['Constants'] = {}

        self.vars_memoryAddresses_Dictionary['Global']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Global']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Global']['char'] = {}

        self.vars_memoryAddresses_Dictionary['Locals']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Locals']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Locals']['char'] = {}

        self.vars_memoryAddresses_Dictionary['Temporals']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['char'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['bool'] = {}

        self.vars_memoryAddresses_Dictionary['Constants']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Constants']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Constants']['char'] = {}
        self.vars_memoryAddresses_Dictionary['Constants']['string'] = {}



    def saveAddress(self, scope, type, varId):
        if(scope == 'Global'):
            ############
            # GLOBALES #
            ############
            #1-10000
            # [ 0001 -> 3333 : ent ]
            # [ 3334 -> 6666 : flot ]
            # [ 6667 -> 10000 : car ]
            if(type == 'int'):
                if(self.globalIntCounter == 3333 or self.globalIntCounter > 3333):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL INT VARS.")
                elif(self.globalIntCounter < 3333):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['int'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.globalIntCounter = self.globalIntCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['int'][varId] = self.globalIntCounter
                        self.memoryAddresses_vars_Dictionary['Global']['int'][self.globalIntCounter] = varId
                        
                        return self.globalIntCounter       
            elif(type == 'float'):
                if(self.globalFloatCounter == 6666 or self.globalFloatCounter > 6666):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL FLOAT VARS.")
                elif(self.globalFloatCounter < 6666):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['float'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.globalFloatCounter = self.globalFloatCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['float'][varId] = self.globalFloatCounter
                        self.memoryAddresses_vars_Dictionary['Global']['float'][self.globalFloatCounter] = varId
                            
                        return self.globalFloatCounter
            elif(type == 'char'):
                if(self.globalCharCounter == 10000 or self.globalCharCounter > 10000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL CHAR VARS.")
                elif(self.globalCharCounter < 10000):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['char'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.globalCharCounter = self.globalCharCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['char'][varId] = self.globalCharCounter
                        self.memoryAddresses_vars_Dictionary['Global']['char'][self.globalCharCounter] = varId
                            
                        return self.globalCharCounter
            else:
                raise TypeError("ERROR: INCORRECT GLOBAL VAR TYPE")
        elif(scope == 'Locals'):
            ###########
            # LOCALES #
            ###########
            #10001-20000
            # [ 10001 -> 13333 : ent ]
            # [ 13334 -> 16666 : flot ]
            # [ 16667 -> 20000 : car ]
            if(type == 'int'):
                if(self.localIntCounter == 13333 or self.localIntCounter > 13333):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL INT VARS.")
                elif(self.localIntCounter < 13333):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['int'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.localIntCounter = self.localIntCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['int'][varId] = self.localIntCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['int'][self.localIntCounter] = varId
                            
                        return self.localIntCounter
            elif(type == 'float'):
                if(self.localFloatCounter == 16666 or self.localFloatCounter > 16666):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL FLOAT VARS.")
                elif(self.localFloatCounter < 16666):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['float'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.localFloatCounter = self.localFloatCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['float'][varId] = self.localFloatCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['float'][self.localFloatCounter] = varId
                            
                        return self.localFloatCounter
            elif(type == 'char'):
                if(self.localCharCounter == 20000 or self.localCharCounter > 20000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL CHAR VARS.")
                elif(self.localCharCounter < 20000):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['char'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                        self.localCharCounter = self.localCharCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['char'][varId] = self.localCharCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['char'][self.localCharCounter] = varId
                            
                        return self.localCharCounter
            else:
                raise TypeError("ERROR: INCORRECT LOCAL VAR TYPE")
        elif(scope == 'Temporals'):
            ############
            # TEMPORAL #
            ############
            #20001-30000
            # [ 20001 -> 22500 : ent ]
            # [ 22501 -> 25000 : flot ]
            # [ 25001 -> 27500 : car ]
            # [ 27501 -> 30000 : bool ]
            if(type == 'int'):
                if(self.temporalsIntCounter == 22500 or self.temporalsIntCounter > 22500):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR TEMPORALS INT VARS.")
                elif(self.temporalsIntCounter < 22500):
                    exists = self.vars_memoryAddresses_Dictionary['Temporals']['int'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                       self.temporalsIntCounter = self.temporalsIntCounter + 1 
                       self.vars_memoryAddresses_Dictionary['Temporals']['int'][varId] = self.temporalsIntCounter
                       self.memoryAddresses_vars_Dictionary['Temporals']['int'][self.temporalsIntCounter] = varId
                            
                       return self.temporalsIntCounter
            elif(type == 'float'):
                if(self.temporalsFloatCounter == 25000 or self.temporalsFloatCounter > 25000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR TEMPORALS FLOAT VARS.")
                elif(self.temporalsFloatCounter < 25000):
                    exists = self.vars_memoryAddresses_Dictionary['Temporals']['float'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                       self.temporalsFloatCounter = self.temporalsFloatCounter + 1 
                       self.vars_memoryAddresses_Dictionary['Temporals']['float'][varId] = self.temporalsFloatCounter
                       self.memoryAddresses_vars_Dictionary['Temporals']['float'][self.temporalsFloatCounter] = varId
                            
                       return self.temporalsFloatCounter
            elif(type == 'char'):
                if(self.temporalsCharCounter == 27500 or self.temporalsCharCounter > 27500):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR TEMPORAL CHAR VARS.")
                elif(self.temporalsCharCounter < 27500):
                    exists = self.vars_memoryAddresses_Dictionary['Temporals']['char'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists =='notDeclared'):
                       self.temporalsCharCounter = self.temporalsCharCounter + 1 
                       self.vars_memoryAddresses_Dictionary['Temporals']['char'][varId] = self.temporalsCharCounter
                       self.memoryAddresses_vars_Dictionary['Temporals']['char'][self.temporalsCharCounter] = varId
                            
                       return self.temporalsCharCounter
            elif(type == 'bool'):
                if(self.temporalsBoolCounter == 30000 or self.temporalsBoolCounter > 30000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR TEMPORAL BOOL VARS.")
                elif(self.temporalsBoolCounter < 30000):
                    exists = self.vars_memoryAddresses_Dictionary['Temporals']['bool'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE.")
                    elif(exists == 'notDeclared'):
                        self.temporalsBoolCounter = self.temporalsBoolCounter + 1
                        self.vars_memoryAddresses_Dictionary['Temporals']['bool'][varId] = self.temporalsBoolCounter
                        self.memoryAddresses_vars_Dictionary['Temporals']['bool'][self.temporalsBoolCounter] = varId
                            
                        return self.temporalsBoolCounter
            else:
                raise TypeError("ERROR: INCORRECT TEMPORAL VAR TYPE")
        elif(scope == 'Constants'):
            ##############
            # CONSTANTES #
            ##############
            #30001-40000
            # [ 30001 -> 32500 : ent ]
            # [ 32501 -> 35000 : flot ]
            # [ 35001 -> 37500 : car ]
            # [ 37501 -> 40000 : cadena ]
            if(type == 'int'):
                if(self.constantsIntCounter == 32500 or self.constantsIntCounter > 32500):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR CONSTANTS INT VARS.")
                elif(self.constantsIntCounter < 32500):
                    exists = self.vars_memoryAddresses_Dictionary['Constants']['int'].get(varId, 'notDeclared')

                    if(exists != 'notDeclared'):
                        return exists
                    elif(exists == 'notDeclared'):
                        self.constantsIntCounter = self.constantsIntCounter + 1 
                        self.vars_memoryAddresses_Dictionary['Constants']['int'][varId] = self.constantsIntCounter
                        self.memoryAddresses_vars_Dictionary['Constants']['int'][self.constantsIntCounter] = varId
                            
                        return self.constantsIntCounter
            elif(type == 'float'):
                if(self.constantsFloatCounter == 35000 or self.constantsFloatCounter > 35000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR CONSTANTS FLOAT VARS.")
                elif(self.constantsFloatCounter < 35000):
                    exists = self.vars_memoryAddresses_Dictionary['Constants']['float'].get(varId, 'notDeclared')

                    if(exists != 'notDeclared'):
                        return exists
                    elif(exists == 'notDeclared'):
                        self.constantsFloatCounter = self.constantsFloatCounter + 1 
                        self.vars_memoryAddresses_Dictionary['Constants']['float'][varId] = self.constantsFloatCounter
                        self.memoryAddresses_vars_Dictionary['Constants']['float'][self.constantsFloatCounter] = varId
                            
                        return self.constantsFloatCounter
            elif(type == 'char'):
                if(self.constantsCharCounter == 37500 or self.constantsCharCounter > 37500):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR CONSTANTS CHAR VARS.")
                elif(self.constantsCharCounter < 37500):
                    exists = self.vars_memoryAddresses_Dictionary['Constants']['char'].get(varId, 'notDeclared')

                    if(exists != 'notDeclared'):
                        return exists
                    elif(exists == 'notDeclared'):
                        self.constantsCharCounter = self.constantsCharCounter + 1 
                        self.vars_memoryAddresses_Dictionary['Constants']['char'][varId] = self.constantsCharCounter
                        self.memoryAddresses_vars_Dictionary['Constants']['char'][self.constantsCharCounter] = varId
                            
                        return self.constantsCharCounter
            elif(type == 'string'):
                if(self.constantsStringCounter == 40000 or self.constantsStringCounter > 40000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR CONSTANTS STRING VARS.")
                elif(self.constantsStringCounter < 40000):
                    exists = self.vars_memoryAddresses_Dictionary['Constants']['string'].get(varId, 'notDeclared')

                    if(exists != 'notDeclared'):
                        return exists
                    elif(exists == 'notDeclared'):
                        self.constantsStringCounter = self.constantsStringCounter + 1 
                        self.vars_memoryAddresses_Dictionary['Constants']['string'][varId] = self.constantsStringCounter
                        self.memoryAddresses_vars_Dictionary['Constants']['string'][self.constantsStringCounter] = varId
                            
                        return self.constantsStringCounter
        else:
            raise TypeError("ERROR: INCORRECT SCOPE TYPE VAR")




    def getVarAddressGlobalOrLocal(self, type, varId):
        varInDictionary = self.vars_memoryAddresses_Dictionary['Locals'][type].get(varId, 'notDeclared')

        if(varInDictionary == 'notDeclared'):
            varInDictionary2 = self.vars_memoryAddresses_Dictionary['Global'][type].get(varId, 'notDeclared')

            if(varInDictionary2 == 'notDeclared'):
                raise TypeError("Var not saved in address global nor local.")
            else:
                return [varInDictionary2, varId]
        else:
            return [varInDictionary, varId]
        

        
    def checkIfCte(self, type, cte):
        varInDictionary = self.vars_memoryAddresses_Dictionary['Constants'][type].get(cte, 'notDeclared')

        if(varInDictionary == 'notDeclared'):
            return [False, 0]
        else:
            return [True, varInDictionary]
        


    def saveArray(self, scope, type, varId, spaces):
        isString = isinstance(spaces, str)

        if(isString == True):
            intSpaces = int(spaces)
        else:
            intSpaces = spaces

        if(scope == 'Global'):
            ############
            # GLOBALES #
            ############
            #1-10000
            # [ 0001 -> 3333 : ent ]
            # [ 3334 -> 6666 : flot ]
            # [ 6667 -> 10000 : car ]
            if(type == 'int'):
                if((self.globalIntCounter + intSpaces) == 3333 or (self.globalIntCounter + intSpaces) > 3333 or self.globalIntCounter == 3333 or self.globalIntCounter > 3333):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL INT VARS.")
                elif(self.globalIntCounter < 3333):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['int'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE (GLOBAL ON VORTUAL MEMORY). VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.globalIntCounter = self.globalIntCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['int'][varId] = self.globalIntCounter
                        self.memoryAddresses_vars_Dictionary['Global']['int'][self.globalIntCounter] = varId
                        
                        baseAddress =  self.globalIntCounter

                        intSpaces = intSpaces - 1

                        self.globalIntCounter = self.globalIntCounter + intSpaces

                        return baseAddress
            elif(type == 'float'):
                if((self.globalFloatCounter + intSpaces) == 6666 or (self.globalFloatCounter + intSpaces) > 6666 or self.globalFloatCounter == 6666 or self.globalFloatCounter > 6666):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL FLOAT VARS.")
                elif(self.globalFloatCounter < 6666):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['float'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE (GLOBAL ON VORTUAL MEMORY). VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.globalFloatCounter = self.globalFloatCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['float'][varId] = self.globalFloatCounter
                        self.memoryAddresses_vars_Dictionary['Global']['float'][self.globalFloatCounter] = varId

                        baseAddress =  self.globalFloatCounter

                        intSpaces = intSpaces - 1

                        self.globalFloatCounter = self.globalFloatCounter + intSpaces

                        return baseAddress
            elif(type == 'char'):
                if((self.globalCharCounter + intSpaces) == 10000 or (self.globalCharCounter + intSpaces)  > 10000 or self.globalCharCounter == 10000 or self.globalCharCounter > 10000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR GLOBAL CHAR VARS (GLOBAL ON VORTUAL MEMORY).")
                elif(self.globalCharCounter < 10000):
                    exists = self.vars_memoryAddresses_Dictionary['Global']['char'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE. VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.globalCharCounter = self.globalCharCounter + 1
                        self.vars_memoryAddresses_Dictionary['Global']['char'][varId] = self.globalCharCounter
                        self.memoryAddresses_vars_Dictionary['Global']['char'][self.globalCharCounter] = varId

                        baseAddress =  self.globalCharCounter

                        intSpaces = intSpaces - 1

                        self.globalCharCounter = self.globalCharCounter + intSpaces

                        return baseAddress
            else:
                raise TypeError("ERROR: INCORRECT GLOBAL VAR TYPE")
        elif(scope == 'Locals'):
            ###########
            # LOCALES #
            ###########
            #10001-20000
            # [ 10001 -> 13333 : ent ]
            # [ 13334 -> 16666 : flot ]
            # [ 16667 -> 20000 : car ]
            if(type == 'int'):
                if((self.localIntCounter + intSpaces) == 13333 or (self.localIntCounter + intSpaces) > 13333 or self.localIntCounter == 13333 or self.localIntCounter > 13333):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL INT VARS.")
                elif(self.localIntCounter < 13333):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['int'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE (LOCAL ON VORTUAL MEMORY). VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.localIntCounter = self.localIntCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['int'][varId] = self.localIntCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['int'][self.localIntCounter] = varId

                        baseAddress =  self.localIntCounter

                        intSpaces = intSpaces - 1

                        self.localIntCounter = self.localIntCounter + intSpaces

                        return baseAddress
            elif(type == 'float'):
                if((self.localFloatCounter + intSpaces) == 16666 or (self.localFloatCounter + intSpaces) > 16666 or self.localFloatCounter == 16666 or self.localFloatCounter > 16666):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL FLOAT VARS.")
                elif(self.localFloatCounter < 16666):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['float'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE (LOCAL ON VORTUAL MEMORY). VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.localFloatCounter = self.localFloatCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['float'][varId] = self.localFloatCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['float'][self.localFloatCounter] = varId
                            
                        baseAddress =  self.localFloatCounter

                        intSpaces = intSpaces - 1

                        self.localFloatCounter = self.localFloatCounter + intSpaces

                        return baseAddress
            elif(type == 'char'):
                if((self.localCharCounter + intSpaces) == 20000 or (self.localCharCounter + intSpaces) > 20000 or self.localCharCounter == 20000 or self.localCharCounter > 20000):
                    raise TypeError("ERROR: REACHED MEMORY LIMIT FOR LOCAL CHAR VARS.")
                elif(self.localCharCounter < 20000):
                    exists = self.vars_memoryAddresses_Dictionary['Locals']['char'].get(varId, 'notDeclared')
    
                    if(exists != 'notDeclared'):
                        raise TypeError("ERROR: VAR ALREADY DECLARED IN THIS SCOPE (LOCAL ON VORTUAL MEMORY). VAR ID:", varId)
                    elif(exists =='notDeclared'):
                        self.localCharCounter = self.localCharCounter + 1
                        self.vars_memoryAddresses_Dictionary['Locals']['char'][varId] = self.localCharCounter
                        self.memoryAddresses_vars_Dictionary['Locals']['char'][self.localCharCounter] = varId
                            
                        baseAddress =  self.localCharCounter

                        intSpaces = intSpaces - 1

                        self.localCharCounter = self.localCharCounter + intSpaces

                        return baseAddress
            else:
                raise TypeError("ERROR: INCORRECT LOCAL VAR TYPE")

        










        return baseAddress




    def resetLocalAndTemporalScope(self):
        self.localIntCounter = 10000
        self.localFloatCounter = 13333
        self.localCharCounter = 16666

        self.temporalsIntCounter = 20000
        self.temporalsFloatCounter = 22500
        self.temporalsCharCounter = 25000
        self.temporalsBoolCounter = 27500


        self.memoryAddresses_vars_Dictionary['Locals']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Locals']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Locals']['char'] = {}

        self.memoryAddresses_vars_Dictionary['Temporals']['int'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['float'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['char'] = {}
        self.memoryAddresses_vars_Dictionary['Temporals']['bool'] = {}


        self.vars_memoryAddresses_Dictionary['Locals']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Locals']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Locals']['char'] = {}

        self.vars_memoryAddresses_Dictionary['Temporals']['int'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['float'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['char'] = {}
        self.vars_memoryAddresses_Dictionary['Temporals']['bool'] = {}

    def getConstantsVirtualMemory(self):
        constants = self.memoryAddresses_vars_Dictionary['Constants']
        return constants


    def printDictionaries(self):
        print(" ")
        print("vars -> memory:")
        print(self.vars_memoryAddresses_Dictionary)
        print(" ")
        print("memory -> vars:")
        print(self.memoryAddresses_vars_Dictionary)
        print(" ")
        print("////////////////////////////////////////////////////////////////////")
