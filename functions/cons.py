class Cons:
    def __init__(self,command):
        if self.lcount(command):
            self.counter(command)
        else:
            print('Unexpected amount of Parenthesis...')


    def lcount(self, command):
        if command.count('(') == command.count(')'):
            return True
        else:
            return False
    
    def counter(self,command):
        temp = []
        command = command.replace('(','').replace(')','').replace("'",'').replace("'",'')
        for i in command.split():
            if i != "cons":
                temp.append(i)
        print(temp)
        return temp


