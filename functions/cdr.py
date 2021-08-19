class Cdr:
    def __init__(self,command):
        self.value = ''
        if self.lcount(command):
            self.value = self.do(command)
        else:
            print('Unexpected amount of Parenthesis...')


    def lcount(self, command):
        if command.count('(') == command.count(')'):
            return True
        else:
            return False

    def do(self, command):
        mylist = command.replace("'","")
        return mylist.split(" ")[1:]
    
    
    def __iter__(self):
        return iter(self.value)