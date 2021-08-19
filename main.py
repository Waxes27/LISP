from functions import list as List
"""
import as below
"""
from functions.atom import Atom as atom
from functions.cons import Cons as cons
from functions.cdr import Cdr as cdr


"""
(cdr (cons ( 'x cons ('y ()))))
(cons '1 (cons '2 (cons '3 '()))) 	
"""


operators = ['+','-','*','/']
list_of_commands = ['cons','atom','quote','car','cdr','eq','cond','lambda','label','defunc']
list_of_separators = [i for i in '()\"']


commands = {
    #add your function here when complete
    'cons' : cons,
    'atom' : atom,
    'cdr' : cdr,
}

def evaluator(command):
    temp = []
    print(command.replace('(',"").split()[::-1][1:])
    value = command
    for i in command.replace('(',"").split()[::-1][1:]:
        temp.append(i)
        # print(temp)
        if i in list_of_commands:
            value = evaluate(temp[::-1])

    return list(value)
    

    


def evaluate(command):
    return commands[command[0]](" ".join(command[1:]))



def main():
    print("Welcome to a lisp interpreter.\n")
    command = ""
    while command != "exit" and command != "quit":
        command = input('>> ')
        print(evaluator(command))

# main()

