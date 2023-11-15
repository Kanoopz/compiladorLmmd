from lmmdParser import *


file = open('./tests/fileToUse.lmmd')
input_str = file.read() 
file.close()

parser.parse(input_str)
