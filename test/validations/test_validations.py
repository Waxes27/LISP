import unittest
from validation import validations

class ValidationTests(unittest.TestCase):
    def bracketsAlwaysEvaluatedProperly(self):
        valid_exp_2 = "()"
        valid_exp_6 = "((()))"
        valid_exp_8 = "(()(()))"
        invalid_exp_3 = "())"
        invalid_exp_4 = "(((("
        invalid_exp_5 = "(+ (5 (+ 14 1))"

        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_2))
        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_6))
        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_8))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_3))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_4))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_5))
        self.assertFalse(validations.isValidExpressionBrackets("("))

if __name__ == "__main__":
    unittest.main()
