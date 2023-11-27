class declaredScopedVars:
    def __init__(self):
        self.declaredVarsScope = {}
        self.isArray = {}

        self.actualScope = 'noInitialized'
        self.actualType = 'noInitialized'


    def addVarInScope(self, scope, var, type): 
        scopeInDictonary = self.declaredVarsScope.get(scope, 'notDeclared')

        if(scopeInDictonary == 'notDeclared'):
            self.declaredVarsScope[scope] = {}

        
        varInDictonary = self.declaredVarsScope[scope].get(var, 'notDeclared')

        if(varInDictonary == 'notDeclared'):
            self.declaredVarsScope[scope][var] = type
        else:

            raise TypeError("ERROR: " + var + " already declared in " + scope + " scope.")

    def setActualScope(self, scope): 
        self.actualScope = scope

    def getActualScope(self): 
        return self.actualScope

    def setActualType(self, type):
        self.actualType = type

    def addVar(self, varId):
        self.addVarInScope(self.actualScope, varId, self.actualType)

    def addArray(self, arrayId, spaces):
        print("ActualDictionary:")
        print(self.isArray)
        print("actualScope:")
        print(self.actualScope)
        print("actualType")
        print(self.actualType)
        print(" ")

        scopeInDictonary = self.isArray.get(self.actualScope, 'notDeclared')
        


        if(scopeInDictonary == 'notDeclared'):
            self.isArray[self.actualScope] = {}

        
        varInDictonary = self.isArray[self.actualScope].get(arrayId, 'notDeclared')

        if(varInDictonary == 'notDeclared'):
            self.isArray[self.actualScope][arrayId] = [self.actualType, spaces]

            return self.isArray
        else:
            raise TypeError("ERROR: " + arrayId + " already declared in " + self.actualScope + " scope.")

    def checkVar(self, varId, scope):
         varInDictonary = self.declaredVarsScope[scope].get(varId, 'notDeclaredInScopeTryingOnGlobal')

         if(varInDictonary == 'notDeclaredInScopeTryingOnGlobal'):
             varInDictonary2 = self.declaredVarsScope['Global'].get(varId, 'notDeclaredInGlobal')

             if(varInDictonary2 == 'notDeclaredInGlobal'):
                 raise TypeError("ERROR: " + varId + " not declared in " + scope + " scope or in Global.")
             else:
                 return True, varInDictonary2
         else:
             return True, varInDictonary

    def checkArray(self, arrayId, scope):
        scopeInDictionary = self.isArray.get(scope, 'scopeNotInDictionary')

        if(scopeInDictionary != 'scopeNotInDictionary'):
            varInDictonary = self.isArray[scope].get(arrayId, 'notDeclaredInScopeTryingOnGlobal')

            if(varInDictonary == 'notDeclaredInScopeTryingOnGlobal'):
                varInDictonary2 = self.isArray['Global'].get(arrayId, 'notDeclaredInGlobal')

                if(varInDictonary2 == 'notDeclaredInGlobal'):
                    raise TypeError("ERROR: " + arrayId + " not declared in " + scope + " scope or in Global.")
                else:
                    return True, varInDictonary2
            else:
                return True, varInDictonary
            
    def getArrayDic(self):
        return self.isArray
        
    def getVarTable(self):
        print("methodGetVarTable")
        print(self.declaredVarsScope)
        print("methodGetArrays")
        print(self.isArray)

    def getVarTableData(self):
        return self.declaredVarsScope

        
