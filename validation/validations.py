class Validations:
    def isValidExpressionBrackets(command) -> bool:
        """Checks if the brackets in an expression are all properly closed"""
        if(command.len() <= 1 or command.count('(') != command.count(')')):
            return false

        leftRoundBracket = 0
        leftCurlyBracket = 0
        i = 0
        while(i < command.len() and leftRoundBracket >= 0 and leftCurlyBracket >= 0):
            if(command[i] == '('):
                leftRoundBracket += 1
            elif(command[i] == ')'):
                leftRoundBracket -= 1
            elif(command[i] == '{'):
                leftCurlyBracket += 1
            elif(command[i] == '}'):
                leftCurlyBracket -= 1

            i += 1

        return leftRoundBracket == 0 and leftCurlyBracket == 0


    def isValidQuote(command) -> bool:
        """Checks if the command is a quote that should be printed as is"""
        #TODO: Implement logic for quote detection
