class Eq:

    def checkEqual(self, expression):
        """
        this is the basic functionality that checks if the first expression is
        equal to the second expression.
        """
        if expression[0] == expression[1]:
            return True
        else:
            return False


    def equalList(self, expression):
        """
        this function is supposed to look for an empty list and return false 
        if it finds it
        """
        if '()' in expression:
            return False