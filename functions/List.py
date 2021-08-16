class List:
    def __init__(self,command):
        if self.lcount(command):
            print(command)
        else:
            print('Unexpected amount of Parenthesis...')


    def lcount(self, command):
        if command.count('(') == command.count(')'):
            return True
        else:
            return False
        


