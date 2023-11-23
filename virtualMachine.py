class VM:
    def __init__(self, quadruples, constants, totalQuadruples):
        self.quadruplesDictionary = quadruples
        #self.constantsDictionary = constants

        self.virtualMemoryDictionary = constants
        
        self.functionsJumpStack = []
        
        self.actualQuadupleCounter = 1
        self.numberOfGenereatedQuaduples = totalQuadruples
    
    def executeQuaduples(self):
        goToMainQuadruple = self.quadruplesDictionary.get(1)
        mainQuadruple = goToMainQuadruple[3]
        
        self.actualQuadupleCounter = mainQuadruple

        #while(self.quadruplesDictionary[self.actualQuadupleCounter][0] != 'End'):
        while(self.actualQuadupleCounter < self.numberOfGenereatedQuaduples or self.actualQuadupleCounter == self.numberOfGenereatedQuaduples):
            actualQuadruple = self.quadruplesDictionary.get(self.actualQuadupleCounter)
            print(" ")
            print('actualQuadruple executing:')
            print(actualQuadruple)
            print(" ")

            if(actualQuadruple[0] == '+'):
                leftOperand = actualQuadruple[1]
                rightOperand = actualQuadruple[2]
                memoryToStore = actualQuadruple[3]

                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = leftValue + rightValue
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '-'):
                leftOperand = actualQuadruple[1]
                rightOperand = actualQuadruple[2]
                memoryToStore = actualQuadruple[3]

                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = leftValue - rightValue
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '*'):
                leftOperand = actualQuadruple[1]
                rightOperand = actualQuadruple[2]
                memoryToStore = actualQuadruple[3]

                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = leftValue * rightValue
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '/'):
                leftOperand = actualQuadruple[1]
                rightOperand = actualQuadruple[2]
                memoryToStore = actualQuadruple[3]

                leftValue = self.virtualMemoryDictionary.get(leftOperand, 'nothing')
                rightValue = self.virtualMemoryDictionary.get(rightOperand, 'nothing')

                ##########################################################
                ##########################################################
                valueToStore = leftValue / rightValue
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '='):
                leftOperand = actualQuadruple[3]
                rightOperand = actualQuadruple[1]

                valueToStore = self.virtualMemoryDictionary.get(rightOperand)
                self.virtualMemoryDictionary[leftOperand] = valueToStore
            
            print(" ")
            print(self.virtualMemoryDictionary)
            print(" ")

            self.actualQuadupleCounter = self.actualQuadupleCounter + 1

    def getVirtualMemoryDictionary(self):
        print("////////////////////////////////////////////////")
        print("//////  VIRTUAL MACHINE MEMORY  ////////////////")
        print("////////////////////////////////////////////////")
        print(" ")
        print(self.virtualMemoryDictionary)

