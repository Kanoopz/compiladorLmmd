class VM:
    def __init__(self, quadruples, constants, totalQuadruples, functions):
        self.quadruplesDictionary = quadruples
        #self.constantsDictionary = constants

        self.virtualMemoryDictionary = constants
        
        self.functionsDictionary = functions
        
        self.functionsJumpStack = []
        #self.functionYetToJumpStack = []
        self.functionsParamStack = []
        
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

    def setParamValuesInLocalAddresses(self):
        ("preInverseParamsStack: ", self.functionsParamStack)
        self.functionsParamStack.reverse()
        ("postInverseParamsStack: ", self.functionsParamStack)

        paramCounter = len(self.functionsParamStack)
        print("quantityOfActualParamsInStack: ", paramCounter)

        intAddressCounter = 10000
        floatAddressCounter = 13333
        charAddressCounter = 16666

        while(paramCounter != 0):
            address = self.functionsParamStack.pop()
            print("addressOfProcessingParamValue, ", address)

            type = self.getAddressType(address)
            print("typeOfTheAddress: ", type)

            if(type == 'int'):
                print("preIntAddress: ", intAddressCounter)
                intAddressCounter = intAddressCounter + 1
                print("postIntAddress: ", intAddressCounter)

                memoryToStore = intAddressCounter

                valueToStore = self.virtualMemoryDictionary.get(address)

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(type == 'float'):
                print("preFloatAddress: ", floatAddressCounter)
                floatAddressCounter = floatAddressCounter + 1
                print("postFloatAddress: ", floatAddressCounter)

                memoryToStore = floatAddressCounter

                valueToStore = self.virtualMemoryDictionary.get(address)

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(type == 'char'):
                charAddressCounter = charAddressCounter + 1
                memoryToStore = charAddressCounter

                valueToStore = self.virtualMemoryDictionary.get(address)

                self.virtualMemoryDictionary[memoryToStore] = valueToStore


            paramCounter = len(self.functionsParamStack)


    def checkIndirectIndex(self, address):
        print("COMPARING INDIRECT ADDRESS")
        print("ADDRESS CHECKING: ", address)

        isString = isinstance(address, str)
        print("isString?: ", isString)
        #addressToCheck = address
        
        if(isString == True and address != ' '):
            #addressToCheck = int(address)
            charFoundCounter = 0
            charCheck = ["{", "}"]

            for char in charCheck:
                if char in address:
                    charFoundCounter = charFoundCounter + 1
            
            if(charFoundCounter == 2):
                print("INDIRECT ADDRESS FOUND:", address)

                processedAddress = address.replace("{", "").replace("}", "")

                print("ADDRESS AFTER DELETING {:", processedAddress)

                # processedAddress2 = processedAddress.replace("} ", "")

                # print("ADDRESS AFTER DELETING }:", processedAddress2)

                intAddress = int(processedAddress)

                indirectAddress = self.virtualMemoryDictionary.get(intAddress, 'error')

                print("indirectAddress: ", indirectAddress)

                if(indirectAddress == 'error'):
                    raise TypeError("ERROR: SOMETHING WENT WRONG GETTING THE INDIRECT ADDRESS")
                else:
                    return indirectAddress
            elif(charCheck == 0):
                return address
            else:
                raise TypeError("ERROR: INDIRECT ADDRESS NOT PROCESSED CORRECTLY")
        elif(isString == False):
            return address
        
    def checkIndirectIndexForMemoryToStore(self, address):
        print("COMPARING INDIRECT ADDRESS")
        print("ADDRESS CHECKING: ", address)

        isString = isinstance(address, str)
        print("isString?: ", isString)
        #addressToCheck = address
        
        if(isString == True and address != ' '):
            #addressToCheck = int(address)
            charFoundCounter = 0
            charCheck = ["{", "}"]

            for char in charCheck:
                if char in address:
                    charFoundCounter = charFoundCounter + 1
            
            if(charFoundCounter == 2):
                print("INDIRECT ADDRESS FOUND:", address)

                processedAddress = address.replace("{", "").replace("}", "")

                print("ADDRESS AFTER DELETING {:", processedAddress)

                # processedAddress2 = processedAddress.replace("} ", "")

                # print("ADDRESS AFTER DELETING }:", processedAddress2)

                intAddress = int(processedAddress)

                #indirectAddress = self.virtualMemoryDictionary.get(intAddress, 'error')

                #print("indirectAddress: ", indirectAddress)

                # if(indirectAddress == 'error'):
                #     raise TypeError("ERROR: SOMETHING WENT WRONG GETTING THE INDIRECT ADDRESS")
                # else:
                #     return indirectAddress

                return [True, intAddress]
            elif(charCheck == 0):
                return [False, address]
            else:
                raise TypeError("ERROR: INDIRECT ADDRESS NOT PROCESSED CORRECTLY")
        elif(isString == False):
            return [False, address]

    def executeQuaduples(self):
        goToMainQuadruple = self.quadruplesDictionary.get(1)
        mainQuadruple = goToMainQuadruple[3]
        
        self.actualQuadupleCounter = mainQuadruple

        #while(self.quadruplesDictionary[self.actualQuadupleCounter][0] != 'End'):
        while(self.actualQuadupleCounter < self.numberOfGenereatedQuaduples or self.actualQuadupleCounter == self.numberOfGenereatedQuaduples):
            actualQuadruple = self.quadruplesDictionary.get(self.actualQuadupleCounter)
            print(" ")
            print('------------ actualQuadruple executing:')
            print('------------ ', actualQuadruple)
            print(" ")

            if(actualQuadruple[0] == '+'):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStoreData = self.checkIndirectIndexForMemoryToStore(actualQuadruple[3])
                memoryToStore = memoryToStoreData[1]

                valueType = self.getAddressType(memoryToStore)

                print("")
                print("Address:")
                print(memoryToStore)
                print("Address Type:")
                print(valueType)

                leftValue = self.virtualMemoryDictionary.get(leftOperand, 'notInDictionary')
                print("leftValue: ", leftValue)
                print("type of leftValue: ", type(leftValue))

                rightValue = self.virtualMemoryDictionary.get(rightOperand, 'notInDictionary')
                print("rightValue: ", rightValue)
                print("type of rightValue: ", type(rightValue))

                print("")
                if(memoryToStoreData[0] == True):
                    print("EL VALOR FUE TRUE")
                    #rightValue = self.checkIndirectIndex(actualQuadruple[2])
                    #rightValue = actualQuadruple[2]
                elif(memoryToStoreData[0] == False):
                    print("EL VALOR FUE FALSE")
                    #diunod
                print("")

                ##########################################################
                ##########################################################
                valueToStore = leftValue + rightValue
                print("RESULTING VALUE: ", valueToStore)
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '-'):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])


                
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
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])



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
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])



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

                if(valueType == 'int'):
                    valueToStoreInt = int(valueToStore)
                    valueToStore = valueToStoreInt
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '='):
                leftOperand = self.checkIndirectIndex(actualQuadruple[3])
                rightOperand = self.checkIndirectIndex(actualQuadruple[1])



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
                memoryValue = self.checkIndirectIndex(actualQuadruple[3])
                storedValue = self.virtualMemoryDictionary.get(memoryValue)

                print("PRINTING....")
                print(storedValue)
            elif(actualQuadruple[0] == '>'):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])


                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = (leftValue > rightValue)
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '<'):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])


                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = (leftValue < rightValue)
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '=='):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])


                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = (leftValue == rightValue)
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == '!='):
                leftOperand = self.checkIndirectIndex(actualQuadruple[1])
                rightOperand = self.checkIndirectIndex(actualQuadruple[2])
                memoryToStore = self.checkIndirectIndex(actualQuadruple[3])


                leftValue = self.virtualMemoryDictionary.get(leftOperand)
                rightValue = self.virtualMemoryDictionary.get(rightOperand)

                ##########################################################
                ##########################################################
                valueToStore = (leftValue != rightValue)
                ##########################################################
                ##########################################################

                self.virtualMemoryDictionary[memoryToStore] = valueToStore
            elif(actualQuadruple[0] == 'goToF'):
                condition = actualQuadruple[1]
                conditionValue = self.virtualMemoryDictionary.get(condition)

                if(conditionValue == True):
                    print("CONDITION TRUE.")
                elif(conditionValue == False):
                    print("CONDITION FALSE.")
                    jump = actualQuadruple[3]
                    
                    self.actualQuadupleCounter = jump - 1
            elif(actualQuadruple[0] == 'goTo'):
                jump = actualQuadruple[3]
                
                self.actualQuadupleCounter = jump - 1
            elif(actualQuadruple[0] == 'Era'):
                print("ERA: virtual memory for function calculated.")
            elif(actualQuadruple[0] == 'Param'):
                print("preParamStack:", self.functionsParamStack)

                print("address sending as param: ", actualQuadruple[1])
                print("value of the address: ", self.virtualMemoryDictionary.get(actualQuadruple[1]))

                self.functionsParamStack.append(actualQuadruple[1])

                print("postParamStack:", self.functionsParamStack)




            elif(actualQuadruple[0] == 'goSub'):
                startingQuadruple = self.functionsDictionary[actualQuadruple[1]].get('startingQuadruple')

                print("Starting quadruple of: ", actualQuadruple[1])
                print("is; ", startingQuadruple)

                self.functionsJumpStack.append(self.actualQuadupleCounter)

                if(len(self.functionsParamStack) != 0):
                    self.setParamValuesInLocalAddresses()


                self.actualQuadupleCounter = startingQuadruple - 1
            elif(actualQuadruple[0] == 'endFunc'):
                self.actualQuadupleCounter = self.functionsJumpStack.pop()
            elif(actualQuadruple[0] == 'Ret'):
                print("Returning funcValue.....")
            elif(actualQuadruple[0] == 'Ver'):
                addressToCompare = self.checkIndirectIndex(actualQuadruple[1])
                addressLowerLimit = actualQuadruple[2]
                addressUpperLimit = actualQuadruple[3]

                valueToCompare = self.virtualMemoryDictionary.get(addressToCompare)
                lowerLimitValue = self.virtualMemoryDictionary.get(addressLowerLimit)
                upperLimitValue = self.virtualMemoryDictionary.get(addressUpperLimit)

                if(valueToCompare == lowerLimitValue or valueToCompare == upperLimitValue or (valueToCompare > lowerLimitValue and valueToCompare < upperLimitValue)):
                    print("ARRAY INDEX IN THE ACCEPTED LIMITS")
                elif(valueToCompare < lowerLimitValue or valueToCompare > upperLimitValue):
                    raise TypeError("ERROR: ARRAY INDEX OFF LIMITS")


            #MANDAR COMO PARAM UN ARREGLO: self.checkIndirectIndex(
                
            




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

