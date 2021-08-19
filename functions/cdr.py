class Cdr:
    def __init__(self,command):
        # if self.lcount(command):
        self.do(command)
        # else:
            # print('Unexpected amount of Parenthesis...')


    def lcount(self, command):
        if command.count('(') == command.count(')'):
            return True
        else:
            return False

    def do(self, command):
        mylist = list(command.replace("'","").replace(' ', ""))
        return mylist[1:]
        
    def dont(self, command):
        temp = []
        cdrCount = 0
        openBrace = False
        tempString = ""
        command = command.replace("("," ( ").replace(")", " ) ")
        
        n = 0

        while (command[n:].find("cdr") > 0):
            cdrCount += 1

            n =  command[n:].find("cdr") 

            for x in command[n:]:
                if (x == "("):
                    openBrace = True
                    continue
                if (x == ")"):
                    openBrace = False
                    #tempString += ")"
                    continue
                if (openBrace == True):
                    tempString += x
                
                if (x == "cdr"):
                    break
            for x in tempString.strip().split(' '):
                temp.append(x)
            tempString = ""
        print(temp[cdrCount:])
        return temp[cdrCount:]