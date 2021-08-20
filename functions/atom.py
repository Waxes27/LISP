class Atom:
    def __init__(self,command):
        """
       checks if the value is an atom 'char or integer
        """
        y=str(command)
        a=list(y)
        if isinstance(a[-1],str)==True:
              print("T")
        elif isinstance(a[-1],int)==True:
            print('T')
        else:
            print("'()")
