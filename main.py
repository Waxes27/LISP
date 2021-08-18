from functions import Atom
from functions import List

operators = ['+','-','*','/']

def evaluator(command):
    if '(' not in command and ')' not in command:
        Atom.Unit(command)
    else:
        List.List(command)

print("Welcome to a lisp interpreter.\n")
command = ""
while command != "exit" and command != "quit":
    command = input('>> ')
    evaluator(command)

