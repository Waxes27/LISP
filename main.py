from functions import list as List
"""
import as below
"""
from functions.atom import Atom as atom
from functions.cons import Cons as cons

operators = ['+','-','*','/']
list_of_commands = [cons,atom,'quote','car','cdr','eq','cond','lambda','label','defunc']

commands = {
    
    """
    add your function here when complete
    """

    'cons' : cons,
    'atom' : atom,
    
}

def evaluator(command):
    if '(' not in command and ')' not in command:
        atom(command)
    elif 'cons' in command:
        cons(command)


        # List.List(command)

print("Welcome to a lisp interpreter.\n")
command = ""
while command != "exit" and command != "quit":
    command = input('>> ')
    evaluator(command)

