from functions import list as List
"""
import as below
"""
from functions.atom import Atom as atom
from functions.cons import Cons as cons


"""
(car (cons ( 'x cons ('y ()))))
(cons '1 (cons '2 (cons '3 '()))) 	
"""


operators = ['+','-','*','/']
list_of_commands = ['cons','atom','quote','car','cdr','eq','cond','lambda','label','defunc']
list_of_separators = [i for i in '()\"']


commands = {
    #add your function here when complete
    'cons' : cons,
    'atom' : atom,
}

def evaluator(command):
    temp = []
    print(command.replace('(',"").split()[::-1][1:])
    for i in command.replace('(',"").split()[::-1][1:]:
        temp.append(i)
        # print(temp)
        if i in list_of_commands:
            value = evaluate(temp[::-1])
            # print(value)
    

    


def evaluate(command):
    return commands[command[0]](" ".join(command[1:]))




print("Welcome to a lisp interpreter.\n")
command = ""
while command != "exit" and command != "quit":
    command = input('>> ')
    evaluator(command)

