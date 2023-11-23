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

print("constantsInt:")
print(constants)
print("constantsFloat:")
print(constantsTwo)

constants.update(constantsTwo)

print("All constants in one dictionary:")
print(constants)

print("")

print("Number of total generated quadruples:")
print(len(resultinQuadruplesDictionary))

vm = VM(resultinQuadruplesDictionary, constants, len(resultinQuadruplesDictionary))

print("")
print("EXECUTION")
print("")

vm.executeQuaduples()
