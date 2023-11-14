class declaredScopedVars:
    def __init__(self):
        self.declaredVarsScope = {}

    def addVarInScope(self, scope, var, type): 
        scopeInDictonary = self.declaredVarsScope.get(scope, 'notDeclared')
        
        print("Searching in dictonary the scope: ", scope)
        print("Result: ", scopeInDictonary)


        if(scopeInDictonary == 'notDeclared'):
            self.declaredVarsScope[scope] = {}
            print("Added new scope: ", self.declaredVarsScope)

        
        varInDictonary = self.declaredVarsScope[scope].get(var, 'notDeclared')

        if(varInDictonary == 'notDeclared'):
            print("Var not declared, adding to dictonary.")
            self.declaredVarsScope[scope][var] = type
            print("Resulting dictonary after adding var: ", self.declaredVarsScope)
        else:
            print("ERROR: var already declared.")

        print(" ")

        
