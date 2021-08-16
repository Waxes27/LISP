from functions import Atom
from functions import List

operators = ['+','-','*','/']

def evaluator(command):
    if '(' not in command and ')' not in command:
        Atom.Unit(command)
    else:
        
        List.List(command)


while True:
    command = input('>> ')
    evaluator(command)
    
    

