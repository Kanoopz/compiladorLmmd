from lmmdParser import *
from virtualMachine import *


file = open('./tests/fileToUse.lmmd')
input_str = file.read() 
file.close()

parser.parse(input_str)

print("")
print("PRINT DESDE EL MAIN EXECUTION:")
print("")

print("resultingQuadruples:")
print(resultinQuadruplesDictionary)

print("")

print("constantsAddresses:")
print(constantsMemoryAddresses)

print("")

constants = constantsMemoryAddresses.get('int')
constantsTwo = constantsMemoryAddresses.get('float')
constantsThree = constantsMemoryAddresses.get('string')

print("constantsInt:")
print(constants)
print("constantsFloat:")
print(constantsTwo)
print("constantsStringt:")
print(constantsThree)

constants.update(constantsTwo)
constants.update(constantsThree)

print("All constants in one dictionary:")
print(constants)

print("")

print("Number of total generated quadruples:")
print(len(resultinQuadruplesDictionary))

print("")

print("Functions dictionary:")
print(funtionsDictionary)

vm = VM(resultinQuadruplesDictionary, constants, len(resultinQuadruplesDictionary), funtionsDictionary, variablesInformation)

print("")
print("EXECUTION")
print("")

vm.executeQuaduples()
