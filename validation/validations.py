class Validations:
	validationsPassed = 0

	def is_valid_expression_brackets(self, command: str) -> bool:
		"""Checks if the brackets in an expression are all properly closed"""
		if(len(command) <= 1 or command.count('(') != command.count(')')):
			return False

		left_round_bracket = 0
		left_curly_bracket = 0
		i = 0
		while i < len(command) and left_round_bracket >= 0 and left_curly_bracket >= 0:
			if command[i] == '(':
				left_round_bracket += 1
			elif command[i] == ')':
				left_round_bracket -= 1
			elif command[i] == '{':
				left_curly_bracket += 1
			elif command[i] == '}':
				left_curly_bracket -= 1

			i += 1

		return left_round_bracket == 0 and left_curly_bracket == 0

	def is_valid_quote(self, command: str) -> bool:
		"""Checks if the command is a quote that should be printed as is"""
		if len(command) > 1:
			if command[0] == "'" or command[:7] == "(quote ":
				return True

		return False
