class Quote:

    def __init__(self,command):
        if self.IsQoute(command):
            self.DisplayQoute(command)
        

    def IsQoute(self,command):
        if len(command)>2:
            if command[1:6].lower() == "quote" or command[:1] == "`":
                return True
            else :
                return False  
        
    def DisplayQoute(self,command):
        if command[:1] == "`":
            print(command[1:])
        elif command[1:6].lower() == "quote" :
            print(command[6:].removesuffix(')').strip(" "))
 

