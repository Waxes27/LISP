from functions import Atom
from functions import List






while True:
    command = input('>> ')
    if '(' not in command and ')' not in command:
        Atom.Unit(command)
    else:
        List.List(command)
    

