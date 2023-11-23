class VM:
    def __init__(self, quadruples, constants, totalQuadruples):
        self.quadruplesDictionary = quadruples
        #self.constantsDictionary = constants

        self.virtualMemoryDictionary = constants
        
        self.functionsJumpStack = []
        
        self.actualQuadupleCounter = 1
        self.numberOfGenereatedQuaduples = totalQuadruples

    def getAddressType(self, address):
        isString = isinstance(address, str)
        addressToCheck = address
        
        if(isString == True):
            addressToCheck = int(address)

        if(addressToCheck == 1 or addressToCheck == 3333 or (addressToCheck > 1 and addressToCheck < 3333)):
            return 'int'
        elif(addressToCheck == 3334 or addressToCheck == 6666 or (addressToCheck > 3334 and addressToCheck < 6666)):
            return 'float'
        elif(addressToCheck == 6667 or addressToCheck == 10000 or (addressToCheck > 6667 and addressToCheck < 10000)):
            return 'char'
        elif(addressToCheck == 10001 or addressToCheck == 13333 or (addressToCheck > 10001 and addressToCheck < 13333)):
            return 'int'
        elif(addressToCheck == 13334 or addressToCheck == 16666 or (addressToCheck > 13334 and addressToCheck < 16666)):
            return 'float'
        elif(addressToCheck == 16667 or addressToCheck == 20000 or (addressToCheck > 16667 and addressToCheck < 20000)):
            return 'char'
        elif(addressToCheck == 20001 or addressToCheck == 22500 or (addressToCheck > 20001 and addressToCheck < 22500)):
            return 'int'
        elif(addressToCheck == 22501 or addressToCheck == 25000 or (addressToCheck > 22501 and addressToCheck < 25000)):
            return 'float'
        elif(addressToCheck == 25001 or addressToCheck == 27500 or (addressToCheck > 25001 and addressToCheck < 27500)):
            return 'char'
        elif(addressToCheck == 27501 or addressToCheck == 30000 or (addressToCheck > 27501 and addressToCheck < 30000)):
            return 'bool'
        elif(addressToCheck == 30001 or addressToCheck == 32500 or (addressToCheck > 30001 and addressToCheck < 32500)):
            return 'int'
        elif(addressToCheck == 32501 or addressToCheck == 35000 or (addressToCheck > 32501 and addressToCheck < 35000)):
            return 'float'
        elif(addressToCheck == 35001 or addressToCheck == 37500 or (addressToCheck > 35001 and addressToCheck < 37500)):
            return 'char'
        elif(addressToCheck == 37501 or addressToCheck == 40000 or (addressToCheck > 37501 and addressToCheck < 40000)):
            return 'string'
        

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

                valueType = self.getAddressType(memoryToStore)
                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)

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


                
                valueType = self.getAddressType(memoryToStore)
                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)



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



                valueType = self.getAddressType(memoryToStore)
                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)



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



                valueType = self.getAddressType(memoryToStore)
                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)



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



                valueType = self.getAddressType(leftOperand)
                print("")
                print("Address:")
                print(leftOperand)
                print("Address Type:")
                print(valueType)



                valueToStore = self.virtualMemoryDictionary.get(rightOperand)
                self.virtualMemoryDictionary[leftOperand] = valueToStore
            elif(actualQuadruple[0] == 'Read'):
                memoryToStore = actualQuadruple[3]

                valueType = self.getAddressType(memoryToStore)
                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)

                inputToRead = input()

                print("")
                print("Value read type:")
                print(type(inputToRead))
                print("")

                inputRead = inputToRead

                if(valueType == 'int'):
                    inputRead = int(inputToRead)
                    print("SHOULD BE TYPE INT")
                elif(valueType == 'float'):
                    inputRead = float(inputToRead)
                    print("SHOULD BE TYPE FLOAT")

                

                self.virtualMemoryDictionary[memoryToStore] = inputRead
            elif(actualQuadruple[0] == 'Write'):
                memoryValue = actualQuadruple[3]
                storedValue = self.virtualMemoryDictionary.get(memoryValue)

                print("PRINTING....")
                print(storedValue)
            




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

