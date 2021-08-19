class Eq:

    def checkEqual(self, expression):
        if expression[0] == expression[1]:
            return True
        else:
            return False


    def equalList(self, expression):
        if '()' in expression:
            return False